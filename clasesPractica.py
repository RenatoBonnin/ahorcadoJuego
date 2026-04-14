from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class Mas1Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        layout = BoxLayout(orientation = "vertical")
        
        self.contador = Contador()

        botonMas1 = Button(text = "+1")
        botonMas1.bind(on_press = self.sumar1)

        botonIr = Button(text = "IR")
        botonIr.bind(on_press = self.ir)

        layout.add_widget(botonMas1)
        layout.add_widget(self.contador)
        layout.add_widget(botonIr)

        self.add_widget(layout)

    def sumar1(self, instance):
        app = App.get_running_app()
        app.contador.cont += 1
        self.contador.text = str(app.contador.text)

    def ir(self, instance):
        self.manager.current = "Restar"
        

class Menos1Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout(orientation = "vertical")

        self.contador = Contador()

        botonMenos1 = Button(text = "-1")
        botonMenos1.bind(on_press = self.restar1)
        
        botonIr = Button(text = "IR")
        botonIr.bind(on_press = self.ir)

        layout.add_widget(botonMenos1)
        layout.add_widget(self.contador)
        layout.add_widget(botonIr)

        self.add_widget(layout)

    def restar1(self, instance):
        app = App.get_running_app()
        app.contador.cont -= 1
        self.contador.text = str(app.contador.text)

    def ir(self, instance):
        self.manager.current = "Sumar"

class Contador(Label):
    cont = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = str(self.cont)

    def on_cont(self, instance, value):
        self.text = str(value)

class MiApp(App):

    contador = Contador()

    def build(self):

        sm = ScreenManager()

        sm.add_widget(Mas1Screen(name = "Sumar"))
        sm.add_widget(Menos1Screen(name = "Restar"))

        return sm

MiApp().run()