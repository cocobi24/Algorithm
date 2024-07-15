# https://www.acmicpc.net/problem/11497

T = int(input())
for _ in range(T) :
    n = int(input())
    num_list = sorted(list(map(int, input().split())))
    left_list = []
    right_list = []

    for i in range(n) :
        if (i+1) % 2 == 0 :
            right_list.append(num_list[i])
        else :
            left_list.append(num_list[i])

    right_list.reverse()
    left_list.extend(right_list)

    answer = 0
    for i in range(1, n) :
        abs_num = abs(left_list[i-1] - left_list[i])
        if abs_num > answer :
            answer = abs_num
    abs_num = abs(left_list[-1] - left_list[0])
    if abs_num > answer:
        answer = abs_num
    print(answer)