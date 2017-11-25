# https://www.hackerrank.com/challenges/string-validators/problem
import string
if __name__ == '__main__':
    s = input()
    alpha = False
    num = False
    lower = False
    upper = False
    for i in s:
        if not lower and i in string.ascii_lowercase:
            lower = True
            alpha = True
        if not upper and i in string.ascii_uppercase:
            upper = True
            alpha = True
        if not num and i.isdigit():
            num = True
        if lower and upper and num:
            break
    print(alpha or num)
    print(alpha)
    print(num)
    print(lower)
    print(upper)