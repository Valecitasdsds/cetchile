"""
CET CHILE - Sistema de Asistencia
screens/bienvenida.py - Pantalla 2: Bienvenida del estudiante
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO, COLOR_BORDE
)


class BienvenidaScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, nombre_estudiante="Estudiante", ultimo_acceso="08:30", **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller
        self.nombre_estudiante = nombre_estudiante
        self.ultimo_acceso = ultimo_acceso

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
        body.pack(fill="both", expand=True)

        top_row = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        top_row.pack(fill="x", padx=40, pady=(30, 0))

        back_btn = ctk.CTkButton(
            top_row, text="←", width=36, height=36, corner_radius=18,
            fg_color=COLOR_FONDO, hover_color="#E5E5E5",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.on_volver
        )
        back_btn.pack(side="left")

        titulo = ctk.CTkLabel(
            body, text=f"¡Bienvenido/a, {self.nombre_estudiante}!",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(pady=(15, 0))

        subtitulo = ctk.CTkLabel(
            body, text="Que tengas un gran día ☀️",
            font=ctk.CTkFont(size=13),
            text_color=COLOR_TEXTO_GRIS
        )
        subtitulo.pack(pady=(2, 30))

        marcar_btn = ctk.CTkButton(
            body, text="🗓  MARCAR ASISTENCIA",
            width=420, height=55, corner_radius=10,
            fg_color=COLOR_AMARILLO, hover_color="#E6C82F",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.on_marcar_asistencia
        )
        marcar_btn.pack(pady=(0, 15))

        historial_btn = ctk.CTkButton(
            body, text="🕒  HISTORIAL DE LLEGADAS",
            width=420, height=55, corner_radius=10,
            fg_color=COLOR_BLANCO, hover_color="#EDEDED",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=14, weight="bold"),
            border_width=1, border_color=COLOR_BORDE,
            command=self.on_historial
        )
        historial_btn.pack(pady=(0, 15))

        acceso_label = ctk.CTkLabel(
            body, text=f"Último acceso: {self.ultimo_acceso}",
            font=ctk.CTkFont(size=11),
            text_color=COLOR_TEXTO_GRIS_CLARO
        )
        acceso_label.pack(pady=(5, 0))

    # ---------- PIE DE PÁGINA ----------
    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color=COLOR_FONDO, height=70, corner_radius=0)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        cet_label = ctk.CTkLabel(
            footer, text="CET CHILE",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        cet_label.pack(pady=(15, 0))

        under_line = ctk.CTkFrame(footer, fg_color=COLOR_AMARILLO, height=2, width=90)
        under_line.pack()

    # ---------- ACCIONES ----------
    def on_volver(self):
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)

    def on_marcar_asistencia(self):
        from screens.asistencia_registrada import AsistenciaRegistradaScreen
        self.controller.mostrar_pantalla(
            AsistenciaRegistradaScreen,
            nombre_estudiante=self.nombre_estudiante,
            hora_llegada="08:30",
            estado="ATRASO"
        )

    def on_historial(self):
        from screens.historial_llegadas import HistorialLlegadasScreen
        self.controller.mostrar_pantalla(
            HistorialLlegadasScreen,
            nombre_estudiante=self.nombre_estudiante,
            origen="bienvenida"
        )