# https://www.acmicpc.net/problem/10448

import sys
input = sys.stdin.readline
T = int(input())

def isEureka(K):
    for i in range(l):
        for j in range(l):
            for k in range(l):
                num = tri_list[i] + tri_list[j] + tri_list[k]
                if K == num:
                    return 1
    return 0

tri_list, tri, i = [], 0, 1
while tri < 1000:
    tri = i * (i + 1) // 2
    tri_list.append(tri)
    i += 1
l = len(tri_list)

for _ in range(T) :
    K = int(input())
    answer = isEureka(K)
    print(answer)