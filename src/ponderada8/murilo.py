import speech_recognition as sr
from pydub import AudioSegment

class MURILO:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def stt(self, audio_file, language='en'):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio, language=language)
            print(f"Text: {text}\n")
            return text

    def convert(self, file, converted_format='wav'):
        self.audio = AudioSegment.from_file(file)
        self.converted = file.replace(file.split(".")[-1], converted_format)
        self.converted = "".join(self.converted)
        self.audio.export(self.converted, format=converted_format)
        print(f"File: {self.converted}")
        return self.converted
