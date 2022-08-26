switch = int(input())
status = list(map(int, input().split()))
sn = int(input())
student = [list(map(int,input().split())) for _ in range(sn)]


for i in range(sn):
    if student[i][0]==1:
        for j in range(student[i][1]-1,switch,student[i][1]):
            status[j] = (status[j]+1)%2
    else:
        s = (student[i][1]-1)
        e = (student[i][1]-1)
        status[s] = (status[s]+1)%2
        while True:
            s -=1
            e +=1
            if s < 0 or s >= switch or e < 0 or e >= switch:
                break
            if status[s]==status[e]:
                status[s] = (status[s]+1)%2
                status[e] = (status[e] + 1) % 2
            else:
                break


count = 0
for i in range(len(status)):
    count+= 1
    print(status[i], end = ' ')
    if count%20 == 0:
        print()

