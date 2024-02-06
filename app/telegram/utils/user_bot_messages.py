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
        "USER_ADD_ERROR" : {
            "en":"Can't create your account. Please write to techsupport",
            "ru": "Не получилось создать профиль пользователя. Обратись в тех. поддержку"
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
            "ru": "Пользователь не активирован. Пожалуйста дождитесь активации"
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
        "TUTORIAL" : {
            "en": "Tutorial",
            "ru": "Инструкция"
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
        "ENTER_SUPPORT_MSG": {
            "en": "🆘 Enter message for techsupport",
            "ru": "🆘 Введите сообщение для техподдержки"
        },
        "GHANGE_SERVER": {
            "en": "Change server",
            "ru": "Сменить сервер"
        },
        "SERVER_CHANGED": {
            "en": "✅ Server has been changed",
            "ru": "✅ Сервер был успешно изменен"
        },
        "TUTORIAL_DESCRIPTION" : {
            "en": f""" 
<b>Quick guide:</b>
\t1. Wait for user activation
\t2. When it happen - download the keys
\t3. Install one the application below, according you operating system
\t4. Import downloaded key to the application by copying text or scanning QR

<b>Applications:</b>
Android - <a href="https://play.google.com/store/apps/details?id=com.v2ray.ang">v2rayng</a>
iOS/MacOS - <a href="https://apps.apple.com/us/app/foxray/id6448898396">foxray</a>
Linux - <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-debian-x64.deb">Nekoray.deb</a>\t <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-debian-x64.deb">Nekoray.AppImage</a>
Windows - <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-windows64.zip">Nekoray</a>
\n\n""",
            "ru": f""" 
<b>Инструкция:</b>
\t1. Дождитесь активации пользователя
\t2. Когда пользователь будет активирован - скачайте ключ
\t3. Скачайте приложение по одной из ссылок ниже
\t4. Импортируйте ключ в приложение скопировав ключ или по QR коду

<b>Приложения:</b>
Android - <a href="https://play.google.com/store/apps/details?id=com.v2ray.ang">v2rayng</a>
iOS/MacOS - <a href="https://apps.apple.com/us/app/foxray/id6448898396">foxray</a>
Linux - <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-debian-x64.deb">Nekoray.deb</a>\t <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-debian-x64.deb">Nekoray.AppImage</a>
Windows - <a href="https://github.com/MatsuriDayo/nekoray/releases/download/3.24/nekoray-3.24-2023-10-28-windows64.zip">Nekoray</a>
\n\n"""
        },
        "TERMS_OF_USE_LABEL" : {
                "en": "Terms of use",
                "ru": "Правила пользования"
        },
        "TERMS_OF_USE" : {
            "en": f""" 
<b>Terms of use:</b>
1. Bot is available only by invitation
2. Invite only trusted friends (who is not relate to censorship organizations)
3. Use proxy only when you really need it. You shouldn't use it 24/7 for safety reasons
4. The keys might be used on several devices (up to 5 devices)
5. It's forbiden to download torrents over proxy
6. If you find bug or has any problem - please report it to techsupport
""",
            "ru": f""" 
<b>Правила использования:</b>
1. Доступ к боту возможен только по приглашению. 
2. Приглашайте только проверенных людей (которые не имеют отношения к гос. организациям, особенно к РКН)
3. Пользуйтесь по мере необходимости. Не нужно использовать в режиме 24/7 (т.к. часть веб ресурсов РФ не доступна вне РФ)
4. Ключи можно использовать на нескольких девайсах (до 5 штук)
5. Нельзя качать торренты
6. Если обнаружили ошибку или проблему - пишите в тех. поддержку
"""
    }
    }

    default_lang="ru"

    @staticmethod
    def get_message(var, user_lang=None):
        if (user_lang in ("ru", "eng")):
            text = UserBotMessages.user_bot_messages_dict[var][user_lang]
        else:
            text = UserBotMessages.user_bot_messages_dict[var][UserBotMessages.default_lang]

        return text
