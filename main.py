import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

            # Add your logic for processing the recognized text here

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said. Please try again.")

    except sr.RequestError as e:
        print(f"Error connecting to the speech recognition service; {e}")

    except KeyboardInterrupt:
        print("Exiting...")
        break
