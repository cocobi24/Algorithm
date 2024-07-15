# https://www.acmicpc.net/problem/5598

s_list = list(input())

for s in s_list :
    ascii_num = ord(s)
    if ascii_num >= 65 and ascii_num <= 67 :
        print(chr(ascii_num + 23), end="")
    else :
        print(chr(ascii_num - 3), end="")