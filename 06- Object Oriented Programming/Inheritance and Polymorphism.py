"""
=============================================================================
INHERITANCE AND POLYMORPHISM IN OOP
=============================================================================
This module demonstrates key OOP concepts:

1. INHERITANCE - Derived classes inherit attributes and methods from base class
   - Parent class (Animal) defines common behavior
   - Child classes (Dog) override or extend parent methods

2. POLYMORPHISM - Objects of different types respond to the same method call
   - Same method name, different implementations
   - Enables writing flexible, reusable code

3. ABSTRACT METHODS - Methods meant to be overridden by subclasses
   - Raises NotImplementedError if not overridden
   - Enforces a contract that subclasses must implement the method
=============================================================================
"""


# ============================================================================
# PART 1: INHERITANCE
# ============================================================================

class Animal():
    """
    Base class representing a generic Animal.
    This class defines common attributes and methods for all animals.
    """
    
    def __init__(self):
        """Constructor - called when an Animal object is created."""
        print("Animal Created... ")
    
    def who_am_i(self):
        """Identifies the animal type."""
        print("Animal... ")
    
    def eat(self):
        """Basic behavior - eating (common to all animals)."""
        print("I am eating")


# Create an Animal instance and test its methods
animal_1 = Animal()
animal_1.who_am_i()  # Output: Animal...
animal_1.eat()       # Output: I am eating


class Dog(Animal):
    """
    Dog class that INHERITS from Animal.
    Demonstrates method overriding - Dog provides its own implementation
    of methods defined in the parent Animal class.
    """
    
    def __init__(self):
        """Constructor - overrides parent's __init__."""
        print("Dog created... ")
    
    def who_am_i(self):
        """Overrides parent method - more specific identification."""
        print("Dog... ")
    
    def bark(self, number):
        """New method specific to Dog class."""
        print(f"Dog is barking {number} times")


# Create a Dog instance
dog_2 = Dog()
print(type(dog_2))     # Output: <class '__main__.Dog'>
dog_2.who_am_i()       # Output: Dog... (overridden method)
dog_2.eat()            # Output: I am eating (inherited from Animal)
dog_2.bark(8)          # Output: Dog is barking 8 times


# ============================================================================
# PART 2: POLYMORPHISM - SAME METHOD NAME, DIFFERENT BEHAVIORS
# ============================================================================

class Dog_1():
    """Dog class with a speak method."""
    
    def __init__(self, name):
        """Initialize dog with a name."""
        self.name = name
    
    def speak(self):
        """Dog's way of speaking - barking."""
        return "The " + self.name + " is barking loudly... Woof! Woof!"


class Cat_1():
    """Cat class with a speak method."""
    
    def __init__(self, name):
        """Initialize cat with a name."""
        self.name = name
    
    def speak(self):
        """Cat's way of speaking - meowing."""
        return "The " + self.name + " says meow gracefully and purrs... Meow!"


# Create instances of different classes
niko = Dog_1("Niko")
felix = Cat_1("Felix")

# Same method name, different outputs based on object type
print(niko.speak())    # Output: The Niko is barking loudly... Woof! Woof!
print(felix.speak())   # Output: The Felix says meow gracefully and purrs... Meow!

# Polymorphism in action - iterate through different types with same method
print("\n--- Polymorphism: Same method, different objects ---")
for pet_in_class in [niko, felix]:
    print(pet_in_class.speak())


# Function that works with any object that has a speak() method
def pet_speak(pet):
    """
    Generic function that calls speak() on any pet object.
    Works with both Dog_1 and Cat_1 objects (polymorphism).
    
    Args:
        pet: Any object that has a speak() method
    """
    print(pet.speak())


print("\n--- Using polymorphic function ---")
pet_speak(niko)    # Works with Dog_1
pet_speak(felix)   # Works with Cat_1


# ============================================================================
# PART 3: ABSTRACT METHODS AND INHERITANCE CONTRACTS
# ============================================================================

class Animal_1():
    """
    Base class that defines an abstract method.
    Subclasses MUST override the speak() method.
    """
    
    def __init__(self, name):
        """Initialize with animal name."""
        self.name = name
    
    def speak(self):
        """
        Abstract method - must be implemented by subclasses.
        Raises NotImplementedError if called on base class.
        This enforces that subclasses must provide their own implementation.
        """
        raise NotImplementedError("Subclass must implement the speak() method")


class Dog_2(Animal_1):
    """Dog class that implements the abstract speak() method."""
    
    def speak(self):
        """
        Concrete implementation for Dog.
        Returns a string describing how a dog speaks.
        """
        return f"The {self.name} is barking loudly and wagging its tail with joy... Woof! Woof!"


class Cat_2(Animal_1):
    """Cat class that implements the abstract speak() method."""
    
    def speak(self):
        """
        Concrete implementation for Cat.
        Returns a string describing how a cat speaks.
        """
        return f"The {self.name} is purring softly and says meow in a charming way... Meow!"


# Create instances of subclasses
kino = Dog_2("Kino")
print(kino.speak())  # Output: The Kino is barking loudly and wagging its tail with joy... Woof! Woof!

darry = Cat_2("Darry")
print(darry.speak()) # Output: The Darry is purring softly and says meow in a charming way... Meow!