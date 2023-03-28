num = int(input_num)
final = []
next_num = num
for i in options:
    if i > next_num:
        final.append('0')
    else:
        final.append('1')
        next_num = next_num % i
''.join(final)