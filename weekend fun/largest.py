number1 = int(input("enter a number: "))
number2 = int(input("enter a number: "))
number3 = int(input("enter a number: "))

largest = number1 

if number2 > largest:

   largest = number2


if largest < number3:
   largest = number3
   print(largest)


else:
   print(largest)


