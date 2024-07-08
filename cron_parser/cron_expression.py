class CronExpression:
    def __init__(self):
        self.minute = None
        self.hour = None
        self.day_of_month = None
        self.month = None
        self.day_of_week = None
        self.command = None

class CronExpressionBuilder:
    def __init__(self):
        self.cron_expression = CronExpression()

    def set_minute(self, minute):
        self.cron_expression.minute = minute
        return self

    def set_hour(self, hour):
        self.cron_expression.hour = hour
        return self

    def set_day_of_month(self, day_of_month):
        self.cron_expression.day_of_month = day_of_month
        return self

    def set_month(self, month):
        self.cron_expression.month = month
        return self

    def set_day_of_week(self, day_of_week):
        self.cron_expression.day_of_week = day_of_week
        return self

    def set_command(self, command):
        self.cron_expression.command = command
        return self

    def build(self):
        return self.cron_expression
