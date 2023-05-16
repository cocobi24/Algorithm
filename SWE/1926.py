N = int(input())

for i in range(1, N+1) :
    num_list = list(str(i))
    if "3" in num_list or "6" in num_list or "9" in num_list :
        crap = num_list.count("3") + num_list.count("6") + num_list.count("9")
        print("-"*crap, end=" ")
    else :
        print(i, end=" ")