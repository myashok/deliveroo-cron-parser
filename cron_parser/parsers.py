from abc import ABC, abstractmethod
from .exceptions import InvalidFieldException
from logger_config import logger

class CronFieldParser(ABC):
    @abstractmethod
    def parse(self, field: str, min_val: int, max_val: int):
        pass

class AsteriskParser(CronFieldParser):
    def parse(self, field: str, min_val: int, max_val: int):
        logger.debug(f"Parsing asterisk field: {field}")
        return list(range(min_val, max_val + 1))

class RangeParser(CronFieldParser):
    def parse(self, field: str, min_val: int, max_val: int):
        try:
            logger.debug(f"Parsing range field: {field}")
            start, end = map(int, field.split('-'))
            return list(range(start, end + 1))
        except ValueError:
            raise InvalidFieldException(field)

class StepParser(CronFieldParser):
    def parse(self, field: str, min_val: int, max_val: int):
        try:
            logger.debug(f"Parsing step field: {field}")
            step = int(field.split('/')[1])
            return list(range(min_val, max_val + 1, step))
        except ValueError:
            raise InvalidFieldException(field)

class ListParser(CronFieldParser):
    def parse(self, field: str, min_val: int, max_val: int):
        try:
            logger.debug(f"Parsing list field: {field}")
            parts = field.split(',')
            result = []
            for part in parts:
                result.extend(CronFieldParserFactory().get_parser(part).parse(part, min_val, max_val))
            return sorted(set(result))
        except ValueError:
            raise InvalidFieldException(field)

class ValueParser(CronFieldParser):
    def parse(self, field: str, min_val: int, max_val: int):
        try:
            logger.debug(f"Parsing value field: {field}")
            return [int(field)]
        except ValueError:
            raise InvalidFieldException(field)

class CronFieldParserFactory:
    def get_parser(self, field: str):
        if field == '*':
            return AsteriskParser()
        elif '-' in field:
            return RangeParser()
        elif '/' in field:
            return StepParser()
        elif ',' in field:
            return ListParser()
        else:
            return ValueParser()
     
