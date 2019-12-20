# The Minion Game
"""Task
Your task is to determine the winner of the game and their score.

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Input Format:
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
0 < len(S) <= 10^6

Output Format:
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
"""


def minion_game(string):
    vowels = 'AEIOU'
    kevin = sum(len(string) - i for i in range(len(string)) if string[i] in vowels)
    stuart = sum(len(string) - i for i in range(len(string)) if string[i] not in vowels)
    """for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i"""
    if kevin > stuart:
        print('%s %d' % ('Kevin', kevin))
    elif kevin < stuart:
        print('%s %d' % ('Stuart', stuart))
    elif kevin == stuart:
        print('Draw')


if __name__ == '__main__':
    s = input('please, enter the word: ').strip()
    if len(s) == 0:
        print('no input data!')
    else:
        if s.isalpha():
            for i in range(len(s)):
                if s[i].islower():
                    s = s.replace(s[i], s[i].upper())
            minion_game(s)
        else:
            print('incorrect input!')
