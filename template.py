from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
# from loginUI import Ui_Form
from PyQt5 import uic

# from main import Ui_Form

Ui_Form, baseclass = uic.loadUiType('loginUI.ui',resource_suffix='.qrc')

class MainWindow(baseclass, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.ui = Ui_Form()
        # self.ui = uic.loadUi('loginUI.ui',self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.authenticate)
        self.lineEdit.textChanged.connect(self.set_button_text)
        self.show()
    
    def set_button_text(self,text):
        if text:
            self.pushButton.setText(f"{text} Log In")
        else:
            self.pushButton.setText("Log In")

    def authenticate(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "user" and password == "pass":
            qtw.QMessageBox.information(self,'Success!', "You are logged in.")
        else:
            qtw.QMessageBox.critical(self, 'Login failed!', "Please try again.")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    w = MainWindow()
    sys.exit(app.exec_())