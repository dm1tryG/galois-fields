import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QApplication,
    QPushBu
)


class InputValue(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)
        qle.textChanged[str].connect(self.onChanged)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('SEQUENCE')
        self.show()


    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputValue()
    sys.exit(app.exec_())