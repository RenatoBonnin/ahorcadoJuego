import Ahorcado as Ah
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock

Ah.ejecutarArchivo()
listaPalabras = Ah.leerArchivo()    

class botonSalirConfigMenu(Button):
    def __init__(self, input = Label(), **kwargs):
        super().__init__(**kwargs)
        self.input = input
        self.text = "VOLVER"

    def on_press(self):
        self.input.text = ""
        self.parent.parent.manager.current = "ConfigMenu"

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
        sm.add_widget(EliminarScreen(name = "Eliminar"))

        self.add_widget(sm)

class ConfigMenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.lay = BoxLayout(orientation = "vertical")

        botonListar = Button(text = "LISTAR PALABRAS")
        botonAgregar = Button(text = "AGREGAR PALABRAS")
        self.botonEliminar = Button(text = "ELIMINAR PALABRAS")
        botonSalir = Button(text = "VOLVER AL MENU")

        botonListar.bind(on_press = self.irAListar)
        botonAgregar.bind(on_press = self.irAAgregar)
        self.botonEliminar.bind(on_press = self.irAEliminar)
        botonSalir.bind(on_press = self.salir)

        self.lay.add_widget(botonListar)
        self.lay.add_widget(botonAgregar)
        if listaPalabras:
            self.lay.add_widget(self.botonEliminar)
        self.lay.add_widget(botonSalir)

        self.add_widget(self.lay)
    
    def irAListar(self, instance):
        if listaPalabras:
            self.manager.current = "Listar"
        else:
            error(self, "No hay palabras para listar")

    def irAAgregar(self, instance):
        self.manager.current = "Agregar"

    def irAEliminar(self, instance):
        self.manager.current = "Eliminar" 
    
    def salir(self, instance):
        Ah.modificarArchivo(listaPalabras)
        self.manager.parent.manager.current = "Menu"

    def on_pre_enter(self, *args):
        if listaPalabras:
            if self.botonEliminar not in self.lay.children:
                self.lay.add_widget(self.botonEliminar, index = 1)
        else:
            if self.botonEliminar in self.lay.children:
                self.lay.remove_widget(self.botonEliminar)

class ListarScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Poner popup para cuando no hay palabras en la lista

        lay = BoxLayout(orientation = "vertical")
        
        self.palabras = Label(text = "")

        lay.add_widget(self.palabras)
        lay.add_widget(botonSalirConfigMenu())

        self.add_widget(lay)

    def volver(self, instance):
        self.manager.current = "ConfigMenu"

    def actualizarLista(self):
        self.palabras.text = Ah.listarPalabrasUI(listaPalabras)

    def on_pre_enter(self, *args):
        self.actualizarLista()

class AgregarScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        lay = BoxLayout(orientation = "vertical")

        self.palabraNueva = TextInput(hint_text = "INGRESE UNA NUEVA PALABRA", multiline = False)

        self.palabraNueva.bind(on_text_validate = self.on_enterApretado)

        self.palabras = Label(text = "")

        lay.add_widget(self.palabras)
        lay.add_widget(self.palabraNueva)
        lay.add_widget(botonSalirConfigMenu(self.palabraNueva))

        self.add_widget(lay)

    def on_enterApretado(self, *args):
        (resultado, alfa, repe) = Ah.agregarPalabraUI(listaPalabras, self.palabraNueva.text)
        if resultado:
            self.actualizarLista()
            self.palabraNueva.text = ""
        elif alfa:
            error(self, "Solo se pueden agregar palabras con letras.", self.palabraNueva)
        elif repe:
            error(self, "Esta palabra ya está agregada. No se pueden agregar palabras repetidas", self.palabraNueva)
        Clock.schedule_once(self.refocus, 0)

    def actualizarLista(self):
        self.palabras.text = Ah.listarPalabrasUI(listaPalabras)

    def on_pre_enter(self, *args):
        self.actualizarLista()

    def refocus(self, dt):
        self.palabraNueva.focus = True

class EliminarScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        lay = BoxLayout(orientation = "vertical")

        self.palabraEliminar = TextInput(hint_text = "INGRESE UNA PALABRA A ELIMINAR", multiline = False)

        self.palabraEliminar.bind(on_text_validate = self.on_enterApretado)

        self.palabras = Label(text = "")

        lay.add_widget(self.palabras)
        lay.add_widget(self.palabraEliminar)
        lay.add_widget(botonSalirConfigMenu(self.palabraEliminar))

        self.add_widget(lay)

    def on_enterApretado(self, *args):
        resultado = Ah.eliminarPalabraUI(listaPalabras, self.palabraEliminar.text)
        if resultado:
            self.actualizarLista()
            self.palabraEliminar.text = ""
            if not listaPalabras:
                self.manager.current = "ConfigMenu"
        elif len(self.palabraEliminar.text) > 1:
            error(self, "No se pudo eliminar la palabra ya que\nno se encontro en la lista.", self.palabraEliminar)
        Clock.schedule_once(self.refocus, 0)

    def actualizarLista(self):
        self.palabras.text = Ah.listarPalabrasUI(listaPalabras)

    def on_pre_enter(self, *args):
        self.actualizarLista()

    def refocus(self, dt):
        self.palabraEliminar.focus = True

class AhorcadoApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name = "Menu"))
        sm.add_widget(JuegoScreen(name = "Juego"))
        sm.add_widget(ConfigScreen(name = "Configuracion"))

        return sm

def error(self, mensaje, input = Label()):

    popup = Popup(title="Error",
                  content=Label(text=mensaje),
                  size_hint=(0.6, 0.4))
    popup.input = input

    popup.input.disabled = True

    popup.bind(on_dismiss=reactivar_input)
    popup.open()

def reactivar_input(self):
    self.input.disabled = False
    self.input.focus = True

app = AhorcadoApp()
app.run()