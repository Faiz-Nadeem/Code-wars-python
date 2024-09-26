# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
#
# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def operations(operator,value1,value2):
    if operator== '+':
        return value1+value2
    elif operator== '-':
        return value1-value2
    elif operator== '*':
        return value1*value2
    elif operator== '/':
        if(value2>0):
            return value1/value2
        else:
            return "number cant be divided by zero"
    else:
        return "invalid number"
print(operations("+",2,3))