import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Рисование')
        uic.loadUi('git.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self, qp):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
