number = int(input("Give me a number"))

if number >= 1 and number <= 99:
    spaces = len(bin(number).split('b')[1]) * ' '
    for i in range(1, number + 1):
        oct_output = oct(i).split('o')[1]
        hex_output = hex(i).split('x')[1].upper()
        bin_output = bin(i).split('b')[1]
        print(f"{i}{spaces}{oct_output}{spaces}{hex_output}{spaces}{bin_output}")
else:
    print("End execution")
