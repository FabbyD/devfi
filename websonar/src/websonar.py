import pyautogui
from sonar_gesture_detector import SonarGestureDetector

def main():
    detector = SonarGestureDetector()
    try:
        while True:
            detector.detect()
    except KeyboardInterrupt as e:
        print("ya champ!")



if __name__ == "__main__":
    main()
