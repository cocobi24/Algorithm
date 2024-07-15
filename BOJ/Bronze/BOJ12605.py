# https://www.acmicpc.net/problem/12605

t = int(input())

for i in range(t) :
    words = input().split()
    print(F"Case #{i+1}: {' '.join(words[::-1])}")