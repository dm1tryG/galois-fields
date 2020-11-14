import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
    QMessageBox,
    QCheckBox
)
from PyQt5.QtCore import Qt, pyqtSlot
from core import main

class InputValue(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        p_lbl = QLabel(self)
        p_lbl.move(40, 40)
        p_lbl.setText("Вычисления индексов децимации")

        p_lbl = QLabel(self)
        p_lbl.move(40, 60)
        p_lbl.setText("Введите значения:")

        p_lbl = QLabel(self)
        p_lbl.move(40, 100)
        p_lbl.setText("p")
        self.p = QLineEdit(self)
        self.p.setText('2')
        self.p.move(60, 100)

        m_lbl = QLabel(self)
        m_lbl.move(40, 140)
        m_lbl.setText("m")
        self.m = QLineEdit(self)
        self.m.setText('7')
        self.m.move(60, 140)

        n_lbl = QLabel(self)
        n_lbl.move(40, 180)
        n_lbl.setText("n")
        self.n = QLineEdit(self)
        self.n.setText('2')
        self.n.move(60, 180)

        self.r_lbl = QLabel(self)
        self.r_lbl.move(40, 240)
        self.r_lbl.setText("r")
        
        self.r = QLineEdit(self)
        self.r.setText('31')
        self.r.move(60, 240)

        self.setGeometry(100, 200, 300, 320)
        self.setWindowTitle('Вычисления индексов децимации.')

        self.cb = QCheckBox('Использовать r? ', self)
        self.cb.move(40, 215)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeTitle)

        button = QPushButton('Вычислить', self)
        button.setToolTip('Вычислить')
        button.move(40, 280)
        button.clicked.connect(self.on_click)
               
        self.show()

    @pyqtSlot()
    def on_click(self):
        try:
            args = {
                "p": int(self.p.text()),
                "m": int(self.m.text()),
                "n": int(self.n.text())
            }
            args['r'] = int(self.r.text()) if self.cb.isChecked() else None
            args['use_r'] = True if self.cb.isChecked() else False 
        except Exception as e:
            QMessageBox.question(self, 'Response', "Sorry, you have error in input values! Please try again.", QMessageBox.Ok, QMessageBox.Ok)
            return 0        
        log, result = main(args)
        print(type(result))
        print(result)
        
        try:
            r = ', '.join([str(x) for x in result])
        except Exception:
            r = "No result"
        
        QMessageBox.question(self, 'Response', f"Response:\nC = ({r})\nM = {len(result)}", QMessageBox.Ok, QMessageBox.Ok)

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('С использованием r')
            self.r.setVisible(True)
            self.r_lbl.setVisible(True)
        else:
            self.setWindowTitle('Без использования r')
            self.r.setVisible(False)
            self.r_lbl.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputValue()
    sys.exit(app.exec_())