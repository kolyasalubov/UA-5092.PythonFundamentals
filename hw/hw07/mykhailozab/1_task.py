#Task1
#Task1. Write a function that returns the largest number of two numbers 
#(use DocStrings documentation strings in the function).

print("Task1")
def max_2_number(a,b):
    """
    This function returns the largest of two numbers
    input parameters: a - int, b - int
    output: int
    """
    return max(a,b)

print("White 2 numbers:")
a = input()
b = input()
print(f"This {max_2_number(a,b)} the largest number")


