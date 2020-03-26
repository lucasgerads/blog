---
title: Connecting an MLX90640 Thermosensor with  Numpy/OpenCV
date: "2020-03-26T22:40:32.169Z"
---
I recently got my hands on a MLX90640 thermosensor. Sparkfunk has a good
[tutorial](https://learn.sparkfun.com/tutorials/qwiic-ir-array-mlx90640-hookup-guide/all)
to get started. However, I wanted to use Numpy and OpenCV to toy around with
the data instead of the [Processing IDE](https://processing.org/). I took
their example and wrote a python script that replaces the Processing IDE and
loads the data into Numpy and OpenCV.

## Prerequisites 

### Hardware
 * Teensy by [PJRC](https://www.pjrc.com/teensy/): I have a Teensy 4.0, but other versions should also work  
 * MLX90640: I have a breakout board from [Seeed Studio](https://www.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array-MLX90640-55-degree-p-4335.html). Other breakout boards also work, or using the MLX90640 directly on breadboard should also be fine. 
 * Serial to USB converter

 ### Software
 All the software I use is open source and free. Beside Python3 I use the following packages.
 * [numpy](https://numpy.org/)
 * [opencv-python](https://pypi.org/project/opencv-python/) 
 * [pyserial](https://pypi.org/project/pyserial/)

To program the Teensy one can use the Arduino IDE or alternatively - what I
prefer - [PlatformIO](https://platformio.org/platformio-ide) in VSCode.

## The Hardware Setup
The MLX90640 has an I2C interface. Connect the SCLO and SDA0 pins of the Teensy with the corresponding pins on the MLX90640 and add a pull-up resistor to 3.3 V (e.g. 10 kOhm). Also connect the GND and the 3.3 V power supply. Now connect the serial to USB converter to a PC. That’s all the hardware!

## Software Setup
The script can be found on my
[Github](https://github.com/lucasgerads/MLX90640_OPENCV). The folder
`Example2_OutputToProcessing` contains the firmware by Sparkfunk which they
use to connect to the Processing IDE. Open the
`Example2_OutputToProcessing.ino` file inside of the Arduino IDE and compile
and transfer it onto the Teensy. Arduino's serial monitor should now show the
raw data that comes from the MLX90640.

To consume the data with numpy, use the `test.py` script. Make sure to change
the serial port on line 5.
```python{numberLines: true}
import numpy as np
import serial, cv2, math

serialport = "COM34" # or something like '/dev/ttyS0' 
scaling = 20

width = scaling * 32
height = scaling * 24

img = np.zeros([height,width,3])
imgGray = np.zeros([height,width,3])

try:
    ser = serial.Serial(serialport,115000)
except serial.SerialException:
    print("Cannot open serial port")
    quit()

try:
    print("press Ctrl-C to end")
    while True:
        # read data from serial port
        cc=str(ser.readline())   
        cc = cc[2:-6]
        data = np.fromstring(cc,  sep=',')
        
        # reshape data into matrix
        output = data.reshape(24,32)
        
        # scaling
        minValue = math.floor(np.amin(output))
        maxValue = math.ceil(np.amax(output))
        output = output - minValue      
        output = output * 255/ (maxValue - minValue) # Now scaled to 0 - 255   

        # resize image
        dim = (width, height)
        output = cv2.resize(output, dim, interpolation = cv2.INTER_LINEAR )
            
        # apply colormap
        imgGray = output.astype(np.uint8)
        img = cv2.applyColorMap(imgGray, cv2.COLORMAP_JET)
        
        # put min/max text on image
        text = "Min: " + str(minValue) +  " C  Max: " + str(maxValue)+ " C"  
        font = cv2.FONT_HERSHEY_SIMPLEX  
        org = (20, 50) 
        image = cv2.putText(img, text, org, font, 1, (255, 255, 255) , 2, cv2.LINE_AA) 
        
        cv2.waitKey(50)
        cv2.imshow("image", img);

except KeyboardInterrupt:
    print("Bye bye :)")
    ser.close()
```

## The Result

A few seconds into the video I hold my soldering iron over the sensor, and
you can see how the colormap adjusts to the temperature range dynamically.

`youtube:https://www.youtube.com/embed/DDcRgSuaJIo`