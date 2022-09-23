di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def go_line(i, j, line):
    # print(len(line), line)
    global num_Set
    if len(line) == 7:
        num_Set.add(''.join(line))
        return
    elif len(line) < 7:
        count = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                count += 1
                line.append(box[ni][nj])
                go_line(ni, nj, line)
                line.pop()


T = int(input())
for tc in range(1, T + 1):
    box = [list(map(str, input().split())) for _ in range(4)]
    num_Set = set()
    for i in range(4):
        for j in range(4):
            line = []
            line.append(box[i][j])
            go_line(i, j, line)
    print(f"#{tc} {len(num_Set)}")
  #  print(num_Set)
