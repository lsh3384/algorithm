def solution(board, skill):
    for i in board:
        print(i)

    print('행', len(board))
    print('열', len(board[0]))

    for j in skill:
        skill_type = j[0]
        print('범위', end='')
        print()
        x1 = j[1]
        print('x1행', x1)
        y1 = j[2]
        print('y1열', y1)
        x2 = j[3]
        print('x2행', x2)
        y2 = j[4]
        print('y2행', y2)
        degree = j[5]

        if skill_type == 1:
            print('공격', end='')
            print()
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    print(board[x][y], end='')
                    board[x][y] -= degree
                print()
        else:
            print('회복', end='')
            print()
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    print(board[x][y], end='')
                    board[x][y] += degree
                print()

    answer = 0
    for y in board:
        for z in y:
            if z >= 1:
                answer += 1
            print(z, end='')
        print()
    print(board)
    print(answer)

    return answer


#
# board = [[5,5,5,5,5],
#          [5,5,5,5,5],
#          [5,5,5,5,5],
#          [5,5,5,5,5]]

board = [[1,2,3],[4,5,6],[7,8,9]]
# board = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4]]
# skill = [[1,0,0,3,4,4],
#          [1,2,0,2,3,2],
#          [2,1,0,3,1,2],
#          [1,0,1,3,3,1]]


skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
# skill = [[1,0,0,3,4,4],
#          [1,2,0,2,3,2]]
# skill = [[1,0,0,3,4,5],
#          [2,0,0,3,4,5]]

solution(board, skill)