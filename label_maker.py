from calc import calculate_unit_price
from inputs import user_input


def main():
    data = user_input()
    calculated_data = calculate_unit_price(data)
    print(calculated_data)


if __name__ == '__main__':
    main()
