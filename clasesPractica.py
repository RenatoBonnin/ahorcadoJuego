from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class SInput(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout(orientation = "vertical")

        titulo = Label(text = "SCREEN INPUT")

        btnirAB = Button(text = "IR A SCREEN B")
        btnirAB.bind(on_press = self.irAB)

        self.input = TextInput(hint_text = "INPUT ACA")

        layout.add_widget(titulo)
        layout.add_widget(self.input)
        layout.add_widget(btnirAB)

        self.add_widget(layout)

    def irAB(self, instance):
        self.manager.current = "SShow"
        
class SShow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout(orientation = "vertical")

        titulo = Label(text = "SCREEN SHOW", color = (0, 1, 0, 1))

        btnirBA = Button(text = "IR A SCREEN A")
        btnirBA.bind(on_press = self.irBA)

        self.label = Label(text = "")

        btnShow = Button(text = "MOSTRAR")
        btnShow.bind(on_press = self.mostrar)

        layout.add_widget(titulo)
        layout.add_widget(self.label)
        layout.add_widget(btnShow)
        layout.add_widget(btnirBA)

        self.add_widget(layout)

    def irBA(self, instance):
        self.manager.current = "SInput"

    def mostrar(self, instance):    
        self.label.text = self.manager.get_screen("SInput").input.text

class MiApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(SInput(name = "SInput"))
        sm.add_widget(SShow(name = "SShow"))

        return sm
    
MiApp().run()