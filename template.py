from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import serial.tools.list_ports as sp
from PyQt5 import uic

LoginUi_Form, baseclass1 = uic.loadUiType('loginUI.ui',resource_suffix='.qrc')
HomeUi_Form, baseclass2 = uic.loadUiType('home-page.ui',resource_suffix='.qrc')

class Canvas1(FigureCanvas):
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(5,5), dpi=60) #dpi is according to resolutions for monitor and figsize is fugure size 
        super().__init__(fig)
        self.setParent(parent)
        self.ax.plot([1,2,3,4,5],[10,11,12,13,14])
        self.ax.grid()

class Canvas2(FigureCanvas):
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(5,5), dpi=60) #dpi is according to resolutions for monitor and figsize is fugure size 
        super().__init__(fig)
        self.setParent(parent)
        self.ax.plot([1,2,3,4,5],[10,11,12,13,14])
        self.ax.grid()

class Canvas3(FigureCanvas):
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(5,5), dpi=60) #dpi is according to resolutions for monitor and figsize is fugure size 
        super().__init__(fig)
        self.setParent(parent)
        self.ax.plot([1,2,3,4,5],[10,11,12,13,14])
        self.ax.grid()

class Canvas4(FigureCanvas):
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(5,5), dpi=60) #dpi is according to resolutions for monitor and figsize is fugure size 
        super().__init__(fig)
        self.setParent(parent)
        self.ax.plot([1,2,3,4,5],[10,11,12,13,14])
        self.ax.grid()

class HomeWindow(baseclass2, HomeUi_Form):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.chart1 = Canvas1(self)
        self.chart1.move(80,20)
        self.chart2 = Canvas2(self)
        self.chart2.move(80,340)
        self.chart3 = Canvas3(self)
        self.chart3.move(400,20)
        self.chart4 = Canvas4(self)
        self.chart4.move(400,340)
        self.show()

class MainWindow(baseclass1, LoginUi_Form):

    authenticated = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.ui = Ui_Form()
        # self.ui = uic.loadUi('loginUI.ui',self)
        
        self.setupUi(self)
        
        number_of_ports = []
        ports = sp.comports()
        for port in ports:
            try:
                number_of_ports.append(port.device)
            except:
                print("No port")
                
        self.Port.addItems(number_of_ports)
        self.Port.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.authenticate)
        self.lineEdit.textChanged.connect(self.set_button_text)
        self.authenticated.connect(self.logged_in)
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
            if self.Port.currentText() == '':
                qtw.QMessageBox.critical(self,'Login Failed!', f"Connect with some port.")    
            else:
                qtw.QMessageBox.information(self,'Success!', f"You are logged in.\nYou are connected with {self.Port.currentText()} port.")
                self.authenticated.emit()
        else:
            qtw.QMessageBox.critical(self, 'Login failed!', "Check username and password.")

    def logged_in(self):
        self.home = HomeWindow()
        self.close()
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    w = MainWindow()
    sys.exit(app.exec_())