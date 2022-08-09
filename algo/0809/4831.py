T = int(input())
# 3 10 5
for tc in range(1, T+1):
    count = 0
    max_fuel, station, fsn = map(int, input().split())
    mf1 = max_fuel
    fs = list(map(int, input().split()))
    for i in range(1, station +1):
        mf1 -= 1
        a = []
        for j in range(i, i+mf1+1):
            if j in fs:
                a.append(j)
        if len(a) > 1:
            continue
        elif len(a) == 0:
            count = 0
            break


        elif i in fs:
            mf1 = max_fuel
            count += 1
        if i + mf1 >= station:
            break
    print(f"#{tc} {count}")






    # print(f"{tc} {count}")


