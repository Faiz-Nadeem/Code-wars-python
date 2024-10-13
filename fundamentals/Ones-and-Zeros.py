# #Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
#
# Examples:
#
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

def one_and_zeros(arr):
    return int("".join(map(str, arr)), 2)

print(one_and_zeros([1,0,0,1,1]))

# The map() function is used to apply the str() function to each element of the array arr.
# This converts the integers 0 and 1 into strings '0' and '1'.
# Example: if arr = [1, 0, 1, 1], map(str, arr) converts it to ['1', '0', '1', '1'].
# "".join(map(str, arr)):
#
# The "".join() method joins the elements of the list into a single string.
# It takes the list ['1', '0', '1', '1'] and joins them into the string "1011".
# Now we have a binary number in string format.
# int("1011", 2):
#
# The int() function is used to convert the string "1011" to an integer.
# The 2 tells Python that the string is in binary format (base 2).
# This converts the binary string "1011" into the decimal number 11.