from datetime import date, timedelta


def half_birthday(yr, mo, d):
    birthday = date(yr, mo, d)
    my_half_birthday = birthday + timedelta(days=183)
    print("My birthday is: ", birthday)
    print("My half birthday is: ", my_half_birthday)


if __name__ == '__main__':
    half_birthday(2020, 4, 20)
    