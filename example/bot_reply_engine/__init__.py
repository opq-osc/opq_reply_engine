from botoy.decorators import ignore_botself
from reply_engine import replyServer
from botoy import logger
import threading
import traceback
from reply_engine.deco import plugin_register

plugin_name = "调教助手"

l_reply_server = replyServer()
replyer_thread = None


def exception_handler(e):
    l_reply_server.reply_super(e)


def run_reply_server():
    except_happened = False
    while True:
        try:
            l_reply_server.wait_for_msg()
        except:
            exception_format = traceback.format_exc()
            logger.error(exception_format)
            logger.error("Reply_server异常，重启中...")
            exception_handler(exception_format)


@plugin_register(plugin_name, l_reply_server.help_self())
@ignore_botself
def main(ctx):
    if not l_reply_server.running:
        replyer_thread = threading.Thread(target=run_reply_server)
        replyer_thread.start()

    l_reply_server.enqueue(ctx)


def receive_group_msg(ctx):
    main(ctx)
