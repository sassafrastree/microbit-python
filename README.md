# Buttons
Buttons are almost always digital inputs. However, it is possible to use analog reading with a resistor ladder but those are not a good long-term solution.
```python
from microbit import *

pin0.read_digital()
```
# LEDs, Buzzers, and Lasers
LEDs, buzzers, and lasers can be either digital or analog outputs. Analog output would be used if you want to change the intensity. In contrast, digital output can be used only to turn it on or off. 

```python
from microbit import *

#fully on
pin0.write_digital(1)
pin1.write_analog(1023)

# fully off
pin0.write_digital(0)
pin1.write_analog(0) 
```
# Motors
Motors are analog outputs. The gray positional motors turn 270º, to set it to that angle you have to use this formula `degrees/3 + 25`. For the orange/green continuous motors 50 is right, 100 is left, and 75 is stop. The closer you get to 75 the slower it will go.
```python
from microbit import *

# continuous
pin0.write_analog(50) # Right
pin0.write_analog(100) # Left
pin0.write_analog(75) # stop

# positional
pin1.write_analog(180/3+25) # 180º
```
# LED Strip
The LED strip (NeoPixels) is an output part of an existing module in the microbit python editor. 
### Useful Links
1. https://www.w3schools.com/colors/colors_rgb.asp

**Setup:** To set up your NeoPixel strip you will need to declare it as a variable. You will set this variable to NeoPixel() with its parameters being: the pin and the number of LEDs

Example: `np = NeoPixel(pin0, 8)`

**Single LEDS:** Now that you have declared your NeoPixel strip it is now a list with its values being RGB codes.

Example: `np[0] = (63, 63, 0)`

**All LEDS:** To set the color of all your LEDs at once you can use VARIABLE.fill((R,G,B))

Example: `np.fill((0, 63, 63))`

**Clear/Show:** Now that you have set up what you want your NeoPixel strip to do you need to tell it to show or clear with VARIABLE.show() and VARIABLE.clear()

Example: `np.show()`
Example: `np.clear()`

```python
from microbit import *
from neopixel import *

np = NeoPixel(pin0, 8)
np.fill((0, 63, 63))
np.show()
```
# Joystick
> [!NOTE]  
> The joystick module isn't necessary however it simplifies the process. The joystick detects from -420 to 420 for both x and y 

**Setup:** To set up your Joystick you will need to declare it as a variable. You will set this variable to Joystick() with its parameters being the pins connected to VRX, VRY, and SW  

Example: `js = Joystick(pin0, pin1, pin2)`

**X & Y:** These are both analog values that range from -420 to 420 with 0 being the center

Example: `js.x`

Example: `js.y`

**SW:** This is a digital value that detects when the joystick is being clicked (like a button)

Example: `js.sw`

```python
if js.x == 0 and js.y == 0:
    # center
if js.x > 400 and js.y > 400:
    # top right
if js.x < -400 and js.y < -400:
    # bottom left
if js.sw == 1:
    # button pressed
```
# OLED
## Stamps
> [!NOTE]  
> Stamps should be used over bitmaps as they draw on small sections of the screen instead of the full-screen

### Useful Links
1. https://tools.withcode.uk/binaryimage/
2. https://www.dcode.fr/binary-image

## create_stamp()
**Choosing a stamp:** You can either use the built-in microbit stamps with Image.[name of image] or build your own with Image([map goes here])

**Custom stamps:** There can be between 5 and 8 rows of five 0’s (off) or 1’s (on). There must be at least 5 pixels in a row and at least 5 rows. Each row string must end with a colon. 

Example:  `create_stamp(Image('01010': '11111:' '11111:' '01110:' '00100:'))` 

To create larger images use more than one stamp.

### draw_stamp()
to draw the stamp you will need to declare your stamp as a variable for this example I will be calling mine “stamp”

The OLED screen is 128x64 pixels however for stamps it uses a 64x32 grid. the top right corner is 0,0. in the draw_stamp() function there are four parameters: x, y, stamp, and color. our OLED screens only have 1 color so set that to 1 as 0 is off.

Example: `draw_stamp(20, 0, stamp, 1)`

```python
from ssd1306 import initialize, clear_oled
from ssd1306_stamp import draw_stamp
from ssd1306_img import create_stamp
from microbit import *

create_stamp(Image('01010:' '11111:' '11111:' '01110:' '00100:'))
draw_stamp(20, 0, stamp, 1)
```
## Bitmaps
> [!IMPORTANT]  
> This section is very complicated so if you don't understand I recommend you look at [the original module](https://github.com/fizban99/microbit_ssd1306)

> [!NOTE]  
> You can not map out the image on your own as the bitmap is stored in hexadecimal as there are 8192 pixels on the OLED screen.

### Useful Links
1. https://javl.github.io/image2cpp/
2. https://vscode.dev/

### show_bitmap()
**Generating your image:** You will want to use the [image to byte array](https://javl.github.io/image2cpp/) tool as mapping these images would be a very tedious process. When clicking generate code at the bottom of the image to byte array link, use the following setting to avoid having your image display scrambled.

- canvas size: 128 x 64
- scaling: scale to fit, keeping proportions
- center image: horizontally
- code output format: plain bytes
- draw mode: Vertical - 1 bit per pixel

**Adding the bitmap to your code (part 1):** Create a list with the values from the previous step 

**create a blank file:** To use this image you will now need to create a blank file with no file type. To create one of these, open any code editor and create a new file without the file type at the end. If you are on a Chromebook you can use the web version of vscode and follow the same instructions. 

**Adding the bitmap to your code (part 2):** Add the following code to your main file

```python
from ssd1306 import initialize, clear_oled
from ssd1306_bitmap import show_bitmap

newFileByteArray = bytearray(list)
with open('blank_file_name', 'wb') as newFile:
    newFile.write(newFileByteArray)
    
show_bitmap("blank_file_name")
```

# Ultrasonic Range Sensor
Notes in progress