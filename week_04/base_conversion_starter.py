def main():
	"""Execute the program."""
	base_10_number = 0
	base_new = 0
	max_number = 0
	place_0 = 0
	place_1 = 0
	place_2 = 0
	place_3 = 0

	base_new = int(input("What base (2 - 9)?: "))
	# calculate the max_number here

	print("The max base 10 number to convert", "to that base is ", str(max_number))

	base_10_number = int(input("What number should we convert?: "))
	# perform your conversion here
	# print the solution here


if __name__ == '__main__':
	"""
	The main function is only invoked if we execute this module as a program.
	We do that like this on the command line (or by clicking the green triangle in PyCharm!):
	
	python3 base_conversion_starter.py
	
	What if this module contains code we want to use in other modules? Then we import it.
	When we import it, the module is not given the name "__main__" by the interpreter.
	So this code in the if-statement is not executed when we import.
	You should have a main() function. The main function is what drives the program."""
	main()
