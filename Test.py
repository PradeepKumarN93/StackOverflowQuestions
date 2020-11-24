from PyQt5 import QtCore, QtGui, QtWidgets, uic
from sys import exit
from os.path import join, dirname, realpath


class DMTInputDownloader(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi(join(dirname(realpath(__file__)), "UI", "DMTInputDownloader.ui"), self)
        self.view.clicked.connect(self.get_data_from_db)

        # auto-completer for search
        self.dmt_title_list = self.get_dmt_titles()
        line_edit_completer = QtWidgets.QCompleter(self.dmt_title_list)
        line_edit_completer.setCaseSensitivity(0)
        line_edit_completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.search.setCompleter(line_edit_completer)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.show()

    def get_dmt_titles(self):
        return ["ABC"]

    def get_data_from_db(self):
        dmt_title = self.search.text()
        values = ["ABC", "XYZ.abc",
                  "asdfghjklasdfghjklasdfghjklasdfghjklasdfghjklasdfghjklasdfghjklasdfghjklasdfghjklasdfghjkl",
                  "zxcvbnm,zxcvbnmzxcvbnmzxcbnmzxcbnm,zxcvbnmzxcvbnmzxcvbnm", "Daily", "6:00 PM"]
        for col in range(5):
            self.set_disp_cell_value(0, col, values[col + 1])

    def set_disp_cell_value(self, row_num, col_num, value):
        self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(value)))


app = QtWidgets.QApplication([])
ui = DMTInputDownloader()
exit(app.exec())
