number =int(input("Enter a number of your choice: "))

last_digit = number % 10
if(last_digit % 3 == 0 ):
    print("{} is divisible by 3 ".format(last_digit))
else:
    print("{} is not divisible by 3".format(last_digit))
