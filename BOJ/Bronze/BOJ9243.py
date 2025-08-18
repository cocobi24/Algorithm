# https://www.acmicpc.net/problem/9243

n = int(input())
t = n % 2
trans_set = {
  '0': str(t),
  '1': '1' if t == 0 else '0'
}

origin = list(input().rstrip())
trans_str = ''.join([trans_set[o] for o in origin])
del_str = input().rstrip()
print("Deletion succeeded" if trans_str == del_str else "Deletion failed")