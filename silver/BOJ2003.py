# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = 1
sum = nums[0]
count = 0

while True :
    if sum < m :
        if right < n :
            sum += nums[right]
            right += 1
        else :
            break
    elif sum == m :
        sum -= nums[left]
        left += 1
        count += 1
    else :
        sum -= nums[left]
        left += 1
print(count)
