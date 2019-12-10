# String Formatting
"""Task
Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should
be space-padded to match the width of the binary value of n.

Input Format:
A single integer denoting n.

Constraints:
* 1 <= n <= 99

Output Format:
Print n lines where each line i (in the range 1 <= i <= n) contains the respective decimal, octal, capitalized
hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.
"""
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(('{0:d}'.format(i)).ljust(n) + '\t' + ('{0:o}'.format(i)).ljust(n) + '\t' + ('{0:X}'.format(i)).ljust(n) +
              '\t' + ('{0:b}'.format(i)).ljust(n))"""


def print_formatted(number):
    b = len('{0:b}'.format(number))
    for i in range(1, number + 1):
        print(('{0:d}'.format(i)).rjust(b) + ' ' + ('{0:o}'.format(i)).rjust(b) + ' ' + ('{0:X}'.format(i)).rjust(b) +
              ' ' + ('{0:b}'.format(i)).rjust(b))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
