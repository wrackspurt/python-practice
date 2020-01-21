# Introduction to Sets
"""Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the
average of all the plants with distinct heights in her greenhouse.
Formula used:
Average = (Sum of Distinct Heights) / (Total Number of Distinct Heights)

Input Format:
* The first line contains the integer, N, the total number of plants.
* The second line contains the N space separated heights of the plants.

Constraints:
0 <= N <= 100

Output Format:
Output the average height value on a single line.
"""


def average(array):
    st = set(array)
    return sum(st) / len(st)


if __name__ == '__main__':
    try:
        n = int(input('please, enter the total number of plants: '))
        arr = list(map(int, input('please, enter the heights of the plants: ').split()))
        if len(arr) == n:
            result = average(arr)
            print(result)
        else:
            print('incorrect input')
    except ValueError:
        print("wrong input")

