import sys
sys.stdin = open("input5.txt", "r")
T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = 0
    for i in range(12):
        if i%2 == 0:
            player1[cards[i]] += 1
            for k in range(0,8):
                if player1[k] != 0 and player1[k+1] != 0 and player1[k+2] != 0:
                    result = 1
                    break
            if result == 1:
                break
            if 3 in player1:
                result = 1
                break



        else:
            player2[cards[i]] += 1

            for k in range(0, 8):
                if player2[k] != 0 and player2[k + 1] != 0 and player2[k + 2] != 0:
                    result = 2
                    break
            if result == 2:
                break

            if 3 in player2:
                result = 2
                break


    print(f"#{tc} {result}")