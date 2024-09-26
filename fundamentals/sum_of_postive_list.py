# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def sum_of_positive_list(arr):
    positive_numbers=[x for x in arr if(x>0)]
    return sum(positive_numbers)

print(sum_of_positive_list([1,-4,6,-7,0]))