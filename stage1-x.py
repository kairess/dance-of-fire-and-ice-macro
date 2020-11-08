from pynput.keyboard import Key, Controller
import time

DELAY_1 = 0.3965

keyboard = Controller()

time.sleep(1)
print('[*] Start!')

def press_space(delay=0):
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    if delay > 0:
        time.sleep(delay)

press_space()
print('[*] 3, 2, 1')
time.sleep(2.3)

for i in range(30):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)

for i in range(14):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)

for i in range(14):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)

for i in range(14):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)

for i in range(14):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)

for i in range(12):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)

for i in range(8):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)

for i in range(12):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)

for i in range(8):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)
press_space(delay=DELAY_1 - DELAY_1 / 2.)

for i in range(2):
    press_space(delay=DELAY_1)

press_space(delay=DELAY_1 - DELAY_1 / 2.)
press_space(delay=DELAY_1 + DELAY_1 / 2.)

for i in range(7):
    press_space(delay=DELAY_1 * 4)

print('[*] Done!')
