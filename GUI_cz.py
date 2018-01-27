from GUI_2048 import Ui_MainWindow
from Zfz2048 import ZFZ2048
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox #QmessageBox是弹出框函数
import os
# -*- coding: utf-8 -*-

class Example(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,a_2):
        super(Example,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("2048_ZFZ")
        #self.score.setText("0")
        #self.maxscore.setText(self.Maxscore())
        #self.game = ZFZ2048(self.a_2)
        self.a_2=a_2
        #print("Welcome to 2048, designed by ZhangFuzuo.")
        self.text = [[self.text_0_0, self.text_0_1, self.text_0_2, self.text_0_3],
                     [self.text_0_4, self.text_0_5, self.text_0_6, self.text_0_7],
                     [self.text_0_8, self.text_0_9, self.text_0_10, self.text_0_11],
                     [self.text_0_12, self.text_0_13, self.text_0_14, self.text_0_15]]
        for i in range(4):
            for j in range(4):
                self.text[i][j].setTextColor(QtGui.QColor(0, 0, 0))
                #self.text[i][j].setStyleSheet("font-alignment:center")
        self.color = []
        self.color.append(QtGui.QColor(255, 235, 203))  # 0
        self.color.append(QtGui.QColor(252, 230, 201))  # 2
        self.color.append(QtGui.QColor(255, 222, 173))  # 4
        self.color.append(QtGui.QColor(237, 145, 33))  # 8
        self.color.append(QtGui.QColor(227, 168, 105))  # 16
        self.color.append(QtGui.QColor(255, 227, 132))  # 32
        self.color.append(QtGui.QColor(255, 128, 0))  # 64
        self.color.append(QtGui.QColor(235, 142, 85))  # 128
        self.color.append(QtGui.QColor(255, 153, 18))  # 256
        self.color.append(QtGui.QColor(227, 168, 105))  # 512
        self.color.append(QtGui.QColor(227, 207, 87))  # 1024
        self.color.append(QtGui.QColor(227, 23, 13))  # 2048
      #  self.Show(self.game.jz)
        self.startgame()
        self.grabKeyboard()
    def Maxscore(self):
        filename="maxscore.txt"
        if os.path.exists(filename) and os.path.isfile(filename):
            file=open(filename)
            maxscore=file.read()
            file.close()
            return maxscore
        else:
            file=open(filename,'w')
            file.write("0")
            file.close()
            return "0"
    def keyPressEvent(self,event):
       if self.game.gamecontinue==False:
            return
       if event.key()==Qt.Key_Up:
           self.game.UpMove()
       if event.key()==Qt.Key_Down:
           self.game.DownMove()
       if event.key()==Qt.Key_Right:
           self.game.RightMove()
       if event.key()==Qt.Key_Left:
           self.game.LeftMove()
       if self.game.contains(0):
           self.game.addnew()
       if self.game.contains(0):
           self.game.addnew()
       self.game.clearmark()
       self.Show(self.game.jz)
       self.score.setText(str(self.game.score))
       if int(self.maxscore.text())<self.game.score:
           self.maxscore.setText(str(self.game.score))
       self.Check()
    def Check(self):
        self.game.check()
        if self.game.gamecontinue:
            return
        if self.game.gamecontinue==False and self.game.sorf==1:  #finished
            QMessageBox.information(self,     # 使用infomation信息框
                                    "游戏结束",
                                    "恭喜！你成功完成了任务! "
                                    "你的得分为：%d" %self.game.score)
        if self.game.gamecontinue==False and self.game.sorf==0:  #unfinished
            QMessageBox.information(self,  # 使用infomation信息框
                                    "游戏结束",
                                    "很遗憾！你未完成了任务！"
                                    "你的得分为：%d" %self.game.score)
        if self.game.gamecontinue==False:
            self.setMaxscore()
        self.restart()

    def restart(self):
        reply = QMessageBox.question(self, '提示', '再来一次？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.startgame()
        else:
            self.close()

    def setMaxscore(self):
        filename = "maxscore.txt"
        file = open(filename, 'w')
        file.write(self.maxscore.text())
        file.close()

    def Show(self,jz):
        for i in range(4):
            for j in range(4):
                if jz[i][j]==0:
                    #pal=QtGui.QPalette()
                    #pal.setColor(self.text[i][j].backgroundRole(),self.color[5])
                    self.text[i][j].clear()
                    #self.text[i][j].setPalette(pal)
                    self.text[i][j].setStyleSheet("background-color: rgb(255, 235, 203);")
                    #self.text[i][j].setTextBackgroundColor(self.color[0])
                else:
                    #self.text[i][j].setTextBackgroundColor(self.color[int(math.log(jz[i][j],2))])
                    #pal = QtGui.QPalette(self.text[i][j])
                    #pal.setColor(self.text[i][j].backgroundRole(), self.color[int(math.log(jz[i][j],2))])
                    #self.text[i][j].setPalette(pal)
                    if jz[i][j]<100:
                        self.text[i][j].setFontPointSize(36)
                        if jz[i][j]==2:
                            self.text[i][j].setStyleSheet("background-color: rgb(252, 230, 201);")  #2
                        if jz[i][j] == 4:
                            self.text[i][j].setStyleSheet("background-color: rgb(255, 222, 173);")  #4
                        if jz[i][j] == 8:
                            self.text[i][j].setStyleSheet("background-color: rgb(237, 145, 33);")  #8
                        if jz[i][j] == 16:
                            self.text[i][j].setStyleSheet("background-color: rgb(227, 168, 105);")  #16
                        if jz[i][j] == 32:
                            self.text[i][j].setStyleSheet("background-color: rgb(255, 227, 132);")  #32
                        if jz[i][j] == 64:
                            self.text[i][j].setStyleSheet("background-color: rgb(255, 128, 0);")  #64
                    else:
                        if jz[i][j]<1000:
                            self.text[i][j].setFontPointSize(25)
                            if jz[i][j] == 128:
                                self.text[i][j].setStyleSheet("background-color: rgb(235, 142, 85);")  #128
                            if jz[i][j] == 256:
                                self.text[i][j].setStyleSheet("background-color: rgb(255, 153, 18);")  #256
                            if jz[i][j] == 512:
                                self.text[i][j].setStyleSheet("background-color: rgb(227, 168, 105);")  #512

                        else:
                            self.text[i][j].setFontPointSize(20)
                            if jz[i][j] == 1024:
                                self.text[i][j].setStyleSheet("background-color: rgb(227, 207, 87);")  #1024
                            if jz[i][j] == 2048:
                                self.text[i][j].setStyleSheet("background-color: rgb(227, 23, 13);")  #2048

                    self.text[i][j].setText(str(jz[i][j]))
        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def startgame(self):
        self.score.setText("0")
        self.maxscore.setText(self.Maxscore())
        self.game = ZFZ2048(self.a_2)
       # print("Welcome to 2048, designed by ZhangFuzuo.")
        self.Show(self.game.jz)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Example(8)
    ui.show()
    sys.exit(app.exec_())