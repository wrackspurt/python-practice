# Check Subset
"""Task
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format:
* The first line will contain the number of test cases, T.
* The first line of each test case contains the number of elements in set A.
* The second line of each test case contains the space separated elements of set A.
* The third line of each test case contains the number of elements in set B.
* The fourth line of each test case contains the space separated elements of set B.

Constraints:
* 0 < T < 21
* 0 < Number of elements in each set < 1001

Output Format:
Output True or False for each test case on separate lines.
"""


if __name__ == '__main__':
    try:
        for _ in range(int(input('please, enter the number of test cases: '))):
            n = int(input('please, enter the number of elements in set A: '))
            a = set(map(int, input('please, enter the elements of set A: ').split()))
            m = int(input('please, enter the number of elements in set B: '))
            b = set(int(i) for i in input('please, enter the elements of set B: ').split())
            if len(a) == n and len(b) == m:
                print('result:', a.issubset(b))
            else:
                print('incorrect input')
    except ValueError:
        print('wrong input')
