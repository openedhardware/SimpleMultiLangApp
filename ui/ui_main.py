# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MultiLangTestApp(object):
    def setupUi(self, MultiLangTestApp):
        if not MultiLangTestApp.objectName():
            MultiLangTestApp.setObjectName(u"MultiLangTestApp")
        MultiLangTestApp.resize(386, 163)
        self.centralwidget = QWidget(MultiLangTestApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_language = QLabel(self.centralwidget)
        self.label_language.setObjectName(u"label_language")

        self.horizontalLayout.addWidget(self.label_language)

        self.comboLanguage = QComboBox(self.centralwidget)
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.setObjectName(u"comboLanguage")

        self.horizontalLayout.addWidget(self.comboLanguage)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_content = QLabel(self.centralwidget)
        self.label_content.setObjectName(u"label_content")
        self.label_content.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_content)

        MultiLangTestApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(MultiLangTestApp)

        QMetaObject.connectSlotsByName(MultiLangTestApp)
    # setupUi

    def retranslateUi(self, MultiLangTestApp):
        MultiLangTestApp.setWindowTitle(QCoreApplication.translate("MultiLangTestApp", u"Multi Lang Test", None))
        self.label_language.setText(QCoreApplication.translate("MultiLangTestApp", u"Language:", None))
        self.comboLanguage.setItemText(0, QCoreApplication.translate("MultiLangTestApp", u"English", None))
        self.comboLanguage.setItemText(1, QCoreApplication.translate("MultiLangTestApp", u"Fran\u00e7ais", None))

        self.label_content.setText(QCoreApplication.translate("MultiLangTestApp", u"This label should be changed.", None))
    # retranslateUi

