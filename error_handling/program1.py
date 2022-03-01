# You're going to write an interactive calculator!
# User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
# (e.g. 1 + --> Split user input and check whether the resulting list is valid:

from sys import flags


class FormulaError(Exception):
   pass
while True:
    inputs=list(map(str,input("Enter your input : ").split()))
    try:
        if 'quit' in inputs[0]:
            break
        else:
            try:
                val = float(inputs[0])
                val2= float(inputs[2])
                if inputs[1]=='+':
                    print(val+val2)
                elif inputs[1]=='-':
                    print(val-val2)
                else:
                    raise FormulaError
            except ValueError:
                raise FormulaError
    except FormulaError:
        print("Try again next time")

            
        

