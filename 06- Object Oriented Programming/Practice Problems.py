"""
=============================================================================
OBJECT ORIENTED PROGRAMMING - PRACTICE PROBLEMS
=============================================================================
This module contains three practice problems demonstrating OOP concepts:

1. LINE CLASS - Calculates distance and slope between two coordinates
2. CYLINDER CLASS - Calculates volume and surface area of a cylinder
3. ACCOUNT CLASS - Bank account management with deposits and withdrawals

These problems reinforce:
- Constructor with parameters
- Mathematical calculations within methods
- Default parameters
- String representation (__str__)
- Data validation
=============================================================================
"""


# ============================================================================
# 1. LINE CLASS - GEOMETRIC CALCULATIONS
# ============================================================================
class Line():
    """
    A Line class that calculates distance and slope between two points.
    Uses coordinate geometry formulas.
    """
    
    def __init__(self, coor1, coor2):
        """
        Constructor - initializes a Line with two coordinate points.
        
        Args:
            coor1 (tuple): First coordinate point as (x1, y1)
            coor2 (tuple): Second coordinate point as (x2, y2)
        """
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        """
        Calculates the Euclidean distance between the two points.
        Formula: distance = √[(x2-x1)² + (y2-y1)²]
        
        Returns:
            float: The distance between coor1 and coor2
        """
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def slope(self):
        """
        Calculates the slope of the line between the two points.
        Formula: slope = (y2-y1) / (x2-x1)
        
        Returns:
            float: The slope of the line
            
        Raises:
            ZeroDivisionError: If x-coordinates are the same (vertical line)
        """
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


# Test the Line class
line_1 = Line((3, 2), (8, 10))
print(line_1.distance())  # Output: 9.433981... (distance between points)
print(line_1.slope())     # Output: 1.6 (slope of the line)


# ============================================================================
# 2. CYLINDER CLASS - VOLUME AND SURFACE AREA
# ============================================================================
class Cylinder():
    """
    A Cylinder class that calculates volume and surface area.
    Uses constant pi = 3.14 for calculations.
    """
    
    # Class attribute - constant value of pi
    pi = 3.14
    
    def __init__(self, height=1, radius=1):
        """
        Constructor - initializes a Cylinder with height and radius.
        Both parameters have default values of 1.
        
        Args:
            height (float): Height of the cylinder (default: 1)
            radius (float): Radius of the cylinder base (default: 1)
        """
        self.height = height
        self.radius = radius
    
    def volume(self):
        """
        Calculates the volume of the cylinder.
        Formula: Volume = π × r² × h
        
        Returns:
            float: The volume of the cylinder
        """
        return Cylinder.pi * self.radius * self.radius * self.height
    
    def surface_area(self):
        """
        Calculates the total surface area of the cylinder.
        Formula: Surface Area = 2πr² + 2πrh
        (Two circular bases + lateral surface area)
        
        Returns:
            float: The total surface area of the cylinder
        """
        return (2 * Cylinder.pi * self.radius * self.radius) + (2 * Cylinder.pi * self.radius * self.height)


# Test the Cylinder class
c = Cylinder(2, 3)
print(c.volume())           # Output: 56.52 (π × 3² × 2)
print(c.surface_area())     # Output: 94.2 (2π×3² + 2π×3×2)


# ============================================================================
# 3. ACCOUNT CLASS - BANK ACCOUNT MANAGEMENT
# ============================================================================
class Account():
    """
    An Account class representing a simple bank account.
    Supports deposits, withdrawals, and balance tracking.
    """
    
    def __init__(self, owner, balance=0):
        """
        Constructor - initializes a bank account.
        
        Args:
            owner (str): The account owner's name
            balance (float): Initial account balance (default: 0)
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits money into the account.
        Increases the balance by the specified amount.
        
        Args:
            amount (float): The amount to deposit (must be positive)
        """
        self.balance += amount
        print("Deposit Accepted ✓")
        print(f"Current Balance: ${self.balance}")
        
    def withdraw(self, amount):
        """
        Withdraws money from the account.
        Checks if sufficient funds are available before withdrawal.
        
        Args:
            amount (float): The amount to withdraw (must be positive)
        """
        if amount > self.balance:
            print("Withdrawal Rejected - Not enough balance available for this transaction")
        else:
            self.balance -= amount
            print("Withdrawal Accepted ✓")
            print(f"Current Balance: ${self.balance}")
    
    def __str__(self):
        """
        Returns a string representation of the account.
        Called by print() function.
        
        Returns:
            str: Formatted account information
        """
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"


# Test the Account class
account_1 = Account("Jose", 100)
print(account_1)          # Output: Account information using __str__
print(account_1.owner)    # Output: Jose
print(account_1.balance)  # Output: 100

account_1.deposit(50)     # Output: Deposit accepted, balance now 150
account_1.withdraw(30)    # Output: Withdrawal accepted, balance now 120
account_1.withdraw(150)   # Output: Rejection message - insufficient funds
