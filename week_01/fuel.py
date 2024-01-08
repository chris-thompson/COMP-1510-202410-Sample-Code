"""
When we request information from the user, we should specify what
kind of information we want.

Remember that the input function creates a string for us to use.

We must convert the string to the correct data type.
"""

kilometres_per_mile = 1.6
litres_per_gallon = 4.54

odometer_start = int(input('Enter starting odometer reading as an integer: '))
odometer_end = int(input('Enter ending odometer reading as an integer: '))
litres_used = float(input('Enter liters of fuel used as a floating point number: '))

kilometres_driven = odometer_end - odometer_start
miles_drives = kilometres_driven / kilometres_per_mile
gallons_used = litres_used / litres_per_gallon

litres_per_100km = round((100 * (litres_used / kilometres_driven)), 1)
miles_per_gallon = round(miles_drives / gallons_used, 1)

print("Your fuel efficiency is:")
print('\t', litres_per_100km, 'liters per 100 kilometers')
print('\t', miles_per_gallon, 'miles per gallon')
