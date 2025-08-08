import sys
from PyQt5.QtWidgets import *         # GUI widgets
from PyQt5.QtGui import QFont         # Fonts
from PyQt5.QtMultimedia import QSound # For playing sound
from PyQt5.QtCore import Qt, QTimer   # For alignment and timers

# I used ChatGPT to document this code. Tinatamad na rin kasi ako isa isahin ano ginagawa. -- REW [18/04/25] --

# Lmao this is code I made months ago -- REW [08/08/2025] --

# Define the main widget class for the Fart Button app
class FartButton(QWidget):
    def __init__(self):
        super().__init__()  # Call QWidget constructor

        # Window setup
        self.setWindowTitle("ShitClick")     # Set title bar text
        self.setFixedSize(300, 300)            # Prevent resizing
        self.setStyleSheet("background: #FFF4E8")  # Set background color

        self.fartcounter = 0  # Initialize counter for fart button presses

        self.initUI()  # Call method to build the UI

    def initUI(self):

        # Main vertical layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center widgets vertically
        self.setLayout(layout)               # Set layout on main window

        # Title Label 
        self.label = QLabel("Fart Button")   # Create label for title
        self.label.setFont(QFont("Comic Sans MS", 16))  # Set font and size
        self.label.setStyleSheet("color: #65350F")       # Font color
        self.label.setAlignment(Qt.AlignCenter)          # Center text horizontally

        # Counter Label 
        self.fartcount = QLabel(f"Farts: {self.fartcounter}")  # Shows fart count
        self.fartcount.setFont(QFont("Comic Sans MS", 10))
        self.fartcount.setStyleSheet("color: #65350F")
        self.fartcount.setAlignment(Qt.AlignCenter)

        # Fart Button 
        self.button = QPushButton("Press me!")        # Create the button
        self.button.setFont(QFont("Comic Sans MS", 15))
        self.button.setFixedSize(150, 100)            # Fixed dimensions (150x100)

        # Style the button with colors and round edges
        self.button.setStyleSheet("""
        QPushButton {
            background-color: #65350F;   
            color: #F4A460;              
            border-radius: 50px;        
            padding: 3px;
        }
        QPushButton:hover {
            background-color: #9A7B4F;   
            color: #65350F;
            }
        """)

        # Connect button to two separate functions/methods
        self.button.clicked.connect(self.fart)          # Plays sound and disables temporarily to avoid any spams
        self.button.clicked.connect(self.incrementfart) # Updates fart counter to display click amounts

        # Add widgets to layout 
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.fartcount)

    def fart(self):
    
        self.button.setEnabled(False)  # Prevent spamming
        QSound.play("soundeffects/fart.wav")  # Play the fart sound
        QTimer.singleShot(1000, lambda: self.button.setEnabled(True))  # Re-enable after 1 second

    def incrementfart(self):

        self.fartcounter += 1
        self.fartcount.setText(f"Farts: {self.fartcounter}")  # Update the UI text

# Entry point of the application
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Start Qt application
    window = FartButton()         # Create an instance of the FartButton UI
    window.show()                 # Display the window
    sys.exit(app.exec_())         # Run the event loop
