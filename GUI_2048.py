# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_2048.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 73, 73))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.text_0_0 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.text_0_0.setObjectName("text_0_0")
        self.gridLayout.addWidget(self.text_0_0, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 73, 73))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_0_1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.text_0_1.setObjectName("text_0_1")
        self.gridLayout_2.addWidget(self.text_0_1, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(150, 40, 73, 73))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.text_0_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.text_0_2.setObjectName("text_0_2")
        self.gridLayout_3.addWidget(self.text_0_2, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(220, 40, 73, 73))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_0_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.text_0_3.setObjectName("text_0_3")
        self.gridLayout_4.addWidget(self.text_0_3, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(220, 110, 73, 73))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.text_0_7 = QtWidgets.QTextBrowser(self.gridLayoutWidget_7)
        self.text_0_7.setObjectName("text_0_7")
        self.gridLayout_7.addWidget(self.text_0_7, 0, 0, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(10, 180, 73, 73))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.text_0_8 = QtWidgets.QTextBrowser(self.gridLayoutWidget_9)
        self.text_0_8.setObjectName("text_0_8")
        self.gridLayout_9.addWidget(self.text_0_8, 0, 0, 1, 1)
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(150, 180, 73, 73))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.text_0_10 = QtWidgets.QTextBrowser(self.gridLayoutWidget_10)
        self.text_0_10.setObjectName("text_0_10")
        self.gridLayout_10.addWidget(self.text_0_10, 0, 0, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(220, 180, 73, 73))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.text_0_11 = QtWidgets.QTextBrowser(self.gridLayoutWidget_11)
        self.text_0_11.setObjectName("text_0_11")
        self.gridLayout_11.addWidget(self.text_0_11, 0, 0, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(10, 110, 73, 73))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.text_0_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget_12)
        self.text_0_4.setObjectName("text_0_4")
        self.gridLayout_12.addWidget(self.text_0_4, 0, 0, 1, 1)
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(150, 250, 73, 73))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.text_0_14 = QtWidgets.QTextBrowser(self.gridLayoutWidget_14)
        self.text_0_14.setObjectName("text_0_14")
        self.gridLayout_14.addWidget(self.text_0_14, 0, 0, 1, 1)
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(220, 250, 73, 73))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.text_0_15 = QtWidgets.QTextBrowser(self.gridLayoutWidget_15)
        self.text_0_15.setObjectName("text_0_15")
        self.gridLayout_15.addWidget(self.text_0_15, 0, 0, 1, 1)
        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(80, 250, 73, 73))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.text_0_13 = QtWidgets.QTextBrowser(self.gridLayoutWidget_16)
        self.text_0_13.setObjectName("text_0_13")
        self.gridLayout_16.addWidget(self.text_0_13, 0, 0, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(10, 250, 73, 73))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.text_0_12 = QtWidgets.QTextBrowser(self.gridLayoutWidget_13)
        self.text_0_12.setObjectName("text_0_12")
        self.gridLayout_13.addWidget(self.text_0_12, 0, 0, 1, 1)
        self.gridLayoutWidget_17 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(80, 180, 73, 73))
        self.gridLayoutWidget_17.setObjectName("gridLayoutWidget_17")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.text_0_9 = QtWidgets.QTextBrowser(self.gridLayoutWidget_17)
        self.text_0_9.setObjectName("text_0_9")
        self.gridLayout_17.addWidget(self.text_0_9, 0, 0, 1, 1)
        self.gridLayoutWidget_18 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_18.setGeometry(QtCore.QRect(80, 110, 73, 73))
        self.gridLayoutWidget_18.setObjectName("gridLayoutWidget_18")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_18.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.text_0_5 = QtWidgets.QTextBrowser(self.gridLayoutWidget_18)
        self.text_0_5.setObjectName("text_0_5")
        self.gridLayout_18.addWidget(self.text_0_5, 0, 0, 1, 1)
        self.gridLayoutWidget_19 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_19.setGeometry(QtCore.QRect(150, 110, 73, 73))
        self.gridLayoutWidget_19.setObjectName("gridLayoutWidget_19")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.text_0_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget_19)
        self.text_0_6.setObjectName("text_0_6")
        self.gridLayout_19.addWidget(self.text_0_6, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 21))
        self.label.setObjectName("label")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(60, 10, 71, 21))
        self.score.setText("")
        self.score.setObjectName("score")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 13, 51, 16))
        self.label_2.setObjectName("label_2")
        self.maxscore = QtWidgets.QLabel(self.centralwidget)
        self.maxscore.setGeometry(QtCore.QRect(210, 10, 71, 21))
        self.maxscore.setText("")
        self.maxscore.setObjectName("maxscore")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_0_0.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#ff5500;\">2</span></p></body></html>"))
        self.text_0_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_0_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "得分："))
        self.label_2.setText(_translate("MainWindow", "最高分："))

