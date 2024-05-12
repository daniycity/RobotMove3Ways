
⌚ About 3 minutes 📅 Last update 06/05/24 - ddMMYY ❓ Intermediate level
# Index
- [First](#first) 
- [SecondWay](#second)
- [ThirdWay](#third)

## RobotMove3Ways
With a kit for arduino compose of a little steering robot i try to move it using an Android App, Iot with Alexa and using AI

## FirstWay <a id="first"></a>
The idea pretty easy and straight forward i did it when i was 15 years old in school i translated the code and the app in english. With an Android app build without no code thank to [App Inventor](https://appinventor.mit.edu/) we just send bluetooth signal at the [Arduino](https://www.arduino.cc/) with some motor and electronics. The code in the arduino will just turn on and off the right pin for make the robot move!
I'll not explain in the detail all the code and the electric diagram i'll just link some tutorial!
- Video [YouTube](https://www.youtube.com/watch?v=QC6TDIduhfg) 
- [Instructable](https://www.instructables.com/Build-a-Bluetooth-Robot-W-Arduino-MIT-App-Inventor/)

RobotApp.aia it's the project to import in app Inventor

## SecondWay <a id="second"></a>
16 years old more or less, using [Raspberry](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/), some utilites like microphone ecc and the api of [Alexa](https://www.alexa.com/). By asking Alexa you can use some custom skill for move the robot forward/ back etc. The code was in python using the Alexa SDK but the api are deprecated and i wasn't able to retrive it ![Deprecated Api Image](/ReadmeImg/AlexaOldApi.PNG)

I've looked in other way to do it and decided to use [Sinric Pro](https://sinric.pro/). 

![Sinric Pro Dashboard](/ReadmeImg/SinricPro.PNG)

I've created a custom template of a device that accept the various stuff the robot can do. With the python SDK written some code that when the mode is forward send the right bluettoth signal to the arduino and that's it! [Sinric Pro tutorial](https://help.sinric.pro/pages/custom-templates) on how to create a custom device it's the basic doc that i've used for creating the project

## ThirdWay <a id="third"></a>
I got really exited by seeing this super viral video.

[![OpenAi Robot](https://img.youtube.com/vi/Sq1QZB5baNw/0.jpg)](https://www.youtube.com/watch?v=Sq1QZB5baNw)

But i'm not that skilled in ai so i just simplify as i can for archive at least some illusion of AI. Using [Open APi](https://openai.com/index/openai-api) and the PythonSdk i've given a contex
    You are a robot that answare two question:

    "What do you see?" or similar meaning question or "Can you pick with a requirements" or similar meaning question:

    At the first one you're going to answare what do you see

    At the second quesiton you're going to answare "yes sure" with at the end in capital letter the "CALLFUNCT(the position of the object LEFT OR RIGHT)"
When i get the CALLFUNCT as a response i know that i have to move the robot by sendind the bluetooth signal at the arduino that will do the right instructions. 

There are other library of utility for reading the response from the api. For use the smarphone camera and take the screenshot of the image. I'll try to link all the resources that i've used.
- How to use android camera in python [GeeksForGeeks](https://www.geeksforgeeks.org/connect-your-android-phone-camera-to-opencv-python/)
- Build an assistant with open api YouTube video [Ai Austin](https://www.youtube.com/watch?v=8z8Cobsvc9k)

