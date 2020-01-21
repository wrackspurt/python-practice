# Check Strict Superset
"""Task
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

Input Format:
* The first line contains the space separated elements of set A.
* The second line contains integer n, the number of other sets.
* The next n lines contains the space separated elements of the other sets.

Constraints:
* 0 < len(set(A)) < 501
* 0 < N < 21
* 0 < len(otherSets) < 101

Output Format:
Print True if set A is a strict superset of all other N sets. Otherwise, print False.
"""


if __name__ == '__main__':
    try:
        a = set(map(int, input('please, enter the elements of set A: ').split()))
        n = int(input('please, enter the number of other sets: '))
        if len(a) > 0 and n > 0:
            lst = []
            for _ in range(n):
                s = set(int(i) for i in input('please, enter the elements of set: ').split())
                if len(s) > 0:
                    lst.append(s)
                else:
                    print('incorrect input')
                    exit(-1)
            print(all(a.issuperset(l) for l in lst))
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
