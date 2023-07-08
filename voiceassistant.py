from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_voiceassistant(object):
    def setupUi(self, voiceassistant):
        voiceassistant.setObjectName("voiceassistant")
        voiceassistant.resize(843, 658)
        self.centralwidget = QtWidgets.QWidget(voiceassistant)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 481, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("jarvisimg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.push_run = QtWidgets.QPushButton(self.centralwidget)
        self.push_run.setGeometry(QtCore.QRect(40, 380, 131, 71))
        self.push_run.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 63 8pt \"Segoe UI Variable Display Semib\";\n"
"border-color: rgb(255, 255, 255);")
        self.push_run.setObjectName("push_run")
        self.push_exit = QtWidgets.QPushButton(self.centralwidget)
        self.push_exit.setGeometry(QtCore.QRect(30, 460, 141, 71))
        self.push_exit.setObjectName("push_exit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 241, 101))
        self.label_2.setStyleSheet("font: 100 italic 15pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        voiceassistant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(voiceassistant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 26))
        self.menubar.setObjectName("menubar")
        voiceassistant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(voiceassistant)
        self.statusbar.setObjectName("statusbar")
        voiceassistant.setStatusBar(self.statusbar)

        self.retranslateUi(voiceassistant)
        QtCore.QMetaObject.connectSlotsByName(voiceassistant)

    def retranslateUi(self, voiceassistant):
        _translate = QtCore.QCoreApplication.translate
        voiceassistant.setWindowTitle(_translate("voiceassistant", "Jarvis"))
        self.push_run.setText(_translate("voiceassistant", "Speak"))
        self.push_exit.setText(_translate("voiceassistant", "Exit"))
        self.label_2.setText(_translate("voiceassistant", "Desktop Assistant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voiceassistant = QtWidgets.QMainWindow()
    ui = Ui_voiceassistant()
    ui.setupUi(voiceassistant)
    voiceassistant.show()
    sys.exit(app.exec_())
