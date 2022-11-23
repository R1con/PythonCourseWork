from PyQt5 import QtCore, QtGui, QtWidgets
from steganocryptopy.steganography import Steganography

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 641)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 551, 651))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(102, 130, 255, 255), stop:0.55 rgba(175, 61, 235, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 10, 380, 46))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 511, 20))
        self.label_2.setObjectName("label_2")
        self.Key_text = QtWidgets.QLineEdit(self.widget)
        self.Key_text.setGeometry(QtCore.QRect(150, 140, 240, 40))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.Key_text.setFont(font)
        self.Key_text.setStyleSheet("QLineEdit{\n"
                                    "    border: 2px solid rgb(37, 39, 48);\n"
                                    "    border-radius: 20px;\n"
                                    "    color:#FFF;\n"
                                    "    padding-left: 20px;\n"
                                    "    padding-right: 20px;\n"
                                    "    background-color: rgb(34, 36, 44);\n"
                                    "}\n"
                                    "QLineEdit:hover{\n"
                                    "    border: 2px solid rgb(48, 50, 62);\n"
                                    "}\n"
                                    "QLineEdit:focus{\n"
                                    "    border: 2px solid rgb(85, 170, 250);\n"
                                    "}")
        self.Key_text.setObjectName("Key_text")
        self.Img_text = QtWidgets.QLineEdit(self.widget)
        self.Img_text.setGeometry(QtCore.QRect(150, 190, 240, 40))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.Img_text.setFont(font)
        self.Img_text.setStyleSheet("QLineEdit{\n"
                                    "    border: 2px solid rgb(37, 39, 48);\n"
                                    "    border-radius: 20px;\n"
                                    "    color:#FFF;\n"
                                    "    padding-left: 20px;\n"
                                    "    padding-right: 20px;\n"
                                    "    background-color: rgb(34, 36, 44);\n"
                                    "}\n"
                                    "QLineEdit:hover{\n"
                                    "    border: 2px solid rgb(48, 50, 62);\n"
                                    "}\n"
                                    "QLineEdit:focus{\n"
                                    "    border: 2px solid rgb(85, 170, 250);\n"
                                    "}")
        self.Img_text.setObjectName("Img_text")
        self.Text_text = QtWidgets.QLineEdit(self.widget)
        self.Text_text.setGeometry(QtCore.QRect(120, 330, 300, 220))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.Text_text.setFont(font)
        self.Text_text.setStyleSheet("QLineEdit{\n"
                                     "    border: 2px solid rgb(37, 39, 48);\n"
                                     "    border-radius: 20px;\n"
                                     "    color:#FFF;\n"
                                     "    padding-left: 20px;\n"
                                     "    padding-right: 20px;\n"
                                     "    background-color: rgb(34, 36, 44);\n"
                                     "}\n"
                                     "QLineEdit:hover{\n"
                                     "    border: 2px solid rgb(48, 50, 62);\n"
                                     "}\n"
                                     "QLineEdit:focus{\n"
                                     "    border: 2px solid rgb(85, 170, 250);\n"
                                     "}")
        self.Text_text.setPlaceholderText("")
        self.Text_text.setObjectName("Text_text")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 121, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border: 2px solid rgb(37, 39, 48);\n"
                                      "    border-radius: 10px;\n"
                                      "    color:#FFF;\n"
                                      "    padding-left: 10px;\n"
                                      "    padding-right: 10px;\n"
                                      "    background-color: rgb(34, 36, 44);\n"
                                      "    border-bottom: 5px solid rgb(34, 36, 44);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border: 2px solid rgb(48, 50, 62);\n"
                                      "}\n"
                                      "QPushButton:focus{\n"
                                      "    border: 2px solid rgb(85, 170, 250);\n"
                                      "}")
        #        self.pushButton.clicked.connect(self.clicked)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome to Azimuth"))
        self.label_2.setText(_translate("Form",
                                        "Shorthand is one of the methods of encoding textual information using special characters."))
        self.Key_text.setPlaceholderText(_translate("Form", "Enter Key..."))
        self.Img_text.setPlaceholderText(_translate("Form", "Enter Img..."))
        self.pushButton.setText(_translate("Form", "Push"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked)


    def clicked(self):
        if not (self.Img_text.text() and self.Key_text.text()):
            msg = QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Вы не полность ввели в поле записи данные , записывать нечего.'
            )
            return
        result = Steganography.decrypt(f'{self.Key_text.text()}', "img/" + f'{self.Img_text.text()}' + ".PNG_cecret.png")


        file_name = "secret_message.txt"
        with open(file_name, 'r', encoding='utf-8') as file:
            record = file.read()
            self.Text_text.setPlaceholderText(record)





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())