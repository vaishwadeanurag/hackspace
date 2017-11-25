# https://www.hackerrank.com/challenges/finding-the-percentage/problem
from statistics import mean
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = map(float, line)
        student_marks[name] = scores
    query_name = input()
    print("%.2f" % mean(student_marks[query_name]))
