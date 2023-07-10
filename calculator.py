# calculator.py
# Author: Ryan Seaman
# Simple calculator to demonstrate importing a package and how users interact with the program.

def help():
    str = "This is a simple Calculator Program.\nThere are 5 functions:\n\t-add\n\t-subract\n\t-multiply\n\t-divide\n\t-exponent\n\nAll functions take two parameters (both numbers).\n\tFor examples:\n\t\tcalc.example('functionname')"
    print(str)

def example(fx):
    if fx == 'add' or fx =='calc.add':
        print('calc.add(5,4)\t-->\t5 + 4')
    elif fx == 'subtract' or fx =='calc.subtract':
        print('calc.subtract(5,4)\t-->\t5 - 4')
    elif fx == 'multiply' or fx =='calc.multiply':
        print('calc.multiply(5,4)\t-->\t5 * 4')
    elif fx == 'divide'or fx =='calc.divide':
        print('calc.divide(5,4)\t-->\t5 / 4')
    elif fx == 'exponent'or fx =='calc.exponent':
        print('calc.exponent(5,4)\t-->\t5 ^ 4')
    else:
        print(fx, "is is not an included function in calculator.\nThere are 5 functions:\n\t-add\n\t-subract\n\t-multiply\n\t-divide\n\t-exponent")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def exponent(x,y):
    return x**y

