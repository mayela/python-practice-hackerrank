def number_to_string(number):
    if number >= 1 and number <= 150:
        numbers = [str(i) for i in range(1, number + 1)]
        return "".join(numbers)

number_to_string(20)