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


class ConfigErrorException(Exception):
    def __init__(self, config_item, error_str):
        super()
        self.config_item = config_item
        self.error_str = error_str

    def default_output(self):
        return f"配置项‘{self.config_name}’错误:{self.error_str}"