#FizzBuzz in Python
#Starting out with a FizzBuzz program written in Python


#The code will first create a range of numbers between 1 and 100.
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#The code first checks to see if the number is divisible by both 3 and 5 and if it is, "FizzBuzz" is printed.
#If not, it then checks to see if it is divisble by 3, if it is, "Fizz" is printed.
#If not that, then it then checks to see if it is divisible by 5, if it is, "Buzz" is printed.
#If not any of the above, then the number itself is printed as an interger.