class LengthConverter:
    def __init__(self):
        self.meter = 0
        self.feet = 0
        self.inch = 0

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        self.__meter = value
        self.__feet = value * 3.28084
        self.__inch = value * 39.3701

    @property
    def feet(self):
        return self.__feet

    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meter = value / 3.28084
        self.__inch = value * 12

    @property
    def inch(self):
        return self.__inch

    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__meter = value / 39.3701
        self.__feet = value / 12
