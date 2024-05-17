
import brainstem
import time
import cv2
import numpy as np
import serial
import subprocess
import pyautogui

hub = brainstem.stem.USBHub3p()
hub.discoverAndConnect(brainstem.link.Spec.USB)

#Variables
MicroIrlogo = 'MicroIrLogo.jpg'
script = 'version info'
MicroIrPath = (r"C:\Program Files (x86)\BAE Systems\MicroIR GUI\MicroIR_GUI.exe")
versionCommand = "version info\r"

BaeVersion4_1 = ''


def PortConnection_0n():
    hub.usb.setPortEnable(0)
    time.sleep(5)
# def send_command_and_get_response(ser, command):
#     ser.write(command.encode())  # Send the command as bytes
#     sleep(1)  # Wait for the response (adjust as needed)
#     ser.readline()  # First line is a reiteration of the command, read and throw away
#     response = ser.readline().decode()  # Second line is the result of the command
#
#     return response

def send_command_and_get_response(ports, command, expected_response, baud_rate):
    for port in ports:
        try:
            ser = serial.Serial(port, baud_rate, timeout=1)  # open COM port with specified baud rate
            ser.write(command.encode())  # send the command as bytes
            time.sleep(1)  # wait for the response (adjust as needed)
            ser.readline()  # first line is a reiteration of the command, read and discard
            response = ser.readline().decode().strip()  # second line is the result of the command
            ser.close()  # disconnect from the COM port
            if response == expected_response:
                return response
        except serial.SerialException:
            pass  # COM port is unavailable

    return 'No response from BAE'
def open_app(app_path):
    try:
        # Open the application using cmd
        subprocess.Popen(['start','', app_path], shell=True)
        print(f"Opening application: {app_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(5)

def LocateImage(image):
    # start_time = time()
    while True:
        # Take a screenshot of the desktop
        screenshot = pyautogui.screenshot()
        # Convert the screenshot to a format compatible with OpenCV
        screenshot_cv = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
        # Load the template image (button)
        template = cv2.imread(image)
        # Convert the template image to grayscale
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot_cv, template_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        locations = np.where(result >= threshold)
        # If locations are found, return the coordinates
        if locations[0].size > 0:
            for loc in zip(*locations[::-1]):
                x, y = loc  # Coordinates of the top-left corner of the match
                return x, y

        # Check if timeout has occurred
        # if time() - start_time >= 15:
        #     break

        # Wait for a few milliseconds before checking again
        time.sleep(1)

def clickOn(xLoc,yLoc):
    pyautogui.moveTo(xLoc,yLoc)
    pyautogui.click(xLoc,yLoc)
    time.sleep(5)

def PortConnection_off():
    hub.usb.setPortDisable(0)


print("Please connect core to 20 board")
answer = input("Was core connected Yes or No : ")

if answer.lower().strip() == 'yes':
    PortConnection_0n()
    command = "version info\r"
    expected_response = "TX79MicroIR Version TWV640 4.1c, built on 12:07:22 Jul 26 2018 by arlene.southern"
    #ports = ["COM1", "COM2", "COM3"]  # specify the COM ports here
    ports = ["COM" + str(i) for i in range(1, 100)]
    baud_rate = 9600  # specify the baud rate here
    response = send_command_and_get_response(ports, command, expected_response, baud_rate)

    if response == "TX79MicroIR Version TWV640 7.1, built on 12:07:22 Jul 26 2018 by arlene.southern":
        print(f'Core already {BaeVersion4_1}, no need to downgrade')
    else:
        print(response)
        open_app(MicroIrPath)
        xLoc, yLoc = LocateImage('Advanced_Button.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('Advanced_Gui_Yes.jpg')
        clickOn(xLoc, yLoc)
        time.sleep(5)
        xLoc, yLoc = LocateImage('Enter_crop_shift_cancel.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('Initialization.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('customer_folder.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('Initialization.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('main_initialization_complete.jpg')
        clickOn(xLoc, yLoc)
        xLoc, yLoc = LocateImage('PixelKill.jpg')
        clickOn(xLoc, yLoc)
#add connected not connected verification
else:
    print("Core not connected, please try again!!")
    answer = input("Was core connected Yes or No")





