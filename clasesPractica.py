from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class boton(Button):
    def __init__(self, nro, **kwargs):
        super().__init__(**kwargs)
        self.text = f"BOTON :{nro}"
        self.background_color = (1, 0, 0, 1)
        self.background_normal = ""
        self.estado = False

    def on_press(self):
        if self.estado:
            self.estado = False
            self.background_color = (1, 0, 0, 1)
            self.bt1.disabled = False
            self.bt2.disabled = False
        else:
            self.estado = True
            self.background_color = (0, 0.5, 0, 1)
            self.bt1.disabled = True
            self.bt2.disabled = True

class MiApp(App):
    def build(self):
       
        lay = BoxLayout()

        bt1 = boton(1)
        bt2 = boton(2)
        bt3 = boton(3)

        bt1.bt1, bt1.bt2 = bt2, bt3
        bt2.bt1, bt2.bt2 = bt1, bt3
        bt3.bt1, bt3.bt2 = bt1, bt2

        lay.add_widget(bt1)
        lay.add_widget(bt2)
        lay.add_widget(bt3)

        return lay

a = MiApp()
a.run()
