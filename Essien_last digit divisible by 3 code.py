number =int(input("Enter a number of your choice: "))

last_digit = number % 10
if(last_digit % 3 == 0 ):
    print(number," is divisible by 3 ")
else:
    print(number," is not divisible by 3")
