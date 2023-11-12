from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import speech_recognition as sr

class SpeechToTextApp(App):
    def build(self):
        self.recognizer = sr.Recognizer()

        # UI components
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.text_input = TextInput(text='Recognized speech will appear here', readonly=True, multiline=True, height=200)
        layout.add_widget(self.text_input)

        self.listen_button = Button(text='Start Listening', on_press=self.start_listening)
        layout.add_widget(self.listen_button)

        return layout

    def start_listening(self, instance):
        try:
            with sr.Microphone() as mic:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio)
                self.text_input.text = text
        except sr.UnknownValueError:
            self.text_input.text = "Sorry, I could not understand what you said. Please try again."
        except sr.RequestError as e:
            self.text_input.text = f"Error connecting to the speech recognition service; {e}"

if __name__ == '__main__':
    SpeechToTextApp().run()

