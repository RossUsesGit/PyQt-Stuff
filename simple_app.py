from PyQt5.QtWidgets import *
from PyQt5.QtCore import *     
import sys                    

# First activity in college involving PyQt6 (I used 5 for now since I haven't installed 6 yet. Still works.)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400,300))

        self.label = QLabel("Hello, welcome to my app!")
        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def button_clicked(self):
        self.label.setText("Button was clicked!")
        self.statusBar().showMessage("You clicked the button")




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
