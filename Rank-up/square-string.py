# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
#
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
#
# Note: The function accepts an integer and returns an integer.

def square(num):
    num_str= str(num)
    square_str= ''.join(str(int(digit)**2) for digit in num_str)
    return int(square_str)

result= square(3345)
print(result)
#  3--9 3--9 4--16 5--25 -----991625 output