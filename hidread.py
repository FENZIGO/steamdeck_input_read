import os
import ctypes

#DeckInput structure using ctypes
class DeckInput(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_uint8),
        ('_a1', ctypes.c_uint8 * 3),
        ('seq', ctypes.c_uint32),
        ('buttons', ctypes.c_uint64),
        ('lpad_x', ctypes.c_int16),
        ('lpad_y', ctypes.c_int16),
        ('rpad_x', ctypes.c_int16),
        ('rpad_y', ctypes.c_int16),
        ('accel_x', ctypes.c_int16),
        ('accel_y', ctypes.c_int16),
        ('accel_z', ctypes.c_int16),
        ('gpitch', ctypes.c_int16),
        ('groll', ctypes.c_int16),
        ('gyaw', ctypes.c_int16),
        ('q1', ctypes.c_uint16),
        ('q2', ctypes.c_uint16),
        ('q3', ctypes.c_uint16),
        ('q4', ctypes.c_uint16),
        ('ltrig', ctypes.c_uint16),
        ('rtrig', ctypes.c_uint16),
        ('stick_x', ctypes.c_int16),
        ('stick_y', ctypes.c_int16),
        ('rstick_x', ctypes.c_int16),
        ('rstick_y', ctypes.c_int16),
        ('dpad_x', ctypes.c_int16),
        ('dpad_y', ctypes.c_int16),
    ]


class DeckButton(ctypes.c_int64):
    DOTS = 0b100000000000000000000000000000000000000000000000000
    RSTICKTOUCH = 0b000100000000000000000000000000000000000000000000000
    LSTICKTOUCH = 0b000010000000000000000000000000000000000000000000000
    RGRIP2 = 0b000000001000000000000000000000000000000000000000000
    LGRIP2 = 0b000000000100000000000000000000000000000000000000000
    RSTICKPRESS = 0b000000000000000000000000100000000000000000000000000
    LSTICKPRESS = 0b000000000000000000000000000010000000000000000000000
    RPADTOUCH = 0b000000000000000000000000000000100000000000000000000
    LPADTOUCH = 0b000000000000000000000000000000010000000000000000000
    RPADPRESS = 0b000000000000000000000000000000001000000000000000000
    LPADPRESS = 0b000000000000000000000000000000000100000000000000000
    RGRIP = 0b000000000000000000000000000000000010000000000000000
    LGRIP = 0b000000000000000000000000000000000001000000000000000
    START = 0b000000000000000000000000000000000000100000000000000
    C = 0b000000000000000000000000000000000000010000000000000
    BACK = 0b000000000000000000000000000000000000001000000000000
    DPAD_DOWN = 0b000000000000000000000000000000000000000100000000000
    DPAD_LEFT = 0b000000000000000000000000000000000000000010000000000
    DPAD_RIGHT = 0b000000000000000000000000000000000000000001000000000
    DPAD_UP = 0b000000000000000000000000000000000000000000100000000
    A = 0b000000000000000000000000000000000000000000010000000
    X = 0b000000000000000000000000000000000000000000001000000
    B = 0b000000000000000000000000000000000000000000000100000
    Y = 0b000000000000000000000000000000000000000000000010000
    LB = 0b000000000000000000000000000000000000000000000001000
    RB = 0b000000000000000000000000000000000000000000000000100
    LT = 0b000000000000000000000000000000000000000000000000010
    RT = 0b000000000000000000000000000000000000000000000000001

# Function to check button presses
def is_button_pressed(buttons, button_mask):
    return buttons & button_mask == button_mask

# Open the device file and read data
device_path = '/dev/hidraw3'

with open(device_path, 'rb') as device:
    while True:
        data = device.read(ctypes.sizeof(DeckInput))  # Read enough bytes for the structure
        if not data:
            break  # Exit if no more data

        # Cast raw data to DeckInput structure
        input_data = DeckInput.from_buffer_copy(data)

        # Print the parsed input data
        print(f"Buttons pressed: {bin(input_data.buttons)}")
        print(f"LPad: X={input_data.lpad_x}, Y={input_data.lpad_y}, Z={input_data.dpad_x}")
        print(f"RPad: X={input_data.rpad_x}, Y={input_data.rpad_y}, Z={input_data.dpad_y}")
        print(f"Acceleration: X={input_data.accel_x}, Y={input_data.accel_y}, Z={input_data.accel_z}")
        print(f"LStick: X={input_data.stick_x}, Y={input_data.stick_y}")
        print(f"RStick: X={input_data.rstick_x}, Y={input_data.rstick_y}")
        print(f"LTrig={input_data.ltrig}, RTrig={input_data.rtrig}")
        # Check for specific button presses
        if is_button_pressed(input_data.buttons, DeckButton.A):
            print("Button A is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.B):
            print("Button B is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.START):
            print("Start button is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.BACK):
            print("Back button is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.DPAD_UP):
            print("D-Pad Up is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.DPAD_RIGHT):
            print("D-Pad Right is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.DPAD_DOWN):
            print("D-Pad Down is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.DPAD_LEFT):
            print("D-Pad Left is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.X):
            print("Button X is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.Y):
            print("Button Y is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.LB):
            print("Button LB is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.RB):
            print("Button RB is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.LT):
            print("Button LT is pressed!")
        if is_button_pressed(input_data.buttons, DeckButton.RT):
            print("Button RT is pressed!")



        # Print the parsed input data
        # print(f"Buttons pressed: {bin(input_data.buttons)}")
        # print(f"LPad: X={input_data.lpad_x}, Y={input_data.lpad_y}")
        # print(f"RPad: X={input_data.rpad_x}, Y={input_data.rpad_y}")
        # print(f"Acceleration: X={input_data.accel_x}, Y={input_data.accel_y}, Z={input_data.accel_z}")
        # print(f"Stick: X={input_data.sitick_x}, Y={input_data.stick_y}")
        # print(f"RStick: X={input_data.rstck_x}, Y={input_data.rstick_y}")
        print(f"Q1={input_data.q1}, Q2={input_data.q2}, Q3={input_data.q3}, Q4={input_data.q4}")
       
        print(f"GPitch={input_data.gpitch}, GRoll={input_data.groll}, GYaw={input_data.gyaw}")
      

        # Check for specific button presses
        #... (button press checks omitted for brevity)

        # Print additional data
        # print(f"_a1: {input_data._a1}")
        # print(f"Type: {input_data.type}")
        # print(f"Seq: {input_data.seq}")