# Iterables and Iterators
"""Task
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based
indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format
* The input consists of three lines.
* The first line contains the integer N, denoting the length of the list.
* The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
* The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Constraints
* 1 <= N <= 10
* 1 <= K <= N
* All the letters in the list are lowercase English letters.

Output Format
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
Note: The answer must be correct up to 3 decimal places.
"""

from itertools import combinations


if __name__ == '__main__':
    try:
        n, l, k = int(input('enter the length of the list: ')), input('enter the elements of the list: ').split(), \
                  int(input('enter the number of indices to be selected: '))
        if 1 <= n <= 10 and len(l) == n and 1 <= k <= n:
            comb = list(combinations(l, k))
            print(round(len(list(filter(lambda x: 'a' in x, comb))) / len(comb), 3))
            # print('{:.3f}'.format((len([r for r in comb if 'a' in r]) / len(comb))))
        else:
            print('wrong input')
    except ValueError:
        print('incorrect input')
