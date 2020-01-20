# Find Angle MBC
"""Task
Your task is to find angle MBC in degrees.

Input Format
* The first line contains the length of side AB.
* The second line contains the length of side BC.

Constraints
* 0 < AB <= 100
* 0 < BC <= 100
* Lengths AB and BC are natural numbers.

Output Format
Output MBC in degrees.

Note: Round the angle to the nearest integer.
"""

import math

if __name__ == '__main__':
    try:
        ab, bc = int(input('enter the length of side AB: ')), int(input('enter the length of side BC: '))
        if 0 < ab <= 100 and 0 < bc <= 100:
            print(round(math.degrees(math.acos(((0.5 * (math.sqrt(ab ** 2 + bc ** 2))) ** 2 + bc ** 2 -
                                                (math.sqrt(ab ** 2 + bc ** 2) / 2) ** 2) /
                                               (2 * (0.5 * (math.sqrt(ab ** 2 + bc ** 2))) * bc)))), '°', sep='')
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
