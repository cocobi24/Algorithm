# https://www.acmicpc.net/problem/17202

phone_1, phone_2 = list(input()), list(input())

new_phone = ''
for i in range(8):
    new_phone += phone_1[i] + phone_2[i]

while True:
    compatibility = ''
    for i in range(len(new_phone)-1):
        num = int(new_phone[i]) + int(new_phone[i+1])
        if num >= 10:
            num = num % 10

        compatibility += str(num)
    new_phone = compatibility

    if len(compatibility) <= 2 :
        break

print(compatibility)