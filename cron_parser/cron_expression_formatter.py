from logger_config import logger

class CronExpressionFormatter:
    def format(self, parsed_cron):
        logger.info("Formatting the parsed cron expression")
        output = ""
        for field in ["minute", "hour", "day_of_month", "month", "day_of_week", "command"]:
            attr_value = getattr(parsed_cron, field, None)
            if attr_value is None:
                logger.error(f"Attribute {field} is not set in parsed_cron")
                continue
            times = " ".join(map(str, attr_value)) if field != "command" else attr_value
            output += f"{field.ljust(14)}{times}\n"
        return output
