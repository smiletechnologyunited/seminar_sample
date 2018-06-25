# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created: Wed Jun 13 19:12:32 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 269)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.replace_search = QtWidgets.QLineEdit(Form)
        self.replace_search.setObjectName("replace_search")
        self.gridLayout.addWidget(self.replace_search, 0, 1, 1, 1)
        self.replace_text = QtWidgets.QLineEdit(Form)
        self.replace_text.setObjectName("replace_text")
        self.gridLayout.addWidget(self.replace_text, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.replace_regex = QtWidgets.QCheckBox(Form)
        self.replace_regex.setObjectName("replace_regex")
        self.gridLayout.addWidget(self.replace_regex, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_help = QtWidgets.QPushButton(Form)
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_6.addWidget(self.btn_help)
        self.btn_default = QtWidgets.QPushButton(Form)
        self.btn_default.setObjectName("btn_default")
        self.horizontalLayout_6.addWidget(self.btn_default)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btn_preview = QtWidgets.QPushButton(Form)
        self.btn_preview.setObjectName("btn_preview")
        self.horizontalLayout_6.addWidget(self.btn_preview)
        self.btn_execute = QtWidgets.QPushButton(Form)
        self.btn_execute.setObjectName("btn_execute")
        self.horizontalLayout_6.addWidget(self.btn_execute)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Text :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Search :", None, -1))
        self.replace_regex.setText(QtWidgets.QApplication.translate("Form", "Use regular expression", None, -1))
        self.btn_help.setText(QtWidgets.QApplication.translate("Form", "Help", None, -1))
        self.btn_default.setText(QtWidgets.QApplication.translate("Form", "Set Default", None, -1))
        self.btn_preview.setText(QtWidgets.QApplication.translate("Form", "Preview", None, -1))
        self.btn_execute.setText(QtWidgets.QApplication.translate("Form", "Execute", None, -1))

