# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue May 21 16:59:59 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import patterns, play_pattern

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
        MainWindow.resize(482, 225)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 469, 181))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pattern = QtGui.QLabel(self.gridLayoutWidget)
        self.pattern.setObjectName(_fromUtf8("Pattern"))
        self.pattern.setText("Pattern :")
        self.gridLayout.addWidget(self.pattern, 0, 1, 1, 1)
        self.gamme = QtGui.QLabel(self.gridLayoutWidget)
        self.gamme.setObjectName(_fromUtf8("Gamme"))
        self.gamme.setText("Gamme :")
        self.gridLayout.addWidget(self.gamme, 0, 4, 1, 1)
        self.gammeBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.gammeBox.setObjectName(_fromUtf8("gammeBox"))
        self.gammeBox.addItem("G")
        self.gammeBox.addItem("G#")
        self.gammeBox.addItem("A")
        self.gammeBox.addItem("A#")
        self.gammeBox.addItem("B")
        self.gammeBox.addItem("B#")
        self.gammeBox.addItem("C")
        self.gammeBox.addItem("C#")
        self.gammeBox.addItem("D")
        self.gammeBox.addItem("D#")
        self.gammeBox.addItem("E")
        self.gammeBox.addItem("E#")
        self.gammeBox.addItem("F")
        self.gammeBox.addItem("F#")
        self.gridLayout.addWidget(self.gammeBox, 0, 5, 1, 1)
        self.patternBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.patternBox.setObjectName(_fromUtf8("patternBox"))
        for i in range(len(patterns.PATTERNS)):
            self.patternBox.addItem("pattern "+str(i))
        self.gridLayout.addWidget(self.patternBox, 0, 2, 1, 1)
        self.tempoBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.tempoBox.setObjectName(_fromUtf8("tempoBox"))
        self.tempoBox.addItem("60")
        self.tempoBox.addItem("70")
        self.tempoBox.addItem("80")
        self.tempoBox.addItem("90")
        self.tempoBox.addItem("100")
        self.tempoBox.addItem("110")
        self.tempoBox.addItem("120")
        self.gridLayout.addWidget(self.tempoBox, 3, 2, 1, 1)
        self.structure = QtGui.QLabel(self.gridLayoutWidget)
        self.structure.setObjectName(_fromUtf8("Structure"))
        self.structure.setText("Structure :")
        self.gridLayout.addWidget(self.structure, 2, 1, 1, 1)
        self.playPattern = QtGui.QPushButton(self.gridLayoutWidget)
        self.playPattern.setObjectName(_fromUtf8("playPattern"))
        self.playPattern.setText("Play")
        self.gridLayout.addWidget(self.playPattern, 0, 3, 1, 1)
        self.validateButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.validateButton.setObjectName(_fromUtf8("validateButton"))
        self.validateButton.setText("Valider")
        self.gridLayout.addWidget(self.validateButton, 4, 5, 1, 1)
        self.longueurText = QtGui.QLineEdit(self.gridLayoutWidget)
        self.longueurText.setText(_fromUtf8(""))
        self.longueurText.setObjectName(_fromUtf8("longueurText"))
        self.gridLayout.addWidget(self.longueurText, 2, 5, 1, 1)
        self.tempo = QtGui.QLabel(self.gridLayoutWidget)
        self.tempo.setObjectName(_fromUtf8("Tempo"))
        self.tempo.setText("Tempo :")
        self.gridLayout.addWidget(self.tempo, 3, 1, 1, 1)
        self.structureBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.structureBox.setObjectName(_fromUtf8("structureBox"))
        self.structureBox.addItem("12")
        self.gridLayout.addWidget(self.structureBox, 2, 2, 1, 1)
        self.longueur = QtGui.QLabel(self.gridLayoutWidget)
        self.longueur.setObjectName(_fromUtf8("Longueur"))
        self.longueur.setText("Longueur :")
        self.gridLayout.addWidget(self.longueur, 2, 4, 1, 1)
        self.mode = QtGui.QLabel(self.gridLayoutWidget)
        self.mode.setObjectName(_fromUtf8("Mode"))
        self.mode.setText("Mode :")
        self.gridLayout.addWidget(self.mode, 3, 4, 1, 1)
        self.modeBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.modeBox.setObjectName(_fromUtf8("modeBox"))
        self.modeBox.addItem("Classique")
        self.modeBox.addItem("Mixolydien")
        self.gridLayout.addWidget(self.modeBox, 3, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionFermer = QtGui.QAction(MainWindow)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))

        self.playPattern.clicked.connect(self.handlePlayPattern)
        self.validateButton.clicked.connect(self.handleValidateButton)

        MainWindow.setWindowTitle("MainWindow")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def handlePlayPattern(self):
        play_pattern.play_pattern(patterns.PATTERNS[self.patternBox.currentIndex()], str(self.gammeBox.currentText()))
        
    def handleValidateButton(self):
        print "Generate Composition with :"
        print "pattern : " + self.patternBox.currentText()
        print "gamme : " + self.gammeBox.currentText()
        print "Structure : " + self.structureBox.currentText()
        print "Longueur : " + self.longueurText.text()
        print "Tempo : " + self.tempoBox.currentText()
        print "Mode : " + self.modeBox.currentText()
        
        