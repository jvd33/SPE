import timeit
from memory_profiler import memory_usage, profile


@profile
def recursive_fib_wrap(n):
    return recursive_fib(n)


def recursive_fib(n):
    if n < 2:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)


@profile
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
@profile
def super_digit_recursive_wrap(n, k):
    return super_digit_recursive(n, k)

@profile
def super_digit_recursive(n, k):
    if len(str(n)) <= 1:
        return n
    x = 0
    for i in str(n):
        x += int(i)
    return super_digit_recursive(x * k, 1)


def super_digit_stack(n=12345, k=3):
    result = 0
    stack = [int(n)]
    while stack:
        x = stack.pop()
        if len(str(x)) <= 1:
            result += x
        else:
            for i in str(x):
                result += int(i)
            stack.append(result * k)
            k = 1
            result = 0
    return result


if __name__ == "__main__":
    f = 10
    s = 123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345
    nr = 1
    fibr = timeit.Timer(lambda: recursive_fib_wrap(f))
    fibs = timeit.Timer(lambda: stack_fib(f))
    sr = timeit.Timer(lambda: print(super_digit_recursive_wrap(s, nr)))
    ss = timeit.Timer(lambda: print(super_digit_stack(s, nr)))

    print(format(fibr.timeit(1), '.20f'))
    print(format(fibs.timeit(1), '.20f'))
    print(format(sr.timeit(1), '.20f'))
    print(format(ss.timeit(1), '.20f'))

