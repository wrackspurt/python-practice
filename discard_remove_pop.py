# Set .discard(), .remove() & .pop()
"""Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format:
* The first line contains integer n, the number of elements in the set s.
* The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than
or equal to 9.
* The third line contains integer N, the number of commands.
* The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints:
* 0 < n < 20
* 0 < N < 20

Output Format:
Print the sum of the elements of set s on a single line.
"""

if __name__ == '__main__':
    try:
        n = int(input('please, enter the number of elements in the set s: '))
        s = set(map(int, input('please, enter the elements of set s: ').split()))
        if len(s) == n:
            for _ in range(int(input('please, enter the number of commands: '))):
                comm, *num = input().split()
                if comm == 'pop':
                    s.pop()
                elif comm == 'remove':
                    s.remove(int(num[0]))
                elif comm == 'discard':
                    s.discard(int(num[0]))
            print(sum(s))
        else:
            print('incorrect input')
    except ValueError:
        print('wrong input')
