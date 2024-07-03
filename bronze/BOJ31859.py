# https://www.acmicpc.net/problem/31859

num, name = map(str, input().rstrip().split())
temp_name = ['']
l = len(name)
for i in range(l):
  if name[i] not in temp_name:
    temp_name.append(name[i])

temp_name.append(str(l - len(temp_name) + 5))
temp_name[0] = str(int(num) + 1906)
temp_name = ''.join(temp_name)

temp_name = temp_name[::-1]
answer = "smupc_" + temp_name
print(answer)