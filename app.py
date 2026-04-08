from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BotonContador(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contador = 0
        self.text = "Clicks: 0"
        self.bind(on_press=self.incrementar)

    def incrementar(self, instance):
            self.contador += 1
            self.text = f"Clicks: {self.contador}"

class MiApp(App):
    def build(self):
        layout = BoxLayout()

        # Creamos varios objetos de la misma clase
        boton1 = BotonContador()
        boton2 = BotonContador()
        boton3 = BotonContador()

        layout.add_widget(boton1)
        layout.add_widget(boton2)
        layout.add_widget(boton3)

        return layout

MiApp().run()