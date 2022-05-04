"""
Module implementing code editor.
"""

import os
from Ui_editor import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot


class codeEditor(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

    def add(self, msg):
        self.textEdit.append(msg)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        save code
        """
        if not os.path.exists(os.getcwd() + "/.datas/robots/"):
            os.makedirs(os.getcwd() + "/.datas/robots/")
        file_name = os.getcwd() + "./.datas/robots/" + self.lineEdit.text()
        print(file_name)
        if self.lineEdit.text() == "":
            return
        print(file_name)
        with open(file_name, 'w') as file:
            print(file)
            file.write(self.plainTextEdit.toPlainText())
        file.close()
