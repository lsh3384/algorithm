def solution(board, skill):
    for j in skill:
        skill_type = j[0]
        x1 = j[1]
        y1 = j[2]
        x2 = j[3]
        y2 = j[4]
        degree = j[5]

        if skill_type == 1:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] -= degree
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] += degree

    answer = 0
    for row in board:
        for element in row:
            if element >= 1:
                answer += 1

    return answer
