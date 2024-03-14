from datetime import datetime as dt
from itertools import islice
from typing import Literal, Dict, List

from telebot import types  # noqa
from app.telegram.utils.user_bot_messages import UserBotMessages

from app import xray

class UserBotKeyboard:

    @staticmethod
    def payment_month_items():
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(
            types.KeyboardButton(text='{}'.format(UserBotMessages.get_message("BUY_MONTH_1")))
        )
        keyboard.add(
            types.KeyboardButton(text='{}'.format(UserBotMessages.get_message("BUY_MONTH_3")))
        )
        keyboard.add(
            types.KeyboardButton(text='{}'.format(UserBotMessages.get_message("BUY_MONTH_6")))
        )
        keyboard.add(
            types.KeyboardButton(text='{}'.format(UserBotMessages.get_message("BUY_MONTH_12")))
        )

        return keyboard

    @staticmethod
    def payment_item():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='💲 {}'.format(UserBotMessages.get_message("BUY_PACKAGE")), callback_data='buy_package')
        )

        return keyboard

    @staticmethod
    def main_menu():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='ℹ {}'.format(UserBotMessages.get_message("GET_INFO")), callback_data='get_info')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='💲 {}'.format(UserBotMessages.get_message("BUY_PACKAGE")), callback_data='buy_package')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='🔑 {}'.format(UserBotMessages.get_message("GET_KEYS")), callback_data='get_keys')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='🔗 {}'.format(UserBotMessages.get_message("GET_REFERAL")), callback_data='get_referal_link')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='🌎 {}'.format(UserBotMessages.get_message("GHANGE_SERVER")), callback_data='show_server')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='📑 {}'.format(UserBotMessages.get_message("TUTORIAL")), callback_data='tutorial_request')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='📝 {}'.format(UserBotMessages.get_message("TERMS_OF_USE_LABEL")), callback_data='terms_of_use')
        )
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

    @staticmethod
    def node_list(nodes: list, current: str = None):
        keyboard = types.InlineKeyboardMarkup()
        if len(nodes) >= 2:
            nodes = [p for p in nodes]
            nodes = [nodes[i:i + 2] for i in range(0, len(nodes), 2)]
        else:
            nodes = [nodes]
        for node in nodes:
            row = []
            for p in node:
                msg = f"{p.name}"
                callback_data=f'change_server:{p.name}'

                if (p.name == current):
                    row.append(types.InlineKeyboardButton(
                        text=f"{p.name} (✅)",
                        callback_data="none"
                    ))
                else:
                    row.append(types.InlineKeyboardButton(
                        text=f"{p.name}",
                        callback_data=callback_data
                    ))
            keyboard.row(*row)

        keyboard.add(
            types.InlineKeyboardButton(
                text='Back',
                callback_data='cancel'
            )
        )
        return keyboard
