#ways to handle errors created bu users in a way that doesn't break the code
#zero division, file not found, value error, type error, index error
#TypeEror represents and error when an operation could not be performed
#ValueError occurs when a function recieves an argument of the correct data type but an inappropiate value
#
class NegativeNumberError(Exception):
    pass
while True:
    try:
        num = int(input("Tell me a number: "))
    except ValueError:
        print("That wasn't a whole number")
        continue
    else:
        break
while True:
    try:
        numTwo = int(input("Tell me another number: "))
        if num <= 0:
            raise NegativeNumberError("Can't be a negative number")
    except (ValueError, NegativeNumberError):
        print("That wasn't a whole number")
        continue
    else:
        try:

            print(f'{str(num)} divided {str(numTwo)} equals {num/numTwo}')
            break
        except ZeroDivisionError:
            print("You can't divide by 0, try again")
            continue
    #finally:


