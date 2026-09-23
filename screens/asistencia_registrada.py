"""
CET CHILE - Sistema de Asistencia
screens/asistencia_registrada.py - Pantalla 3: Confirmación de asistencia registrada
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO,
    COLOR_BORDE, COLOR_VERDE
)


class AsistenciaRegistradaScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, nombre_estudiante="Estudiante",
                 hora_llegada="08:30", estado="ATRASO", **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller
        self.nombre_estudiante = nombre_estudiante
        self.hora_llegada = hora_llegada
        self.estado = estado

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

        back_btn = ctk.CTkButton(
            header, text="←", width=32, height=32, corner_radius=16,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.on_volver
        )
        back_btn.place(relx=0.02, rely=0.5, anchor="w")

    # ---------- CUERPO ----------
    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=COLOR_FONDO, corner_radius=0)
        body.pack(fill="both", expand=True)

        # Ícono de check verde
        check_circle = ctk.CTkLabel(
            body, text="✓",
            width=60, height=60, corner_radius=30,
            fg_color=COLOR_VERDE, text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=28, weight="bold")
        )
        check_circle.pack(pady=(35, 15))

        titulo = ctk.CTkLabel(
            body, text="ASISTENCIA REGISTRADA",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(pady=(0, 25))

        # Tarjeta con los datos
        info_card = ctk.CTkFrame(
            body, fg_color=COLOR_BLANCO, corner_radius=10,
            border_width=1, border_color=COLOR_BORDE, width=420
        )
        info_card.pack(pady=(0, 20))

        self._info_row(info_card, "👤", "Estudiante", self.nombre_estudiante)
        self._info_row(info_card, "🕒", "Hora de llegada", self.hora_llegada)
        self._info_row(info_card, "⚠", "Estado", self.estado, is_badge=True)

        pregunta = ctk.CTkLabel(
            body, text="¿Deseas ver tu historial de llegadas?",
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXTO_GRIS
        )
        pregunta.pack(pady=(5, 15))

        # Botones lado a lado
        btn_row = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        btn_row.pack()

        ver_historial_btn = ctk.CTkButton(
            btn_row, text="VER HISTORIAL",
            width=190, height=45, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.on_ver_historial
        )
        ver_historial_btn.grid(row=0, column=0, padx=8)

        salir_btn = ctk.CTkButton(
            btn_row, text="SALIR",
            width=190, height=45, corner_radius=8,
            fg_color=COLOR_BLANCO, hover_color="#EDEDED",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=13, weight="bold"),
            border_width=1, border_color=COLOR_BORDE,
            command=self.on_salir
        )
        salir_btn.grid(row=0, column=1, padx=8)

    def _info_row(self, parent, icono, label, valor, is_badge=False):
        row = ctk.CTkFrame(parent, fg_color=COLOR_BLANCO)
        row.pack(fill="x", padx=20, pady=8)

        icono_label = ctk.CTkLabel(row, text=icono, font=ctk.CTkFont(size=14), width=20)
        icono_label.pack(side="left")

        label_widget = ctk.CTkLabel(
            row, text=label, font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXTO_GRIS_CLARO, width=140, anchor="w"
        )
        label_widget.pack(side="left", padx=(10, 0))

        if is_badge:
            badge = ctk.CTkLabel(
                row, text=valor, font=ctk.CTkFont(size=11, weight="bold"),
                text_color=COLOR_AZUL_OSCURO, fg_color=COLOR_AMARILLO,
                corner_radius=6, width=80, height=24
            )
            badge.pack(side="left")
        else:
            valor_widget = ctk.CTkLabel(
                row, text=valor, font=ctk.CTkFont(size=12, weight="bold"),
                text_color=COLOR_AZUL_OSCURO, anchor="w"
            )
            valor_widget.pack(side="left")

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
        from screens.bienvenida import BienvenidaScreen
        self.controller.mostrar_pantalla(BienvenidaScreen, nombre_estudiante=self.nombre_estudiante)

    def on_ver_historial(self):
        from screens.historial_llegadas import HistorialLlegadasScreen
        self.controller.mostrar_pantalla(
            HistorialLlegadasScreen,
            nombre_estudiante=self.nombre_estudiante,
            origen="asistencia_registrada"
        )

    def on_salir(self):
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)