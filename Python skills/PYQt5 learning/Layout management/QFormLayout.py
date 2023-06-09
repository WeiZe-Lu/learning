# 文件名称:E:\python Project\py skill files\PYQt5 learning\Layout management\QFormLayout.py(中文意思为:源代码查询)
# 注释添加日期:2022-08-03 15:57:03.347656
# 编写工具:PyChame
# 编写目的:使用表格布局
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QFormLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.f_layout = QFormLayout()                           # 1
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.f_layout.addRow(self.user_label, self.user_line)   # 2
        self.f_layout.addRow(self.pwd_label, self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.all_v_layout.addLayout(self.f_layout)              # 3
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())