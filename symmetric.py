# Symmetric Difference
"""Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference
indicates those values that exist in either M or N but do not exist in both.

Input Format:
* The first line of input contains an integer, M.
* The second line contains M space-separated integers.
* The third line contains an integer, N.
* The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
"""

if __name__ == '__main__':
    try:
        m = int(input('please, enter the integer (m): '))
        ml = set(map(int, input('please, enter the list of integers (m): ').split()))
        n = int(input('please, enter the integer (n): '))
        nl = set(map(int, input('please, enter the list of integers (n): ').split()))
        if len(ml) == m and len(nl) == n:
            nnl = nl.difference(ml)
            nml = ml.difference(nl)
            res = nnl.union(nml)
            for r in sorted(res):
                print(r)
        else:
            print('wrong input')
    except ValueError:
        print('incorrect input')
