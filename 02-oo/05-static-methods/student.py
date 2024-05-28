class Duration:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    @staticmethod
    def from_seconds(seconds):
        duration = Duration()
        duration.minutes = seconds // 60
        duration.seconds = seconds % 60

    @staticmethod
    def from_minutes(minutes):
        duration = Duration()
        duration.minutes = minutes

    @staticmethod
    def from_hours(hours):
        duration = Duration()
        duration.hours = hours

    @property
    def seconds(self):
        return self.seconds

    @property
    def minutes(self):
        return self.minutes

    @property
    def hours(self):
        return self.hours
