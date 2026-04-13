from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# -------- Pantalla 1 (Menú) --------
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout()

        titulo = Label(text="MENÚ")

        btn_ir = Button(text="Ir al contador")
        btn_ir.bind(on_press=self.ir_contador)

        layout.add_widget(titulo)
        layout.add_widget(btn_ir)

        self.add_widget(layout)

    def ir_contador(self, instance):
        self.manager.current = "contador"


# -------- Pantalla 2 (Contador) --------
class ContadorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.contador = 0

        layout = BoxLayout(orientation='vertical')

        self.label = Label(text=str(self.contador), font_size=40)

        btn_sumar = Button(text="+1")
        btn_sumar.bind(on_press=self.sumar)

        btn_volver = Button(text="Volver al menú")
        btn_volver.bind(on_press=self.volver_menu)

        layout.add_widget(self.label)
        layout.add_widget(btn_sumar)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def sumar(self, instance):
        self.contador += 1
        self.label.text = str(self.contador)

    def volver_menu(self, instance):
        self.manager.current = "menu"


# -------- App principal --------
class MiApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ContadorScreen(name="contador"))

        return sm


if __name__ == "__main__":
    MiApp().run()