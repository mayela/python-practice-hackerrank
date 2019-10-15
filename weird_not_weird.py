def weird_not_weird(n):
    #breakpoint()
    if not n % 2 == 0:
        return "Weird"
    elif n % 2 == 0 and n in range(2,6):
        return "Not weird"
    elif n % 2 == 0 and n in range(6, 21):
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not weird"