# https://www.acmicpc.net/problem/10769

input = input().replace(":-)", " *HAPPY* ").replace(":-(", " *SAD* ")
str_list = input.split()
str_list = list(filter(lambda x : x == "*HAPPY*" or x == "*SAD*", str_list))
answers = {'happy' : 0, 'sad' : 0}

if len(str_list) == 0 :
    print("none")
else :
    for s in str_list :
        if s == "*HAPPY*" :
            answers["happy"] += 1
        if s == "*SAD*" :
            answers["sad"] += 1

    if answers["happy"] == answers["sad"] :
        print("unsure")
    elif answers["happy"] > answers["sad"] :
        print("happy")
    else :
        print("sad")