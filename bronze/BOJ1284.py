# https://www.acmicpc.net/problem/1284

while True :
    nums = list(map(int, input()))
    answer = 0

    if nums[0] == 0 :
        break

    answer += len(nums)+1
    for i in nums :
        if i == 1 :
            answer += 2
        elif i == 0 :
            answer += 4
        else :
            answer += 3

    print(answer)