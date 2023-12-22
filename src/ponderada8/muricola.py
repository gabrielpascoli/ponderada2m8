from murilo import MURILO
from potara import POTARA
from nicola import NICOLA
import sys
import os

class MURICOLA:
    def init(self):

        self.murilo = MURILO()
        self.potara = POTARA()
        self.nicola = NICOLA()
        self.audio = "speech.mp3"
        self.audio_file = self.murilo.convert(sys.argv[1])

    def supremo(self):
        text = self.murilo.stt(self.audio_file)
        text = self.potara.translate(text)
        self.audio = self.nicola.tts(text)
        self.nicola.play_audio(self.audio)
        
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

if __name__ == "__main__":
    main()