# https://www.acmicpc.net/problem/1205

n, taesu_score, p = map(int, input().split())

if n == 0 :
    print(1)
else :
    rank_list = list(map(int, input().split()))
    bottom_rank = min(rank_list)
    l = len(rank_list)

    if taesu_score <= bottom_rank and n == p :
        print(-1)
    elif taesu_score < bottom_rank and n < p :
        print(len(rank_list)+1)
    else :
        for i in range(l) :
            if taesu_score >= rank_list[i] :
                print(i + 1)
                break