# Tuples
"""Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and
print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split(' ')))
    print(integer_list)
