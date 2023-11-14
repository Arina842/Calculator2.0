
from PyQt6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import math as mt
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-weight: 600;\n"
"\n"
"}\n"
"QPushButton{\n"
"     background-color: transparent ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#666 ;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:#777 ;\n"
"}")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: #888")
        self.label.setLineWidth(8)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setStyleSheet("font-size: 40pt;\n"
"border: none;")
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.Layout_buttons = QtWidgets.QGridLayout()
        self.Layout_buttons.setObjectName("Layout_buttons")
        self.Button_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy)
        self.Button_9.setObjectName("Button_9")
        self.Layout_buttons.addWidget(self.Button_9, 2, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setObjectName("pushButton_25")
        self.Layout_buttons.addWidget(self.pushButton_25, 1, 3, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        self.Button_3.setObjectName("Button_3")
        self.Layout_buttons.addWidget(self.Button_3, 4, 3, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy)
        self.Button_5.setObjectName("Button_5")
        self.Layout_buttons.addWidget(self.Button_5, 3, 1, 1, 1)
        self.Button_ravno = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_ravno.sizePolicy().hasHeightForWidth())
        self.Button_ravno.setSizePolicy(sizePolicy)
        self.Button_ravno.setObjectName("Button_ravno")
        self.Layout_buttons.addWidget(self.Button_ravno, 5, 4, 1, 1)
        self.Button_del = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_del.sizePolicy().hasHeightForWidth())
        self.Button_del.setSizePolicy(sizePolicy)
        self.Button_del.setObjectName("Button_del")
        self.Layout_buttons.addWidget(self.Button_del, 1, 1, 1, 1)
        self.Button_mnog = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_mnog.sizePolicy().hasHeightForWidth())
        self.Button_mnog.setSizePolicy(sizePolicy)
        self.Button_mnog.setObjectName("Button_mnog")
        self.Layout_buttons.addWidget(self.Button_mnog, 2, 4, 1, 1)
        self.Button_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_minus.sizePolicy().hasHeightForWidth())
        self.Button_minus.setSizePolicy(sizePolicy)
        self.Button_minus.setObjectName("Button_minus")
        self.Layout_buttons.addWidget(self.Button_minus, 3, 4, 1, 1)
        self.Button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy)
        self.Button_4.setObjectName("Button_4")
        self.Layout_buttons.addWidget(self.Button_4, 3, 0, 1, 1)
        self.Button_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_plus.sizePolicy().hasHeightForWidth())
        self.Button_plus.setSizePolicy(sizePolicy)
        self.Button_plus.setObjectName("Button_plus")
        self.Layout_buttons.addWidget(self.Button_plus, 4, 4, 1, 1)
        self.Button_delenie = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_delenie.sizePolicy().hasHeightForWidth())
        self.Button_delenie.setSizePolicy(sizePolicy)
        self.Button_delenie.setObjectName("Button_delenie")
        self.Layout_buttons.addWidget(self.Button_delenie, 1, 4, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setObjectName("pushButton_26")
        self.Layout_buttons.addWidget(self.pushButton_26, 1, 0, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        self.Button_1.setObjectName("Button_1")
        self.Layout_buttons.addWidget(self.Button_1, 4, 0, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy)
        self.Button_7.setObjectName("Button_7")
        self.Layout_buttons.addWidget(self.Button_7, 2, 0, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy)
        self.Button_8.setObjectName("Button_8")
        self.Layout_buttons.addWidget(self.Button_8, 2, 1, 1, 1)
        self.Button_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy)
        self.Button_6.setObjectName("Button_6")
        self.Layout_buttons.addWidget(self.Button_6, 3, 3, 1, 1)
        self.Button_point = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_point.sizePolicy().hasHeightForWidth())
        self.Button_point.setSizePolicy(sizePolicy)
        self.Button_point.setObjectName("Button_point")
        self.Layout_buttons.addWidget(self.Button_point, 5, 3, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        self.Button_2.setObjectName("Button_2")
        self.Layout_buttons.addWidget(self.Button_2, 4, 1, 1, 1)
        self.Button_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy)
        self.Button_0.setObjectName("Button_0")
        self.Layout_buttons.addWidget(self.Button_0, 5, 0, 1, 2)
        self.verticalLayout.addLayout(self.Layout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_25.setText(_translate("MainWindow", "!"))
        self.pushButton_25.setShortcut(_translate("MainWindow", "!"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.setShortcut(_translate("MainWindow", "3"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.setShortcut(_translate("MainWindow", "5"))
        self.Button_ravno.setText(_translate("MainWindow", "="))
        self.Button_ravno.setShortcut(_translate("MainWindow", "="))
        self.Button_ravno.setShortcut(_translate("MainWindow", "Enter"))
        self.Button_del.setText(_translate("MainWindow", "CE"))
        self.Button_del.setShortcut(_translate("MainWindow", "Del"))
        self.Button_mnog.setText(_translate("MainWindow", "*"))
        self.Button_mnog.setShortcut(_translate("MainWindow", "*"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_minus.setShortcut(_translate("MainWindow", "-"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.setShortcut(_translate("MainWindow", "4"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_plus.setShortcut(_translate("MainWindow", "+"))
        self.Button_delenie.setText(_translate("MainWindow", "/"))
        self.Button_delenie.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_26.setText(_translate("MainWindow", "C"))
        self.pushButton_26.setShortcut(_translate("MainWindow", "Backspace"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_1.setShortcut(_translate("MainWindow", "1"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.setShortcut(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.setShortcut(_translate("MainWindow", "8"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.setShortcut(_translate("MainWindow", "6"))
        self.Button_point.setText(_translate("MainWindow", "."))
        self.Button_point.setShortcut(_translate("MainWindow", "."))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.setShortcut(_translate("MainWindow", "2"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.setShortcut(_translate("MainWindow", "0"))


    def add_function(self):

        self.Button_0.clicked.connect(lambda: self.write_number(self.Button_0.text()))
        self.Button_1.clicked.connect(lambda: self.write_number(self.Button_1.text()))
        self.Button_2.clicked.connect(lambda: self.write_number(self.Button_2.text()))
        self.Button_3.clicked.connect(lambda: self.write_number(self.Button_3.text()))
        self.Button_4.clicked.connect(lambda: self.write_number(self.Button_4.text()))
        self.Button_5.clicked.connect(lambda: self.write_number(self.Button_5.text()))
        self.Button_6.clicked.connect(lambda: self.write_number(self.Button_6.text()))
        self.Button_7.clicked.connect(lambda: self.write_number(self.Button_7.text()))
        self.Button_8.clicked.connect(lambda: self.write_number(self.Button_8.text()))
        self.Button_9.clicked.connect(lambda: self.write_number(self.Button_9.text()))
        self.Button_plus.clicked.connect(lambda: self.write_number(self.Button_plus.text()))
        self.Button_minus.clicked.connect(lambda: self.write_number(self.Button_minus.text()))
        self.Button_delenie.clicked.connect(lambda: self.write_number(self.Button_delenie.text()))
        self.Button_mnog.clicked.connect(lambda: self.write_number(self.Button_mnog.text()))
        self.Button_point.clicked.connect(lambda: self.write_number(self.Button_point.text()))
        self.pushButton_25.clicked.connect(lambda: self.write_number(self.pushButton_25.text()))
        self.pushButton_26.clicked.connect(self.clear_all)
        self.Button_del.clicked.connect(self.clear_entry)
        self.Button_ravno.clicked.connect(self.results)


    def write_number(self, number):

        if self.lineEdit.text() == "0":
            self.lineEdit.setText(number)
        else:
            self.lineEdit.setText(self.lineEdit.text()+number)


    def clear_all(self) -> None:
        self.lineEdit.setText('0')
        self.label.setText(' ')
    def clear_entry(self) -> None:
        self.lineEdit.setText('0')





    def results(self):

        self.label.setText(self.lineEdit.text())
        res = eval(self.lineEdit.text())
        self.lineEdit.setText(str(res))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_function()
    MainWindow.show()
    sys.exit(app.exec())
