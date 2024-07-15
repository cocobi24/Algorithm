# https://www.acmicpc.net/problem/17269

N, M = map(int, input().split())
L = 0

A, B = list(map(list, input().split()))
name = ""

num_set = {
    "A" : 3, "B": 2 , "C" : 1 , "D" : 2, "E" : 4 , "F" : 3 , "G" : 1 , "H" : 3 , "I" : 1 , "J" : 1
    , "K" : 3 , "L" : 1 , "M" : 3 , "N" : 2 , "O" : 1 , "P" : 2 , "Q" : 2 , "R" : 2 , "S" : 1 , "T" : 2
    , "U" : 1 , "V" : 1 , "W" : 1 , "X" : 2 , "Y" : 2 , "Z" : 1
}

if N > M :
    L = M
else :
    L = N

for i in range(L) :
    name += A[i] + B[i]

if N > M :
    name += ''.join(A[L:])
else :
    name += ''.join(B[L:])

nums = []
for c in name :
    nums.append(num_set[c])

z = 0
while True :
    nums_clone = nums.copy()
    nums = []
    for i in range(len(nums_clone)-1) :
        num = nums_clone[i] + nums_clone[i+1]
        if num >= 10 :
            num = num % 10
        nums.append(num)

    if len(nums) == 2 :
        break
print(str(nums[0]) + str(nums[1]) + "%" if nums[0] != 0 else str(nums[1]) + "%")