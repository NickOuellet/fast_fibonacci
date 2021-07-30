import time

def fast_fib(n):
    look_up_table = dict()
    look_up_table[0] = 0
    look_up_table[1] = 1
    def fast_fib_helper(n):
        if n in look_up_table.keys():
            return look_up_table[n]
        look_up_table[n] = fast_fib_helper(n-1) + fast_fib_helper(n-2)
        return look_up_table[n]
    return fast_fib_helper(n)

def slow_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return slow_fib(n-1) + slow_fib(n-2)

start_fast = time.time()
print(fast_fib(40))
print(time.time() - start_fast)

start_slow = time.time()
print(slow_fib(40))
print(time.time() - start_slow)
