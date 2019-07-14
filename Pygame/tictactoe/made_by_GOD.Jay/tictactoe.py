# Tic Tac Toe with PyQt5
# Made by Jea Kwon
# Library Requirements numpy, PyQt5
# File Requirements "main_window.ui"cd

import sys
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.__call__()

    def __call__(self):
        self.setupUi(self)

        self.count = 0
        self.btns = [
            [self.btn00, self.btn01, self.btn02], 
            [self.btn10, self.btn11, self.btn12], 
            [self.btn20, self.btn21, self.btn22]]
            
        for row in self.btns:
            for btn in row:
                btn.clicked.connect(self.clicked)
                btn.value = 0
                btn.setStyleSheet("QPushButton { background-color: grey }")

    def clicked(self):
        btn = self.sender()
        self.count += 1
        if self.count % 2 == 0:
            btn.setStyleSheet("QPushButton { background-color: blue }" )
            btn.setText('O')
            btn.value = 1

        elif self.count % 2 == 1:
            btn.setStyleSheet("QPushButton { background-color: red }" )
            btn.setText('X')
            btn.value = -1

        btn.setEnabled(False)
        arr = np.array([[btn.value for btn in row] for row in self.btns])
    
        if self.check(arr,3):
            ans = QMessageBox.question(self, "message", 'Blue Wins, Try again?')
            if ans==QMessageBox.Yes:
                self.__call__()
            else:
                sys.exit()

        if self.check(arr,-3):  
            ans = QMessageBox.question(self, "message", 'Red Wins, Try again?')
            if ans==QMessageBox.Yes:
                self.__call__()
            else:
                sys.exit()

        if self.count==9:
            ans = QMessageBox.question(self, "message", 'Draw! Try again?')
            if ans==QMessageBox.Yes:
                self.__call__()
            else:
                sys.exit()

    @staticmethod
    def check(arr, num):
        if num in arr.sum(axis=0):
            return True
        elif num in arr.sum(axis=1):
            return True
        elif num in [arr.trace(), np.fliplr(arr).trace()]:
            return True
        return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()