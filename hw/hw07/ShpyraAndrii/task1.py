def get_largest_num(n1, n2):
    """Returns the largest number of two numbers"""
    return n1 if n1 >= n2 else n2


if __name__ == '__main__':
    print(get_largest_num(5, 4))
    print(get_largest_num(1, 3))
    print(get_largest_num(2, 0))
    print(get_largest_num.__doc__)
