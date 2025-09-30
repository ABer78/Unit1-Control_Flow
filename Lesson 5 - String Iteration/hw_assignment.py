password = input("Please enter a password: ")
print(f"Password: {password}")

# Character Counts:
length = len(password)
uppercase = 0
lowercase = 0
digits = 0
special_char_count = 0
special_char = "!.,:;?/{[]}|\@#$%^&*()`~-_+="

print(f"Legth: {length}")

for char in password:
    if "A" <= char <= "Z":
        uppercase += 1
    if "a" <= char <= "z":
        lowercase += 1
    if "0" <= char <= "9":
        digits += 1
    if char in special_char:
        special_char_count += 1

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digits}")
print(f"Special characters: {special_char_count}")

# Requirements Check:
if length >= 8:
    print("Length (8+ characters): PASSED")
else:
    print("Length(8+ characters): More characters needed in password")

if uppercase > 0:
    print("Uppercase length: PASSED")
else:
    print(
        "Uppercase length: Please include at least one uppercase letter in your password"
    )

if lowercase > 0:
    print("Lowercase length: PASSED")
else:
    print(
        "Lowercase length: Please include at least one lowercase letter in your password"
    )

if digits > 0:
    print("Digits: PASSED")
else:
    print("Digits: Please include at least one digit in your password")

if special_char_count > 0:
    print("Special characters: PASSED")
else:
    print(
        "Special characters: Please include at least one special character in your password"
    )
