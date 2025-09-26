# String Indexing
word = "Python"
#       012345 (positive indexing)
#      -654321 (negative indexing)
word[0]  # P (first character)
word[1]  # y (second character)
word[5]  # n (last character)

word[-1]  # n (last character)
len(word)  # length of string
word[len(word) - 1]  # n (last character)

# String Slicing
word[0:3]  # Pyt (index 0, 1, 2)
word[
    :3
]  # Pyt (index 0, 1, 2) (if there is no first number, it starts from the beginning)

word[2:5]  # tho (index 2, 3, 4)
word[2 : len(word)]  # thon (2, 3, 4, 5)
word[2:6]  # thon (index 2, 3, 4, 5)
word[
    2:
]  # thon (index 2, 3, 4, 5) (if there is no second number, it prints the rest of the string)

word[-3:]  # hon (index -3, -2, -1 / 3, 4, 5)

# Part 1 - String Iteration Patterns
# Direct character iteration
word = "Hello"

for char in word:
    print(char)  # H e l l o

# Index based iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")

# Character classification
# char = "A"
char = input("Press a key: ")

# check character types using ASCII ranges
if "A" <= char <= "z":
    print(f"'{char}' is a letter")
if "A" <= char <= "Z":
    print(f"'{char}' is uppercase")
if "a" <= char <= "z":
    print(f"'{char}' is lowercase")
if "0" <= char <= "9":
    print(f"'{char}' is a digit")
