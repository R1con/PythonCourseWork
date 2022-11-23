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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        # self.Format_text = QtWidgets.QLineEdit(self.widget)
        # self.Format_text.setGeometry(QtCore.QRect(150, 240, 240, 40))
        # font = QtGui.QFont()
        # font.setFamily("MS Reference Sans Serif")
        # font.setPointSize(12)
        # self.Format_text.setFont(font)
        # self.Format_text.setStyleSheet("QLineEdit{\n"
        #                                "    border: 2px solid rgb(37, 39, 48);\n"
        #                                "    border-radius: 20px;\n"
        #                                "    color:#FFF;\n"
        #                                "    padding-left: 20px;\n"
        #                                "    padding-right: 20px;\n"
        #                                "    background-color: rgb(34, 36, 44);\n"
        #                                "}\n"
        #                                "QLineEdit:hover{\n"
        #                                "    border: 2px solid rgb(48, 50, 62);\n"
        #                                "}\n"
        #                                "QLineEdit:focus{\n"
        #                                "    border: 2px solid rgb(85, 170, 250);\n"
        #                                "}")
        # self.Format_text.setObjectName("Format_text")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 10, 380, 46))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Text_text = QtWidgets.QLineEdit(self.widget)
        self.Text_text.setGeometry(QtCore.QRect(120, 240, 301, 221))
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
        self.Text_text.setObjectName("Text_text")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(210, 520, 111, 61))
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
        self.pushButton.setObjectName("pushButton")
        #        self.pushButton.clicked.connect(self.clicked)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("Form", "Welcome to Azimuth"))
        self.label_2.setText(_translate("Form", "Shorthand is one of the methods of encoding textual information using special characters."))
        self.Key_text.setPlaceholderText(_translate("Form", "Enter Key..."))
        self.Img_text.setPlaceholderText(_translate("Form", "Enter Img..."))
        # self.Format_text.setPlaceholderText(_translate("Form", "Enter Format..."))
        self.Text_text.setPlaceholderText(_translate("Form", "Enter Text..."))
        self.pushButton.setText(_translate("Form", "Push"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked)


    def clicked(self):
        listFileName = self.Img_text.text().split(".")
        if not (self.Text_text.text() and self.Key_text.text() and self.Img_text.text()):
            QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Вы не полность ввели в поле записи данные , записывать нечего.'
            )
            return
        if  (listFileName[1]!= "PNG" and listFileName[1] != 'jpg'):
            msg = QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Данный формат файла не поддерживается. Введите файл с .jpg, .png'
            )
            return
        Steganography.generate_key("")
        secret = Steganography.encrypt(f"{self.Key_text.text()}",
                                       'img/' + f'{self.Img_text.text()}',
                                       'secret_message.txt')
        secret.save("img/" + f'{self.Img_text.text()}' + "_cecret.png")
        print(f'{self.Key_text.text()}')
        print(f'{self.Img_text.text()}')
        print(f'{self.Text_text.text()}')


        file_name = "secret_message.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f' {self.Text_text.text()}')

        msg = QtWidgets.QMessageBox.information(
            self,
            'Успех',
            f'Введенные данные записаны в файл {file_name} и сохранены ваши параметры.'
        )



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())