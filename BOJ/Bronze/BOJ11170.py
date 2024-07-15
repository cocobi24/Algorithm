# https://www.acmicpc.net/problem/11170

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    nums = [str(i) for i in range(n, m+1) if '0' in str(i)]
    answer = 0
    if len(nums) > 0 :
        for num in nums :
            answer += num.count('0')
    print(answer)