# Alphabet Rangoli
"""Task
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art
based on creation of patterns.)
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical
order).

Input Format:
Only one line of input containing N, the size of the rangoli.

Constraints:
0 < N < 27

Output Format:
Print the alphabet rangoli in the format explained above.
"""

# import string


def print_rangoli(size):
    # 1st way
    alph = 'a'
    for i in range(98, 123):
        alph += chr(i)
    # 2nd way
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # 3rd way
    # alph = string.ascii_lowercase
    line = alph[0:size]
    for i in range(size-1, -size, -1):
        j = abs(i)
        print('-' * 2 * j + '-'.join(line[n:j:-1] + line[j:n]) + '-' * 2 * j)


if __name__ == '__main__':
    try:
        n = int(input('please, enter the number: '))
        if n < 0:
            print('the number is not whole!')
        elif n == 0:
            print("it's a zero!")
        elif n >= 27:
            print('the number is too big!')
        else:
            print_rangoli(n)
    except ValueError:
        print("it's not an integer!")

