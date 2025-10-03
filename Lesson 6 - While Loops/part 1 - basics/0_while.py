# syntax:
"""
initialize variable
while conidtion(test variable):
    code block
    increment/decrement variable
"""

num = 5
while num >= 1:
    print(num)
    num -= 1

print("")

num2 = 1
sum = 0
# while num2 <= 10:
#     sum += num2
#     num2 += 1
# print(f"The sum of numbers from 1-10 is: {sum}")
while num2 <= 10:
    sum += num2
    if num2 < 10:
        print(num2, end="+")
    else:
        print(num2, end="=")
    num2 += 1
print(sum)  # 1+2+3+4+5+6+7+8+9+10=55
print(sum)  # 55

print()

# Sum of digits
# take user input as int, and add the digits
# number = input("Enter a number: ")
total = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     total += int(char)
# print(f"Total: {total}")

# i = 0
# while i < len(number):
#     total += int(number[i])
#     i += 1
# print(f"Total: {total}")

number = int(input("Enter a number: "))
n = number
sum = 0
while n > 0:
    digit = n % 10  # get the last digit
    sum += digit  # add to the sum
    n = n // 10  # remove the last digit
print(f"The sum of digits in {number}: {sum}")

print()

# Algorithm - count digits (as integer)
number = 54321
n = number
count = 0
while n > 0:
    count += 1
    n = n // 10
print(f"The number of digits in {number}: {count}")
