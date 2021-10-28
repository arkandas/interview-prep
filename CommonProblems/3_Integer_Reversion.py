# Reverse an integer

def integer_reverser(inputInt):

    int_reversed = 0
    mod_remainder = 0

    while inputInt > 0:
        mod_remainder = inputInt % 10
        inputInt = inputInt // 10
        int_reversed = int_reversed * 10 + mod_remainder
    return int_reversed

if __name__ == "__main__":
    print(integer_reverser(4567363434))