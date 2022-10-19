import kivy

kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button

from googletrans import Translator


class ButtonApp(App):

    def build(self):
        btn = Button(text="press it",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        return btn

    # callback function tells when button pressed
    def callback(self, event):
        translator = Translator()
        translate = translator.translate('Hier steht der zu übersetzende Eingabetext', lang_tgt="en")
        print(translate.text)


# creating the object root for ButtonApp() class
root = ButtonApp()

if __name__ == "__main__":
    root.run()