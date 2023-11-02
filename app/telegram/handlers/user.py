from datetime import datetime
from app.db import GetDB, crud
from app.models.user import UserResponse
from app.telegram import bot
from app.telegram.handlers.report import report_new_user
from app.telegram.utils.custom_filters import (cb_query_equals,
                                               cb_query_startswith)
from app.telegram.utils.user_bot_messages import UserBotMessages
from telebot.formatting import escape_markdown


from telebot import types
from app import xray

import io
import qrcode
import sqlalchemy

from app.telegram import wallet_api
from pytz import UTC
from telebot.custom_filters import ChatFilter
from telebot.util import extract_arguments
from app.telegram.utils.user_keyboard import UserBotKeyboard
from telebot.util import user_link
from app.utils.system import readable_size
from app.models.user import UserCreate, UserStatus
from config import TELEGRAM_BOT_URL, TELEGRAM_ADMIN_ID


bot.add_custom_filter(ChatFilter())


def create_order(user_id):
    return wallet_api.create_order(
        amount=100,
        currency_code="USD",
        description="Test Order",
        external_id="12345",
        timeout_seconds=3600,
        customer_telegram_user_id=user_id
    )


@bot.message_handler(commands=['echo'])
def usage_command(message):
    print(message)
    # username = extract_arguments(message.text)
    # if not username:
    #     return bot.reply_to(message, 'Usage: `/usage <username>`', parse_mode='MarkdownV2')
    # create_order(message.from_user.id)
    return bot.reply_to(message, "`{}`".format(str(message.from_user)), parse_mode='MarkdownV2')



def add_new_user(from_user, referent):
    inbounds={"shadowsocks": ["Shadowsocks"], "vless": ["VLESS TCP REALITY"]}
    new_user = UserCreate(
        username="user" + str(from_user.id),
        expire=None,
        data_limit=10*1024*1024*1024,
        proxies={p: {} for p in inbounds},
        inbounds=inbounds
    )

    try:
        with GetDB() as db:
            tguser = crud.get_tguser_by_id(db, from_user.id)
            if (tguser):
                return True 
            db_user = crud.create_user(db, new_user, status=UserStatus.disabled)
            tg_user = crud.create_tguser(db, from_user.id, db_user.id, from_user.first_name, from_user.username, from_user.last_name,  from_user.language_code, True, referent)
            report_new_user(db_user.id, db_user.username, "self-added", db_user.expire, db_user.data_limit, db_user.proxies, db_user.status)

    except sqlalchemy.exc.IntegrityError as exp:
        print(exp)
        db.rollback()
        return False
    else:
        return True

@bot.message_handler(commands=['signoff'])
def signoff_command(message: types.Message):
    if (message.from_user.is_bot):
        return bot.reply_to(message, escape_markdown(UserBotMessages.get_message("BOTS_ARE_NOT_ALLOWED")), parse_mode='MarkdownV2')

    response = UserBotMessages.get_message("MAIN_MENU")
    with GetDB() as db:
        res = crud.update_tguser_active(db, message.from_user.id, False)
        if not res:
            return bot.send_message(message.chat.id, escape_markdown(UserBotMessages.get_message("NO_USER")), parse_mode='MarkdownV2')

    return bot.send_message(message.chat.id, escape_markdown(UserBotMessages.get_message("SIGNOFF_SUCCESFULL")), parse_mode="MarkdownV2")


@bot.message_handler(commands=['start', 'menu'])
def start_command(message: types.Message):
    start_args = (message.text.split(" "))
    referent = None
    if (len(start_args) > 1):
        referent = int(start_args[1])
    if (message.from_user.is_bot):
        return bot.reply_to(message, escape_markdown(UserBotMessages.get_message("BOTS_ARE_NOT_ALLOWED")), parse_mode='MarkdownV2')

    response = UserBotMessages.get_message("MAIN_MENU")
    with GetDB() as db:
        tguser = crud.get_tguser_by_id(db, message.from_user.id)
        if not tguser:
            if (not referent):
                return bot.reply_to(message, escape_markdown(UserBotMessages.get_message("AVAILABLE_BY_INVITATION")), parse_mode='MarkdownV2')
            elif (not crud.get_tguser_by_id(db, referent) and referent != TELEGRAM_ADMIN_ID):
                return bot.reply_to(message, escape_markdown(UserBotMessages.get_message("AVAILABLE_BY_INVITATION")), parse_mode='MarkdownV2')
            add_new_user(message.from_user, referent)
            response = """
{user_link} {welcome_msg}
""".format(user_link=user_link(message.from_user), welcome_msg=UserBotMessages.get_message("WELCOME_MSG"))
        else:
            crud.update_tguser_active(db, message.from_user.id, True)

    return bot.reply_to(message,  response, parse_mode="html", reply_markup=UserBotKeyboard.main_menu())

def show_user_info(from_user):
    return str(text)

def get_user_info_text(
        username: str, inbounds: dict, data_limit: int | None = None, usage: int | None = None, expire: int |
        None = None, status: str | None = None) -> str:
    protocols = ""
    for p, inbounds in inbounds.items():
        protocols += f"\n\t\t<b>{p.upper()}</b>\n"
        protocols += "\t\t\t\t" + ", ".join([f"<code>{i}</code>" for i in inbounds])
    text = f"""
{UserBotMessages.get_message("USERNAME")}: <b>{username}</b>
{UserBotMessages.get_message("USAGE_LIMIT")}: <b>{readable_size(data_limit) if data_limit else 'Unlimited'}</b>
{UserBotMessages.get_message("USED_TRAFFIC")}: <b>{readable_size(usage) if usage else "-"}</b>
{UserBotMessages.get_message("EXPIRY_DATE")} <b>{datetime.fromtimestamp(expire).strftime('%Y-%m-%d') if expire else 'Never'}</b>
{UserBotMessages.get_message("PROTOCOL")}: {protocols},
{UserBotMessages.get_message("STATUS")}: {status}
        """
    return text



@bot.callback_query_handler(cb_query_startswith('get_info'))
def get_info_command(call: types.CallbackQuery):
    with GetDB() as db:
        tguser = crud.get_tguser_by_id(db, call.from_user.id)
        if not tguser:
            return bot.answer_callback_query(
                        call.id,
                        UserBotMessages.get_message("NO_ACCOUNT"),
                        show_alert=True
                    )
        dbuser = crud.get_user_by_id(db, tguser.user_id)
        if not dbuser:
            return bot.answer_callback_query(
                call.id,
                UserBotMessages.get_message("NO_USER"),
                show_alert=True
            )
        user = UserResponse.from_orm(dbuser)

    text = get_user_info_text(
        username=user.username, inbounds=user.inbounds,
        data_limit=user.data_limit, usage=user.used_traffic, expire=user.expire, status=user.status),
    bot.edit_message_text(
        text,
        call.message.chat.id, call.message.message_id, parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu())

@bot.callback_query_handler(cb_query_equals('get_keys'))
def get_keys_command(call: types.CallbackQuery):
    with GetDB() as db:
        tguser = crud.get_tguser_by_id(db, call.from_user.id)
        if not tguser:
            return bot.answer_callback_query(
                        call.id,
                        UserBotMessages.get_message("NO_ACCOUNT"),
                        show_alert=True
                    )
        dbuser = crud.get_user_by_id(db, tguser.user_id)
        if not dbuser:
            return bot.answer_callback_query(call.id, UserBotMessages.get_message("NO_USER"), show_alert=True)

        user = UserResponse.from_orm(dbuser)

        if (user.status == UserStatus.disabled):
            return bot.answer_callback_query(call.id, UserBotMessages.get_message("USER_DISABLED"), show_alert=True)

        if (user.status == UserStatus.limited):
            return bot.answer_callback_query(call.id, UserBotMessages.get_message("USER_LIMITED"), show_alert=True)

    bot.answer_callback_query(call.id, UserBotMessages.get_message("GENERATING_QR"))

    for link in user.links:
        f = io.BytesIO()
        qr = qrcode.QRCode(border=6)
        qr.add_data(link)
        qr.make_image().save(f)
        f.seek(0)
        bot.send_photo(
            call.message.chat.id,
            photo=f,
            caption=f"<code>{link}</code>",
            parse_mode="HTML"
        )

    return bot.send_message(call.message.chat.id, UserBotMessages.get_message("MAIN_MENU"), parse_mode="html", reply_markup=UserBotKeyboard.main_menu())


@bot.callback_query_handler(cb_query_equals('change_country'))
def change_country_command(call: types.CallbackQuery):
    text = f"<code>change_country_command</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )

@bot.callback_query_handler(cb_query_equals('get_referal_link'))
def get_referal_link_command(call: types.CallbackQuery):
    text = UserBotMessages.get_message("SHARE_LINK")
    text += "\n"
    text += TELEGRAM_BOT_URL + "?start=" +  str(call.from_user.id)

    return bot.send_message(call.message.chat.id, escape_markdown(text), parse_mode="MarkdownV2", reply_markup=UserBotKeyboard.main_menu())



@bot.callback_query_handler(cb_query_equals('report'))
def report_command(call: types.CallbackQuery):
    text = f"<code>report_command</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )
