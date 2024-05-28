class Time:
    def __init__(self, hours, minutes, seconds):
        if hours < 0 or hours > 23:
            raise ValueError("Hours must be between 0 and 23")
        if minutes < 0 or minutes > 59:
            raise ValueError("Minutes must be between 0 and 59")
        if seconds < 0 or seconds > 59:
            raise ValueError("Seconds must be between 0 and 59")

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if value < 0 or value > 23:
            raise ValueError("Hours must be between 0 and 23")
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if value < 0 or value > 59:
            raise ValueError("Minutes must be between 0 and 59")
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if value < 0 or value > 59:
            raise ValueError("Seconds must be between 0 and 59")
        self.__seconds = value
