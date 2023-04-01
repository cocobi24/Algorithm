# https://www.acmicpc.net/problem/2828

n, m = map(int, input().split())
j = int(input())
left, right = 1, m

move = 0
for _ in range(j):
    apple_position = int(input())
    if left <= apple_position and right >= apple_position:
        continue
    elif left > apple_position:
        move += (left - apple_position)
        right -= (left - apple_position)
        left = apple_position
    else:
        move += (apple_position - right)
        left += (apple_position - right)
        right = apple_position

print(move)