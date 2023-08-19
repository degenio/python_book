# Car Class
class Car:
    """Initializer"""
    def __init__(self, title, distance, consumption, fuel_cost):
        self.title = title
        self.distance = distance
        self.consumption = consumption
        self.fuel_cost = fuel_cost

    def __str__(self):
        return "Title: {:<10s} Distance: {:7.2f}, Consumption: {:7.2f}, " \
               "Fuel Cost: {:7.2f}  " \
            .format(self.title, self.distance, self.consumption, self.fuel_cost)

    def calculate_trip_cost(self):
        return (self.distance * self.consumption * self.fuel_cost) / 100.0


def main():
    """Instantiate object"""
    title = input('Enter the car name:')
    distance = float(input('Enter the distance:'))
    fuel_cost = float(input('Enter the fuel cost:'))
    consumption = float(input('Enter the car consumption:'))
    car1 = Car(title=title, distance=distance,
               consumption=consumption, fuel_cost=fuel_cost)
    print(car1)

    # Calculate the trip cost
    total_cost = car1.calculate_trip_cost()
    print('The total cost of the trip is: {:.2f}'.format(total_cost))


if __name__ == '__main__':
    main()