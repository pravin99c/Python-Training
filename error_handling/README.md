
## 1.You're going to write an interactive calculator!
## Input:

User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
(e.g. 1 + --> Split user input and check whether the resulting list is valid:
-> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
-> If the second input is not '+' or '-', again raise a FormulaError
-> If the input is valid, perform the calculation and print out the result.
-> The user is then prompted to provide new input, and so on until the user enters quit.

   
## Output :
   ry to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# testcases

| Input | Output |
| ------ | ------ |
| 1+5 | 6.0 |
| 5-2 | 3.0 |
## Development



## 2. Create while loop which increase counter by one every second.

## Input:
    -> Start count from 0
    -> Stop while loop when counter is grater than 500
    Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x) 


## Output :
   not stop any keyboard key press
# testcases

| Input | Output |
| ------ | ------ |
| ctrl+c | continue |
| ctrl+x | continue |

## Development