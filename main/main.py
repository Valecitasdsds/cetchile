"""
CET CHILE - Sistema de Asistencia
main.py - Punto de entrada. Controla la navegación entre pantallas.
"""

import customtkinter as ctk
import sys
import os

# Permite importar desde las carpetas screens/ y utils/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.theme import ANCHO_VENTANA, ALTO_VENTANA, COLOR_FONDO
from screens.login import LoginScreen


class CetChileApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CET CHILE - Sistema de Asistencia")
        self.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.resizable(False, False)
        self.configure(fg_color=COLOR_FONDO)

        # Contenedor donde van a vivir todas las pantallas (una encima de otra)
        self.container = ctk.CTkFrame(self, fg_color=COLOR_FONDO)
        self.container.pack(fill="both", expand=True)

        # Diccionario para guardar las pantallas ya creadas
        self.frames = {}

        # Registramos la primera pantalla
        self.mostrar_pantalla(LoginScreen)

    def mostrar_pantalla(self, screen_class, **kwargs):
        """
        Crea (si no existe) y muestra la pantalla indicada.
        screen_class: la clase de la pantalla (ej. LoginScreen)
        kwargs: datos opcionales que la pantalla necesite (ej. nombre del estudiante)
        """
        # Si ya existe una instancia previa, la destruimos para poder pasar datos nuevos
        for frame in self.container.winfo_children():
            frame.destroy()

        frame = screen_class(self.container, controller=self, **kwargs)
        frame.pack(fill="both", expand=True)
        return frame


if __name__ == "__main__":
    app = CetChileApp()
    app.mainloop()