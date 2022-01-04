# You are given a string .
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

from itertools import combinations

word, size = tuple(input().split())

possible_combinations = list()
word = ''.join(sorted(list(word)))

for i in range(1, int(size) + 1):
    combination = combinations(word, i)
    sorted_combinations = list(map(lambda x: ''.join(x), combination))
    for item in sorted_combinations:
        print(item)


