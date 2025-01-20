# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import rc_imagez
import rc_imagez

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(594, 296)
        icon = QIcon()
        icon.addFile(u":/iamgez/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #7CF5FF; /* Light blue background */\n"
"    border: 2px solid #00CCDD; /* Border around the window */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 10px; /* Padding around the content */\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #FFFFFF; /* White background for child widgets */\n"
"    border: none; /* No border for inner widgets */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white; /* White text */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: #4F75FF; /* Solid background color */\n"
"    border: 2px solid #00CCDD; /* Border color */\n"
"    padding: 5px; /* Padding */\n"
"    border-radius: 6px; /* Rounded corners */\n"
"    text-align: center; /* Center text */\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white; /* White text */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: #00CCDD; /* Button background */\n"
"    border"
                        ": 2px solid #4F75FF; /* Button border */\n"
"    padding: 8px; /* Padding */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4F75FF; /* Background on hover */\n"
"    border: 2px solid #6439FF; /* Border color on hover */\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(140, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.uploadBtn = QPushButton(Dialog)
        self.uploadBtn.setObjectName(u"uploadBtn")
        font1 = QFont()
        font1.setBold(True)
        self.uploadBtn.setFont(font1)
        self.uploadBtn.setStyleSheet(u"color: rgb(0, 0, 0);")
        icon1 = QIcon()
        iconThemeName = u"modem"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/iamgez/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.uploadBtn.setIcon(icon1)

        self.gridLayout.addWidget(self.uploadBtn, 0, 4, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0); /* White text color */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: ; /* Background color */\n"
"	color: rgb(0, 0, 0);\n"
"    border: 2px solid #00CCDD; /* Border color */\n"
"    padding: 3px; /* Padding inside the line edit */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #6439FF; /* Change border color on focus */\n"
"   \n"
"    selection-background-color: #00CCDD; /* Selection color */\n"
"    selection-color: rgb(0, 0, 0); /* Text color during selection */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(29, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.trainB = QPushButton(Dialog)
        self.trainB.setObjectName(u"trainB")
        self.trainB.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.trainB, 1, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setStyleSheet(u"font: 20pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(255, 216, 212);\n"
"background-color: transparent;\n"
"border: 2px solid #00CCDD; /* Border color */")

        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 5)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #00CCDD; /* Border around the progress bar */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"    text-align: center; /* Center text in the progress bar */\n"
"    color: white; /* Text color */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: #4F75FF; /* Background color when the bar is empty */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #7CF5FF; /* Color of the progress bar chunk */\n"
"    border-radius: 8px; /* Rounded corners on the progress chunk */\n"
"    width: 20px; /* Width of each chunk */\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 5)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Train Window", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Documents:", None))
        self.uploadBtn.setText("")
        self.trainB.setText(QCoreApplication.translate("Dialog", u"Start training", None))
    # retranslateUi

