options = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

def binary_string(input_number):
    num = int(input_number)
    final = []
    next_num = num
    for i in options:
        if i > next_num:
            final.append('0')
        else:
            final.append('1')
            next_num = next_num % i
    return ''.join(final)


if __name__ == "__main__":
    binary_string(input_num)
    