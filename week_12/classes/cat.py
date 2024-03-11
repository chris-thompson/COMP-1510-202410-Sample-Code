class Cat:
    """
    Meow. This class represents a Cat. It needs comments!
    """

    counter = 0  # There is one counter in memory and every Cat can access it

    def __init__(self, name: str, age: int):
        self.__name = name

        if age < 0:
            raise ValueError("Cats cannot have a negative age, try again!")
        else:
            self.__age_in_years = age

        self.__id = Cat.counter
        Cat.counter += 1

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age_in_years

    def __str__(self):
        return "Cat{id " + str(self.__id) + " of " + str(Cat.counter) + "}"


def main():
    """
    Drive the program.
    """
    print(Cat.counter)

    try:
        one = Cat("Mr. Snuggle-bunny", -1)
    except ValueError:
        print("NO! Bad kitty!")
    else:
        print(one)
    two = Cat("Duchess", 8)
    three = Cat("Cleo", 8)

    print(two)
    print(three)

    print(three.counter)
    print(Cat.counter)


if __name__ == "__main__":
    main()
