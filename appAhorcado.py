import Ahorcado as Ah
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

        sm = ScreenManager()

        sm.add_widget(ConfigMenuScreen(name = "ConfigMenu"))
        sm.add_widget(ListarScreen(name = "Listar"))
        sm.add_widget(AgregarScreen(name = "Agregar"))

        self.add_widget(sm)

class ConfigMenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        lay = BoxLayout(orientation = "vertical")

        self.sm = ScreenManager()

        botonListar = Button(text = "LISTAR PALABRAS")
        botonAgregar = Button(text = "AGREGAR PALABRAS")
        botonEliminar = Button(text = "ELIMINAR PALABRAS")
        botonSalir = Button(text = "VOLVER AL MENU")

        botonListar.bind(on_press = self.irAListar)
        botonAgregar.bind(on_press = self.irAAgregar)
        #BOTON ELIMINAR SI HAY AL MENOS UNA PALABRA
        botonSalir.bind(on_press = self.salir)

        lay.add_widget(botonListar)
        lay.add_widget(botonAgregar)
        lay.add_widget(botonSalir)

        self.add_widget(lay)
    
    def irAListar(self, instance):
        self.manager.current = "Listar"

    def irAAgregar(self, instance):
        self.manager.current = "Agregar"
    
    def salir(self, instance):
        self.manager.parent.manager.current = "Menu"



class AgregarScreen(Screen):
    pass

class ListarScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        lay = BoxLayout(orientation = "vertical")

        botonVolver = Button(text = "VOLVER")
        botonVolver.bind(on_press = self.volver)

        palabras = Label(text = Ah.listarPalabrasUI(listaPalabras))


        lay.add_widget(palabras)
        lay.add_widget(botonVolver)


        self.add_widget(lay)

    def volver(self, instance):
        self.manager.current = "ConfigMenu"

class EliminarScreen(Screen):
    pass


class AhorcadoApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name = "Menu"))
        sm.add_widget(JuegoScreen(name = "Juego"))
        sm.add_widget(ConfigScreen(name = "Configuracion"))

        return sm

Ah.ejecutarArchivo()
listaPalabras = Ah.leerArchivo()

app = AhorcadoApp()
app.run()