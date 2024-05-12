
from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import time
import requests 
import cv2 
import numpy as np 
import imutils 
import os
import base64
from gtts import gTTS
import bluetooth

#Set  apikey
client = OpenAI(
    api_key="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"
)

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
url = "http://192.168.1.4:8080/shot.jpg"

# Replace with bluetooth module of Arduino
target_device = "98:d3:71:fd:45:d1"

#Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
      audio = recognizer.record(source)
    try:
      return recognizer.recognize_google(audio)
    except:
      print("Skipping unknown error")

def generate_response(prompt, contextForGpt):
  #tell the ai how to answer to the question in the way
  #we can extract the info and move the robot accordingly Also contain
  #User previous messages if any, else empty
  img_resp = requests.get(url) 
  img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
  img = cv2.imdecode(img_arr, -1) 
  img = imutils.resize(img, width=1000, height=1800) 
  path = 'C:/Users/CASA/Documents'
  cv2.imwrite(os.path.join(path , 'waka.jpg'),img)
  # Getting the base64 string
  base64_image = encode_image(os.path.join(path , 'waka.jpg'))

  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {
        "role": "system",
        "content": [
          {"type": "text", "text": contextForGpt}
        ],
      },
      {
        "role": "user",
        "content": [
          {"type": "text", "text": prompt},
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}",
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )
  return response.choices[0]

def speak_text(text):
  engine.say(text)
  engine.runAndWait()


def sendBluettothArduino(response):
  # establish a connection with the device
  if(response.contains("CALLFUNCT(")):

    try:
      sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
      sock.connect((target_device, 1))

      action=response[response.find("CALLFUNCT(")+len("CALLFUNCT("):response.find(")")]
      print(f"I received to do ACTION ->{action}")

      if(action.lower=="right"):
        # send a message over the Bluetooth socket
        sock.send("right")
      if (action.lower=="left"):
        # send a message over the Bluetooth socket
        sock.send("left")

      # close the Bluetooth socket
      sock.close()

    except bluetooth.btcommon.BluetoothError as e:
        print("Error bluetooth:", e)

def main():
  contextForGpt="""You are a robot that answare two question:

              "What do you see?" or similar meaning question or "Can you pick with a requirements" or similar meaning question:

              At the first one you're going to answare what do you see

              At the second quesiton you're going to answare "yes sure" with at the end in capital letter the "CALLFUNCT(the position of the object LEFT OR RIGHT)"

              """
  while True:
    # Wait for user to say "Armando"
    print("Say 'Armando' to start recording your question...")
    with sr.Microphone() as source:
      recognizer = sr.Recognizer()
      audio=recognizer.listen(source)
      try:
        transcription = recognizer.recognize_google(audio)
        if transcription.lower() == "armando":
          #Record audio
          filename = "input.wav"
          print("Say your question...")
          with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            source.pause_threshold=1
            audio = recognizer.listen(source,phrase_time_limit=None, timeout=None)
            with open(filename,"wb") as f:
              f.write(audio.get_wav_data())
          # Transcribe audio to text
          text = transcribe_audio_to_text(filename)
          if text:
            print(f"You said: {text}")

            #Generate response using gtp-3
            response = generate_response(text,contextForGpt).message.content
            print(f"GPT-2 Says: {response}")
            contextForGpt+=response

            #Record audio with gtts for vide
            tts= gTTS(text=response, lang="en")
            tts.save("sample.mp3")

            #Send bluetoothSignal to Arduino for move robot if needed
            sendBluettothArduino(response)

            #Read response using text-to-speech
            speak_text(response)
      except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
  main()