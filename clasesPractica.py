from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

def popup_confirmar(mensaje, on_confirmar):
    layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

    texto = Label(text=mensaje)

    botones = BoxLayout(size_hint_y=0.4, spacing=10)

    btn_si = Button(text="Sí")
    btn_no = Button(text="No")

    botones.add_widget(btn_si)
    botones.add_widget(btn_no)

    layout.add_widget(texto)
    layout.add_widget(botones)

    popup = Popup(
        title="Confirmación",
        content=layout,
        size_hint=(0.6, 0.4),
        auto_dismiss=False
    )

    btn_si.bind(on_press=lambda x: confirmar(popup, on_confirmar))
    btn_no.bind(on_press=popup.dismiss)

    popup.open()



popup_confirmar("", Button())

def confirmar(popup, accion):
    accion()
    popup.dismiss()