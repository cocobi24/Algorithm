# https://www.acmicpc.net/problem/4641

while True :
    nums = list(map(int, input().split()))
    answer = 0
    if nums[0] == -1 :
        break
    for n in nums :
        nn = n*2
        if nn in nums :
            answer += 1
    print(answer-1)