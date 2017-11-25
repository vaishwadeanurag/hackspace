def subArrayExceedsSum(arr, target):
    if sum(arr) < target:
        return -1
    count = 0
    r = [[]]
    for e in arr:
        r += [x + [e] for x in r]
    for sub in r:
        if sum(sub) == target:
            # print(sub)
            count += 1
    return count - 1


print(subArrayExceedsSum([1,2,3,4,6], 6))