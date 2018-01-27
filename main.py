from Zfz2048 import ZFZ2048
from GUI_2048 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def main(a_2):
    while(1):
        game=ZFZ2048(a_2)
        print("Welcome to 2048, designed by ZhangFuzuo.")
        game.show()
        while(game.gamecontinue):
            keyboard=input()
            if keyboard=='a':
                game.LeftMove()
            if keyboard=='d':
                game.RightMove()
            if keyboard=='w':
                game.UpMove()
            if keyboard=='s':
                game.DownMove()
            if game.contains(0):
                game.addnew()
            if game.contains(0):
                game.addnew()
            game.clearmark()
            game.show()
            game.check()
        print("Input Q or q to quit. Any other press to continue!")
        press=input()
        if press=='Q' or press=='q':
            break

main(9)