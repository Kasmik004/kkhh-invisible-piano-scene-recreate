# Invisible Piano - Kuch Kuch Hota Hai Scene Recreation


### Recreate the magic of the invisible piano scene from *Kuch Kuch Hota Hai* with your webcam!

This fun and interactive project uses computer vision and hand-tracking to simulate the iconic moment where Shah Rukh Khan mimics playing an invisible piano in the air. As you press down with your fingers, real piano notes are played to recreate the melody from the movie.

---

## Features

* Uses your webcam to detect hand movements
* Plays piano notes when specific fingers press down
* Fully replicates the feel of the movie scene
* Built with Python, OpenCV, MediaPipe, and Pygame

---

## Tech Stack

* `OpenCV` - For video capture and display
* `MediaPipe` - For accurate hand landmark tracking
* `Pygame` - For audio playback

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Kasmik004/kkhh-invisible-piano-scene-recreate.git
   cd invisible-piano
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure the `.wav` files (note sounds) are placed in `./notes/` directory. These are required for the piano notes to play.

5. Run the program:

   ```bash
   python main.py
   ```

---

## Project Structure

```
.
├── notes/             # Contains .wav piano note files
├── main.py                  # Main application file
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Contributions & Collabs

I'm always open to collaborations, improvements, and bug fixes. If you have ideas or want to contribute, feel free to open an issue or pull request!

Let’s build cool stuff together 🤝

---

## License & Attribution

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this code **as long as you give proper credit** to the original author.

> **If you use this project in any form (forks, demos, videos, or mashups), you must mention me with a link back to this repository.**

---


## Contact

Feel free to reach out via GitHub Issues or \[[rkasmik@gmail.com](mailto:rkasmik@gmail.com)].

---

**Enjoy recreating the invisible piano magic!** 
