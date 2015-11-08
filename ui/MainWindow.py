# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(954, 421)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Execute = QtGui.QPushButton(self.centralwidget)
        self.Execute.setObjectName(_fromUtf8("Execute"))
        self.gridLayout.addWidget(self.Execute, 3, 0, 1, 2)
        self.ConsoleLabel = QtGui.QLabel(self.centralwidget)
        self.ConsoleLabel.setObjectName(_fromUtf8("ConsoleLabel"))
        self.gridLayout.addWidget(self.ConsoleLabel, 0, 0, 1, 2)
        self.TableLabel = QtGui.QLabel(self.centralwidget)
        self.TableLabel.setObjectName(_fromUtf8("TableLabel"))
        self.gridLayout.addWidget(self.TableLabel, 0, 2, 1, 2)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.tableWidget, 1, 2, 1, 2)
        self.NewCommand = QtGui.QPushButton(self.centralwidget)
        self.NewCommand.setObjectName(_fromUtf8("NewCommand"))
        self.gridLayout.addWidget(self.NewCommand, 3, 3, 1, 1)
        self.ConsoleOutput = QtGui.QPlainTextEdit(self.centralwidget)
        self.ConsoleOutput.setPlainText(_fromUtf8(""))
        self.ConsoleOutput.setObjectName(_fromUtf8("ConsoleOutput"))
        self.gridLayout.addWidget(self.ConsoleOutput, 1, 0, 1, 2)
        self.DeleteCommand = QtGui.QPushButton(self.centralwidget)
        self.DeleteCommand.setObjectName(_fromUtf8("DeleteCommand"))
        self.gridLayout.addWidget(self.DeleteCommand, 3, 2, 1, 1)
        self.TeachCommand = QtGui.QPushButton(self.centralwidget)
        self.TeachCommand.setObjectName(_fromUtf8("TeachCommand"))
        self.gridLayout.addWidget(self.TeachCommand, 4, 2, 1, 1)
        self.UpdateModel = QtGui.QPushButton(self.centralwidget)
        self.UpdateModel.setObjectName(_fromUtf8("UpdateModel"))
        self.gridLayout.addWidget(self.UpdateModel, 4, 3, 1, 1)
        self.DatabaseLoaded = QtGui.QCheckBox(self.centralwidget)
        self.DatabaseLoaded.setEnabled(False)
        self.DatabaseLoaded.setMouseTracking(False)
        self.DatabaseLoaded.setCheckable(True)
        self.DatabaseLoaded.setAutoExclusive(False)
        self.DatabaseLoaded.setObjectName(_fromUtf8("DatabaseLoaded"))
        self.gridLayout.addWidget(self.DatabaseLoaded, 4, 0, 1, 1)
        self.ActiveModel = QtGui.QCheckBox(self.centralwidget)
        self.ActiveModel.setEnabled(False)
        self.ActiveModel.setMouseTracking(False)
        self.ActiveModel.setCheckable(True)
        self.ActiveModel.setAutoExclusive(False)
        self.ActiveModel.setObjectName(_fromUtf8("ActiveModel"))
        self.gridLayout.addWidget(self.ActiveModel, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave_Database = QtGui.QAction(MainWindow)
        self.actionSave_Database.setObjectName(_fromUtf8("actionSave_Database"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNew_Database = QtGui.QAction(MainWindow)
        self.actionNew_Database.setObjectName(_fromUtf8("actionNew_Database"))
        self.menuFile.addAction(self.actionNew_Database)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Leap Commander", None))
        self.Execute.setText(_translate("MainWindow", "Execute", None))
        self.ConsoleLabel.setText(_translate("MainWindow", "Console Output", None))
        self.TableLabel.setText(_translate("MainWindow", "Table of Commands", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Command", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number of Datapoints", None))
        self.NewCommand.setText(_translate("MainWindow", "New Command", None))
        self.DeleteCommand.setText(_translate("MainWindow", "Delete Command", None))
        self.TeachCommand.setText(_translate("MainWindow", " Teach Command", None))
        self.UpdateModel.setText(_translate("MainWindow", "Update Model", None))
        self.DatabaseLoaded.setText(_translate("MainWindow", "Database Loaded", None))
        self.ActiveModel.setText(_translate("MainWindow", "Active Model", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open Database", None))
        self.actionSave_Database.setText(_translate("MainWindow", "Save Database", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNew_Database.setText(_translate("MainWindow", "New Database", None))

