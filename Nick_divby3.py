num = int(input("enter a number: "))
ones = num % 10
if ones % 3 == 0:
    print("last digit divisible by 3")
else:
    print("last digit is not divisible by 3")
