import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox

# Sample Data Structure
playlists = {
    "Happy": [
        ("Happy Song 1", "Artist 1"),
        ("Happy Song 2", "Artist 2"),
        ("Happy Song 3", "Artist 3"),
        ("Happy Song 4", "Artist 4"),
        ("Happy Song 5", "Artist 5")
    ],
    "Sad": [
        ("Sad Song 1", "Artist 1"),
        ("Sad Song 2", "Artist 2"),
        ("Sad Song 3", "Artist 3"),
        ("Sad Song 4", "Artist 4"),
        ("Sad Song 5", "Artist 5")
    ],
    "Energetic": [
        ("Energetic Song 1", "Artist 1"),
        ("Energetic Song 2", "Artist 2"),
        ("Energetic Song 3", "Artist 3"),
        ("Energetic Song 4", "Artist 4"),
        ("Energetic Song 5", "Artist 5")
    ]
}

class Playlist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mood-Based Playlist Generator")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Select your mood and press 'Generate Playlist'")
        layout.addWidget(self.label)

        self.mood_selector = QComboBox()
        self.mood_selector.addItems(playlists.keys())
        layout.addWidget(self.mood_selector)

        self.button = QPushButton("Generate Playlist")
        self.button.clicked.connect(self.generate_playlist)
        layout.addWidget(self.button)

        self.playlist_label = QLabel("")
        layout.addWidget(self.playlist_label)

        self.show()

    def generate_playlist(self):
        selected_mood = self.mood_selector.currentText()
        songs = playlists[selected_mood]
        random_songs = random.sample(songs, 3)  # Select 3 random songs
        song_list = "\n".join([f"{title} by {artist}" for title, artist in random_songs])
        self.playlist_label.setText(f"Playlist for {selected_mood} mood:\n{song_list}")

app = QApplication(sys.argv)
playlist = Playlist()
sys.exit(app.exec())