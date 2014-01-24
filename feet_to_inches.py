# June 22nd, 2010
# CS 110
# Amanda L. Moen
# 1. Feet to Inches
# One foot equals 12 inches.  Write a function named
# feet_to_inches that accepts a number of feet as an
# argument, and returns the number of inches in that
# many feet.  Use the function in a program that prompts
# the user to enter a number of feet and then displays
# the number of inches in that many feet.

# Write a function that converts feet to inches.
def feet_to_inches(feet):
    return 12.0 * feet


# Main function
def main():
    # Ask the user for the number of feet to be converted to inches.
    feet = input('Enter the number of feet you would like converted to inches: ')

    # Convert feet to inches
    inches = feet_to_inches(feet)
    # Print inches
    print 'There are', inches, "inches in", feet, "feet."

# Call the main function.
main()
