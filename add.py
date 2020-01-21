# Set .add()
"""Task
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her
collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input Format:
* The first line contains an integer N, the total number of country stamps.
* The next N lines contains the name of the country where the stamp is from.

Constraints:
0 < N < 1000

Output Format:
Output the total number of distinct country stamps on a single line.
"""


if __name__ == '__main__':
    try:
        n = int(input('please, enter the total number of country stamps: '))
        s = set()
        for _ in range(n):
            s.add(input('please, enter the name of the country where the stamp is from: '))
        print(len(s))
    except ValueError:
        print('wrong input')

    """without .add():
    try:
        print(len(set(input('please, enter the name of the country where the stamp is from: ') for _ in
                      range(int(input('please, enter the total number of country stamps: '))))))
    except ValueError:
        print('wrong input')"""
