from googletrans import Translator

class POTARA:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, target_language='pt'):
        self.translation = self.translator.translate(text, dest=target_language)
        self.translated_text = self.translation.text
        print(f"Translated text: {self.translated_text}\n")
        return self.translated_text
