"""
=============================================================================
DATETIME MODULE DEMONSTRATION
=============================================================================
This script demonstrates how to work with Python's datetime module, including:
- time objects
- date objects
- datetime objects
- Replacing date/time values
- Calculating differences between dates and datetimes
=============================================================================
"""

import datetime


# ============================================================================
# 1. TIME OBJECTS
# ============================================================================
# time(hour, minute, second, microsecond)

mytime_1 = datetime.time(2, 20)
mytime_2 = datetime.time(13, 20, 25, 30)

print("Time 1:", mytime_1)
print("Time 2:", mytime_2)

# Accessing individual components
print("Hour:", mytime_1.hour)
print("Minute:", mytime_1.minute)
print("Second:", mytime_2.second)
print("Microsecond:", mytime_2.microsecond)

# Checking the type
print("Type of mytime_1:", type(mytime_1))


# ============================================================================
# 2. DATE OBJECTS
# ============================================================================
# Get today's date
today = datetime.date.today()

print("\nToday's Date:", today)
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

# Human-readable string representation
print("Formatted Date:", today.ctime())


# ============================================================================
# 3. DATETIME OBJECTS
# ============================================================================
from datetime import datetime

# Creating a specific datetime object
mydatetime = datetime(2025, 10, 3, 14, 20, 13)
print("\nOriginal datetime:", mydatetime)

# Replace returns a NEW datetime object (does not modify original)
mydatetime = mydatetime.replace(year=2026)
print("Updated datetime:", mydatetime)


# ============================================================================
# 4. DATE DIFFERENCE (TIMEDELTA)
# ============================================================================
from datetime import date

date1 = date(2026, 5, 6)
date2 = date(2024, 6, 8)

# Difference between two dates
diff = date1 - date2
print("\nDifference between dates:", diff)
print("Days difference:", diff.days)


# ============================================================================
# 5. DATETIME DIFFERENCE
# ============================================================================
mydatetime_1 = datetime(2025, 10, 3, 1, 58, 13)
mydatetime_2 = datetime(2023, 10, 6, 14, 20, 13)

# Difference between two datetime objects
diff_1 = mydatetime_1 - mydatetime_2
print("\nDifference between datetimes:", diff_1)
