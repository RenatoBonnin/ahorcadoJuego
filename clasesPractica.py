from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Boton(Button):
    def __init__(self, et, cambio, **kwargs):
        super().__init__(**kwargs)
        self.et = et
        self.cambio = cambio
        self.text = cambio

    def on_press(self):
        self.et.text = self.cambio
        
class Etiqueta(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Iniciado"


class MiApp(App):
    def build(self):
       
        lay = BoxLayout()
        et = Etiqueta()
        lay.add_widget(et)
        lay.add_widget(Boton(et, "HOLA"))
        lay.add_widget(Boton(et, "MUNDO"))
        lay.add_widget(Boton(et, "PUTO"))
        return lay


a = MiApp()

a.run()
