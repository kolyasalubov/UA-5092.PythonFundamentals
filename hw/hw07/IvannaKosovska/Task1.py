x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))

largestNum = lambda x, y: x if x > y else y
"""
This lambda function returns the largest number of two entered numbers
"""
print(largestNum(x, y))