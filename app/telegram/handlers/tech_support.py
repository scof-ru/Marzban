from app.telegram import bot
from telebot import types
from app.telegram.utils.custom_filters import (cb_query_equals,
                                               cb_query_startswith)
from app.telegram.utils.user_keyboard import UserBotKeyboard
from app.telegram.utils.user_bot_messages import UserBotMessages


from config import TELEGRAM_SUPPORT_CHAT_ID
from app.db import GetDB, crud


REPLY_TO_THIS_MESSAGE="User above don't allow forward his messages. Reply to this message."
WRONG_REPLY="User above don't allow forward his messages. You must reply to bot reply under user forwarded message."

@bot.callback_query_handler(cb_query_equals('techsupport_request'))
def techsupport_command(call: types.CallbackQuery):
    username_msg = bot.send_message(
        call.message.chat.id,
        UserBotMessages.get_message("ENTER_SUPPORT_MSG")
        # reply_markup=UserBotKeyboard.main_menu()
    )
    #schedule_delete_message(template_msg.message_id)
    bot.register_next_step_handler(username_msg, forward_to_chat)

def forward_to_chat(message: types.Message):
    print(message)
    forwarded = bot.forward_message(TELEGRAM_SUPPORT_CHAT_ID, message.chat.id, message.message_id)
    if not forwarded.forward_from:
        bot.send_message(
            chat_id=TELEGRAM_SUPPORT_CHAT_ID,
            reply_to_message_id=forwarded.message_id,
            text=f'{update.message.from_user.id}\n{REPLY_TO_THIS_MESSAGE}'
        )
    # TODO: Show notification, that message will be processed soon

def report_all_clients(message: str, parse_mode="html", keyboard=None):
    id = username.replace("user", "")
    id = int(id)
    with GetDB() as db:
        tguser = crud.get_tguser_active(db)
        for user in tguser:
            try:
                bot.send_message(tguser.id, message, parse_mode=parse_mode, reply_markup=keyboard)
            except ApiTelegramException as e:
                logger.error(e)


@bot.message_handler(content_types=['text', 'photo', 'document', 'video', 'video_note', 'web_app_data'], is_admin=True)
def forward_to_all_users(message):
    user_id = None
    with GetDB() as db:
        tgusers = crud.get_tguser_active(db)
        for user in tgusers:
            user_id = user.id
            bot.copy_message(
                message_id=message.message_id,
                chat_id=user_id,
                from_chat_id=message.chat.id
            )


@bot.message_handler(content_types=['text'], is_techsupport=True)
def forward_to_user(message):
    user_id = None
    print(message)
    if message.reply_to_message.forward_from:
        user_id = message.reply_to_message.forward_from.id
    elif REPLY_TO_THIS_MESSAGE in message.reply_to_message.text:
        try:
            user_id = int(message.reply_to_message.text.split('\n')[0])
        except ValueError:
            user_id = None
    if user_id:
        bot.copy_message(
            message_id=message.message_id,
            chat_id=user_id,
            from_chat_id=message.chat.id
        )
    else:
        bot.send_message(
            chat_id=TELEGRAM_SUPPORT_CHAT_ID,
            text=WRONG_REPLY
        )
