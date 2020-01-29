# Maximize It!
"""Task
You are given a function f(X) = X^2. You are also given K lists. The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(X1) + f(X2) + ... + f(Xk)) % M
* Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
* % denotes the modulo operator.
Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares
of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to
the problem.

Input Format
* The first line contains 2 space separated integers K and M.
* The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space
separated integers denoting the elements in the list.

Constraints
* 1 <= K <= 7
* 1 <= M <= 1000
* 1 <= Ni <= 7
* 1 <= Magnitude of elements in list <= 10^9

Output Format
Output a single integer denoting the value Smax.
"""
from itertools import product

if __name__ == '__main__':
    try:
        k, m = list(map(int, input(' please, enter the values of k and m: ').split()))
        if 1 <= k <= 7 and 1 <= m <= 1000:
            n = []
            for _ in range(k):
                _, *ni = input('please, enter the list (the 1st value denotes the length of the list): ').split()
                n.append([int(i) for i in ni])
            """s = 0
            res = []
            for l in list(product(*n)):
                for i in l:
                    s += i**2
                    res.append(s % m)
                s = 0
            print(max(res))"""
            print(max(list(map(lambda x: sum(i ** 2 for i in x) % m, list(product(*n))))))
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
