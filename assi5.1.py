students = {"ram": 95 , "ved" : 90 , "sid" : 85 , "rohan" : 80 }

user_input = input("Enter the Student's Name: ")
try:
    result = students[user_input.lower()]
    print(f"{user_input}'s marks: {result}")
except:
    print(f"{user_input} no such student")
