# https://www.acmicpc.net/problem/9946

idx = 1
while True:
  word = input().rstrip()
  retrieve = input().rstrip()

  if word == "END" and word == retrieve:
    break

  ans = "same" if sorted(word) == sorted(retrieve) else "different"
  print(f"Case {idx}: {ans}")
  idx += 1