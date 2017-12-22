from collections import defaultdict
n = int(input())
for i in range(n):
    no_of_elements = int(input())
    elements = [str(bin(int(x))[2:]) for x in input().split(' ')]
    count_dict = defaultdict(list)
    for ele in elements:
        count_dict[ele.count('1')].append(int(ele, 2))
    result_list = []
    for count, elements_list in count_dict.items():
        result_list.append(sorted(elements_list)[0])
    print(*result_list)


