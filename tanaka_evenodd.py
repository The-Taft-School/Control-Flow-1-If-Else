#Write a program to check whether a number entered by user is even or odd.
number = int(input("give me an integer: "))
if number % 2 == 0:
    print(f"wow cool {number} is even")
else:
    print(f"oh no why did you give me {number} it's an odd number")
