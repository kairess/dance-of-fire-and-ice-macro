from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(1)
print('[*] Start!')

def press_space():
    print('Space')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

press_space()
print('[*] 3, 2, 1')
time.sleep(2.8)

for i in range(7):
    press_space()
    time.sleep(0.54)

time.sleep(0.27)
press_space()

time.sleep(0.54 - 0.27)
press_space()

for i in range(9):
    press_space()
    time.sleep(0.54)