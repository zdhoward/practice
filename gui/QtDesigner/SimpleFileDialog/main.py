from PyQt5 import QtCore, QtGui, QtWidgets, uic
from os import listdir
from os.path import exists, isdir, dirname


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("mainwindow.ui", self)

    def browse(self):
        print("Browsing")
        dir = self.lineEdit.text()
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QtWidgets.QFileDialog.getOpenFileName()",
            dir,
            "All Files (*);;Python Files (*.py)",
            options=options,
        )
        if fileName:
            print(fileName)
            self.lineEdit.setText(fileName)

    def listDir(self):
        print("Listing Dir")
        dir = self.lineEdit.text()
        if exists(dir):
            if not isdir(dir):
                dir = dirname(dir)
            contents = listdir(dir)
            for item in contents:
                if isdir(item):
                    self.textBrowser.setSource(item)

    def processMenu(self, action):
        print("Processing Menu")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
