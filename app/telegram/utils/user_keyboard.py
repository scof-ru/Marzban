from datetime import datetime as dt
from itertools import islice
from typing import Literal, Dict, List

from telebot import types  # noqa
from app.telegram.utils.user_bot_messages import UserBotMessages

from app import xray

class UserBotKeyboard:

    @staticmethod
    def main_menu():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='ℹ {}'.format(UserBotMessages.get_message("GET_INFO")), callback_data='get_info')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='🔑 {}'.format(UserBotMessages.get_message("GET_KEYS")), callback_data='get_keys')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='🔗 {}'.format(UserBotMessages.get_message("GET_REFERAL")), callback_data='get_referal_link')
        )
        # keyboard.add(
        #     types.InlineKeyboardButton(text='➕ Change country', callback_data='change_country')
        # )
        keyboard.add(
            types.InlineKeyboardButton(text='🆘 {}'.format(UserBotMessages.get_message("REPORT_PROBLEMS")), callback_data='techsupport_request')
        )

        return keyboard

    @staticmethod
    def info(info):
        keyboard = types.InlineKeyboardMarkup()
        if len(users) >= 2:
            users = [p for p in users]
            users = [users[i:i + 2] for i in range(0, len(users), 2)]
        else:
            users = [users]
        for user in users:
            row = []
            for p in user:
                status = {
                    UserBotMessages.get_message("STATUS_ACTIVE"): '✅',
                    UserBotMessages.get_message("STATUS_EXPIRED"): '🕰',
                    UserBotMessages.get_message("STATUS_LIMITED"): '📵',
                    UserBotMessages.get_message("STATUS_DISABLED"): '❌'
                }
                row.append(types.InlineKeyboardButton(
                    text=f"{p.username} ({status[p.status]})",
                    callback_data=f'user:{p.username}:{page}'
                ))
            keyboard.row(*row)
        # if there is more than one page
        if total_pages > 1:
            if page > 1:
                keyboard.add(
                    types.InlineKeyboardButton(
                        text="⬅️ Previous",
                        callback_data=f'users:{page - 1}'
                    )
                )
            if page < total_pages:
                keyboard.add(
                    types.InlineKeyboardButton(
                        text="➡️ Next",
                        callback_data=f'users:{page + 1}'
                    )
                )
        keyboard.add(
            types.InlineKeyboardButton(
                text='Back',
                callback_data='cancel'
            )
        )
        return keyboard