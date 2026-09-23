"""
CET CHILE - Sistema de Asistencia
screens/historial_llegadas.py - Pantalla 4: Historial de llegadas del estudiante
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_BLANCO, COLOR_BORDE, COLOR_VERDE
)

# Datos de ejemplo (luego vendrán de una base de datos real)
HISTORIAL_EJEMPLO = [
    {"fecha": "22/09/2026", "hora": "08:30", "estado": "Atraso"},
    {"fecha": "21/09/2026", "hora": "07:58", "estado": "A tiempo"},
    {"fecha": "18/09/2026", "hora": "08:02", "estado": "A tiempo"},
    {"fecha": "17/09/2026", "hora": "08:41", "estado": "Atraso"},
    {"fecha": "16/09/2026", "hora": "07:55", "estado": "A tiempo"},
]


class HistorialLlegadasScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, nombre_estudiante="Estudiante",
                 origen="bienvenida", **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller
        self.nombre_estudiante = nombre_estudiante
        # "origen" nos dice a qué pantalla volver con la flecha ←
        self.origen = origen

        self._build_header()
        self._build_body()
        self._build_footer()

    # ---------- ENCABEZADO ----------
    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color=COLOR_AZUL_OSCURO, height=60, corner_radius=0)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        cet_label = ctk.CTkLabel(
            header, text="CET CHILE",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_BLANCO
        )
        cet_label.place(relx=0.05, rely=0.5, anchor="w")

    # ---------- CUERPO ----------
    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=COLOR_FONDO, corner_radius=0)
        body.pack(fill="both", expand=True, padx=40, pady=20)

        top_row = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        top_row.pack(fill="x", pady=(10, 20))

        back_btn = ctk.CTkButton(
            top_row, text="←", width=36, height=36, corner_radius=18,
            fg_color=COLOR_FONDO, hover_color="#E5E5E5",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.on_volver
        )
        back_btn.pack(side="left")

        titulo = ctk.CTkLabel(
            top_row, text="Historial de llegadas",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(side="left", padx=(10, 0))

        # Tabla
        tabla_card = ctk.CTkFrame(
            body, fg_color=COLOR_BLANCO, corner_radius=10,
            border_width=1, border_color=COLOR_BORDE
        )
        tabla_card.pack(fill="both", expand=True)

        # Encabezados de columna
        header_row = ctk.CTkFrame(tabla_card, fg_color=COLOR_BLANCO)
        header_row.pack(fill="x", padx=20, pady=(15, 5))

        ctk.CTkLabel(header_row, text="Fecha", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=140, anchor="w").pack(side="left")
        ctk.CTkLabel(header_row, text="Hora", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=140, anchor="w").pack(side="left")
        ctk.CTkLabel(header_row, text="Estado", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=120, anchor="w").pack(side="left")

        separador = ctk.CTkFrame(tabla_card, fg_color=COLOR_BORDE, height=1)
        separador.pack(fill="x", padx=20)

        # Filas de datos
        for registro in HISTORIAL_EJEMPLO:
            self._fila(tabla_card, registro["fecha"], registro["hora"], registro["estado"])

    def _fila(self, parent, fecha, hora, estado):
        row = ctk.CTkFrame(parent, fg_color=COLOR_BLANCO)
        row.pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(row, text=fecha, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=140, anchor="w").pack(side="left")
        ctk.CTkLabel(row, text=hora, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=140, anchor="w").pack(side="left")

        color_badge = COLOR_AMARILLO if estado == "Atraso" else COLOR_VERDE
        texto_color = COLOR_AZUL_OSCURO if estado == "Atraso" else COLOR_BLANCO

        badge = ctk.CTkLabel(
            row, text=estado, font=ctk.CTkFont(size=11, weight="bold"),
            text_color=texto_color, fg_color=color_badge,
            corner_radius=6, width=80, height=24
        )
        badge.pack(side="left")

    # ---------- PIE DE PÁGINA ----------
    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color=COLOR_FONDO, height=60, corner_radius=0)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        cet_label = ctk.CTkLabel(
            footer, text="CET CHILE",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        cet_label.pack(pady=(12, 0))

        under_line = ctk.CTkFrame(footer, fg_color=COLOR_AMARILLO, height=2, width=90)
        under_line.pack()

    # ---------- ACCIONES ----------
    def on_volver(self):
        if self.origen == "asistencia_registrada":
            from screens.asistencia_registrada import AsistenciaRegistradaScreen
            self.controller.mostrar_pantalla(
                AsistenciaRegistradaScreen,
                nombre_estudiante=self.nombre_estudiante,
                hora_llegada="08:30",
                estado="ATRASO"
            )
        else:
            from screens.bienvenida import BienvenidaScreen
            self.controller.mostrar_pantalla(BienvenidaScreen, nombre_estudiante=self.nombre_estudiante)