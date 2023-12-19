from murilo import MURILO
from potara import POTARA
from nicola import NICOLA
import sys
import os

class MURICOLA:
    def _init_(self):
        self.audio_file = sys.argv[1]
        self.murilo = MURILO()
        self.potara = POTARA()
        self.nicola = NICOLA()
        self.audio = "speech.mp3"
        
        if len(sys.argv) != 2 or not os.path.exists(self.audio_file) or not self.audio_file.endswith(".wav"):
            print("ERROR: Invalid arguments.")
            sys.exit(1)

    def supremo(self):
        text = self.murilo.stt(self.audio_file)
        text = self.potara.translate(text)
        self.audio = self.nicola.tts(text)
        self.nicola.play_audio(self.audio)

def main():
    muricola = MURICOLA()
    muricola.supremo()

if _name_ == "_main_":
    main()