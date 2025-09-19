age = input("Enter your age:")
if age:
    age = int(age)

rating = input("Enter the movie rating:")

if rating == "G":
    print("You can watch this movie")
elif rating == "PG" and age >= 6:
    print("You can watch this movie")
elif rating == "PG" and age < 6:
    print("You can not watch this movie")
elif rating == "PG-13" and age >= 13:
    print("You can watch this movie")
elif rating == "PG-13" and age < 13:
    print("You can not watch this movie")
elif rating == "R" and age >= 17:
    print("You can watch this movie")
elif rating == "R" and age < 17:
    print("You can not watch this movie")
