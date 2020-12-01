
#ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Unable to Divide By Zero")
#IndexError
arr = [1, 2, 3]

try:
    print(arr[3])
except IndexError:
    print('Index not found in array')

#KeyError
dicti = {"1" : 1, "2" : 2, "3" : 3}

try:
    print(dicti["4"])
except KeyError:
    print('Key not found in dictionary')

#ModuleNotFoundError
try:
    import flask
except ModuleNotFoundError:
    print("Module not found")

#Design a simple calculator app with try and except for all use cases
symbols = '+ - x / % \n'

try:
    input_one = int(input('Enter your 1st input :'))
    print(symbols)
    chosen_symbol = input('Choose your symbol from above :')
    input_two = int(input('Enter your 2st input :'))

    if chosen_symbol in symbols:
        if chosen_symbol == '+':
            print(input_one, '+', input_two, '=',input_one + input_two)
        elif chosen_symbol == '-':
            print(input_one, '-', input_two, '=',input_one - input_two)
        elif chosen_symbol == 'x':
            print(input_one, 'x', input_two, '=',input_one * input_two)
        elif chosen_symbol == '/':
            print(input_one, '/', input_two, '=',input_one / input_two)
        elif chosen_symbol == '%':
            print(input_one, '%', input_two, '=',input_one % input_two)
except ValueError:
    print("Enter Proper Numbers For Input!")
except ZeroDivisionError:
    print("Unable to Divide by Zero (0) !")

#print one message if the try block raises a NameError and another for other errors
try:
    print(newArr)
except NameError:
      print("newArr not defined")
except:
      print("Unknown Error")

#Try getting an input inside the try catch block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")