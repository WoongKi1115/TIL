T = 10
for tc in range(1,T+1):
    count = int(input())
    box = list(map(int,input().split()))
    for i in range(count):
        max = [0,0]
        min = [200,0]
        for j in range(len(box)):
            if max[0]<=box[j]:
                max = [box[j], j]  
            elif min[0]>=box[j]:
                min = [box[j], j]
        box[max[1]] -= 1
        box[min[1]] += 1
    print(f"#{tc} {max[0]-min[0]}")

