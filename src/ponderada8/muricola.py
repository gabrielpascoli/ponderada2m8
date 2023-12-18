from murilo import MURILO
from potara import POTARA
from nicola import NICOLA
import sys
import os

class EpicTranslator:
    def __init__(self):
        print("\nInitializing EpicTranslator...\n")
        self.audio_path = sys.argv[1]
        self.murilo = MURILO()
        self.super_translator = POTARA()
        self.nicola = NICOLA()
        self.audio = "speech.mp3"
        
        if len(sys.argv) != 2:
            print("Usage: python muricola.py <audio_path>")
            sys.exit(1)

        if not os.path.exists(self.audio_path):
            print("Audio path does not exist.")
            sys.exit(1)

        if not self.audio_path.endswith(".wav"):
            print("Converting audio to a compatible format...")
            self.audio_path = self.murilo.process_audio(self.audio_path)

    def start(self):
        text = self.murilo.speech_to_text(self.audio_path)
        text = self.super_translator.translate(text)
        self.audio = self.nicola.text_to_speech(text)
    
    def  play(self):
        self.nicola.play_audio(self.audio)
