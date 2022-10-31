# https://www.acmicpc.net/problem/2910

n, c = map(int, input().split())
nums = num = list(map(int, input().split()))
answers = {}

for num in nums :
    if num not in answers :
        answers[num] = 1
    else :
        answers[num] += 1

answers = sorted(answers.items(), key = lambda x : x[1], reverse = True)
l = len(answers)

for i in range(l) :
   num, r = answers[i]
   for j in range(r) :
       print(num, end=' ')