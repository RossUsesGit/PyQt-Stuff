from PyQt5.QtWidgets import *
import sys


# A PyQt5 program that hides and reveals a mock profile via a toggle button

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set the window to an unchangeable size
        self.setWindowTitle("Profile Card")
        self.setFixedSize(450,250)

        # Button to show or hide the profile information
        self.showprofile = QPushButton("Show My Profile")
        self.showprofile.setFixedSize(100,50)
        self.showprofile.clicked.connect(self.revealthyself) # connected function so one can reveal thyself

        # False (Hidden) state properties
        self.myname = QLabel("[REDACTED]") # Text for hiding the profile, SCP ahh
        self.myname.setStyleSheet("font-weight: bold;")
      
        self.displaystate = False # Used to create a state where profile is hidden

        # Extra pizzazz
        self.profilestatus = QLabel("Profile Top Secret")
        self.profilestatus.setStyleSheet("font-style: italic")
        
        # Layout and container for organization
        self.container = QWidget()
        self.layout = QHBoxLayout()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Add the elements we made to the layout
        self.layout.addWidget(self.showprofile)
        self.layout.addWidget(self.myname)  
        self.layout.addWidget(self.profilestatus)

    def revealthyself(self): # Aristotle ahh

        # Toggles display in between states
        if self.displaystate == False:

            self.myname.setText("[PROFILE LOADED]\n"
            "Welcome, Ross Andrew Bulaong\n" 
            "Age: 18\n" 
            "Status: Alive and despising Differential Equations\n" 
            "Marital Status: Married\n" 
            "Sex: Sure ")
            self.myname.setStyleSheet("")

            self.profilestatus.setText("")

            self.showprofile.setText("Hide")

            self.displaystate = True # Updates the display state as "showing"

        else:

            self.myname.setText("[REDACTED]")
            self.myname.setStyleSheet("font-weight: bold;")

            self.profilestatus.setText("Profile Top Secret")

            self.showprofile.setText("Show My Profile")

            self.displaystate = False # Updaets the display state as "hidden"

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())   
