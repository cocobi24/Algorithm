# https://www.acmicpc.net/problem/5568

from itertools import permutations
n = int(input())
k = int(input())
card_list = [int(input()) for _ in range(n)]
p_list = list(permutations(card_list,k))

answer = set()
for p in p_list:
    n =''.join((map(str, p)))
    answer.add(n)
    
print(len(answer))