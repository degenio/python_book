LOW_SPEED = 1
MEDIUM_SPEED = 2
HIGH_SPEED = 3

class Fan:
    """Initializer"""
    def __init__(self, speed=LOW_SPEED, is_on=False, radius=5, color='blue'):
        self.speed = speed
        self.is_on = is_on
        self.radius = radius
        self.color = color

    def __str__(self):
        status = "on" if self.is_on else "off"
        return "Speed:{:2d} radius: {:2d} " \
               "status: {:<10} color: {:<10s} " \
               .format(self.speed, self.radius, status, self.color)

def main():
    """Instantiate objects"""
    obj1 = Fan(speed=HIGH_SPEED, color='yellow', radius=10, is_on=True)
    print(obj1)
    obj2 = Fan(speed=MEDIUM_SPEED)
    print(obj2)
    # Display the percentage change

if __name__ == '__main__':
    main()
