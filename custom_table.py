import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
    QMessageBox,
    QCheckBox,
    QComboBox,
    QTableWidget,
    QTableWidgetItem
)
from PyQt5.QtGui import QKeySequence


class TableWidgetCustom(QTableWidget):
    def __init__(self, parent=None):
        super(TableWidgetCustom, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Copy):
            self.copy()
        else:
            QTableWidget.keyPressEvent(self, event)

    def copy(self):
        selection = self.selectionModel()
        indexes = selection.selectedIndexes()
        if len(indexes) < 1:
            return

        row = indexes[0].row()
        col = indexes[0].column()
        buffer = []
        line = []
        for idx in indexes:
            item = self.item(idx.row(), idx.column())
            if idx.row() != row:
                buffer += ['\t'.join(line)]
                row = idx.row()
                line = []
            line += [item.text()]            
            
            if idx == indexes[-1]:
                buffer += ['\t'.join(line)]

        QApplication.clipboard().setText("\n".join(buffer))

    def unselect(self):
        selection = self.selectionModel()
        indexes = selection.selectedIndexes()
        if len(indexes) < 1:
            return

        for i in indexes:
            self.item(i.row(), i.column()).setSelected(False)
