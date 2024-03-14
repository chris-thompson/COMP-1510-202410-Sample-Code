class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize a new Dog object."""
        self.__name = name.title()
        self.__age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.__name + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.__name + " rolled over!")


def main():
    """
    Drive the program.
    """
    my_dog = Dog('Hecataeus', 6)
    your_dog = Dog('Metrodorus', 3)

    # print("My dog's name is " + my_dog.__name + ".")

    # Report anyone who does this it is a crime against humanity
    print("My dog is " + str(my_dog._Dog__age) + " years old.")
    my_dog.sit()
    your_dog.roll_over()


if __name__ == "__main__":
    main()
