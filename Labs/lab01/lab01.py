from operator import mul
from functools import reduce


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    """ My tedious answer
    i = 0
    result = 1
    while i < k:
        result *= n
        n -= 1
        i += 1
    return result
    """
    """ Good Answer
    result = 1
    while k > 0:
        result *= n
        n -= 1
        k -= 1
    return result
    """
    if k == 0:
        return 1
    else:
        return reduce(mul, range(n, n - k, -1))


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    """ My tedious answer

    num_of_bit = len(str(y))
    result = 0
    while num_of_bit >= 1:
        divisor = pow(10, num_of_bit - 1)
        quotient, remainder = y // divisor, y % divisor
        result += quotient
        y = remainder
        num_of_bit -= 1
    return result
    """
    ans = 0
    while y:
        ans += y % 10
        y = y // 10
    return ans


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    """ My tedious answer
    count = 0
    while n:
        if n % 10 == 8:
            count += 1
        else:
            if count == 1:
                count -= 1
        n //= 10

        if count == 2:
            return True
    return False
    """

    """ Good Answer
    count = 0
    while n:
        if n % 10 == 8:
            count += 1
            if count == 2:
                return True
        else:
            count = 0
        n //= 10
    return False
    """

    while n:
        last = n % 10
        n //= 10
        if 8 == last == n % 10:
            return True
    return False
