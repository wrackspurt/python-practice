# Integers Come In All Sizes
"""Task
Read four numbers, a, b, c, and d, and print the result of a^b + c^d.

Input Format
Integers a, b, c, and d are given on four separate lines, respectively.

Constraints
* 1 <= a <= 1000
* 1 <= b <= 1000
* 1 <= c <= 1000
* 1 <= d <= 1000

Output Format
Print the result of a^b + c^d on one line.
"""


if __name__ == '__main__':
    try:
        print(pow(int(input('enter a: ')), int(input('enter b: '))) +
              pow(int(input('enter c: ')), int(input('enter d: '))))
    except ValueError:
        print('wrong input')
