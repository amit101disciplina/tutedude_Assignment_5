dict = {"Alice": 85, "Harry": 90, "Mike": 78}
key = input("Enter the student's name: ")
if key in dict.keys():
    print(f"{key}'s marks: {dict[key]}")
else:
    print("Student not found.")