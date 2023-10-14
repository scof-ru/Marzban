from datetime import datetime
from app.db import GetDB, crud
from app.models.user import UserResponse
from app.telegram import bot
from app.telegram.utils.custom_filters import (cb_query_equals,
                                               cb_query_startswith)
from telebot import types

from app.telegram import wallet_api
from pytz import UTC
from telebot.custom_filters import ChatFilter
from telebot.util import extract_arguments
from app.telegram.utils.user_keyboard import UserBotKeyboard
from telebot.util import user_link
from app.utils.system import readable_size

bot.add_custom_filter(ChatFilter())

get_user_text = """
*Username*: `{username}`
*Status*: `{status}`
*Traffic limit*: `{traffic_limit}`
*Used traffic*: `{used_traffic}`
*Expiry date*: `{expires_at}`
*Created at*: `{created_at}`
*Proxy protocols*: `{protocols}`
"""

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
    username = extract_arguments(message.text)
    if not username:
        return bot.reply_to(message, 'Usage: `/usage <username>`', parse_mode='MarkdownV2')
    # create_order(message.from_user.id)
    return bot.reply_to(message, "`{}`".format(str(message.from_user)), parse_mode='MarkdownV2')


@bot.message_handler(commands=['usage'])
def usage_command(message):
    username = extract_arguments(message.text)
    if not username:
        return bot.reply_to(message, 'Usage: `/usage <username>`', parse_mode='MarkdownV2')

    with GetDB() as db:
        dbuser = crud.get_user(db, username)

        if not dbuser:
            return bot.reply_to(message, "No user found with this username")
        user = UserResponse.from_orm(dbuser)

        text = get_user_text.format(
            username=user.username,
            status=user.status,
            traffic_limit=readable_size(user.data_limit) if user.data_limit else '-',
            used_traffic=readable_size(user.used_traffic),
            expires_at=datetime.fromtimestamp(user.expire, UTC).strftime('%m/%d/%Y') if user.expire else '-',
            created_at=user.created_at.strftime('%m/%d/%Y'),
            protocols=','.join(user.proxies.keys())
        )

    return bot.reply_to(message, text, parse_mode='MarkdownV2')

@bot.message_handler(commands=['start', 'help'])
def help_command(message: types.Message):
    return bot.reply_to(message, """
{user_link} Welcome to Wall Breaker Telegram-Bot Panel.
Here you can manage your profile.
To get started, use the buttons below.
""".format(
        user_link=user_link(message.from_user)
    ), parse_mode="html", reply_markup=UserBotKeyboard.main_menu())

def show_user_info(from_user):
    return str(text)

@bot.callback_query_handler(cb_query_equals('get_info'))
def get_info_command(call: types.CallbackQuery):
    text = "<code>{}</code>".format(str(call.message.from_user))
    # text = show_user_info(call.message.from_user)

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )


@bot.callback_query_handler(cb_query_equals('get_keys'))
def get_keys_command(call: types.CallbackQuery):
    text = f"<code>KEYS: asdasdasdsadsad</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )


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
