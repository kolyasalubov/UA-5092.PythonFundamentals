def largenumb(a, b):
    """
    Returns the largest number of two numbers.
    """
    if a > b:
        return a
    if a < b:
        return b

num1 = int(input("First number:"))
num2 = int(input("Sec number:"))

print("Leargest number:", largenumb(num1, num2))