# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QToolButton, QVBoxLayout, QWidget)
import rc_imagez
import rc_imagez

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(841, 470)
        icon = QIcon()
        icon.addFile(u":/iamgez/train.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name = QWidget(Widget)
        self.icon_name.setObjectName(u"icon_name")
        self.icon_name.setStyleSheet(u"QWidget{\n"
"background-color:#00CCDD;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height: 30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(245, 250, 254);	\n"
"	color: rgb(31, 149, 239);\n"
"	font-weight:bold;\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 50, -1)
        self.pushButton_3 = QPushButton(self.icon_name)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        icon1 = QIcon()
        iconThemeName = u"applications-office"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/iamgez/profile2_0_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(40, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.label_3 = QLabel(self.icon_name)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 15, 0, -1)
        self.homeBtn = QPushButton(self.icon_name)
        self.homeBtn.setObjectName(u"homeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/iamgez/dashboard_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/iamgez/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.homeBtn.setIcon(icon2)
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.chatBtn = QPushButton(self.icon_name)
        self.chatBtn.setObjectName(u"chatBtn")
        icon3 = QIcon()
        icon3.addFile(u":/iamgez/image.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/iamgez/chatbot.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.chatBtn.setIcon(icon3)
        self.chatBtn.setIconSize(QSize(30, 40))
        self.chatBtn.setCheckable(True)
        self.chatBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.chatBtn)

        self.emailBtn = QPushButton(self.icon_name)
        self.emailBtn.setObjectName(u"emailBtn")
        icon4 = QIcon()
        icon4.addFile(u":/iamgez/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/iamgez/email (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.emailBtn.setIcon(icon4)
        self.emailBtn.setIconSize(QSize(30, 25))
        self.emailBtn.setCheckable(True)
        self.emailBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.emailBtn)

        self.pushButton_9 = QPushButton(self.icon_name)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon5 = QIcon()
        icon5.addFile(u":/iamgez/settings_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/iamgez/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.verticalSpacer_5 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.pushButton_10 = QPushButton(self.icon_name)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon6 = QIcon()
        icon6.addFile(u":/iamgez/log_out_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_10)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_name, 0, 1, 1, 1)

        self.main_menu = QWidget(Widget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout = QVBoxLayout(self.main_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/iamgez/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon7)
        self.menuBtn.setIconSize(QSize(20, 25))
        self.menuBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.menuBtn)

        self.horizontalSpacer = QSpacerItem(173, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0); /* White text color */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: ; /* Background color */\n"
"	color: rgb(255, 255, 255);\n"
"    border: 2px solid #00CCDD; /* Border color */\n"
"    padding: 3px; /* Padding inside the line edit */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #6439FF; /* Change border color on focus */\n"
"    background-color: #7CF5FF; /* Lighter background color on focus */\n"
"    selection-background-color: #00CCDD; /* Selection color */\n"
"    selection-color: white; /* Text color during selection */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/iamgez/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(173, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"border:none")
        icon9 = QIcon()
        icon9.addFile(u":/iamgez/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_6 = QGridLayout(self.home)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white; /* White text color */\n"
"    font-size: 24px; /* Increased font size for a welcoming feel */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: #4F75FF; /* Solid background color */\n"
"    border: 2px solid #00CCDD; /* Border color */\n"
"    padding: 15px; /* Increased padding for a larger look */\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"    qproperty-alignment: 'AlignCenter'; /* Vertically align the text */\n"
"    letter-spacing: 1px; /* Slightly spaced out letters */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: #6c757d; /* Grey text when disabled */\n"
"    background-color: #f0f2f5; /* Light grey background when disabled */\n"
"    border: 1px solid #6c757d; /* Grey border when disabled */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.home)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/iamgez/chatbot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(200, 160))
        self.pushButton_4.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/iamgez/email (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(200, 160))
        self.pushButton_5.setFlat(True)

        self.gridLayout_6.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.chatbot = QWidget()
        self.chatbot.setObjectName(u"chatbot")
        self.gridLayout_4 = QGridLayout(self.chatbot)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 8, 4, 1, 1)

        self.microBtn = QToolButton(self.chatbot)
        self.microBtn.setObjectName(u"microBtn")
        self.microBtn.setStyleSheet(u"QToolButton#microBtn {\n"
"    color: white; /* White text color */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #00CCDD, \n"
"        stop:0.4 #7CF5FF, \n"
"        stop:1 #6439FF\n"
"    ); /* Conical gradient background */\n"
"    border: 2px dashed #6439FF;\n"
"    padding: 6px; /* Padding for space */\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"    display: inline-block; /* Inline-block for proper alignment */\n"
"}\n"
"\n"
"QToolButton#microBtn:hover {\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #6439FF, \n"
"        stop:0.4 #4F75FF, \n"
"        stop:1 #00CCDD\n"
"    ); /* Reversed conical gradient on hover */\n"
"    border: 2px solid #4F75FF; /* Hover border color */\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/iamgez/micro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.microBtn.setIcon(icon12)
        self.microBtn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.microBtn, 2, 5, 1, 1)

        self.trainBtn = QPushButton(self.chatbot)
        self.trainBtn.setObjectName(u"trainBtn")
        self.trainBtn.setStyleSheet(u"QPushButton#trainBtn {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #7CF5FF, \n"
"        stop:0.33 #00CCDD, \n"
"        stop:0.66 #4F75FF, \n"
"        stop:1 #6439FF\n"
"    );\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"    font-size: 18px;\n"
"    border: 3px solid #4F75FF;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#trainBtn:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #6439FF, \n"
"        stop:0.33 #4F75FF, \n"
"        stop:0.66 #00CCDD, \n"
"        stop:1 #7CF5FF\n"
"    );\n"
"    color: white;\n"
"    border: 3px solid #6439FF;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/images/train.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trainBtn.setIcon(icon13)
        self.trainBtn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.trainBtn, 8, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.chatbot)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font: 700 12pt \"Rockwell\";")

        self.gridLayout_2.addWidget(self.plainTextEdit, 6, 0, 1, 6)

        self.label_5 = QLabel(self.chatbot)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* White text color */\n"
"    font-size: 20px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #7CF5FF, \n"
"        stop:0.5 #00CCDD, \n"
"        stop:1 #4F75FF\n"
"    ); /* Gradient background */\n"
"    border: 2px solid #6439FF; /* Purple border */\n"
"    padding: 3px; /* Padding */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"    vertical-align: middle; /* Center text vertically */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: #6c757d; /* Grey text when disabled */\n"
"    background-color: #f0f2f5; /* Light grey background when disabled */\n"
"    border: 1px solid #6c757d; /* Grey border when disabled */\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 6)

        self.lineEdit = QLineEdit(self.chatbot)
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

        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 5)

        self.pushButton = QPushButton(self.chatbot)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton, QPushButton#trainBtn {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #7CF5FF, \n"
"        stop:0.33 #00CCDD, \n"
"        stop:0.66 #4F75FF, \n"
"        stop:1 #6439FF\n"
"    );\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 2px;\n"
"    font-size: 16px;\n"
"    border: 2px solid #4F75FF;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover, QPushButton#trainBtn:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 #6439FF, \n"
"        stop:0.33 #4F75FF, \n"
"        stop:0.66 #00CCDD, \n"
"        stop:1 #7CF5FF\n"
"    );\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton, 3, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.chatbot)
        self.email = QWidget()
        self.email.setObjectName(u"email")
        self.gridLayout_5 = QGridLayout(self.email)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mailgenBtn = QPushButton(self.email)
        self.mailgenBtn.setObjectName(u"mailgenBtn")
        self.mailgenBtn.setStyleSheet(u"QPushButton#mailgenBtn {\n"
"    color: white; /* White text color */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #00CCDD, \n"
"        stop:0.4 #7CF5FF, \n"
"        stop:1 #6439FF\n"
"    ); /* Conical gradient background */\n"
"    border: 2px dashed #6439FF; /* Dashed border */\n"
"    padding: 1px; /* Padding for space */\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"}\n"
"\n"
"QPushButton#mailgenBtn:hover {\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #6439FF, \n"
"        stop:0.4 #4F75FF, \n"
"        stop:1 #00CCDD\n"
"    ); /* Reversed conical gradient on hover */\n"
"    border: 2px dashed #4F75FF; /* Hover border color */\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/iamgez/1000_F_195075949_QsG9tAFj2UlZTqBLfoppKu4WBZ7atSh9-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mailgenBtn.setIcon(icon14)
        self.mailgenBtn.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.mailgenBtn, 3, 0, 1, 1)

        self.plainTextEdit2 = QPlainTextEdit(self.email)
        self.plainTextEdit2.setObjectName(u"plainTextEdit2")
        self.plainTextEdit2.setStyleSheet(u"font: 600 11pt \"Segoe UI Semibold\";\n"
" border: 2px solid #6439FF; /* Dashed border for a different style */\n"
"selection-background-color: #00CCDD; /* Selection color */")

        self.gridLayout_3.addWidget(self.plainTextEdit2, 6, 0, 1, 6)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 3, 4, 1, 1)

        self.mdpE = QLineEdit(self.email)
        self.mdpE.setObjectName(u"mdpE")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdpE.sizePolicy().hasHeightForWidth())
        self.mdpE.setSizePolicy(sizePolicy1)
        self.mdpE.setStyleSheet(u"QLineEdit {\n"
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
        self.mdpE.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.mdpE, 2, 1, 1, 5)

        self.line = QFrame(self.email)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 5, 1, 1, 3)

        self.toolButton = QToolButton(self.email)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton#toolButton {\n"
"    color: white; /* White text color */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #00CCDD, \n"
"        stop:0.4 #7CF5FF, \n"
"        stop:1 #6439FF\n"
"    ); /* Conical gradient background */\n"
"    border: 2px dashed #6439FF;\n"
"    padding: 3px; /* Padding for space */\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"    display: inline-block; /* Inline-block for proper alignment */\n"
"}\n"
"\n"
"QToolButton#toolButton:hover {\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #6439FF, \n"
"        stop:0.4 #4F75FF, \n"
"        stop:1 #00CCDD\n"
"    ); /* Reversed conical gradient on hover */\n"
"    border: 2px solid #4F75FF; /* Hover border color */\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/iamgez/unnamed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon15)

        self.gridLayout_3.addWidget(self.toolButton, 3, 5, 1, 1)

        self.label_2 = QLabel(self.email)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.mailE = QLineEdit(self.email)
        self.mailE.setObjectName(u"mailE")
        self.mailE.setStyleSheet(u"QLineEdit {\n"
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
        self.mailE.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.mailE, 1, 1, 1, 5)

        self.checkBtn = QPushButton(self.email)
        self.checkBtn.setObjectName(u"checkBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBtn.sizePolicy().hasHeightForWidth())
        self.checkBtn.setSizePolicy(sizePolicy2)
        self.checkBtn.setStyleSheet(u"QPushButton#checkBtn {\n"
"    color: white; /* White text color */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #00CCDD, \n"
"        stop:0.4 #7CF5FF, \n"
"        stop:1 #6439FF\n"
"    ); /* Conical gradient background */\n"
"    border: 2px solid #6439FF; /* Solid border */\n"
"    padding: 3px; /* Padding for space */\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"    display: inline-block; /* Inline-block for proper alignment */\n"
"}\n"
"\n"
"QPushButton#checkBtn:hover {\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #6439FF, \n"
"        stop:0.4 #4F75FF, \n"
"        stop:1 #00CCDD\n"
"    ); /* Reversed conical gradient on hover */\n"
"    border: 2px solid #4F75FF; /* Hover border color */\n"
"}\n"
"")
        self.checkBtn.setCheckable(False)

        self.gridLayout_3.addWidget(self.checkBtn, 3, 2, 1, 2)

        self.label_6 = QLabel(self.email)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: white; /* White text color */\n"
"    font-size: 18px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    background-color: qconicalgradient(\n"
"        cx:0.5, cy:0.5, angle:0, \n"
"        stop:0 #00CCDD, \n"
"        stop:0.4 #7CF5FF, \n"
"        stop:1 #6439FF\n"
"    ); /* Conical gradient background for uniqueness */\n"
"    border: 2px solid #6439FF; /* Dashed border for a different style */\n"
"    padding: 5px; /* Increased padding for more space */\n"
"    border-radius: 15px; /* Larger, rounded corners */\n"
"    text-align: center; /* Center text horizontally */\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: #6c757d; /* Grey text when disabled */\n"
"    background-color: #f0f2f5; /* Light grey background when disabled */\n"
"    border: 1px solid #6c757d; /* Grey border when disabled */\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 6)

        self.label_7 = QLabel(self.email)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 3, 1, 1, 1)

        self.emailTable = QTableView(self.email)
        self.emailTable.setObjectName(u"emailTable")
        self.emailTable.setStyleSheet(u"font: 700 11pt \"Tahoma\";\n"
" border: 2px solid #6439FF; /* Dashed border for a different style */\n"
"selection-background-color: #00CCDD; /* Selection color */")

        self.gridLayout_3.addWidget(self.emailTable, 4, 0, 1, 6)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.email)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_name_2 = QWidget(Widget)
        self.icon_name_2.setObjectName(u"icon_name_2")
        self.icon_name_2.setStyleSheet(u"QWidget{\n"
"background-color: #00CCDD;\n"
"}\n"
"QPushButton{\n"
"		color:white;\n"
"	height: 30px;\n"
"	border:none;\n"
"border-radius:10px\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(245, 250, 254);	\n"
"	color: rgb(31, 149, 239);\n"
"	font-weight:bold;\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.icon_name_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.pushButton_2 = QPushButton(self.icon_name_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"text-align:right;")
        icon16 = QIcon()
        icon16.addFile(u":/iamgez/profile2_0_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QSize(40, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.homeBtn1 = QPushButton(self.icon_name_2)
        self.homeBtn1.setObjectName(u"homeBtn1")
        self.homeBtn1.setIcon(icon2)
        self.homeBtn1.setCheckable(True)
        self.homeBtn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeBtn1)

        self.chatBtn1 = QPushButton(self.icon_name_2)
        self.chatBtn1.setObjectName(u"chatBtn1")
        self.chatBtn1.setIcon(icon3)
        self.chatBtn1.setIconSize(QSize(30, 30))
        self.chatBtn1.setCheckable(True)
        self.chatBtn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.chatBtn1)

        self.emailBtn1 = QPushButton(self.icon_name_2)
        self.emailBtn1.setObjectName(u"emailBtn1")
        self.emailBtn1.setIcon(icon4)
        self.emailBtn1.setIconSize(QSize(30, 25))
        self.emailBtn1.setCheckable(True)
        self.emailBtn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.emailBtn1)

        self.pushButton_17 = QPushButton(self.icon_name_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.verticalSpacer_6 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.pushButton_18 = QPushButton(self.icon_name_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon17 = QIcon()
        icon17.addFile(u":/iamgez/log_out_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/iamgez/log_out.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_18.setIcon(icon17)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_18)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.icon_name_2, 0, 0, 1, 1)


        self.retranslateUi(Widget)
        self.menuBtn.toggled.connect(self.icon_name_2.setHidden)
        self.menuBtn.toggled.connect(self.icon_name.setVisible)
        self.pushButton_17.toggled.connect(self.pushButton_9.setChecked)
        self.emailBtn1.toggled.connect(self.emailBtn.setChecked)
        self.chatBtn1.toggled.connect(self.chatBtn.setChecked)
        self.homeBtn1.toggled.connect(self.homeBtn.setChecked)
        self.homeBtn.toggled.connect(self.homeBtn1.setChecked)
        self.chatBtn.toggled.connect(self.chatBtn1.setChecked)
        self.emailBtn.toggled.connect(self.emailBtn1.setChecked)
        self.pushButton_9.toggled.connect(self.pushButton_17.setChecked)
        self.pushButton_18.toggled.connect(Widget.close)
        self.pushButton_10.toggled.connect(Widget.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Smart App", None))
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"Yassin Sadfi", None))
        self.homeBtn.setText(QCoreApplication.translate("Widget", u"Home", None))
        self.chatBtn.setText(QCoreApplication.translate("Widget", u"ChatBot", None))
        self.emailBtn.setText(QCoreApplication.translate("Widget", u"Email checking", None))
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"Settings", None))
        self.pushButton_10.setText(QCoreApplication.translate("Widget", u"Log out", None))
        self.menuBtn.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Segoe UI','Tahoma','sans-serif'; font-size:36pt; color:#ffffff; background-color:#4f75ff;\">Welcome to Our </span></p><p align=\"center\"><span style=\" font-family:'Segoe UI','Tahoma','sans-serif'; font-size:26pt; text-decoration: underline; color:#00ccdd;\">Humanoid Robot Demo App</span></p><p><span style=\" font-family:'Segoe UI','Tahoma','sans-serif'; font-size:9pt; font-weight:400; color:#ffcfc6;\">By Yassin Sadfi &amp; Wassim Belhouwene</span></p></body></html>", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.microBtn.setText("")
        self.trainBtn.setText(QCoreApplication.translate("Widget", u"Train your model", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Generate response..", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"                                Chat bot", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"How can I help you ?", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.mailgenBtn.setText("")
        self.plainTextEdit2.setPlaceholderText(QCoreApplication.translate("Widget", u"Your email generated", None))
        self.mdpE.setInputMask("")
        self.mdpE.setText("")
        self.mdpE.setPlaceholderText(QCoreApplication.translate("Widget", u"password", None))
        self.toolButton.setText(QCoreApplication.translate("Widget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Email adress :", None))
        self.mailE.setInputMask("")
        self.mailE.setPlaceholderText(QCoreApplication.translate("Widget", u"mail", None))
        self.checkBtn.setText(QCoreApplication.translate("Widget", u"Check", None))
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Widget", u"                             Email Checker", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Password :", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_2.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_2.setText("")
        self.homeBtn1.setText("")
        self.chatBtn1.setText("")
        self.emailBtn1.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
    # retranslateUi

