import cv2
import os
import mediapipe as mp
import pygame
import time

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Load note sounds
notes_needed = []
for note in [
    "B4",
    "C5",
    "B4",
    "A4",
    "G4",
    "B4",
    "B4",
    "C5",
    "B4",
    "A4",
    "G4",
    "B4",
    "A4",
    "B4",
    "A4",
    "G4",
    "GB4",
    "A4",
    "D4",
    "A4",
    "G4",
    "B4",
    "G4",
    "G4",
    "G4",
]:
    path = f"./another_one/{note}.wav"
    if os.path.exists(path):
        notes_needed.append(pygame.mixer.Sound(path))

max_notes = len(notes_needed)
counter = 0


def test_play_all_notes(notes_dict, delay=0.6):
    """
    Play all notes in the dict sequentially with their names printed.
    `notes_dict` should be a list of (note_name, sound) tuples.
    """
    print("Starting note playback test...")
    for i, (note_name, sound) in enumerate(notes_dict):
        print(f"Playing note {i + 1}/{len(notes_dict)}: {note_name}")
        sound.play()
        time.sleep(delay)
    print("Finished playing all notes.")


class HandTracking:
    def __init__(self):
        self.handsMp = mp.solutions.hands
        self.hands = self.handsMp.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.4,
        )
        self.tipIds = [4, 8, 12, 16, 20]
        self.finger_states = {"index": False, "middle": False, "ring": False}

    def findLandmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            h, w, _ = frame.shape
            return [
                [id, int(lm.x * w), int(lm.y * h)]
                for id, lm in enumerate(handLms.landmark)
            ]
        return []

    def detectPress(self, lmsList):
        global counter
        pressed = {}
        mapping = {"index": 1, "middle": 2, "ring": 3}
        for name, idx in mapping.items():
            tip = self.tipIds[idx]
            pip = tip - 2
            if tip < len(lmsList) and pip < len(lmsList):
                tip_y = lmsList[tip][2]
                pip_y = lmsList[pip][2]
                is_pressed = tip_y >= pip_y - 5
                if is_pressed and not self.finger_states[name]:
                    self.finger_states[name] = True
                    # Play sound (non-blocking)
                    notes_needed[counter % max_notes].play()
                    counter += 1
                elif not is_pressed:
                    self.finger_states[name] = False


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    detector = HandTracking()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        lmsList = detector.findLandmarks(frame)
        if lmsList:
            detector.detectPress(lmsList)

        cv2.imshow("Piano", frame)
        key = cv2.waitKey(1)
        time.sleep(0.01)  # Throttle CPU
        if key & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    # test_play_all_notes(notes_needed)
