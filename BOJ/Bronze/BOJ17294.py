# https://www.acmicpc.net/problem/17294

k = input()
nums = list(map(int, list(k)))
answer = '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'

if int(k) >= 10 :
    d = nums[1] - nums[0]

    for i in range(2, len(nums)):
        if d != nums[i] - nums[i-1]:
            answer = '흥칫뿡!! <(￣ ﹌ ￣)>'
            break

print(answer)