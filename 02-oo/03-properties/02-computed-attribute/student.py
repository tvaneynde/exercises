class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight = weight_in_kg
        self.height = height_in_m

    def bmi(self):
        bmi = self.weight / (self.height**2)
        if bmi < 18.5:
            return "underweight"
        elif 18.5 > bmi < 25:
            return "normal"
        elif bmi < 25:
            return "overweight"
