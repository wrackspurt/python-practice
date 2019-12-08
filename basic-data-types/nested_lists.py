# Nested Lists
"""Task
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print
the name(s) of any student(s) having the second lowest grade.
"""
if __name__ == '__main__':
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]
    students.sort(key=lambda i: i[1])
    scores = [i[1] for i in students]
    names = [i[0] for i in students]
    minimum = min(scores)
    while scores[0] == minimum:
        scores.remove(scores[0])
        names.remove(names[0])
    res = []
    for i in range(0, len(scores)):
        if scores[i] == min(scores):
            res.append(names[i])
            res.sort()
    for i in res:
        print(i)
