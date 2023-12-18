from googletrans import Translator

class POTARA:
    def translate(self, text, target_language='pt'):
        self.translator = Translator()
        self.translation = self.translator.translate(text, dest=target_language)
        self.text = self.translation.text
        print(f"Translated text: {self.text}\n")
        return self.text