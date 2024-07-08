from logger_config import logger

class CronParserException(Exception):
    pass

class InvalidCronExpressionException(CronParserException):
    def __init__(self, expression):
        self.expression = expression
        self.message = f"Invalid cron expression: {expression}"
        logger.error(self.message)
        super().__init__(self.message)

class InvalidFieldException(CronParserException):
    def __init__(self, field):
        self.field = field
        self.message = f"Invalid cron field: {field}"
        logger.error(self.message)
        super().__init__(self.message)

class CommandExecutionException(CronParserException):
    def __init__(self, command):
        self.command = command
        self.message = f"Failed to execute command: {command}"
        logger.error(self.message)
        super().__init__(self.message)
