"""
refactoring_calories.py

This program initializes a dictionary, and then repeatedly prompts the user
for new food items and their associated calories. The new items are added
to the dictionary. Each time an item is added, the list of foods is printed
along with total and average calories.

The program works as is, and contains no bugs.

Unfortunately this program is just written as one big script, and is not very
well organized. It needs to use functions like we have discussed in class, a
proper command loop inside a main function, and unit tests to prove it all works.

Your tasks:

1. Refactor this program so that it is composed of short, atomic, and
   re-usable functions
2. Add a suite of unit tests that prove everything works as it should.
"""

# Global Constant YUCK!
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
             "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
             "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
             }

# Input loop
new_item = input("Enter food item to add, or 'q' to exit: ")
while new_item != "q":

    new_item_calories = int(input("Enter calories for " + new_item + ": "))
    _calories[new_item] = new_item_calories

    total_calories = 0
    for item in _calories:
        total_calories = total_calories + _calories[item]

    food_item_names = []
    for item in _calories:
        food_item_names.append(item)

    avg_calories = total_calories / len(_calories)

    print("\nFood Items:", sorted(food_item_names))
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)

    new_item = input("Enter food item to add, or 'q' to exit: ")
