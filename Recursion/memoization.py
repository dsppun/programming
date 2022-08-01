def fibonacci_series_without_memoization(n):
    """
    Fibonacci Series is series of numbers where next number is found by adding up the two numbers before it.
    1,1,2,3,5,8,13 .. etc
    """
    if n < 2:
        return n
    else:
        return fibonacci_series_without_memoization(n - 1) + fibonacci_series_without_memoization(n - 2)


def fib_with_memoization(n):
    cache_store = {}  # Used to store result of each iteration

    def fib_recur(n):
        """
        Base Recursion Code
        """
        if n in cache_store:  # Check if this is already calculated and return if yes
            return cache_store[n]
        elif n < 2:
            return n
        else:
            res = fib_recur(n - 1) + fib_recur(n - 2)

        cache_store[n] = res  # Store result for future use.
        return res

    return fib_recur(n)


def climb_stairs(n):
    """
    To reach 2 --> 2 combos
             3 --> 3 combos
             4 --> 5 combos
             5 --> 7 combos

    So, it is following the fibonacci series
    """
    dict_cache = {}

    def get_steps(n):
        if n in dict_cache:
            return dict_cache[n]
        if n < 2:
            return n
        else:
            out = get_steps(n - 1) + get_steps(n - 2)
        dict_cache[n] = out
        return out
    return get_steps(n)


print(climb_stairs(9))

print(fibonacci_series_without_memoization(9))
print(fib_with_memoization(9))
