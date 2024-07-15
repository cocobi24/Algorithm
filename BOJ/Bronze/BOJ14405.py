# https://www.acmicpc.net/problem/14405

S = input()
passible_list = ["pi", "ka", "chu"]
for passible in passible_list :
    S = S.replace(passible, " ")
print("YES" if len(S.strip()) == 0 else "NO")