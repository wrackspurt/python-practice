# Designer Door Mat
"""Task
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
specifications:
* Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

Input Format:
A single line containing the space separated values of N and M.

Constraints:
* 5 < N < 101
* 15 < M < 303

Output Format:
Output the design pattern.
"""


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(int(n/2)):
        print(('.|.' * i).rjust(int((m - 2) / 2), '-') + '.|.' + ('.|.' * i).ljust(int((m - 2) / 2), '-'))
    print('WELCOME'.center(m, '-'))
    for i in reversed(range(int(n/2))):
        print(('.|.' * i).rjust(int((m - 2) / 2), '-') + '.|.' + ('.|.' * i).ljust(int((m - 2) / 2), '-'))
