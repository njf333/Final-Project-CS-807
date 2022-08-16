<h1><b> Hand Gesture Controlled computer </h1></b>

<p> The project is focused on implementing the technique to control computer using hand gestures. The concept behind Arduino-based Gesture maintained computer is simple
and is implemented using Python. The principle here uses 2 Ultrasonic sensors with Arduino and the central part is the position of the ultrasonic sensors. It works by placing our hands in front of the ultrasonic sensor and then calculating the distance between the hand and the sensor. The computer uses this information to perform relevant actions. The positioning of ultrasonic sensors is the most crucial part here. The project proposal focuses on making modifications to the existing project,
implementing multiple gestures to control computer actions.
  
 ![image](https://user-images.githubusercontent.com/103396922/184795946-089e7153-cd96-497a-acbf-7e33a03c01b4.png)

  
<p> 
Firstly, the device takes power by connecting 5v pin in Arduino uno to the VCC pin in the ultrasonic sensor and connecting GND pin in Arduino uno to the GND pin in the
ultrasonic sensor. The trig pin data will be sent to the (5) digital pin in the Arduino uno, and the echo pin data will be sent to the (6) digital pin in the Arduino uno. The transmitter in the sensor will send ultrasonic waves and the waves will stop at an object and come back to the receiver, so then the Arduino uno will calculate the time between sending the waves and receiving the waves, and then we will use this equation to find the distance between the sensor and the object (duration * 0.034 / 2). The Arduino uno will check if the distance is between 2cm and 10cm if yes then it will print “VOLUME-UP” in the serial, if no then it will check if the distance is between 12cm and 20cm if yes then it will print “VOLUME-DOWN” in the serial, if no then it will check if the distance is between 22cm and 30cm if yes then it will print “BRIGHTNESS-UP” in the serial, if no then it will check if the distance is between 32cm and 50cm if yes then it will print “BRIGHTNESS-DOWN” in the serial.

<p> The Python script will get the serial of the device by the port number (e.g. com1, com2, com3, come4. . . etc.), and it will check if it prints “VOLUME-UP” then it will volume up the computer audio, if no it will check if it prints “VOLUME-DOWN” if yes it will volume down the computer audio, if no it will check if it prints “BRIGHTNESS-UP” if yes It will increase computer brightness, if no then it will check if it prints “BRIGHTNESS-DOWN” if yes It will decrease computer brightness. My sensor is connected to the Arduino uno via the 5v pin, and the trig pin has been connected to the 5 digital pins of the Arduino uno. I have also connected the VCC pin of the sensor to the Arduino uno’s VCC pin. In addition, the sensor’s echo pin is connected to the Arduino uno’s six digital pins, and the sensor’s GND (Ground) pin is connected to the Arduino uno’s GND pin.
  
  ![image](https://user-images.githubusercontent.com/103396922/184796065-8002c06f-707e-4af6-abfe-632a66b858de.png)

Repository Contents
  
Here is a map of all the top-level contents listed in the repository:

<br> /Diagrams - This is where the image files for this readme are.
<br> /Python code - This is the place where the code is divided into segments, for better understanding and the main.py file.
<br> /README.md - This is the file you're reading now!
<br> /Final project.pdf - This is the project report.
<br> /Code - This is the C++ code that I have worked on.
  
  <h3> Device Information </h3>
  
  The device used:
<br>1 bread board,
<br>1 ultrasonic sensor,
<br>1 Arduino uno,
<br>4 male to male jumper wires,
<br>1 USB Cable A male to B male.

![image](https://user-images.githubusercontent.com/103396922/184796170-dcfd69e8-0265-4246-babc-29c7e4674df3.png)


![image](https://user-images.githubusercontent.com/103396922/184796211-2f9d47ed-d7e6-4cf1-98ba-7c5621688964.png)

<h3> Usage </h3>

I have successfully implemented hand gestures controlled computer system using the distance reading concept, which means the volume on the computer will turn up if there is a specific distance between the hand and the sensors and the same implies to all the gestures.

Connect the device to the computer by the USB cable, and run the Python script in the computer, and then put your hand above the sensor and according to the distance it will do an action in your computer (Volume up, Volume down, Brightness up, and Brightness down).

A. Action 1

When a hand is at a specific distance from the sensors, the volume turns up. The Arduino uno will check if the distance is between 2cm and 10cm if yes then it will print “VOLUME-UP” in the serial.

B. Action 2

When a hand is at a specific distance from the sensors, the volume turns down. The Arduino uno will check if the distance is between 12cm and 20cm if yes then it will print “VOLUME-DOWN” in the serial.

C. Action 3

When a hand is at a specific distance from the sensors, the brightness turns high. The Arduino uno will check if the distance is between 22cm and 30cm if yes then it will print “BRIGHTNESS-UP” in the serial.

D. Action 4

When a hand is at a specific distance from the sensors, the brightness turns low. The Arduino uno will check if the distance is between 32cm and 50cm if yes then it will print “BRIGHTNESS-DOWN” in the serial.


<h3> Contributor </h3>

This project is done only by me - Nirja Joshi and no teammates were involved in this project. To ensure the smooth functioning of the prototype, all project selection, research, hardware design, prototype testing, writing the paper, and GitHub documentation were entirely done by me.




