import board
import busio
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.matrix import MatrixScanner
from kmk.keys import KC

# [AW9523B driver classes from previous example]
# ... (include the AW9523B and AW9523BPin classes here)

# Set up I2C and expander
i2c = busio.I2C(board.SCL, board.SDA)
aw = AW9523B(i2c, address=0x58)

# Mix expander pins and native board pins
# Example: columns use expander, rows use native GPIO
col_pins = [
    aw.get_pin(9),
    aw.get_pin(10),
    aw.get_pin(11),
    aw.get_pin(12),
    aw.get_pin(13),
    aw.get_pin(14),
    aw.get_pin(15),
    board.GP10,
    board.GP9,
    board.GP8,
]

row_pins = [
    aw.get_pin(0),
    aw.get_pin(1),
    aw.get_pin(2),
    aw.get_pin(3),
    aw.get_pin(4),
    aw.get_pin(5),
    aw.get_pin(6),
    aw.get_pin(7),
    aw.get_pin(8),
]

# Configure expander pins
for i, pin in enumerate(col_pins):
    if hasattr(pin, 'aw9523'):  # It's an expander pin
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = True
    else:  # It's a native board pin
        native_pin = digitalio.DigitalInOut(pin)
        native_pin.direction = digitalio.Direction.OUTPUT
        native_pin.value = True
        col_pins[i] = native_pin

# Configure native row pins
for i, pin in enumerate(row_pins):
    native_pin = digitalio.DigitalInOut(pin)
    native_pin.direction = digitalio.Direction.INPUT
    native_pin.pull = digitalio.Pull.DOWN
    row_pins[i] = native_pin

# Initialize keyboard
keyboard = KMKKeyboard()
keyboard.matrix = MatrixScanner(
    cols=col_pins,
    rows=row_pins,
    diode_orientation=DiodeOrientation.COL2ROW
)

# TODO: actually do the keymap
# my god why didn't i just use a 24-pin thing and done a sensible matrix layout this would've been so much easier
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H]
]

if __name__ == '__main__':
    keyboard.go()