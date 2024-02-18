from application import salary
from application/db import people


def main():
    get_employees()
    calculate_salary()
    current_date = datetime.datetime.now().date()
    print(current_date)


if __name__ == '__main__':
    print('START METHOD MAIN')
    main()



