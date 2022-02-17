from botoy import GroupMsg, S
from reply_engine.cmd_server import pluginManager
import re


def plugin_register(name: str, help_content="", super_user=0):
    def deco(func):
        async def inner(ctx: GroupMsg):
            ret = None
            h_plugin = pluginManager(name)
            if (super_user and super_user == ctx.FromGroupId) or h_plugin.bind(ctx):
                if re.match(f"^帮助\s*{name}$", ctx.Content):
                    sender = S.bind(ctx)
                    if len(help_content):
                        await sender.atext(help_content)
                    else:
                        await sender.atext("没有找到帮助说明\U0001F97A")
                ret = await func(ctx)

                if ret:
                    h_plugin.app_usage(ctx.FromUserId)
            return ret

        return inner

    return deco
