# https://www.acmicpc.net/problem/21921

n, x = map(int, input().split())
visit_history = list(map(int, input().split()))

if max(visit_history) == 0 :
    print("SAD")
else :
    sum_history = sum(visit_history[:x])
    max_visit = sum_history
    count = 1

    for i in range(x, n):
        sum_history += visit_history[i]
        sum_history -= visit_history[i - x]

        if sum_history > max_visit :
            max_visit = sum_history
            count = 1
        elif sum_history == max_visit :
            count += 1

    print(max_visit, count, sep="\n")