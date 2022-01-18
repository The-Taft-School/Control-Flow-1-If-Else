#Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
a = int(input("give me a long fun integer: "))
b = a % 10

if b == 3:
    print(f"the last digit of {a} is divisble by 3")
elif b == 6:
    print(f"the last digit of {a} is divisble by 3")
elif b == 9:
    print(f"the last digit of {a} is divisble by 3")
else:
    print(f"the last digit of {a} is not divisible by 3")
