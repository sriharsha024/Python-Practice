# ============================================================================
# WHILE LOOPS - Python Iteration Control Flow Examples
# ============================================================================
# While loops execute a code block as long as a condition is True
# They continue until the condition becomes False
# ============================================================================


# ============================================================================
# 1. BASIC WHILE LOOP - SIMPLE COUNTER
# ============================================================================

# Initialize counter
i = 0

# Loop while i is less than 10
while i < 10:
    print(i)
    i = i + 1  # Increment counter (must increment, or loop runs forever!)
# Output:
# 0
# 1
# 2
# 3
# ... up to 9


# ============================================================================
# 2. WHILE LOOP WITH CONDITIONAL LOGIC - EVEN AND ODD NUMBERS
# ============================================================================

# Initialize counter
j = 0

# Loop while j is less than 20
while j < 20:
    # Check if j is divisible by 2 (even) or odd
    if j % 2 == 0:
        print("{} is even".format(j))
    else:
        print(f"{j} is odd")
    j += 1  # Equivalent to j = j + 1
# Output:
# 0 is even
# 1 is odd
# 2 is even
# ... and so on


# ============================================================================
# 3. WHILE LOOP WITH MULTIPLICATION TABLE
# ============================================================================

# Initialize counter
count = 0

# Loop while count is less than or equal to 10
while count <= 10:
    print("5 * {} = {}".format(count, count * 5))
    count += 1  # Increment counter
# Output:
# 5 * 0 = 0
# 5 * 1 = 5
# 5 * 2 = 10
# ... up to 5 * 10 = 50


# ============================================================================
# 4. BREAK STATEMENT - EXIT LOOP EARLY
# ============================================================================

# The break statement terminates the loop immediately

for item in range(1, 20):
    # Stop loop completely at 15 (don't execute remaining iterations)
    if item == 15:
        break
    print(f"Processing: {item}")

# Output:
# Processing: 1
# Processing: 2
# ... up to Processing: 14
# (Loop exits when item == 15, doesn't print 15-19)


# ============================================================================
# 5. CONTINUE STATEMENT - SKIP TO NEXT ITERATION
# ============================================================================

# The continue statement skips the rest of current iteration and goes to next

for item in range(1, 20):
    # Skip numbers divisible by 5 (don't print, go to next iteration)
    if item % 5 == 0:
        continue
    
    # Check divisibility and print appropriate message
    if item % 2 == 0 and item % 3 == 0:
        print(f"{item} is divisible by both 2 and 3")
    elif item % 3 == 0:
        print(f"{item} is divisible by 3")
    elif item % 2 == 0:
        print(f"{item} is even")
    else:
        # pass is a placeholder that does nothing
        pass
        print(f"{item} is odd")

# Output:
# 1 is odd
# 2 is even
# 3 is divisible by 3
# 4 is even
# (skips 5)
# 6 is divisible by both 2 and 3
# ... and so on


# ============================================================================
# LOOP CONTROL SUMMARY
# ============================================================================
# ┌──────────┬─────────────────────────────────────┬──────────────────┐
# │ Statement│ What it does                        │ Where to use     │
# ├──────────┼─────────────────────────────────────┼──────────────────┤
# │ break    │ Exit loop immediately               │ for / while      │
# │ continue │ Skip to next iteration              │ for / while      │
# │ pass     │ Placeholder (do nothing)            │ anywhere         │
# └──────────┴─────────────────────────────────────┴──────────────────┘
