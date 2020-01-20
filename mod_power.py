# Power - Mod Power
"""Task
You are given three integers: a, b, and m, respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format
The first line contains a, the second line contains b, and the third line contains m.

Constraints
* 1 <= a <= 10
* 1 <= b <= 10
* 2 <= m <= 1000
"""


if __name__ == '__main__':
    try:
        a, b, m = int(input('please, enter a: ')), int(input('please, enter b: ')), int(input('please, enter m: '))
        if 1 <= a <= 10 and 1 <= b <= 10 and 2 <= m <= 1000:
            print(pow(a, b), pow(a, b, m), sep='\n')
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
