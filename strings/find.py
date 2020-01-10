# Find a string
"""Task
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""


def count_substring(string, sub_string):
    count = 0
    pos = string.find(sub_string)
    if pos == -1:
        return count
    else:
        for _ in range(0, len(string)):
            while pos != -1:
                pos = string.find(sub_string, pos + 1)
                count += 1
        return count


if __name__ == '__main__':
    string = input('please, enter a string: ').strip()
    sub_string = input('please, enter a substring: ').strip()

    count = count_substring(string, sub_string)
    print(count)
