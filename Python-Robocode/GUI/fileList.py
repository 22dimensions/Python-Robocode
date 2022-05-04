"""
Module implementing code editor.
"""

import os
from Ui_fileList import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from editor import codeEditor


class fileList(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.editor = codeEditor(self)
        botnames = []
        self.listBots = {}
        botFiles = os.listdir(os.getcwd() + "/.datas/robots/")
        for botFile in botFiles[:-1]:
            self.listWidget.addItem(botFile)

    def add(self, msg):
        self.textEdit.append(msg)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        file_name = self.listWidget.currentItem().text()
        file_path = os.getcwd() + "/.datas/robots/" + file_name
        self.editor.show()
        self.editor.lineEdit.setEnabled(False)
        content = ""
        with open(file_path, "r") as file:
            content = file.read()
            file.close()
        self.editor.plainTextEdit.setPlainText(content)
        self.editor.lineEdit.setText(file_name)