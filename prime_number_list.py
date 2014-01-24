# June 22nd, 2010
# CS 110
# Amanda L. Moen
# 9. Prime Number List
# This exercise assumes you have already written the is_prime
# function in Programming Exercise 8.  Write another program
# that displays all of the prime numbers from 1 through 100.
# The program should have a loop that calls the is_prime function.

# Create the is_prime function from Exercise 8.
def is_prime(number):
    # Set up the testing loop.
    for test in range(2,number):
        if ( (number % test) == 0):
            # The number's not prime.
            return False
    # If we get to this point, the number must be prime.
    return True

def main():
    # Program needs to list all of the prime numbers 1-100
    for value in range(1, 101):

        # Create a loop that calls the is_prime function.
        if ( is_prime(value) ):
            print value, ' is prime'

# Call the main function.
main()
