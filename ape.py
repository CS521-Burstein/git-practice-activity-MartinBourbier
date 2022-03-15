def sum_digits(n):
    if n < 0:
        return sum_digits(-n)
    if n == 0:
        return 0
    else:
        remain = n % 10
        number = n // 10
        return remain + sum_digits(number)

def reverse_print(s):
    if len(s) == 0:
        print()
    else:
        print(s[-1], end='')
        reverse_print(s[:-1])
