"""
=============================================================================
MAIN PROGRAM - MODULES AND PACKAGES DEMONSTRATION
=============================================================================
This script demonstrates how to import and use functions from:
1. A standalone module (mymodule)
2. Packages (MyMainPackage)
3. Sub-packages (MyMainPackage.SubPackage)

It shows two different import styles:
- FROM imports (importing specific functions)
- Module imports (importing the module itself)

Directory Structure:
    myprogram.py (this file)
    mymodule.py
    MyMainPackage/
        __init__.py
        some_main_script.py
        SubPackage/
            __init__.py
            mysubscript.py
=============================================================================
"""


# ============================================================================
# IMPORT STYLE 1: DIRECT FUNCTION IMPORTS
# ============================================================================
# Import specific functions directly from modules and packages
from mymodule import my_func
from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage.mysubscript import sub_report

print("=== STYLE 1: DIRECT FUNCTION IMPORTS ===\n")

# Call functions imported directly
my_func()           # Calls function from standalone module
report_main()       # Calls function from package module
sub_report()        # Calls function from sub-package module


# ============================================================================
# IMPORT STYLE 2: MODULE IMPORTS
# ============================================================================
# Import entire modules/packages and access functions via dot notation
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

print("\n=== STYLE 2: MODULE IMPORTS ===\n")

# Call functions by accessing them through the module object
some_main_script.report_main()  # Access function via module.function()
mysubscript.sub_report()        # Access function via module.function()

print("\n=== Program completed successfully! ===")