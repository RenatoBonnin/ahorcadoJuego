from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class boton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contador = 0
        self.text = (f"CONTADOR: {self.contador}")

    def on_press(self):
        self.contador += 1
        self.text = (f"CONTADOR: {self.contador}")

class MiApp(App):
    def build(self):
        return boton()
    
MiApp().run()