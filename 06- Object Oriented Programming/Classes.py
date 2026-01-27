"""
=============================================================================
OBJECT ORIENTED PROGRAMMING - CLASSES INTRODUCTION
=============================================================================
This module demonstrates fundamental OOP concepts:
- Class definition
- Instance attributes (initialized in __init__)
- Class attributes (shared across all instances)
- Methods (functions within a class)
- Creating and using objects

Examples:
1. Dog class - showing attributes and methods
2. Circle class - showing math calculations
=============================================================================
"""


# ============================================================================
# 1. DOG CLASS - BASIC CLASS STRUCTURE
# ============================================================================
class Dog():
    """
    A Dog class that demonstrates basic OOP concepts.
    
    Class Attributes:
        species (str): Shared by all Dog instances
    
    Instance Attributes:
        name (str): The dog's name
        breed (str): The dog's breed
        spots (bool): Whether the dog has spots
    """
    
    # Class attribute - shared across all instances
    species = "Mammal"
    
    def __init__(self, name, breed, spots):
        """
        Constructor - initializes a Dog object.
        
        Args:
            name (str): The dog's name
            breed (str): The dog's breed
            spots (bool): Whether the dog has spots (True/False)
        """
        # Instance attributes - unique to each object
        self.name = name
        self.breed = breed
        self.spots = spots
    
    def bark(self, number):
        """
        Method that makes the dog bark a specified number of times.
        
        Args:
            number (int): Number of times the dog barks
        """
        print(f"{self.name} is barking {number} times")


# ============================================================================
# DOG CLASS - CREATE AND USE INSTANCES
# ============================================================================

# Create first dog instance
dog_1 = Dog(name="Sam", breed="German Shepherd", spots=False)

# Access and print attributes
print(type(dog_1))     # Output: <class '__main__.Dog'>
print(dog_1.name)      # Output: Sam
print(dog_1.breed)     # Output: German Shepherd
print(dog_1.spots)     # Output: False

# Call method
dog_1.bark(5)          # Output: Sam is barking 5 times

# Create second dog instance
dog_2 = Dog(name="Daw", breed="Police", spots=True)

# Access and print attributes
print(type(dog_2))     # Output: <class '__main__.Dog'>
print(dog_2.name)      # Output: Daw
print(dog_2.breed)     # Output: Police
print(dog_2.spots)     # Output: True

# Call method
dog_2.bark(3)          # Output: Daw is barking 3 times


# ============================================================================
# 2. CIRCLE CLASS - GEOMETRIC CALCULATIONS
# ============================================================================
class Circle():
    """
    A Circle class that demonstrates geometric calculations.
    
    Class Attributes:
        pi (float): Constant value of pi (3.14)
    
    Instance Attributes:
        radius (float): The circle's radius
        area (float): The circle's area (calculated in constructor)
    """
    
    # Class attribute - constant used in calculations
    pi = 3.14
    
    def __init__(self, radius):
        """
        Constructor - initializes a Circle object.
        
        Args:
            radius (float): The circle's radius
        """
        # Instance attributes
        self.radius = radius
        # Calculate area when object is created
        self.area = Circle.pi * self.radius * self.radius
    
    def circumference(self):
        """
        Calculates the circumference of the circle.
        Formula: C = 2 * π * r
        
        Returns:
            float: The circumference of the circle
        """
        return 2 * Circle.pi * self.radius
    
    def area_check(self):
        """
        Calculates the area of the circle.
        Formula: A = π * r²
        
        Returns:
            float: The area of the circle
        """
        return Circle.pi * self.radius * self.radius


# ============================================================================
# CIRCLE CLASS - CREATE AND USE INSTANCE
# ============================================================================

# Create a Circle instance with radius 7
circle_1 = Circle(7)

# Access and print attributes
print(circle_1.radius)          # Output: 7
print(circle_1.area)            # Output: 153.86 (3.14 * 7 * 7)

# Call methods to calculate geometric properties
print(circle_1.circumference()) # Output: 43.96 (2 * 3.14 * 7)
print(circle_1.area_check())    # Output: 153.86 (3.14 * 7 * 7)