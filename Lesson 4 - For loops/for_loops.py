# Three forms of range() function
# 1. range(stop)
for i in range(5):
    print(i)
print("")

# 2. range(start, stop)
for i in range(3, 8):
    print(i)
print("")

# 3. range(start, stop, step)
# counting up
for i in range(2, 11, 2):  # 2, 4, 6, 8, 10
    print(i)
print("")

# counting down
for i in range(10, 1, -2):  # 10, 8, 6, 4, 2
    print(i)
print("")

# countdown timer
# import time
# for seconds in range(10, -1, -1):
#     print(f"{seconds} - seconds ")
#     time.sleep(1) # wait 1 second  between numbers
# print("BLAST OFF! 🚀")
print("")

# multiplication table
# Take user input for the number and print the table (from 1 to 10)
num = int(input("Enter a number (1-12): "))
if 1 <= num <= 12:
    for i in range(1, 13):
        result = num * i
        print(f"{num} * {i} = {result}")
        # print(f"{num} * {i:2d} = {result: 3d}")
else:
    print("Please enter a number between 1 and 12")
print("")

# 4. range()
for i in range(2):
    print(i)

print("")
