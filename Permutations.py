# You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

from itertools import permutations
word, size = tuple(input().split())

permuted = list(permutations(word,int(size)))

sorted_permutations = sorted(list(map(lambda x : ''.join(x),permuted)))


for item in sorted_permutations :
    print(item)