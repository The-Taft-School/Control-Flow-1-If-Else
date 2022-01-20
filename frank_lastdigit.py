print("Is the last digit of your number divisible by three?")

a = (int(input("Enter a multidigit number ")))

b = a % 10
if b % 3 == 0:
    print("Yes, your number's last digit is divisible by three")
else:
    print("No, your number's last digit is not divisible by three")
