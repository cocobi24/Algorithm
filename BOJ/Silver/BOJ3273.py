# https://www.acmicpc.net/problem/3273

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n-1
answer = 0

while left < right :
    hap = arr[left] + arr[right]
    if hap == x :
        answer += 1
    elif hap < x :
        left += 1
        continue
    right -= 1
    
print(answer)