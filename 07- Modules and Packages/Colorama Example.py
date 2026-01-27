"""
=============================================================================
COLORAMA MODULE DEMONSTRATION
=============================================================================
Colorama is a Python library that simplifies writing colored text to terminals.

Features:
- Cross-platform terminal color support (Windows, Mac, Linux)
- Support for foreground colors, background colors, and text styles
- Automatic terminal reset after colored output
- Easy-to-use constants for common colors

Installation: pip install colorama

Main Classes:
- Fore: Foreground colors (text color)
- Back: Background colors (text background)
- Style: Text styles (BRIGHT, DIM, NORMAL, RESET_ALL)
=============================================================================
"""

from colorama import init, Fore, Back, Style

# Initialize colorama (enables ANSI escape sequences on Windows)
# This step is important for proper color rendering, especially on Windows
init()


# ============================================================================
# FOREGROUND COLORS (TEXT COLOR)
# ============================================================================
print("=== FOREGROUND COLORS (Text Colors) ===\n")

print(Fore.RED + "This text is displayed in bright red color")
print(Fore.GREEN + "This text is displayed in bright green color")
print(Fore.YELLOW + "This text is displayed in bright yellow color")
print(Fore.BLUE + "This text is displayed in bright blue color")
print(Fore.MAGENTA + "This text is displayed in vibrant magenta color")
print(Fore.CYAN + "This text is displayed in bright cyan color")
print(Fore.WHITE + "This text is displayed in white color")
print(Fore.BLACK + "This text is displayed in black color")

# Reset to default color
print(Style.RESET_ALL + "Back to default color")


# ============================================================================
# BACKGROUND COLORS
# ============================================================================
print("\n=== BACKGROUND COLORS (Text Background) ===\n")

print(Back.RED + Fore.WHITE + "White text on red background")
print(Back.GREEN + Fore.BLACK + "Black text on green background")
print(Back.YELLOW + Fore.BLACK + "Black text on yellow background")
print(Back.BLUE + Fore.WHITE + "White text on blue background")

# Reset to default
print(Style.RESET_ALL + "Back to normal")


# ============================================================================
# TEXT STYLES
# ============================================================================
print("\n=== TEXT STYLES ===\n")

print(Style.BRIGHT + Fore.CYAN + "This text is displayed in bright/bold style")
print(Style.DIM + Fore.MAGENTA + "This text is displayed in dim/faint style")
print(Style.NORMAL + Fore.GREEN + "This text is displayed in normal style")

# Reset all styles and colors
print(Style.RESET_ALL + "All styles and colors reset to default")


# ============================================================================
# COMBINING COLORS AND STYLES
# ============================================================================
print("\n=== COMBINING COLORS AND STYLES ===\n")

print(Style.BRIGHT + Back.BLUE + Fore.YELLOW + "Bold yellow text on blue background")
print(Style.DIM + Back.WHITE + Fore.RED + "Dim red text on white background")
print(Style.NORMAL + Back.BLACK + Fore.CYAN + "Normal cyan text on black background")

# Final reset
print(Style.RESET_ALL)

print("Program completed successfully!")