# https://www.acmicpc.net/problem/20300

N = int(input())
t_list = sorted(map(int, input().split()))

max_t = t_list[-1]
if len(t_list) % 2 != 0 :
    t_list.pop()

for i in range(N//2) :
    pt = t_list[i] + t_list[-i-1]
    if pt > max_t :
        max_t = pt

print(max_t)