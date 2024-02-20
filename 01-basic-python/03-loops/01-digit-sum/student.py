def digit_sum(n):
    result = 0
    while n:
        result += n % 10
        n //= 10
    return result


def last_digit(n):
    return n % 10


def remove_last_digit(n):
    return n // 10
