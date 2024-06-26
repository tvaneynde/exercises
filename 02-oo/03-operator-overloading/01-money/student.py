class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Invalid value for amount")
        self.__amount = value

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value == "":
            print("Invalid value for currency")
        self.__currency = value

    def __add__(self, other):
        if self.__currency == other.__currency:
            return Money(self.__amount + other.__amount, self.__currency)
        else:
            print("Cannot add different currencies")

    def __sub__(self, other):
        if self.__currency == other.__currency:
            return Money(self.__amount - other.__amount, self.__currency)
        else:
            print("Cannot subtract different currencies")
