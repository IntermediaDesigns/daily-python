# Required Libraries: sys, random, PyQt6
# pip install PyQt6

import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class Playlist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playlist")
        self.setGeometry(100, 100, 400, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel("Press the button to play a random song")
        layout.addWidget(self.label)
        self.button = QPushButton("Play")
        self.button.clicked.connect(self.play)
        layout.addWidget(self.button)
        self.show()

    def play(self):
        songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]
        song = random.choice(songs)
        self.label.setText(f"Playing: {song}")


app = QApplication(sys.argv)
playlist = Playlist()
sys.exit(app.exec())
