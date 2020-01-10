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
        n = int(input('please, enter the number of other sets: '))
        if len(a) == m:
            for _ in range(n):
                operation, *length = input('please, enter the operation name and the length of the set: ').split()
                if operation == 'update':
                    update_set = set(map(int, input('please, enter the elements of the set: ').split()))
                    a.update(update_set)
                    if len(update_set) != int(length[0]):
                        print('something went wrong')
                elif operation == 'intersection_update':
                    intersection_update_set = set(map(int, input('please, enter the elements of the set: ').split()))
                    a.intersection_update(intersection_update_set)
                    if len(intersection_update_set) != int(length[0]):
                        print('something went wrong')
                elif operation == 'difference_update':
                    difference_update_set = set(map(int, input('please, enter the elements of the set: ').split()))
                    a.difference_update(difference_update_set)
                    if len(difference_update_set) != int(length[0]):
                        print('something went wrong')
                elif operation == 'symmetric_difference_update':
                    symm_diff_set = set(map(int, input('please, enter the elements of the set: ').split()))
                    a.symmetric_difference_update(symm_diff_set)
                    if len(symm_diff_set) != int(length[0]):
                        print('something went wrong')
        print(sum(a))
    except ValueError:
        print('wrong input')
