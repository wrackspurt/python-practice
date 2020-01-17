# Set Mutations
"""Task
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

Input Format:
* The first line contains the number of elements in set A.
* The second line contains the space separated list of elements in set A.
* The third line contains integer N, the number of other sets.
* The next 2 * N lines are divided into N parts containing two lines each.
* The first line of each part contains the space separated entries of the operation name and the length of the other
set.
* The second line of each part contains space separated list of elements in the other set.

Constraints:
* 0 < len(set(A)) < 1000
* 0 < len(otherSets) < 100
* 0 < N < 100

Output Format:
Output the sum of elements in set A.
"""


if __name__ == '__main__':
    try:
        m = int(input('please, enter the number of elements in set A: '))
        a = set(int(i) for i in input('please, enter the elements of set A: ').split())
        if len(a) == m:
            for _ in range(int(input('please, enter the number of other sets: '))):
                operation, *length = input('please, enter the operation name and the length of the set: ').split()
                # 1
                """commands = {
                    'update': "a.update(set(map(int, input('please, enter the elements of the set: ').split())))",
                    'intersection_update': "a.intersection_update(set(map(int, input('please, enter the elements of the set: ').split())))",
                    'difference_update': "a.difference_update(set(map(int, input('please, enter the elements of the set: ').split())))",
                    'symmetric_difference_update': "a.symmetric_difference_update(set(map(int, input('please, enter the elements of the set: ').split())))"}
                try:
                    exec(commands[operation])
                except KeyError:
                    print('something went wrong')"""
                # 2
                try:
                    eval('a.{0}({1})'.format(operation,
                                             set(map(int, input('please, enter the elements of the set: ').split()))))
                except AttributeError:
                    print('something went wrong')
                    exit(-1)
        else:
            print('incorrect input')
            exit(-1)
        print(sum(a))
    except ValueError:
        print('wrong input')
