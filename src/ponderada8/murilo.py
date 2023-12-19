import speech_recognition as sr

class MURILO():
    def _init_(self):
        self.recognizer = sr.Recognizer()

    def stt(self, audio_file, language='en'):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}\n")
            return text