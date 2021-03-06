# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CurWork = QtWidgets.QScrollArea(self.centralwidget)
        self.CurWork.setGeometry(QtCore.QRect(20, 180, 591, 461))
        self.CurWork.setWidgetResizable(True)
        self.CurWork.setObjectName("CurWork")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 587, 457))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.CurWork.setWidget(self.scrollAreaWidgetContents)
        self.Themes = QtWidgets.QScrollArea(self.centralwidget)
        self.Themes.setGeometry(QtCore.QRect(630, 80, 501, 561))
        self.Themes.setWidgetResizable(True)
        self.Themes.setObjectName("Themes")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 497, 557))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Themes.setWidget(self.scrollAreaWidgetContents_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 1116, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.NameWork = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.NameWork.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NameWork.setFont(font)
        self.NameWork.setDragEnabled(True)
        self.NameWork.setObjectName("NameWork")
        self.horizontalLayout.addWidget(self.NameWork)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(609, 60, 16, 591))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-20, 50, 1171, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 591, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.NVar = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NVar.setFont(font)
        self.NVar.setObjectName("NVar")
        self.horizontalLayout_2.addWidget(self.NVar)
        self.Import = QtWidgets.QPushButton(self.centralwidget)
        self.Import.setGeometry(QtCore.QRect(20, 650, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Import.setFont(font)
        self.Import.setObjectName("Import")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 20))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Ctrl_N = QtWidgets.QAction(MainWindow)
        self.action_Ctrl_N.setObjectName("action_Ctrl_N")
        self.action_Ctrl_I = QtWidgets.QAction(MainWindow)
        self.action_Ctrl_I.setObjectName("action_Ctrl_I")
        self.action_Word_Shift_I = QtWidgets.QAction(MainWindow)
        self.action_Word_Shift_I.setObjectName("action_Word_Shift_I")
        self.menuMenu.addAction(self.action_Ctrl_N)
        self.menuMenu.addAction(self.action_Word_Shift_I)
        self.menuHelp.addAction(self.action_Ctrl_I)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "???????????? ????????????:"))
        self.label.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.label_3.setText(_translate("MainWindow", "  ???????????????? ???????? ??????????????, ?????????????? ???????????? ?? ????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????????? ??????????????????"))
        self.Import.setText(_translate("MainWindow", "?????????????????????????? ?? Word"))
        self.menuMenu.setTitle(_translate("MainWindow", "????????"))
        self.menuHelp.setTitle(_translate("MainWindow", "????????????"))
        self.action_Ctrl_N.setText(_translate("MainWindow", "???????????????? ???????????? (Ctrl + N)"))
        self.action_Ctrl_I.setText(_translate("MainWindow", "?????????????? (Ctrl + I)"))
        self.action_Word_Shift_I.setText(_translate("MainWindow", "?????????????????????????? ?? Word (Shift + I)"))
