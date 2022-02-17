from botoy import GroupMsg, S
from reply_engine.cmd_server import pluginManager
import re


def plugin_register(name: str, help_content="", super_user=0):
    def deco(func):
        def inner(ctx: GroupMsg):
            ret = None
            h_plugin = pluginManager(name)
            if (super_user and super_user == ctx.FromUserId) or h_plugin.bind(ctx):
                if re.match(f"^帮助\s*{name}$", ctx.Content):
                    sender = S.bind(ctx)
                    if len(help_content):
                        sender.text(help_content)
                    else:
                        sender.text("没有找到帮助说明\U0001F97A")
                else:
                    ret = func(ctx)

                if ret:
                    h_plugin.app_usage(ctx.FromUserId)
            return ret

        return inner

    return deco
