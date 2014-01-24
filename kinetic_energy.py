# June 22nd, 2010
# CS 110
# Amanda L. Moen
# 5. Kinetic Energy
# In physics, an object that is in motion is said to have
# kinetic energy.  The following formula can be used to
# determine a moving object's kinetic energy:
#       KE = 1/2 mv**2
# The variables in the formula are as follows: KE is the
# kinetic energy in joules, m is the object's mass in
# kilograms, and v is the object's velocity in meters per
# second.
# Write a function named kinetic_energy that accepts an
# object's mass in kilograms and velocity in meters per
# second as arguments.  The function should return the
# amount of kinetic energy that the object has.  Write a
# program that asks the user to enter values for mass and
# velocity, and then calls the kinetic_energy function to
# get the object's kinetic energy.

# Create the kinetic_energy function.
def kinetic_energy(m, v):
    # The formula for kinetic energy.
    KE = 0.5 * m * v**2
    return KE

# Main function
def main():
    # Ask for the mass in kilograms.
    m = input("Please enter the mass in kilograms: ")
    # Ask for the velocity in meters per second.
    v = input("Please enter the velocity in meters per second: ")

    # Run the kinetic_energy function and return the 'answer'
    print kinetic_energy(m, v), "is the object's kinetic energy."

# Call main function
main()
