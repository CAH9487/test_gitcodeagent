def reverse(x: int) -> int:
    """Reverse digits of a 32-bit signed integer.

    If the reversed integer overflows, return 0.
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    rev = 0

    while x_abs != 0:
        digit = x_abs % 10
        x_abs //= 10
        if rev > (INT_MAX - digit) // 10:
            return 0
        rev = rev * 10 + digit

    result = sign * rev
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result


if __name__ == "__main__":
    examples = [123, -123, 120]
    for num in examples:
        print(f"reverse({num}) = {reverse(num)}")
