def is_a_leap_year(year):
    if 1900 <= year and year <= 10 ** 5:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

year = int(input("Enter a number"))
print(is_a_leap_year(year))