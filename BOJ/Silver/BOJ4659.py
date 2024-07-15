# https://www.acmicpc.net/problem/4659

import sys
input = sys.stdin.readline
vowel_list = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input().rstrip()

    if password == "end" :
        break

    accept_flag = False
    for vowle in vowel_list:
        if vowle in password :
            accept_flag = True
            break

    if accept_flag != False:
        for i in range(1, len(password)) :
            if password[i] != 'o' and password[i] != 'e':
                    if password[i] == password[i-1] :
                        accept_flag = False
                        break

        for i in range(len(password)-2) :
            if password[i] in vowel_list and password[i+1] in vowel_list and password[i+2] in vowel_list :
                accept_flag = False
            elif not(password[i] in vowel_list) and not(password[i+1]in vowel_list) and not(password[i+2] in vowel_list) :
                accept_flag = False

    if accept_flag == False :
        print(f"<{password}> is not acceptable.")
        continue

    print(f"<{password}> is acceptable.")