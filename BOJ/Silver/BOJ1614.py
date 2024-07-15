# https://www.acmicpc.net/problem/1614

finger = int(input())
count = int(input())
answer = 0

if finger == 1:
    answer = count * 8
elif finger == 5:
    answer = count * 8 + 4
else:
    if count % 2 == 0:
        answer = 4 * count + (finger - 1)
    else:
        answer = 4 * count + (5 - finger)

print(answer)