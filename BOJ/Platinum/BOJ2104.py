# https://www.acmicpc.net/problem/2104

N = int(input())
arr = list(map(int, input().split()))

def sub_array(start, end):
    if start == end:
        return arr[start]**2

    mid = (start + end) // 2
    left, right = mid, mid + 1

    total = arr[left] + arr[right]
    min_value = min(arr[left], arr[right])
    max_value = max(sub_array(start, mid), sub_array(right, end), min_value * total)

    while left > start or right < end:
        if right < end and (left == start or arr[left-1] < arr[right+1]):
            right += 1
            direction = right
        else:
            left -= 1
            direction = left

        total += arr[direction]
        min_value = min(min_value, arr[direction])
        max_value = max(max_value, min_value * total)

    return max_value

answer = sub_array(0, N-1)
print(answer)