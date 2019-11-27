import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox, QPushButton, QApplication)  


class MinesweeperGUI(QWidget):
    
    def __init__(self, MinesweeperGame):
        super().__init__()
        self.game = MinesweeperGame
        self.buttons = [[0 for i in range(self.game.boardSize[1])] for j in range(self.game.boardSize[0])]
        self.initUI()
        
    def initUI(self):
        m = self.game.boardSize[0]
        n = self.game.boardSize[1]
        
        button_size = 50
        for i in range(m):
            for j in range(n):
                self.buttons[i][j] = QPushButton(' ', self)
                self.buttons[i][j].resize(button_size, button_size)
                self.buttons[i][j].move(button_size*j, button_size*i)
                self.buttons[i][j].clicked.connect(self.on_click(j, i))
        
        self.setGeometry(300, 300, button_size*n, button_size*m)
        self.setWindowTitle('Minesweeper')    
        self.show()

    def on_click(self, x, y):
        def ret():
            return self.show_button_value(x, y)
        return ret

    def show_button_value(self, x, y):
        self.game.board_updater(x, y)
        m = self.game.boardSize[0]
        n = self.game.boardSize[1]
        for i in range(m):
            for j in range(n):
                if self.game.userBoard[i][j] != '-':
                    self.buttons[i][j].setText(str(self.game.userBoard[i][j]))
                    self.buttons[i][j].setEnabled(False)
        if self.game.is_ended():
            QMessageBox.about(self, "Game Ended", "You won")
            sys.exit()
        if self.game.ended:
            QMessageBox.about(self, "Game Ended", "You lost")
            sys.exit()

if __name__ == '__main__':
    from minesweeper import MineSweeper
    game = MineSweeper('parsa', 8, (8,7))
    app = QApplication(sys.argv)
    ex = MinesweeperGUI(game)
    sys.exit(app.exec_())
