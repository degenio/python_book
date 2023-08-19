class Patient:  # Entity or domain class
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Weight: {}, Height: {}".format(
            self.name, self.age, self.weight, self.height)

    def calculate_bmi(self):
        return self.weight / self.height ** 2
