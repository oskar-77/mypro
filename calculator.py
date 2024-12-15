

import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 676)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(193, 31, 185, 255), stop:1 rgba(70, 46, 255, 255));\n"
"")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(330, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(410, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(490, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("border-radius: 35px;\n"
"padding: 10px;\n"
"color: white;\n"
"background-color: rgb(96, 163, 188);")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton5 = QtWidgets.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(410, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(490, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(Form)
        self.pushButton7.setGeometry(QtCore.QRect(330, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton7.setFont(font)
        self.pushButton7.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton0 = QtWidgets.QPushButton(Form)
        self.pushButton0.setGeometry(QtCore.QRect(330, 500, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton0.setFont(font)
        self.pushButton0.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton0.setObjectName("pushButton0")
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(330, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton8 = QtWidgets.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(410, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton8.setFont(font)
        self.pushButton8.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton9 = QtWidgets.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(490, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.pushButton9.setFont(font)
        self.pushButton9.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.pushButton9.setObjectName("pushButton9")
        self.push_add = QtWidgets.QPushButton(Form)
        self.push_add.setGeometry(QtCore.QRect(570, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.push_add.setFont(font)
        self.push_add.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(248, 194, 145);\n"
"padding: 10px;\n"
"color: black;")
        self.push_add.setObjectName("push_add")
        self.push_div = QtWidgets.QPushButton(Form)
        self.push_div.setGeometry(QtCore.QRect(570, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.push_div.setFont(font)
        self.push_div.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(248, 194, 145);\n"
"padding: 10px;\n"
"color: black;\n"
"")
        self.push_div.setObjectName("push_div")
        self.push_sub = QtWidgets.QPushButton(Form)
        self.push_sub.setGeometry(QtCore.QRect(570, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.push_sub.setFont(font)
        self.push_sub.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(248, 194, 145);\n"
"padding: 10px;\n"
"color: black;")
        self.push_sub.setObjectName("push_sub")
        self.push_mul = QtWidgets.QPushButton(Form)
        self.push_mul.setGeometry(QtCore.QRect(570, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        self.push_mul.setFont(font)
        self.push_mul.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(248, 194, 145);\n"
"padding: 10px;\n"
"color: black;")
        self.push_mul.setObjectName("push_mul")
        self.push_clear = QtWidgets.QPushButton(Form)
        self.push_clear.setGeometry(QtCore.QRect(330, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_clear.setFont(font)
        self.push_clear.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(74, 105, 189);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.push_clear.setObjectName("push_clear")
        self.push_deci = QtWidgets.QPushButton(Form)
        self.push_deci.setGeometry(QtCore.QRect(490, 500, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.push_deci.setFont(font)
        self.push_deci.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(96, 163, 188);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.push_deci.setObjectName("push_deci")
        self.push_del = QtWidgets.QPushButton(Form)
        self.push_del.setGeometry(QtCore.QRect(410, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_del.setFont(font)
        self.push_del.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(74, 105, 189);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.push_del.setObjectName("push_del")
        self.push_per = QtWidgets.QPushButton(Form)
        self.push_per.setGeometry(QtCore.QRect(490, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_per.setFont(font)
        self.push_per.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(74, 105, 189);\n"
"padding: 10px;\n"
"color: white;\n"
"")
        self.push_per.setObjectName("push_per")
        self.push_equal = QtWidgets.QPushButton(Form)
        self.push_equal.setGeometry(QtCore.QRect(570, 500, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.push_equal.setFont(font)
        self.push_equal.setStyleSheet("border-radius: 35px;\n"
"background-color: rgb(248, 194, 145);\n"
"padding: 10px;\n"
"color: black;")
        self.push_equal.setObjectName("push_equal")
        self.push_sin = QtWidgets.QPushButton(Form)
        self.push_sin.setGeometry(QtCore.QRect(90, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_sin.setFont(font)
        self.push_sin.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_sin.setObjectName("push_sin")
        self.push_cos = QtWidgets.QPushButton(Form)
        self.push_cos.setGeometry(QtCore.QRect(170, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_cos.setFont(font)
        self.push_cos.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_cos.setObjectName("push_cos")
        self.push_tan = QtWidgets.QPushButton(Form)
        self.push_tan.setGeometry(QtCore.QRect(250, 260, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_tan.setFont(font)
        self.push_tan.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_tan.setObjectName("push_tan")
        self.push_sqrt = QtWidgets.QPushButton(Form)
        self.push_sqrt.setGeometry(QtCore.QRect(90, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_sqrt.setFont(font)
        self.push_sqrt.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_sqrt.setObjectName("push_sqrt")
        self.push_exp = QtWidgets.QPushButton(Form)
        self.push_exp.setGeometry(QtCore.QRect(250, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_exp.setFont(font)
        self.push_exp.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_exp.setObjectName("push_exp")
        self.push_log10 = QtWidgets.QPushButton(Form)
        self.push_log10.setGeometry(QtCore.QRect(250, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_log10.setFont(font)
        self.push_log10.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_log10.setObjectName("push_log10")
        self.push_pi = QtWidgets.QPushButton(Form)
        self.push_pi.setGeometry(QtCore.QRect(90, 500, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_pi.setFont(font)
        self.push_pi.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_pi.setObjectName("push_pi")
        self.push_degree = QtWidgets.QPushButton(Form)
        self.push_degree.setGeometry(QtCore.QRect(170, 500, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_degree.setFont(font)
        self.push_degree.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_degree.setObjectName("push_degree")
        self.push_rad = QtWidgets.QPushButton(Form)
        self.push_rad.setGeometry(QtCore.QRect(250, 500, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_rad.setFont(font)
        self.push_rad.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_rad.setObjectName("push_rad")
        self.push_close = QtWidgets.QPushButton(Form)
        self.push_close.setGeometry(QtCore.QRect(250, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_close.setFont(font)
        self.push_close.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_close.setObjectName("push_close")
        self.push_open = QtWidgets.QPushButton(Form)
        self.push_open.setGeometry(QtCore.QRect(170, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_open.setFont(font)
        self.push_open.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_open.setObjectName("push_open")
        self.push_fact = QtWidgets.QPushButton(Form)
        self.push_fact.setGeometry(QtCore.QRect(90, 180, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_fact.setFont(font)
        self.push_fact.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_fact.setObjectName("push_fact")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 50, 551, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setStyleSheet("border-color: rgb(8, 11, 77);\n"
                                    "background-color: rgb(0,0,0,100); \n"
                                    "border-radius: 20px;\n"
                                    
"border-top-color: rgb(5, 5, 99);\n"
"text-align: center;\n"
"color: rgb(0, 221, 255);")
        self.textEdit.setObjectName("textEdit")
        self.push_cube = QtWidgets.QPushButton(Form)
        self.push_cube.setGeometry(QtCore.QRect(170, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_cube.setFont(font)
        self.push_cube.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_cube.setObjectName("push_cube")
        self.push_sq = QtWidgets.QPushButton(Form)
        self.push_sq.setGeometry(QtCore.QRect(90, 340, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_sq.setFont(font)
        self.push_sq.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_sq.setObjectName("push_sq")
        self.push_ln = QtWidgets.QPushButton(Form)
        self.push_ln.setGeometry(QtCore.QRect(170, 420, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.push_ln.setFont(font)
        self.push_ln.setStyleSheet("border-radius: 35px;\n"
"background-color: #ff5e00;\n"
"padding: 10px;\n"
"color: white;")
        self.push_ln.setObjectName("push_ln")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
         # adding action to each of the button
       
        self.pushButton0.clicked.connect(lambda: self.append_text("0"))
        self.pushButton1.clicked.connect(lambda: self.append_text("1"))
        self.pushButton2.clicked.connect(lambda: self.append_text("2"))
        self.pushButton3.clicked.connect(lambda: self.append_text("3"))
        self.pushButton4.clicked.connect(lambda: self.append_text("4"))
        self.pushButton5.clicked.connect(lambda: self.append_text("5"))
        self.pushButton6.clicked.connect(lambda: self.append_text("6"))
        self.pushButton7.clicked.connect(lambda: self.append_text("7"))
        self.pushButton8.clicked.connect(lambda: self.append_text("8"))
        self.pushButton9.clicked.connect(lambda: self.append_text("9"))
        
        self.push_div.clicked.connect(lambda: self.append_text("/"))
        self.push_mul.clicked.connect(lambda: self.append_text("*"))
        self.push_add.clicked.connect(lambda: self.append_text("+"))
        self.push_sub.clicked.connect(lambda: self.append_text("-"))
        self.push_per.clicked.connect(lambda: self.append_text("%"))
        
        self.push_sin.clicked.connect(lambda: self.append_text("sin("))
        self.push_cos.clicked.connect(lambda: self.append_text("cos("))
        self.push_tan.clicked.connect(lambda: self.append_text("tan("))
        self.push_sqrt.clicked.connect(lambda: self.append_text("sqrt("))
        self.push_exp.clicked.connect(lambda: self.append_text("**"))
        self.push_log10.clicked.connect(lambda: self.append_text("log("))
        self.push_pi.clicked.connect(lambda: self.append_text("π"))
        self.push_degree.clicked.connect(lambda: self.append_text("deg"))
        self.push_rad.clicked.connect(lambda: self.append_text("rad"))
        self.push_fact.clicked.connect(lambda: self.append_text("factorial("))
        self.push_cube.clicked.connect(lambda: self.append_text("**3"))
        self.push_sq.clicked.connect(lambda: self.append_text("**2"))
        self.push_ln.clicked.connect(lambda: self.append_text("ln("))
        self.push_deci.clicked.connect(lambda: self.append_text("."))
    
        self.push_clear.clicked.connect(self.action_clear)
        self.push_del.clicked.connect(self.action_del)
        self.push_equal.clicked.connect(self.result)
        
        self.push_open.clicked.connect(self.action_open)
        self.push_close.clicked.connect(self.action_close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mr.OSKAR Calculator"))
        self.pushButton0.setText(_translate("Form", "0"))
        self.pushButton1.setText(_translate("Form", "1"))
        self.pushButton2.setText(_translate("Form", "2"))
        self.pushButton3.setText(_translate("Form", "3"))
        self.pushButton5.setText(_translate("Form", "5"))
        self.pushButton6.setText(_translate("Form", "6"))
        self.pushButton7.setText(_translate("Form", "7"))
        self.pushButton4.setText(_translate("Form", "4"))
        self.pushButton8.setText(_translate("Form", "8"))
        self.pushButton9.setText(_translate("Form", "9"))
        self.push_add.setText(_translate("Form", "+"))
        self.push_div.setText(_translate("Form", "÷"))
        self.push_sub.setText(_translate("Form", "-"))
        self.push_mul.setText(_translate("Form", "x"))
        self.push_clear.setText(_translate("Form", "C"))
        self.push_deci.setText(_translate("Form", "."))
        self.push_del.setText(_translate("Form", "DEL"))
        self.push_per.setText(_translate("Form", "%"))
        self.push_equal.setText(_translate("Form", "="))
        self.push_sin.setText(_translate("Form", "sin"))
        self.push_cos.setText(_translate("Form", "cos"))
        self.push_tan.setText(_translate("Form", "tan"))
        self.push_sqrt.setText(_translate("Form", "√"))
        self.push_exp.setText(_translate("Form", "xⁿ"))
        self.push_log10.setText(_translate("Form", "log"))
        self.push_pi.setText(_translate("Form", "π"))
        self.push_degree.setText(_translate("Form", "deg"))
        self.push_rad.setText(_translate("Form", "rad"))
        self.push_close.setText(_translate("Form", ")"))
        self.push_open.setText(_translate("Form", "("))
        self.push_fact.setText(_translate("Form", "x!"))
        self.push_cube.setText(_translate("Form", "x³"))
        self.push_sq.setText(_translate("Form", "x²"))
        self.push_ln.setText(_translate("Form", "ln"))
        
    def append_text(self,text):
        current_text = self.textEdit.toPlainText()
        self.textEdit.setPlainText(current_text + text)
        
    def result(self):
        current_text = self.textEdit.toPlainText()
        try:
            if "%" in current_text:
                parts = current_text.split('%')
                if len(parts) == 2:
                    num = parts[0]
                    result = float(num) / 100
                else:
                    # Handle the case where '%' is not present in the input
                    result = None  # or any other appropriate value
                    
            else:

                # Evaluating trigonometric and logarithmic expressions
                result = eval(current_text, {"sin": math.sin, "cos": math.cos, "tan": math.tan, 
                                         "sqrt": math.sqrt, "log": math.log10, "ln": math.log, 
                                         "π": math.pi, "factorial": math.factorial, "deg": math.degrees,
                                         "rad": math.radians, "e": math.e})

            self.textEdit.setPlainText(f"{current_text} = {result}")
        except Exception:
            self.textEdit.setPlainText("Invalid input")
        
    def action_open(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setText(text + " ( ")
    
    def action_close(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setText(text + " ) ")
 
    def action_clear(self):
        # clearing the label text
        self.textEdit.clear()
 
    def action_del(self):
        # clearing a single digit
        current_text = self.textEdit.toPlainText()
        self.textEdit.setPlainText(current_text[:-1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
