from datetime import datetime
from app.db import GetDB, crud
from app.models.user import UserResponse
from app.telegram import bot
from pytz import UTC
from telebot.custom_filters import ChatFilter
from telebot.util import extract_arguments
from app.telegram.utils.use_keyboard import UserBotKeyboard

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

@bot.message_handler(commands=['start', 'help'], is_admin=False)
def help_command(message: types.Message):
    return bot.reply_to(message, """
{user_link} Welcome to Wall Breaker Telegram-Bot Panel.
Here you can manage your profile.
To get started, use the buttons below.
""".format(
        user_link=user_link(message.from_user)
    ), parse_mode="html", reply_markup=UserBotKeyboard.main_menu())


def show_user_info(from_user):
    text = f"""
📊 User Info:
┌ Username: <b>{username}</b>
├ Usage Limit: <b>{readable_size(data_limit) if data_limit else 'Unlimited'}</b>
├ Used Traffic: <b>{readable_size(usage) if usage else "-"}</b>
├ Expiry Date <b>{datetime.fromtimestamp(expire).strftime('%Y-%m-%d') if expire else 'Never'}</b>
├ Protocols: {protocols}
└ Subscription URL: <code>{sub_url}</code>
    """

    return text

@bot.callback_query_handler(cb_query_equals('get_info'), is_admin=False)
def get_info_command(call: types.CallbackQuery):
    text = ""
    text = show_user_info(call.message.from_user)

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )


@bot.callback_query_handler(cb_query_equals('get_keys'), is_admin=False)
def get_keys_command(call: types.CallbackQuery):
    text = f"<code>KEYS: asdasdasdsadsad</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )


@bot.callback_query_handler(cb_query_equals('change_country'), is_admin=False)
def change_country_command(call: types.CallbackQuery):
    text = f"<code>change_country_command</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )


@bot.callback_query_handler(cb_query_equals('report'), is_admin=False)
def report_command(call: types.CallbackQuery):
    text = f"<code>report_command</code>\n\n"

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode="HTML",
        reply_markup=UserBotKeyboard.main_menu()
    )