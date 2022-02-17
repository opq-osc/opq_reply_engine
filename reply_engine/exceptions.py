class CmdLimitExceedException(Exception):
    pass


class ReplyLimitExceedException(Exception):
    pass


class CmdLengthExceedException(Exception):
    pass


class CmdWithRegExpException(Exception):
    pass


class CmdStartsWithBuiltInKeyException(Exception):
    pass
