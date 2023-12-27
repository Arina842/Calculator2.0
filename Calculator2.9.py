import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QDialog, QLabel,QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg  as FigureCanvas
from matplotlib.figure import Figure
import os
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 520)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #121212;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-weight: 600;\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "     background-color: transparent ;\n"
                                 "    font-size: 10.5pt;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    font-size: 10.5pt;\n"
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
        self.label.setStyleSheet("font-size: 10.5pt;" "color: #888")
        self.label.setLineWidth(25)
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setStyleSheet("font-size: 40pt;\n"
                                    "border: none;")
        self.lineEdit.setMaxLength(25)
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
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
        self.Button_Graph = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Graph.sizePolicy().hasHeightForWidth())
        self.Button_Graph.setSizePolicy(sizePolicy)
        self.Button_Graph.setObjectName("pushButton_25")
        self.Layout_buttons.addWidget(self.Button_Graph, 1, 5, 1, 1)
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
        self.Button_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_equal.sizePolicy().hasHeightForWidth())
        self.Button_equal.setSizePolicy(sizePolicy)
        self.Button_equal.setObjectName("Button_ravno")
        self.Layout_buttons.addWidget(self.Button_equal, 5, 4, 1, 1)
        self.Button_CE = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_CE.sizePolicy().hasHeightForWidth())
        self.Button_CE.setSizePolicy(sizePolicy)
        self.Button_CE.setObjectName("Button_del")
        self.Layout_buttons.addWidget(self.Button_CE, 1, 1, 1, 1)
        self.Button_multiply = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_multiply.sizePolicy().hasHeightForWidth())
        self.Button_multiply.setSizePolicy(sizePolicy)
        self.Button_multiply.setObjectName("Button_mnog")
        self.Layout_buttons.addWidget(self.Button_multiply, 2, 4, 1, 1)
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
        self.Button_division = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_division.sizePolicy().hasHeightForWidth())
        self.Button_division.setSizePolicy(sizePolicy)
        self.Button_division.setObjectName("Button_delenie")
        self.Layout_buttons.addWidget(self.Button_division, 1, 4, 1, 1)
        self.Button_C = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_C.sizePolicy().hasHeightForWidth())
        self.Button_C.setSizePolicy(sizePolicy)
        self.Button_C.setObjectName("pushButton_26")
        self.Layout_buttons.addWidget(self.Button_C, 1, 0, 1, 1)
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
        self.Button_del1 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_del1.sizePolicy().hasHeightForWidth())
        self.Button_del1.setSizePolicy(sizePolicy)
        self.Button_del1.setObjectName("Button_delenie")
        self.Layout_buttons.addWidget(self.Button_del1, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.Layout_buttons)
        self.Button_parentheses = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_parentheses.sizePolicy().hasHeightForWidth())
        self.Button_parentheses.setSizePolicy(sizePolicy)
        self.Button_parentheses.setObjectName("Button_skobki")
        self.Layout_buttons.addWidget(self.Button_parentheses, 2, 5, 1, 1)
        self.Button_square = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_square.sizePolicy().hasHeightForWidth())
        self.Button_square.setSizePolicy(sizePolicy)
        self.Button_square.setObjectName("Button_sqrt")
        self.Layout_buttons.addWidget(self.Button_square, 3, 5, 1, 1)
        self.Button_22 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_22.sizePolicy().hasHeightForWidth())
        self.Button_22.setSizePolicy(sizePolicy)
        self.Button_22.setObjectName("Button_sqrt")
        self.Layout_buttons.addWidget(self.Button_square, 4, 5, 1, 1)
        self.Button_23 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_23.sizePolicy().hasHeightForWidth())
        self.Button_23.setSizePolicy(sizePolicy)
        self.Button_23.setObjectName("Button_sqrt")
        self.Layout_buttons.addWidget(self.Button_23, 5, 5, 1, 1)
        self.verticalLayout.addLayout(self.Layout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.lineEdit.setText(_translate("MainWindow", "0"))

        self.Button_Graph.setText(_translate("MainWindow", "Graph"))
        self.Button_Graph.setShortcut(_translate("MainWindow", "Graph"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.setShortcut(_translate("MainWindow", "0"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_1.setShortcut(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.setShortcut(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.setShortcut(_translate("MainWindow", "3"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.setShortcut(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.setShortcut(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.setShortcut(_translate("MainWindow", "6"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.setShortcut(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.setShortcut(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.setShortcut(_translate("MainWindow", "9"))
        self.Button_equal.setText(_translate("MainWindow", "="))
        self.Button_equal.setShortcut(_translate("MainWindow", "="))
        self.Button_equal.setShortcut(_translate("MainWindow", "Enter"))
        self.Button_CE.setText(_translate("MainWindow", "CE"))
        self.Button_CE.setShortcut(_translate("MainWindow", "Del"))
        self.Button_multiply.setText(_translate("MainWindow", "*"))
        self.Button_multiply.setShortcut(_translate("MainWindow", "*"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_minus.setShortcut(_translate("MainWindow", "-"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_plus.setShortcut(_translate("MainWindow", "+"))
        self.Button_division.setText(_translate("MainWindow", "/"))
        self.Button_division.setShortcut(_translate("MainWindow", "/"))
        self.Button_C.setText(_translate("MainWindow", "C"))
        self.Button_C.setShortcut(_translate("MainWindow", ""))
        self.Button_del1.setText(_translate("MainWindow", "🖾"))
        self.Button_del1.setShortcut(_translate("MainWindow", "Backspace"))
        self.Button_point.setText(_translate("MainWindow", "."))
        self.Button_point.setShortcut(_translate("MainWindow", "."))
        self.Button_parentheses.setText(_translate("MainWindow", "()"))
        self.Button_parentheses.setShortcut(_translate("MainWindow", "()"))



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
        self.Button_division.clicked.connect(lambda: self.write_number(self.Button_division.text()))
        self.Button_multiply.clicked.connect(lambda: self.write_number(self.Button_multiply.text()))
        self.Button_point.clicked.connect(lambda: self.write_number(self.Button_point.text()))
        self.Button_del1.clicked.connect(self.del1)
        self.Button_Graph.clicked.connect(self.show_plot)
        self.Button_C.clicked.connect(self.clear_all)
        self.Button_CE.clicked.connect(self.clear_entry)
        self.Button_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.lineEdit.text() == "0":
            self.lineEdit.setText(number)
        else:
            self.lineEdit.setText(self.lineEdit.text() + number)
            k = self.lineEdit.text()[-2:]
            l = ''.join(k)
            if l == '/0':
                self.label.setText('Division by zero is not possible')
                k = self.lineEdit.text()[:-1]
                l = ''.join(k)
                self.lineEdit.setText(l)
                #while l == 'self.Button_ravno.blockSignals(True)
            if l == '..' or l == '++' or l == '--' or l == '//' or l == '-*' or l == '+-+'or l == '-+-':
                k = self.lineEdit.text()[:-1]
                l = ''.join(k)
                self.lineEdit.setText(l)
            if l == '/*' or l == '*/' or l == '.-' or l == '-.' or l == '+.' or l == '.+':
                k = self.lineEdit.text()[:-2] + self.lineEdit.text()[-1:]
                l = ''.join(k)
                self.lineEdit.setText(l)

    def del1(self):
        k = self.lineEdit.text()[:-1]
        l = ''.join(k)
        self.lineEdit.setText(l)
    def clear_all(self) -> None:
        self.lineEdit.setText('0')
        self.label.setText(' ')

    def clear_entry(self) -> None:
        self.lineEdit.setText('0')




    def results(self):
        try:
            self.label.setText(self.lineEdit.text() + self.Button_equal.text())
            res = eval(self.lineEdit.text())
            rounded_res = round(res, 4)
            self.lineEdit.setText(str(rounded_res))
        except:
            self.label.setText('incorrect input')
            self.lineEdit.setText('0')


    def show_plot(self):
        self.plotDialog.show()

    def setPlot(self, Dialog):
        self.plotDialog = Dialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 520)
        Dialog.move(1055, 180)
        Dialog.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-weight: 600;\n"
"\n"
"}\n"
"QLineEdit{\n"
"    background-color: transparent ;\n"
"    border: none;\n"
"    font-size: 10.5pt;\n"
"}\n"
"\n"
"QListWidget{\n"
"     background-color: transparent ;\n"
"     border: none;\n"
"}\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.figure = plt.figure(dpi=85)
        self.figure.suptitle("Graph", fontsize=14)

        self.canvas = FigureCanvas(self.figure)
        self.ax_G = self.figure.add_subplot()
        self.ax_G.set_ylabel("y", fontsize=11)
        self.ax_G.set_xlabel("x", fontsize=11)
        self.ax_G.grid()
        self.canvas.draw()
        self.verticalLayout.addWidget(self.canvas)

        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.Button_1 = QtWidgets.QPushButton(parent=Dialog)
        self.Button_1.setMinimumSize(QtCore.QSize(0, 20))
        self.Button_1.setObjectName("")
        self.verticalLayout.addWidget(self.Button_1)
        self.Button_1.clicked.connect(self.show_plot)
        self.Button_2 = QtWidgets.QPushButton(parent=Dialog)
        self.Button_2.setMinimumSize(QtCore.QSize(0, 20))
        self.Button_2.setObjectName("")
        self.Button_2.clicked.connect(self.delete_xy)
        self.verticalLayout.addWidget(self.Button_2)
        self.Button_3 = QtWidgets.QPushButton(parent=Dialog)
        self.Button_3.setMinimumSize(QtCore.QSize(0, 20))
        self.Button_3.setObjectName("")
        self.Button_3.clicked.connect(self.clear_all)
        self.verticalLayout.addWidget(self.Button_3)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def delete_xy (self, Dialog):

        self.lineEdit.setText('y=')
        self.lineEdit_2.setText('x=')


    def clear_all(self, Dialog):

        self.lineEdit.setText('y=')
        self.lineEdit_2.setText('x=')
        self.ax_G.cla()
        self.ax_G.grid()
        self.ax_G.set_ylabel("y")
        self.ax_G.set_xlabel("x")
        self.canvas.draw()

    def show_plot(self, Dialog):
        try:
            y = self.lineEdit.text()
            x = self.lineEdit_2.text()
            if 'y=' in y or 'x=' in x:
                y = y.replace('y=', '')
                x = x.replace('x=', '')
            y = y.split(',')
            y = list(map(int, y))
            x = x.split(',')
            x = list(map(int, x))
            self.ax_G.plot(x, y)
            self.canvas.draw()
        except:
            dlg = QMessageBox()
            dlg.setWindowTitle("Mistake")
            dlg.setText("Enter other values")
            dlg.move(1200, 350)
            dlg.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "y="))
        self.lineEdit_2.setText(_translate("Dialog", "x="))
        self.Button_1.setText(_translate("Dialog", "Create"))
        self.Button_2.setText(_translate("Dialog", "Delete x, y"))
        self.Button_3.setText(_translate("Dialog", "Clear all"))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_function()
    MainWindow.show()
    Dialog = QtWidgets.QDialog()
    uid = Ui_Dialog()
    uid.setupUi(Dialog)
    ui.setPlot(Dialog)
    sys.exit(app.exec())
