"""
=============================================================================
MATH AND RANDOM MODULES DEMONSTRATION
=============================================================================
This script demonstrates commonly used functions from:
- math module   : Mathematical operations and constants
- random module : Random number generation and selection utilities

These modules are widely used in:
- Scientific calculations
- Simulations
- Games
- Data analysis
=============================================================================
"""

import math
import random


# ============================================================================
# 1. MATH MODULE BASICS
# ============================================================================
print("Value of PI:", math.pi)
print("Square root of 9:", math.sqrt(9))

# Trigonometric functions
print("Sine of 45 (in radians):", math.sin(45))
print("90 degrees in radians (PI/2):", math.pi / 2)
print("Sine of 90 degrees:", math.sin(math.pi / 2))

# Rounding functions
print("Ceiling of 5.5:", math.ceil(5.5))
print("Floor of 5.5:", math.floor(5.5))

# Angle conversions
print("Degrees of PI/2:", math.degrees(math.pi / 2))
print("Radians of 180 degrees:", math.radians(180))

# Mathematical constants
print("Value of e:", math.e)
print("Infinity value:", math.inf)
print("NaN value:", math.nan)

# Logarithmic functions
print("Natural log of e:", math.log(math.e))
print("Log base 10 of 1000:", math.log(1000, 10))


# ============================================================================
# 2. RANDOM MODULE BASICS
# ============================================================================
# Generate a random integer between 0 and 100
print("\nRandom integer between 0 and 100:", random.randint(0, 100))

# Seeding random for reproducible results
random.seed(101 / 42)

# Create a list of numbers from 0 to 19
mylist = list(range(0, 20))
print("Original list:", mylist)

# Select a single random element
print("Random choice from list:", random.choice(mylist))

# Select multiple random elements (with replacement)
print("Random choices (k=10):", random.choices(mylist, k=10))

# Select multiple unique random elements (without replacement)
print("Random sample (k=10):", random.sample(population=mylist, k=10))

# Shuffle the list in place
random.shuffle(mylist)
print("Shuffled list:", mylist)

# Generate a random floating-point number within a range
print("Random float between 0 and 520:", random.uniform(0, 520))
