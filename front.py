import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton
)


class InputValue(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        p_lbl = QLabel(self)
        p_lbl.move(40, 60)
        p_lbl.setText("Input values")

        p_lbl = QLabel(self)
        p_lbl.move(40, 100)
        p_lbl.setText("p")
        p = QLineEdit(self)
        p.move(60, 100)

        m_lbl = QLabel(self)
        m_lbl.move(40, 140)
        m_lbl.setText("m")
        m = QLineEdit(self)
        m.move(60, 140)

        n_lbl = QLabel(self)
        n_lbl.move(40, 180)
        n_lbl.setText("n")
        n = QLineEdit(self)
        n.move(60, 180)

        r_lbl = QLabel(self)
        r_lbl.move(40, 220)
        r_lbl.setText("r")
        r = QLineEdit(self)
        r.move(60, 220)

        self.setGeometry(100, 200, 800, 600)
        self.setWindowTitle('ITMO (Dmitry Galkin)')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputValue()
    sys.exit(app.exec_())