# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
import fonctions
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QStandardItemModel
from ui_trainwindow import Ui_Dialog


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create an instance of the Fonctions class and pass the Widget instance to it
        self.funcs = fonctions.Fonctions(self)
        # Create a model for the QTableView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Date", "Sender", "Subject", "Text"])
        self.ui.emailTable.setModel(self.model)

        #stacked widgets buttons
        self.ui.homeBtn.clicked.connect(self.switch_to_home)
        self.ui.homeBtn1.clicked.connect(self.switch_to_home)
        self.ui.chatBtn.clicked.connect(self.switch_to_chatbot)
        self.ui.chatBtn1.clicked.connect(self.switch_to_chatbot)
        self.ui.emailBtn.clicked.connect(self.switch_to_email)
        self.ui.emailBtn1.clicked.connect(self.switch_to_email)

        # Connect the buttons click event to the slot
        self.ui.pushButton.clicked.connect(self.funcs.response_text)
        self.ui.checkBtn.clicked.connect(self.funcs.checkemail)
        self.ui.microBtn.clicked.connect(self.funcs.start_microphone)
        self.ui.toolButton.clicked.connect(self.funcs.SpeakText)
        self.ui.mailgenBtn.clicked.connect(self.funcs.response_email)
        self.ui.trainBtn.clicked.connect(self.open_train_window)
        # Connect the signal to update the line edit
        self.funcs.update_line_edit.connect(self.ui.lineEdit.setText)
        self.funcs.timer.timeout.connect(self.funcs.update_label_text)

    def switch_to_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_chatbot(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_email(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    #Function to open trainwindow
    def open_train_window(self):
       self.window2 = QDialog()
       self.ui_train = Ui_Dialog()
       self.ui_train.setupUi(self.window2)
       # Pass the train window UI to Fonctions
       self.funcs.set_train_ui(self.ui_train,self.window2)
       self.window2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
