# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created: Wed Jun 13 19:12:32 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 269)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.replace_search = QtGui.QLineEdit(Form)
        self.replace_search.setObjectName("replace_search")
        self.gridLayout.addWidget(self.replace_search, 0, 1, 1, 1)
        self.replace_text = QtGui.QLineEdit(Form)
        self.replace_text.setObjectName("replace_text")
        self.gridLayout.addWidget(self.replace_text, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.replace_regex = QtGui.QCheckBox(Form)
        self.replace_regex.setObjectName("replace_regex")
        self.gridLayout.addWidget(self.replace_regex, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 44, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_help = QtGui.QPushButton(Form)
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_6.addWidget(self.btn_help)
        self.btn_default = QtGui.QPushButton(Form)
        self.btn_default.setObjectName("btn_default")
        self.horizontalLayout_6.addWidget(self.btn_default)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btn_preview = QtGui.QPushButton(Form)
        self.btn_preview.setObjectName("btn_preview")
        self.horizontalLayout_6.addWidget(self.btn_preview)
        self.btn_execute = QtGui.QPushButton(Form)
        self.btn_execute.setObjectName("btn_execute")
        self.horizontalLayout_6.addWidget(self.btn_execute)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Text :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Search :", None, QtGui.QApplication.UnicodeUTF8))
        self.replace_regex.setText(QtGui.QApplication.translate("Form", "Use regular expression", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_help.setText(QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_default.setText(QtGui.QApplication.translate("Form", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_preview.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_execute.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))

