a=(int(input("Enter a multidigit number ")))

print("Is the last digit of your number divisible by three?")

b = a % 10
if b % 3 == 0:
    print("Yes")
else:
    print("No")
