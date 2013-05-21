# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue May 21 16:21:31 2013
#      by: PyQt4 UI code generator 4.10.1
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
        MainWindow.resize(434, 224)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 421, 181))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_4 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_4, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 4, 1, 1)
        self.longueur = QtGui.QSlider(self.gridLayoutWidget)
        self.longueur.setMinimumSize(QtCore.QSize(164, 22))
        self.longueur.setOrientation(QtCore.Qt.Horizontal)
        self.longueur.setObjectName(_fromUtf8("longueur"))
        self.gridLayout.addWidget(self.longueur, 1, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFermer = QtGui.QAction(MainWindow)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
        self.menuFichier.addAction(self.actionFermer)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "60", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "70", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "80", None))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "90", None))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "100", None))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "110", None))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "120", None))
        self.label_3.setText(_translate("MainWindow", "Structure", None))
        self.label_2.setText(_translate("MainWindow", "Gamme", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "A", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "A#", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "B#", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "C", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "C#", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "D", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "D#", None))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "E", None))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "E#", None))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "F", None))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "F#", None))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "G", None))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "G#", None))
       
        import patterns
        for i in range(len(patterns.PATTERNS)):
            print i
            self.comboBox.setItemText(i, _translate("MainWindow", "Pattern " + str(i+1), None))
        self.label.setText(_translate("MainWindow", "Pattern", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "12", None))
        self.label_4.setText(_translate("MainWindow", "Tempo", None))
        self.label_5.setText(_translate("MainWindow", "Longueur", None))
        self.pushButton.setText(_translate("MainWindow", "Valider", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionFermer.setText(_translate("MainWindow", "Fermer", None))

