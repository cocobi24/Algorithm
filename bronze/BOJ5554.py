# https://www.acmicpc.net/problem/5554

time = sum([int(input()) for _ in range(4)])
print(time//60,time%60,sep='\n')