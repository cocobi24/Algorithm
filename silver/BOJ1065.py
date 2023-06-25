# https://www.acmicpc.net/problem/1065

num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n < 100 :
        hansu += 1
    else :
        nums = list(map(int, str(n)))
        diff_1 = nums[0] - nums[1]
        diff_2 = nums[1] - nums[2]
        hansu = hansu+1 if diff_1 == diff_2 else hansu

print(hansu)