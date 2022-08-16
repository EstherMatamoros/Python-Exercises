# Primer Ejercicio

import numbers


def divisible_by_3_5(): 
    for number in range(1, 100):

        if  number%3 == 0 and number%5 == 0 :
            print("FizzBuzz")
        elif  number%5 == 0:
            print("Buzz")
        elif number%3 == 0 :
            print("Fizz")
        else :
            print(number)

divisible_by_3_5()




