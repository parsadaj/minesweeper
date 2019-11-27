import datetime
import random


class MineSweeper:

    last_gameID = 0
    
    def __init__(self, player, totalBombsCount, boardSize):
        self.player = player
        self.gameID = MineSweeper.last_gameID + 1
        MineSweeper.last_gameID += 1
        self.boardSize = boardSize
        self.totalBombsCount = totalBombsCount
        self.board = self.board_generator()
        self.numberOfTilesOpened = totalBombsCount
        self.userBoard = [['-' for i in range(boardSize[1])] for j in range(boardSize[0])]
        self.visited = [[False for i in range(boardSize[1])] for j in range(boardSize[0])]
        self.ended = False

    def board_generator(self):
        m = self.boardSize[0]
        n = self.boardSize[1]

        bombs = []
        while len(bombs) < self.totalBombsCount:
            x = random.randint(0, m-1)
            y = random.randint(0, n-1)
            if (x,y) not in bombs:
                bombs.append((x,y))

        board =[]
        for i in range(m):
            row = []
            for j in range(n):
                if (i,j) in bombs:
                    row.append('*')
                else:
                    row.append('-')
            board.append(row)
        #return [['-', '-', '*', '-', '*', '-', '-'], ['-', '*', '-', '*', '-', '-', '-'], ['-', '-', '*', '*', '-', '-', '-'], ['-', '-', '-', '-', '-', '*', '-'], ['*', '-', '-', '*', '-', '*', '-'], ['-', '-', '-', '-', '*', '-', '-'], ['-', '-', '-', '-', '*', '*', '-'], ['-', '*', '*', '-', '-', '-', '-']]
        return board

    def expand(self, x, y):
        m = self.boardSize[0]
        n = self.boardSize[1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if y+i >= 0 and y+i < m and x+j >= 0 and x+j < n \
                  and (i != 0 or j != 0) and not self.visited[y+i][x+j]:
                    self.board_updater(x+j, y+i)

    def number_of_bombs_nearby(self, x, y):
        m = self.boardSize[0]
        n = self.boardSize[1]
        number_of_bombs= 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if y+i >= 0 and y+i < m and x+j >= 0 and x+j < n \
                  and self.board[y+i][x+j] == '*' and (i != 0 or j != 0):
                    number_of_bombs += 1
        return number_of_bombs

    def board_updater(self, x, y):
        self.visited[y][x] = True
        if self.board[y][x] == '*':
            print('bomb')
            print('You lost')
            self.ended = True
            self.userBoard[y][x] = '*'
            return

        number_of_bombs_nearby = self.number_of_bombs_nearby(x, y)
        self.board[y][x] = number_of_bombs_nearby
        self.userBoard[y][x] = number_of_bombs_nearby
        if number_of_bombs_nearby == 0:
            self.expand(x, y)

    def board_displayer(self, boardType):
        # boardType = True for full board and False for userBoard
        m = self.boardSize[0]
        n = self.boardSize[1]
        board = self.board if boardType == 1 else self.userBoard
        for i in range(m):
            for j in range(n):
                print(board[i][j], end=' ')
            print()

    def ask_update(self):
        x = int(input('x = ')) - 1
        y = int(input('y = ')) - 1
        return x,y

    def is_ended(self):
        board = self.board
        m = self.boardSize[0]
        n = self.boardSize[1]
        for i in range(m):
            for j in range(n):
                if board[i][j] == '-':
                    return False
        return True        
    
    def start(self):
        self.ended = False
        while not self.ended:
            x,y = self.ask_update()
            self.board_updater(x,y)
            self.board_displayer(self.ended)
            self.ended = self.is_ended()


if __name__ == '__main__':
    game = MineSweeper('parsa', 8, (8,7))
    game.start()
