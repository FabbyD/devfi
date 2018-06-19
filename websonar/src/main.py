from sonar_gesture_detector import SonarGestureDetector
from sonar_driver import SonarDriver
from websonar import WebSonar

def main():
    try:
        driver = SonarDriver()
    except Exception as e:
        print(e)
        print('Exiting')
        return
    detector = SonarGestureDetector()
    websonar = WebSonar()

    driver.add_listener(detector)
    detector.add_listener(websonar)

    print("Started!")
    try:
        while True:
            driver.drive()
    except KeyboardInterrupt as e:
        print("\rGoodbye!")



if __name__ == "__main__":
    main()
