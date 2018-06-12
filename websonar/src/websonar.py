import pyautogui
from sonar_gesture_detector import SonarGestureDetector
from sonar_driver import SonarDriver

def main():
    driver = SonarDriver()
    detector = SonarGestureDetector()

    print("Started!")
    try:
        while True:
            driver.drive()
    except KeyboardInterrupt as e:
        print("ya champ!")



if __name__ == "__main__":
    main()
