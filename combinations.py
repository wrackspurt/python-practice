# itertools.combinations()
"""Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string S and the integer value k.

Constraints
* 0 < k <= len(S)
* The string contains only UPPERCASE characters.

Output Format
Print the different combinations of string S on separate lines.
"""


from itertools import combinations

if __name__ == '__main__':
    s, k = input('please, enter the string and the integer value: ').split()
    try:
        if 0 < int(k) <= len(s):
            for i in range(1, int(k) + 1):
                for l in combinations(sorted(s), i):
                    print(*l, sep='')
        else:
            print('incorrect integer value')
    except ValueError:
        print('wrong input')
