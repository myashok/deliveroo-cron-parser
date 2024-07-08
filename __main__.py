import sys
from cron_parser.cron_facade import CronFacade
from cron_parser.exceptions import CronParserException
from logger_config import logger

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python -m cron_parser '<cron_expression>'")
        sys.exit(1)

    cron_expression = sys.argv[1]

    try:
        facade = CronFacade(cron_expression)
        output = facade.process()
        print(output)
        # Execute command
    except CronParserException as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
