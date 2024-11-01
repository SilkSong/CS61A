from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


# To-do
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # return sum(x ** 2 for x in sorted([x,y,z])[:2]) 更复杂的一种实现
    return x**2 + y**2 + z**2 - max(x, y, z) ** 2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    for num in range(1, n):
        if n % num == 0:
            result = num
    return result


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


# To-do
def cond():
    "*** YOUR CODE HERE ***"
    print("42")
    return True


def true_func():
    "*** YOUR CODE HERE ***"
    print("47")


def false_func():
    "*** YOUR CODE HERE ***"
    print("42")


# To-do
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    def travel(length, n):
        # print(n)
        if n == 1:
            return length
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        length += 1
        return travel(length, n)

    length = 1
    return travel(length, n)


# n is the range
def find_max_hailstone(n):
    maximum_length = 1
    result_number = 0
    for x in range(1, n):
        length = hailstone(x)
        print(length)
        print(x)
        if length > maximum_length:
            maximum_length = length
            result_number = x
    print(f"maximum length is {maximum_length}, the number is {result_number}")
