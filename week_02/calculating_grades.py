"""
An instructor gives five-point quizzes that are assigned letter grades
according to the scale: 5 -> A, 4 -> B, 3 -> C, 2 -> D, 1 -> F, 0 -> F.

Write a program that takes a quiz score as input and prints the grade.

Your program should work like this:
    >> Enter the quiz score: 3
    >> The letter grade is: C
"""

score = int(input("Enter the quiz score: "))

if score == 5:
    grade = 'A'
elif score == 4:
    grade = 'B'
elif score == 3:
    grade = 'C'
elif score == 2:
    grade = 'D'
elif (score == 1) or (score == 0):
    grade = 'F'
else:
    grade = 'Undefined'

print("The letter grade is:", grade)
