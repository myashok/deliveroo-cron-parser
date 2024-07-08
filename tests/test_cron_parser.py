import unittest
from cron_parser.parsers import CronFieldParserFactory, InvalidFieldException
from cron_parser.cron_expression_parser import CronExpressionParser
from cron_parser.cron_expression_formatter import CronExpressionFormatter

class TestCronFieldParser(unittest.TestCase):
    def setUp(self):
        self.factory = CronFieldParserFactory()

    def test_asterisk_parser(self):
        parser = self.factory.get_parser('*')
        result = parser.parse('*', 0, 59)
        self.assertEqual(result, list(range(0, 60)))

    def test_range_parser(self):
        parser = self.factory.get_parser('1-5')
        result = parser.parse('1-5', 0, 59)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_step_parser(self):
        parser = self.factory.get_parser('*/15')
        result = parser.parse('*/15', 0, 59)
        self.assertEqual(result, [0, 15, 30, 45])

    def test_list_parser(self):
        parser = self.factory.get_parser('1,2,3,4,5')
        result = parser.parse('1,2,3,4,5', 0, 59)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_value_parser(self):
        parser = self.factory.get_parser('5')
        result = parser.parse('5', 0, 59)
        self.assertEqual(result, [5])

    def test_invalid_field(self):
        with self.assertRaises(InvalidFieldException):
            parser = self.factory.get_parser('invalid')
            parser.parse('invalid', 0, 59)


class TestCronExpressionParser(unittest.TestCase):
    def setUp(self):
        self.parser = CronExpressionParser("*/15 0 1,15 * 1-2  /usr/bin/find")

    def test_parse(self):
        result = self.parser.parse()
        expected_result = {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day_of_month": [1, 15],
            "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "day_of_week": [1, 2],
            "command": "/usr/bin/find"
        }
        self.assertEqual(result.minute, expected_result["minute"])
        self.assertEqual(result.hour, expected_result["hour"])
        self.assertEqual(result.day_of_month, expected_result["day_of_month"])
        self.assertEqual(result.month, expected_result["month"])
        self.assertEqual(result.day_of_week, expected_result["day_of_week"])
        self.assertEqual(result.command, expected_result["command"])

class TestCronExpressionFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = CronExpressionFormatter()

    def test_format(self):
        class ParsedCron:
            minute = [0]
            hour = [15]
            day_of_month = [1]
            month = ['1-2']
            day_of_week = [1]
            command = "/usr/bin/find"
        
        parsed_cron = ParsedCron()
        result = self.formatter.format(parsed_cron)
        expected_result = (
            "minute        0\n"
            "hour          15\n"
            "day_of_month  1\n"
            "month         1-2\n"
            "day_of_week   1\n"
            "command       /usr/bin/find\n"
        )
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
