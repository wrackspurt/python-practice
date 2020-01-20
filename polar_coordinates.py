# Polar Coordinates
"""Task
You are given a complex z. Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number z.
Note: complex() function can be used in python to convert the input as a complex number.

Constraints
Given number is a valid complex number.

Output Format
Output two lines:
The first line should contain the value of r.
The second line should contain the value of φ.
"""


import cmath


if __name__ == '__main__':
    try:
        print(*cmath.polar(complex(input('please, enter the complex number: '))), sep='\n')
    except ValueError:
        print('wrong input')
