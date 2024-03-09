import itertools
from datetime import datetime

from app import logger, scheduler, xray
from app.db import GetDB, get_users, update_user_status
from app.models.user import UserStatus
from app.utils import report
from dateutil.relativedelta import relativedelta


def review():
    now = datetime.utcnow().timestamp()
    with GetDB() as db:
        for user in get_users(db, status=UserStatus.active):

            limited = user.data_limit and user.used_traffic >= user.data_limit
            expired = user.expire and user.expire <= now
            if limited:
                status = UserStatus.limited
            elif expired:
                status = UserStatus.expired
            else:
                continue

            xray.operations.remove_user(user)
            update_user_status(db, user, status)
            report.status_change(user.username, status)

            logger.info(f"User \"{user.username}\" status changed to {status}")

def review_expire_date():
    deadline_date = datetime.now() + relativedelta(days=3)
    with GetDB() as db:
        for user in get_users(db, status=UserStatus.active):
            if user.expire:
                expired_date = datetime.fromtimestamp(user.expire)
                delta = expired_date - datetime.now()
                if (delta.days <= 3):
                    report.user_expiring(user.username, delta.days)
                    logger.info(f"User \"{user.username}\" expired notification")

scheduler.add_job(review, 'interval', seconds=5)
scheduler.add_job(review_expire_date, 'interval', days=1)
