# Capitalize!
"""Task
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format:
A single line of input containing the full name, S.

Constraints:
* 0 < len(S) < 1000
* The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format:
Print the capitalized string, S.
"""


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    """l = []
    for i in s.split():
        l.append(i.capitalize())
    return ' '.join(l)"""
    # return ' '.join([i.capitalize() for i in s])
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


if __name__ == '__main__':
    s = input('please, enter your first and last names: ')
    if len(s) == 0:
        print('no input data!')
    else:
        result = solve(s)
        print(result)
