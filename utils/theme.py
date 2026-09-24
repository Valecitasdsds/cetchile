"""
CET CHILE - Sistema de Asistencia
Tema compartido: colores y estilos usados en todas las pantallas
"""

import customtkinter as ctk

# ---------- CONFIGURACIÓN GENERAL DE LA APP ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ---------- PALETA DE COLORES ----------
COLOR_AZUL_OSCURO = "#0F1E33"
COLOR_AMARILLO = "#F4D93E"
COLOR_FONDO = "#F5F7FA"
COLOR_TEXTO_GRIS = "#4A4A4A"
COLOR_TEXTO_GRIS_CLARO = "#8A8A8A"
COLOR_BLANCO = "#FFFFFF"
COLOR_BORDE = "#DDDDDD"
COLOR_VERDE = "#2FA84F"   # para estados "A tiempo"
COLOR_ROJO = "#D9534F"    # para errores

# ---------- FUENTES ----------
def font_titulo(size=22):
    return ctk.CTkFont(size=size, weight="bold")

def font_subtitulo(size=13):
    return ctk.CTkFont(size=size)

def font_boton(size=14):
    return ctk.CTkFont(size=size, weight="bold")

# ---------- TAMAÑO DE VENTANA (se usa en main.py) ----------
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720