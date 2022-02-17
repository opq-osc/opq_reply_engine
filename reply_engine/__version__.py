from .cmd_dbi import cmdDB
from .db_setup import update_db
from botoy import logger
import sqlite3
import traceback

__version__ = "0.8.0"


def check_version():
    check_db_version()


def check_db_version():
    db = cmdDB()
    db_version = db.check_db_version()
    if not db_version or db_version != __version__:
        try:
            logger.info(f"reply_engine: 当前版本为[{__version__}], db版本为{db_version}, 更新中...")
            update_db()
            db.update_db_version(__version__)
            logger.info("reply_engine: db更新成功")
        except:
            logger.error("reply_engine: db更新失败")
            logger.error(traceback.format_exc())
