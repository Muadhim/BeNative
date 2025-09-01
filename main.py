import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import SpeechApp

def main():
    app = QApplication(sys.argv)

    window = SpeechApp()

    # Open and read the QSS file
    with open("ui/style.qss", "r") as file:
        qss = file.read()

    # Apply the stylesheet to the application
    app.setStyleSheet(qss)
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
