# DefaultDict Tutorial
"""Task
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There
are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print
the indices of each occurrence of m in group A. If it does not appear, print -1.

Input Format
* The first line contains integers, n and m separated by a space.
* The next n lines contains the words belonging to group A.
* The next m lines contains the words belonging to group B.

Constraints
* 1 <= n <= 10000
* 1 <= m <= 100
* 1 <= length of each word in the input <= 100

Output Format
* Output m lines.
* The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
"""


from collections import defaultdict


if __name__ == '__main__':
    try:
        n, m = list(map(int, input('please, input the integers n and m: ').split()))
        if 1 <= n <= 10000 and 1 <= m <= 100:
            a, b = defaultdict(list), list()
            for i in range(1, n + 1):
                a[input('please, enter the element of group a: ')].append(str(i))
            for _ in range(m):
                b.append(str(input('please, enter the element of group b: ')))
            for l in b:
                if l in a.keys():
                    print(*a[l])
                else:
                    print(-1)
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
