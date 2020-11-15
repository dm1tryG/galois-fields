import sys
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
from PyQt5.QtCore import Qt, pyqtSlot
from core import without_r, compute_indexes

from custom_table import TableWidgetCustom

class InputValue(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lvl = 100
        
        p_lbl = QLabel(self)
        p_lbl.move(40, 40)
        p_lbl.setText("Вычисление индексов децимации")

        p_lbl = QLabel(self)
        p_lbl.move(40, 60)
        p_lbl.setText("Введите значения:")

        p_lbl = QLabel(self)
        p_lbl.move(40, lvl)
        p_lbl.setText("p")

        # Combo for p
        self.p = QComboBox(self)
        self.p.addItems(['2', '3', '5', '7', '11', '13'])
        self.p.currentIndexChanged.connect(self.select_p)
        self.p.move(54, lvl - 4)

        m_lbl = QLabel(self)
        m_lbl.move(130, lvl)
        m_lbl.setText("m")
        self.m = QLineEdit(self)
        self.m.setText('7')
        self.m.move(150, lvl)

        n_lbl = QLabel(self)
        n_lbl.move(130, lvl + 25)
        n_lbl.setText("n")
        self.n = QLineEdit(self)
        self.n.setText('2')
        self.n.move(150, lvl + 25)


        self.setGeometry(100, 200, 440, 600)
        self.setWindowTitle('Вычисление индексов децимации.')


        button = QPushButton('Вычислить', self)
        button.setToolTip('Вычислить')
        button.move(300, lvl - 4)
        button.clicked.connect(self.on_click)

        try:
            p = int(self.p.currentText())
            m = int(self.m.text())
            n = int(self.n.text())
        except Exception as e:
            QMessageBox.question(self, 'Ошибка', "Введены неверные значения!\nПроверьте, пожалуйста!", QMessageBox.Ok, QMessageBox.Ok)
            return 0
        self.computed_m = without_r(p, m, n)

        self.tableWidget = TableWidgetCustom(self)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.tableWidget.move(40, 200)
        self.tableWidget.resize(100, 300)
        self.tableWidget.setColumnWidth(0, 80);
        self.create_vector_r(self.computed_m)

        self.indexes, self.p_indexes = compute_indexes(p, m, n, self.computed_m[0])
        self.tableOfIndexes = TableWidgetCustom(self)
        self.tableOfIndexes.setColumnCount(2)
        self.tableOfIndexes.move(200, 200)
        self.tableOfIndexes.resize(200, 300)
        self.tableOfIndexes.setColumnWidth(0, 80)
        self.create_table_of_indexes()
        self.show()

    def create_table_of_indexes(self):
        self.tableOfIndexes.setRowCount(len(self.indexes))
        self.tableOfIndexes.setHorizontalHeaderLabels(['C10', 'p-ичная'])
        for i in range(len(self.indexes)):
            self.tableOfIndexes.setItem(i, 0, QTableWidgetItem(str(self.indexes[i])))

        for i in range(len(self.p_indexes)):
            self.tableOfIndexes.setItem(i, 1, QTableWidgetItem(str(self.p_indexes[i])))


    def create_vector_r(self, r):
        # Create table
        self.tableWidget.setRowCount(len(r))
        self.tableWidget.setHorizontalHeaderLabels(['r'])
        for i in range(len(r)):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(r[i])))

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        try:
            p = int(self.p.currentText())
            m = int(self.m.text())
            n = int(self.n.text())
            
            if p**(m*n) - 1 > 10000000:
                raise Exception
        except Exception as e:
            QMessageBox.question(self, 'Ошибка', "Введены неверные значения!\nПроверьте, пожалуйста!", QMessageBox.Ok, QMessageBox.Ok)
            return 0
        
        self.tableOfIndexes.unselect()
        self.tableWidget.unselect()
        self.tableWidget.item(0, 0).setSelected(True)
        
        # msg = f"""
        # N = {p}^{S} - 1 = {p**S - 1}
        # R10 = {r}
        # R{p} = {[convert_base(i, p) for i in r]}
        #     """      
        self.computed_m = without_r(p, m, n)
        print(self.computed_m)
        self.create_vector_r(self.computed_m)
        self.cell_was_clicked(0, 0)
        self.tableWidget.item(0, 0).setSelected(True)

        

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('С использованием r')
            self.r.setVisible(True)
            self.r_lbl.setVisible(True)
        else:
            self.setWindowTitle('Без использования r')
            self.r.setVisible(False)
            self.r_lbl.setVisible(False)

    def select_p(self, i):
        for count in range(self.p.count()):
            print(self.p.itemText(count))
    

    def cell_was_clicked(self, r, c):
        try:
            p = int(self.p.currentText())
            m = int(self.m.text())
            n = int(self.n.text())

            if p**(m*n) - 1 > 10000000:
                raise Exception

        except Exception as e:
            QMessageBox.question(self, 'Ошибка', "Введены неверные значения!\nПроверьте, пожалуйста!", QMessageBox.Ok, QMessageBox.Ok)
            return 0
        r = self.computed_m[r]

        print(p, m, n, r)
        self.indexes, self.p_indexes = compute_indexes(p, m, n, r)
        print(self.indexes, self.p_indexes)
        self.create_table_of_indexes()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputValue()
    sys.exit(app.exec_())