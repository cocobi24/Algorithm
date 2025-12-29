# https://www.acmicpc.net/problem/25703

N = int(input())
print("int a;")
print("int *ptr = &a;")

for i in range(1, N):
    print(f"int {'*' * (i+1)}ptr{i+1} = &ptr{i if i > 1 else ''};")