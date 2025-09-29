text = "Hello World"
count = 0
# for char in text:
#     if "A" <= char <= "z":
#         if char == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "U":
#             count += 1
# print(f"Vowels in '{text}': {count}")

vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        count += 1
print(f"Vowels in '{text}': {count}")

text2 = "ABC123abc"
for i in text2:
    if "0" <= text2 <= "9":
        print(f"Digit at position {i}: {text2[i]}")

word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")
