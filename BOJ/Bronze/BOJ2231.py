# https://www.acmicpc.net/problem/2231

n = int(input())
flag = (len(str(n//10)) + 1) * 9
answers = []
startIdx = n-flag

if startIdx < 0 :
    startIdx = 0

for i in range(startIdx, n) :
    nums = list(map(int, str(i)))
    add = sum(nums) + i

    if add == n :
        answers.append((i))

if answers :
    print(min(answers))
else :
    print(0)