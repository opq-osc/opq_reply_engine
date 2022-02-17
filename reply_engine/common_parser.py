from botoy import GroupMsg, MsgTypes
import json
import re


class picObj:
    url: str
    md5: str

    def __init__(self):
        url = ""
        md5 = ""


class commonContext:
    from_user: int
    from_group: int
    content: str
    at_target: list
    pic: picObj

    def __init__(self):
        self.from_user = 0
        self.from_group = 0
        self.content = ""
        self.at_target = []
        self.pic = None


def common_group_parser(ctx: GroupMsg) -> commonContext:
    common_ctx = commonContext()
    common_ctx.from_user = ctx.FromUserId
    common_ctx.from_group = ctx.FromGroupId
    if ctx.MsgType == MsgTypes.PicMsg or ctx.MsgType == MsgTypes.AtMsg:
        content_json = json.loads(ctx.Content)
        if "Content" not in content_json:
            return None
        common_ctx.content = content_json["Content"]
        if "UserExt" in content_json:
            for user in content_json["UserExt"]:
                common_ctx.content = re.sub(f"@{user['QQNick']}\\s+", "", common_ctx.content)
                common_ctx.at_target.append(user['QQUid'])

        if "GroupPic" in content_json:
            common_ctx.pic = picObj()
            common_ctx.pic.md5 = content_json["GroupPic"][0]["FileMd5"]
            common_ctx.pic.url = content_json["GroupPic"][0]["Url"]
    else:
        common_ctx.content = ctx.Content

    return common_ctx
