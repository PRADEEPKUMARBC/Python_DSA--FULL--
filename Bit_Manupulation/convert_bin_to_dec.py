def convert_bin_to_dec(bin_digit):
    decimal_number = 0
    power = 0
    index = len(bin_digit) - 1
    while index >= 0:
        num = int(bin_digit[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number
print(convert_bin_to_dec("1110101"))