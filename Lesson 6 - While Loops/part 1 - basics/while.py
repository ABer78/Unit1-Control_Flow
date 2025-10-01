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
number = input("Enter a number: ")
total = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     total += int(char)
# print(f"Total: {total}")

i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(f"Total: {total}")
