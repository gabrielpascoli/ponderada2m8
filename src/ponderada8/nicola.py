from gtts import gTTS
from pygame import mixer

class NICOLA:
    def tts(self, text, language='pt-br', file="speech.mp3"):
        gtts = gTTS(text, lang=language)
        gtts.save(file)
        return file

    def play_audio(self, audio_file):
        mixer.init()
        mixer.music.load(audio_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        mixer.quit()
