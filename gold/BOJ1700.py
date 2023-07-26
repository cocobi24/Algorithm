# https://www.acmicpc.net/problem/1700

N, K = map(int, input().split())
elec_list = list(map(int, input().split()))
multitap = []
unplug_count = 0

if N >= K :
    print(unplug_count)
else :
    for i in range(K):
        elec = elec_list[i]

        if elec in multitap :
            continue

        if len(multitap) < N :
            multitap.append(elec)
            continue

        min_num = ( multitap[0], 0 )
        remove_num, flag = 0, 0
        for j in range(N):
            if multitap[j] not in elec_list[i:] :
                remove_num = multitap[j]
                flag = 1
                break
            else :
                now = elec_list[i:].index(multitap[j])
                if now > min_num[1]:
                    min_num = (multitap[j], now)
        if flag == 1:
            multitap.remove(remove_num)
            multitap.append(elec)
            unplug_count += 1
        else :
            multitap.remove(min_num[0])
            multitap.append(elec)
            unplug_count += 1
    print(unplug_count)