# There was a test in your class and you passed it. Congratulations!

# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return true if you're better, else false!

def better_then_average(class_point, your_score):
    average= sum(class_point)/ len(class_point)  #len define total no of list of test scores
    return your_score> average


print(better_then_average([2, 3], 5))  # Output should be True
print(better_then_average([21, 13], 5))

