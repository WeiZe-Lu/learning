# 文件名称:E:\python Project\py skill files\PYQt5 learning\Layout management\QGridLayout.py(中文意思为:源代码查询)
# 注释添加日期:2022-08-03 15:57:38.108398
# 编写工具:PyChame
# 编写目的:使用网格布局
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()                                # 1
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)         # 2
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)                       # 3
        self.v_layout.addLayout(self.h_layout)                          # 4

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())