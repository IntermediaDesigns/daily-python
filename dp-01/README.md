# Project Level: Real-World
This project is designed for learners who know Python fundamentals and are learning to build real-world programs.

## Project Description
Today, we will build a Mood-Based Playlist Generator with Python that generates a playlist based on the user’s mood. By simply choosing from options like “Happy,” “Sad,” or “Energetic,” the app will provide a selection of songs that match that mood. The app will fetch song recommendations from a mock API (to keep it simple), and you can expand this by integrating it with real music APIs like Spotify or YouTube. We will use the PyQt6 library for this, but you can use any other GUI library

## Expected Output
The GUI lets the user select their mood from a list of three moods (Happy, Sad, and Energetic).

After selecting a mood, the user can press the “Generate Playlist” button to get a recommendation of songs.

We are simplifying the code by getting the data from a dictionary stored inside the script:

Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.


## Prerequisites
Required Libraries: sys, random, PyQt6
pip install PyQt6
Required Files: No files are required.
IDE: Use any IDE.
```

## Features

- Simple GUI interface built with PyQt6
- Mood selection from dropdown menu
- Generate playlist button
- Display of recommended songs based on selected mood
- Mock playlist database included in the code

## Sample Data Structure

The application uses the following data structure for playlists:

```python
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
```

## Development Environment

You can use any IDE or text editor of your choice to work with this project.

## Future Enhancements

The project can be enhanced by:
- Integrating with real music APIs (Spotify, YouTube)
- Adding more mood options
- Including actual song recommendations
- Adding playback functionality
- Implementing user accounts and saved playlists

## Support

This project is part of Daily Python Projects. To receive new posts and support the work, consider becoming a free or paid subscriber.