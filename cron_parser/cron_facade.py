from cron_parser.cron_expression_parser import CronExpressionParser
from cron_parser.cron_expression_formatter import CronExpressionFormatter
from logger_config import logger

class CronFacade:
    def __init__(self, expression):
        self.parser = CronExpressionParser(expression)
        self.formatter = CronExpressionFormatter()

    def process(self):
        logger.info("Processing the cron expression")
        parsed_cron = self.parser.parse()
        logger.debug(f"Parsed cron expression is: {vars(parsed_cron)}")
        return self.formatter.format(parsed_cron)
