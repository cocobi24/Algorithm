T = int(input())

for idx in range(T) :
    num = input()
    answer = 9999999999
    for i in range(len(num)-1) :
        x, y = int(num[:i+1]), int(num[i+1:])
        if x + y < answer :
            answer = x + y
    print(f"#{idx+1}", answer)