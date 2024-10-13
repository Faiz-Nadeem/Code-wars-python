# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def reverse(x):
    return [int(digit) for digit in str(x)[::-1]]

# print(reverse(12345678))

f= input("Enter numbers you want to reverse: ")
print(reverse(f))

