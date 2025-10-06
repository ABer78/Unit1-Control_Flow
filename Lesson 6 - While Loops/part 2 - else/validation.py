# Input Validation 1 - Username Validation
while True:
    username = input("Enter a username (3-15 characters): ")
    if len(username) < 3:
        print("Username is too short; Min: 3 characters")
        continue
    if len(username) > 15:
        print("Username is too long; Max: 15 characters")
        continue
    # check if username has a space
    has_space = False
    for char in username:
        if char == " ":
            has_space = True
            break
    if has_space:
        print("No spaces allowed")
        continue
    # username validation passed
    print(f"Username '{username}' accepted \n")
    break
