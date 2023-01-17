# https://www.acmicpc.net/problem/10610

n = input()
num_list = list(n)

if '0' in num_list :
    num_list.sort(reverse=True)
    num_sum = int(''.join(num_list))
    if num_sum % 30 == 0 :
        print(num_sum)
    else :
        print(-1)
else :
    print(-1)