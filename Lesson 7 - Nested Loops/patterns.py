# Pyramid Pattern

# Step-by-step guide:
# Row 0: 4 spaces, 1 star
# Row 1: 3 spaces, 3 star
# Row 2: 2 spaces, 5 star
# Row 3: 1 spaces, 7 star
# Row 4: 0 spaces, 9 star

rows = 5
# Step 1: create an outer loop for the row
for i in range(rows):
    # Step 2: print the spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Step 3: print the stars 2*i+1
    for k in range(2 * i + 1):
        print("*", end="")
    # Step 4: print a new line
    print()
