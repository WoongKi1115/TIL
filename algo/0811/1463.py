x = int(input())
count = 0
while True:
    if x == 1:
        break

    elif x>=3 and x%3 ==0 :
        x = x//3
        count += 1
    elif x%3 == 2:
        x -= 1
        count += 1
    elif x%2 == 0:
        x = x//2
        count += 1
    else:
        x -= 1
        count += 1

print(count)
