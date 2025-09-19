age = input("Enter your age:")
if age:
    age = int(age)

rating = input("Enter the movie rating (G, PG, PG-13, R):")

if age == "":
    print("Please enter your age")
elif rating == "":
    print("Please enter the movie rating")
elif rating == "G":
    print("APPROVED: You can watch this movie")
elif rating == "PG" and age >= 6:
    print("APPROVED: You can watch this movie")
elif rating == "PG" and age < 6:
    print("DENIED: You can not watch this movie")
elif rating == "PG-13" and age >= 13:
    print("APPROVED: You can watch this movie")
elif rating == "PG-13" and age < 13:
    print("DENIED: You can not watch this movie")
elif rating == "R" and age >= 17:
    print("APPROVED: You can watch this movie")
elif rating == "R" and age < 17:
    print("DENIED:You can not watch this movie")
