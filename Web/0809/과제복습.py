T = 10

for t in range(1,T+1):
	n = int(input()) #빌딩에 있는 땅의 너비
	bulidings = list(map(int,input().split()))
	count = 0 #조망권이 확보된 세대 수
	for i in range(2,n-2): #양쪽 2칸씩 비어있다.
		height = bulidings[i] #i위치에 있는 빌딩 높이
		for floor in range(height,-1,-1): #현재 건물의 가장 위층부터 하나씩 검사
			#현재 위치에서 왼쪽 두칸 오른쪽 두칸 검사
			if floor > bulidings[i-1] and floor >bulidings[i-2] and floor > bulidings[i+1] and floor > bulidings[i+2]:
				count += 1
			else:
				break

	print(f"#{t} {count}")