# https://www.acmicpc.net/problem/11728

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))
answer = sorted(n_list + m_list)
print(*answer, end='')