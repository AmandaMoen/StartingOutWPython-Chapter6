# June 22nd, 2010
# CS 110
# Amanda L. Moen
# 3. Maximum of Two Values
# Write a function named maximum that accepts two integer
# values as arguments and returns the value that is the
# greater of the two.  For example, if 7 and 12 are passed
# as arguments to the function, the function should return
# 12.  Use the function in a program that prompts the user
# to enter two integer values.  The program should display
# the value that is the greater of the two.

# Write a function that takes two numbers and returns
# the greater of the two numbers.
def maximum(num1, num2):
    # Create an if-else statement.
    # If num 1 is bigger return num1
    if num1 > num2:
        return num1
    else:
        return num2

# Main function.
def main():
    # Ask the user to enter two numbers.
    num1 = input("Please enter your first number: ")
    num2 = input("Please enter your second number: ")

    # Return/Print which number is greater.
    print maximum(num1, num2), "is the greater of the two numbers."

# Call the main function.
main()
