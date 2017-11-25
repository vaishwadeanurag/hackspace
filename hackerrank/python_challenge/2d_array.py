"""
Question URl - https://www.hackerrank.com/challenges/2d-array/problem
"""

def calculatesum(arr):
    max_sum = None
    for i in range(4):
        for m in range(4):
            res = 0
            for j in range(m, m+3):
                print("res=%s + a[%s][%s]=%s" % (res, i, j, arr[i][j]))
                res += arr[i][j]
                res += arr[i+2][j]
            print("res=%s + a[%s][%s]=%s" % (res, i+1, m+1, arr[i+1][m+1]))
            res += arr[i+1][m+1]
            print("res:%s,  max_sum:%s" % (res, max_sum))
            if max_sum is None or max_sum < res:
                max_sum = res
    return max_sum


result = calculatesum([[-1, 1, -1, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0],
                       [-1, -1, -1, 0, 0, 0],
                       [0, -9, 2, -4, -4, 0],
                       [-7, 0, 0, -2, 0, 0],
                       [0, 0, -1, -2, -4, 0]])
print(result)
assert result == -19