# Set .symmetric_difference() Operation
"""Task
Students of District College have subscriptions to English and French newspapers. Some students have subscribed to
English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the
English or the French newspaper but not both.

Input Format:
* The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
* The second line contains n space separated roll numbers of those students.
* The third line contains b, the number of students who have subscribed to the French newspaper.
* The fourth line contains b space separated roll numbers of those students.

Constraints:
0 < Total number of students in college < 1000

Output Format:
Output total number of students who have subscriptions to the English or the French newspaper but not both.
"""


if __name__ == '__main__':
    try:
        n = int(input())
        ns = set(map(int, input().split()))
        b = int(input())
        bs = set(int(i) for i in input().split())
        if len(ns) == n and len(bs) == b:
            print(len(ns.symmetric_difference(bs)))
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
