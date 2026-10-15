def largest_num(x: int, y: int) -> int:
    """
    This function returns the largest number of two entered numbers
    """
    return max(x, y)

if __name__ == "__main__":
    x = int(input("Enter number 1:"))
    y = int(input("Enter number 2:"))
    print(largest_num(x, y))