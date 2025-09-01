import threading
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from core.conversation import conversation_loop

class SpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BeNative")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("BeNative - English Practice")
        layout.addWidget(self.label)

        self.start_btn = QPushButton("Start Conversation")
        self.start_btn.clicked.connect(self.start_conversation)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Conversation")
        self.stop_btn.clicked.connect(self.stop_conversation)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)

        self.stop_event = None
        self.thread = None

    def start_conversation(self):
        if not self.thread or not self.thread.is_alive():
            self.stop_event = threading.Event()
            self.thread = threading.Thread(target=conversation_loop, args=(self.stop_event,))
            self.thread.start()
            self.label.setText("Conversation running...")

    def stop_conversation(self):
        if self.stop_event:
            self.stop_event.set()
            self.thread.join()
            self.label.setText("Conversation stopped.")
