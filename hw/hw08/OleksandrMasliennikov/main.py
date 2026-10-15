from areas_calc import rectangle_area, triangle_area, circle_area


def run_areas_calc():
    print('Select a geometric shape to calculate the area:')
    print('1 - Rectangle')
    print('2 - Triangle')
    print('3 - Circle')

    choice = input('Your choice (1-3): ')

    try:
        if choice == '1':
            a = float(input('a: '))
            b = float(input('b: '))
            print(f'Area: {rectangle_area(a, b):.2f}')
        elif choice == '2':
            h = float(input('h: '))
            a = float(input('a: '))
            print(f'Area: {triangle_area(h, a):.2f}')
        elif choice == '3':
            r = float(input('r: '))
            print(f'Area: {circle_area(r):.2f}')
        else:
            print('Invalid choice')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    run_areas_calc()
