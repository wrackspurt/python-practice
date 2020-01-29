# itertools.product()
"""Task
You are given a two lists A and B. Your task is to compute their cartesian product AxB.

Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

Constraints
* 0 < A < 30
* 0 < B < 30

Output Format
Output the space separated tuples of the cartesian product.
"""

from itertools import product

if __name__ == '__main__':
    a, b = set(map(int, input().split())), set(map(int, input().split()))
    for l in list(product(a, b)):
        print(l, end=' ')
