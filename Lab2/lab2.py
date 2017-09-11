import timeit
from memory_profiler import memory_usage, profile
import tracemalloc


def recursive_fib_wrap(n):
    return recursive_fib(n)


def recursive_fib(n):
    if n < 2:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)


def memoize(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]

    return helper


def stack_fib(n):
    result = 0
    stack = [n]
    while stack:
        x = stack.pop()
        if x < 2:
            result += x
        else:
            stack.append(x - 1)
            stack.append(x - 2)
    return result


# hackerrank recursive problem, returns the super digit of the digit sum of n
def super_digit_recursive_wrap(n, k):
    return super_digit_recursive(n, k)


def super_digit_recursive(n, k):
    n = str(n) * k
    if len(str(n)) <= 1:
        return n
    x = 0
    for i in str(n):
        x += int(i)
    return super_digit_recursive(x, 1)


def super_digit_stack(n=12345, k=3):
    n = str(n) * k
    result = 0
    stack = [int(n)]
    while stack:
        x = stack.pop()
        if len(str(x)) <= 1:
            result += x
        else:
            for i in str(x):
                result += int(i)
            stack.append(result)
            result = 0
    return result


if __name__ == "__main__":
    f = 30
    s = 98237450192834571829
    nr = 1000
    runs = 1
    fib = memoize(recursive_fib_wrap)
    fibx = timeit.Timer(lambda: fib(f))
    fibr = timeit.Timer(lambda: recursive_fib_wrap(f))
    fibs = timeit.Timer(lambda: stack_fib(f))
    sr = timeit.Timer(lambda: super_digit_recursive_wrap(s, nr))
    ss = timeit.Timer(lambda: super_digit_stack(s, nr))

    print(format(fibx.timeit(runs)/runs, '.20f'))

    print(format(fibr.timeit(runs)/runs, '.20f'))
    print(format(fibs.timeit(runs)/runs, '.20f'))
    print(format(sr.timeit(runs)/runs, '.20f'))
    print(format(ss.timeit(runs)/runs, '.20f'))

