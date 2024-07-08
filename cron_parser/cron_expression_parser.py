from cron_parser.parsers import CronFieldParserFactory
from cron_parser.cron_expression import CronExpressionBuilder
from cron_parser.exceptions import InvalidCronExpressionException
from logger_config import logger

class CronExpressionParser:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = ["minute", "hour", "day of month", "month", "day of week", "command"]
        self.min_max_values = {
            "minute": (0, 59),
            "hour": (0, 23),
            "day of month": (1, 31),
            "month": (1, 12),
            "day of week": (0, 6)
        }

    def parse(self):
        logger.info(f"Parsing cron expression: {self.expression}")
        parts = self.expression.split()
        if len(parts) < 6:
            raise InvalidCronExpressionException(self.expression)

        builder = CronExpressionBuilder()
        for i, field in enumerate(self.fields[:-1]):
            field_part = parts[i]
            min_val, max_val = self.min_max_values[field]
            parser = CronFieldParserFactory().get_parser(field_part)
            parsed_field = parser.parse(field_part, min_val, max_val)
            getattr(builder, f'set_{field.replace(" ", "_")}')(parsed_field)

        builder.set_command(parts[5])
        return builder.build()
