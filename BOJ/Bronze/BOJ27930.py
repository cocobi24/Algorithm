# https://www.acmicpc.net/problem/27930

S = list(input())
korea, k_cnt = "KOREA", 0
yonsei, y_cnt = "YONSEI", 0

for s in S :
    if s == korea[k_cnt] :
        k_cnt += 1
    if s == yonsei[y_cnt] :
        y_cnt += 1

    if k_cnt == 5 or y_cnt == 6 :
        break
print("KOREA" if k_cnt == 5 else "YONSEI")