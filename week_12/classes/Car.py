"""
Represent a simple car.
"""


class Car:
    """A simple car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.__manufacturer = manufacturer # every car object has its own manufacturer string
        self.__model = model # every car object has its own model string
        self.__year = year # every car object has its own year integer
        self.__odometer_reading = 0 # every car object has its own odometer reading

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.__year) + ' ' + self.__manufacturer + ' ' + self.__model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.__odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            raise ValueError("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.__odometer_reading += miles

    def __str__(self):
        """Return a string representation of the car."""
        return str(self.get_descriptive_name())


def main():
    """
    Drive the program.
    """
    hot_rod = Car("Mazda", "MX5", 2008)
    print(hot_rod) # What does this print?
    # hot_rod.__year = 2050 # Don't access dunders directly!
    try:
        hot_rod.update_odometer(-1000)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
