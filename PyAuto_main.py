import subprocess
import time
import pyautogui


def time_app(path_to_application, loading_image):
    # Start time
    start_time = time.time()

    # Start the application using subprocess
    app = subprocess.Popen(path_to_application)

    # Check for the image on screen
    on_screen = pyautogui.locateOnScreen(loading_image)
    while on_screen is None:
        on_screen = pyautogui.locateOnScreen(loading_image, grayscale=True, confidence=.65)

    # calculate load time
    total_time = time.time() - start_time

    # Close the application
    app.kill()
    app.terminate()

    return total_time
