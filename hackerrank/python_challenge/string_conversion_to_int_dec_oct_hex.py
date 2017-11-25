def print_formatted(number):
    # your code goes here
    # padding_len = len(str(bin(number))[2:])
    # print(padding_len)
    padding_len = len("{0:b}".format(n))
    for i in range(1, number+1):
        # print("{:>{}}{:>{}}{:>{}}{:>{}}".format(i, padding_len, str(oct(i))[2:], padding_len, str(hex(i))[2:].upper(), padding_len, str(bin(i))[2:], padding_len))
        print("{0:{padding_len}d} {0:{padding_len}o} {0:{padding_len}X} {0:{padding_len}b}".format(i, padding_len=padding_len))


print(print_formatted(17))