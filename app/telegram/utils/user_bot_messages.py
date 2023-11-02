from telebot.formatting import escape_markdown

class UserBotMessages():
    user_bot_messages_dict = {
        "BOTS_ARE_NOT_ALLOWED" : {
            "en": "Bots are not allowed to perform cmds",
            "ru": "Команда не поддерживается для ботов"
        },
        "WELCOME_MSG" : {
            "en": """Welcome to Wall Breaker bot. Here you can manage your profile.
To get started, use the buttons below.""", 
            "ru": """Добро пожаловать в Wall Breaker bot. Здесь ты можешь управлять своим аккаунтом.
Используй кнопки ниже"""
        },
        "NO_ACCOUNT" : {
            "en":"Oops, it seems you have no account yet. Try /start command to create profile",
            "ru": "Упс. Кажется твой аккаунт еще не создан. Попробуй использовать команду /start для создания профиля"
        },
        "SIGNOFF_SUCCESFULL": {
            "en": "Successfully signed off. To resume the subscription use /start command",
            "ru": "Вы были успешно отписаны. Чтобы возобновить подписку воспользуйтесь командой /start"

        },
        "NO_USER" : {
            "en":"It seems your profile has been deleted or not created. Please write to tech support",
            "ru": "Кажется твой аккаунт был удален или не был создан. Напиши в тех. поддержку"
        },
        "USER_DISABLED" : {
            "en": "User status is disabled. Please wait for activating",
            "ru": "Пользователь не активирован. Пожайлуста дождитесь активации"
        },
        "USER_LIMITED" : {
            "en": "User status is limited or expired. Please request more details in main menu",
            "ru": "Достигнут лимит трафика или срок действия. Проверьте ваш статус в главном меню"
        },
        "AVAILABLE_BY_INVITATION" : {
            "en": "Bot available only by invitation",
            "ru": "Бот доступен только по приглашению"    
        },
        "MAIN_MENU" : {
            "en": "Main menu",
            "ru": "Главное меню"
        },
        "GENERATING_QR" : {
            "en": "Generating QR code...",
            "ru": "Генерируем QR код..."
        },
        "GET_INFO" : {
            "en":"Get information",
            "ru": "Получить информацию"
        },
        "GET_REFERAL" : {
            "en": "Invite friends",
            "ru": "Пригласить друга"
        }, 
        "GET_KEYS" : {
            "en":"Get keys",
            "ru": "Получить ключи"
        },
        "REPORT_PROBLEMS" : {
            "en":"Report problems",
            "ru": "Написать в тех. поддержку"
        },
        "STATUS_ACTIVE": {
            "en": "active",
            "ru": "активен"
        },
        "STATUS_DISABLED": {
            "en": "disabled",
            "ru": "неактивен"
        },
        "STATUS_EXPIRED": {
            "en": "expired",
            "ru": "истек срок действия"
        },
        "STATUS_LIMITED": {
            "en": "limited",
            "ru": "ограничен"
        },
        "USER_STATUS_CHANGE": {
            "en": "Your Status Changed\n➖➖➖➖➖➖➖\n\tStatus: <b>{status}</b>",
            "ru": "Ваш статус изменен\n➖➖➖➖➖➖➖\n\tСтатус: <b>{status}</b>"
        },
        "USERNAME": {
            "en": "Username",
            "ru": "Пользователь"
        },
        "USAGE_LIMIT": {
            "en": "Usage Limit",
            "ru": "Лимит трафика"
        },
        "USED_TRAFFIC": {
            "en": "Used traffic",
            "ru": "Использованный трафик"
        },
        "EXPIRY_DATE": {
            "en": "Expiry date",
            "ru": "Срок действия"
        },
        "PROTOCOL": {
            "en": "Protocols",
            "ru": "Протоколы"
        },
        "STATUS": {
            "en": "Status",
            "ru": "Статус"
        },
        "SHARE_LINK" : {
            "en": "Use the link below to share among your friends",
            "ru": "Используй ссылку ниже для того, чтобы пригласить друзей"
        }, 
    }

    default_lang="ru"

    @staticmethod
    def get_message(var, user_lang=None):
        if (user_lang in ("ru", "eng")):
            text = UserBotMessages.user_bot_messages_dict[var][user_lang]
        else:
            text = UserBotMessages.user_bot_messages_dict[var][UserBotMessages.default_lang]

        return text
