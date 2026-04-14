from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        lay = BoxLayout(orientation = "vertical")

        botonJugar = Button(text = "JUGAR")
        botonConfig = Button(text = "CONFIGURACION")
        botonSalir = Button(text = "SALIR")

        botonJugar.bind(on_press = self.irAJugar)
        botonConfig.bind(on_press = self.irAConfig)
        botonSalir.bind(on_press = self.salir)

        lay.add_widget(botonJugar)
        lay.add_widget(botonConfig)
        lay.add_widget(botonSalir)

        self.add_widget(lay)
    
    def irAJugar(self, instance):
        self.manager.current = "Juego"
    def irAConfig(self, instance):
        self.manager.current = "Configuracion"
    def salir(self, instance):
        App.get_running_app().stop()

class JuegoScreen(Screen):
    pass

class ConfigScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        lay = BoxLayout(orientation = "vertical")

        sm = ScreenManager()

        botonListar = Button(text = "LISTAR PALABRAS")
        botonAgregar = Button(text = "AGREGAR PALABRAS")
        botonEliminar = Button(text = "ELIMINAR PALABRAS")
        botonSalir = Button(text = "VOLVER AL MENU")

        botonListar.bind(on_press = self.irAListar)
        botonAgregar.bind(on_press = self.irAAgregar)



        botonSalir.bind(on_press = self.salir)

        lay.add_widget(botonListar)
        lay.add_widget(botonAgregar)
        lay.add_widget(botonSalir)
        
        return lay
    
    def irAListar(self, instance):
        self.manager.current = "Listar"

    def irAAgregar(self, instance):
        self.manager.current = "Agregar"
    
    def salir(self, instance):
        self.manager.current = "Menu"



class AgregarScreen(Screen):
    pass

class ListarScreen(Screen):
    pass

class EliminarScreen(Screen):
    pass


class MiApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name = "Menu"))
        sm.add_widget(JuegoScreen(name = "Juego"))
        sm.add_widget(ConfigScreen(name = "Configuracion"))

        return sm

app = MiApp()
app.run()