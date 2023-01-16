# https://www.acmicpc.net/problem/1769

num = input()
count = 0
answer = 'NO'

if int(num) > 10 :
    while True :
        num_list = list(map(int, str(num)))
        num = sum(num_list)
        count += 1
        if num >= 10 :
            continue
        else :
            break

if (int(num) % 3) == 0 :
    answer = "YES"

print(count)
print(answer)