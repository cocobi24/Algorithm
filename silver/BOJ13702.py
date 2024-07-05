# https://www.acmicpc.net/problem/13702

def solve(N, K, volumes):
  def isDivide(volume):
    total = 0
    for v in volumes:
      total += v // volume
    return total >= K

  low, high = 1, max(volumes)
  while low <= high:
    mid = (low + high) // 2
    if isDivide(mid):
      low = mid + 1
    else:
      high = mid - 1
  return low - 1


N, K = map(int, input().split())
volumes = [int(input()) for _ in range(N)]
print(solve(N, K, volumes))