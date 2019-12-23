# Text Wrap
"""Task
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
"""


import textwrap


def wrap(string, max_width):
    """l = []
    for i in range(0, len(string), max_width):
        l.append(string[i:i + max_width])
    return '\n'.join(l)"""
    return '\n'.join([string[i:i + max_width] for i in range(0, len(string), max_width)])
    # return textwrap.TextWrapper(width=max_width).fill(text=string)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
