"""
CET CHILE - Sistema de Asistencia
screens/login.py - Pantalla 1: Login - Selección de método de inicio de sesión
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_BLANCO, COLOR_BORDE
)


class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller

        self._build_header()
        self._build_body()
        self._build_footer()

    # ---------- ENCABEZADO ----------
    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color=COLOR_AZUL_OSCURO, height=140, corner_radius=0)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        gear_btn = ctk.CTkButton(
            header, text="⚙", width=36, height=36, corner_radius=18,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            font=ctk.CTkFont(size=18), command=self.on_settings
        )
        gear_btn.place(relx=0.97, rely=0.15, anchor="ne")

        title = ctk.CTkLabel(
            header, text="¡BIENVENIDOS ESTUDIANTES!",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=COLOR_AMARILLO
        )
        title.place(relx=0.05, rely=0.55, anchor="w")

        subtitle = ctk.CTkLabel(
            header, text="CET CHILE - CORPORACIÓN EDUCACIONAL TECNOLÓGICA DE CHILE",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=COLOR_BLANCO
        )
        subtitle.place(relx=0.05, rely=0.78, anchor="w")

    # ---------- CUERPO ----------
    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=COLOR_FONDO, corner_radius=0)
        body.pack(fill="both", expand=True)

        pregunta = ctk.CTkLabel(
            body, text="¿Cómo deseas iniciar sesión?",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        pregunta.pack(pady=(35, 20))

        options_frame = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        options_frame.pack(pady=10)

        self._create_option_card(
            options_frame, icono="📱", texto="CÓDIGO QR",
            command=self.on_codigo_qr
        ).grid(row=0, column=0, padx=15)

        self._create_option_card(
            options_frame, icono="🙂", texto="RECONOCIMIENTO FACIAL",
            command=self.on_reconocimiento_facial
        ).grid(row=0, column=1, padx=15)

    def _create_option_card(self, parent, icono, texto, command):
        card = ctk.CTkButton(
            parent,
            text=f"{icono}\n\n{texto}",
            width=180, height=130,
            corner_radius=12,
            fg_color=COLOR_BLANCO,
            hover_color="#EDEDED",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=13, weight="bold"),
            border_width=1,
            border_color=COLOR_BORDE,
            command=command
        )
        return card

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

        sub = ctk.CTkLabel(
            footer, text="CORPORACIÓN EDUCACIONAL TECNOLÓGICA DE CHILE",
            font=ctk.CTkFont(size=9),
            text_color=COLOR_TEXTO_GRIS
        )
        sub.pack(pady=(2, 0))

    # ---------- ACCIONES ----------
    def on_codigo_qr(self):
        from screens.escaneo_qr import EscaneoQRScreen
        self.controller.mostrar_pantalla(EscaneoQRScreen)

    def on_reconocimiento_facial(self):
        from screens.reconocimiento_facial import ReconocimientoFacialScreen
        self.controller.mostrar_pantalla(ReconocimientoFacialScreen)

    def on_settings(self):
        from screens.admin_login import AdminLoginScreen
        self.controller.mostrar_pantalla(AdminLoginScreen)