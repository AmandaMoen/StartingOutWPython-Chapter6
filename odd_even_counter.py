# June 22nd, 2010
# CS 110
# Amanda L. Moen
# 7. Odd/Even Counter
# In this chapter you saw an example of how to write an algorithm
# that determines whether a number is even or odd.  Write a program
# that generates 100 random numbers, and keeps a count of how many
# of those random numbers are even and how many are odd.

# Import random
import random

def is_even(number):
    # Determine whether the number is even.
    if (number %2) == 0:
        return True
    else:
        return False
        

# Main function.
def main():
    # The count for even numbers starts at 0.
    even = 0
    # The count for odd numbers starts at 0.
    odd = 0
    # Specify the range for the random numbers.
    for count in range(100):
        # Get a random number.
        number = random.randint(1, 100)
        # Display the number.
        print number

        # Set up the counter for the even and odd numbers)
        if (is_even(number)):
            even += 1
        else:
            odd += 1

    # Print how many even numbers there are.
    print "There are", even, "even numbers."
    # Print how many odd numbers there are.
    print "There are", odd, "odd numbers."
        
# Call the main function.
main()
