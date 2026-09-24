"""
CET CHILE - Sistema de Asistencia
screens/escaneo_qr.py - Pantalla intermedia: el tótem escanea el QR del estudiante
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO, COLOR_VERDE
)

# Dato de ejemplo: en el futuro esto vendría de buscar en la base de datos
# al estudiante dueño del código QR que se escaneó
ESTUDIANTE_EJEMPLO = "Catalina Cortes"


class EscaneoQRScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller
        self.reconocido = False

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

        # Contenedor que se redibuja según el estado (esperando / reconocido)
        self.estado_frame = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        self.estado_frame.pack(expand=True)
        self._dibujar_estado()

    def _dibujar_estado(self):
        for widget in self.estado_frame.winfo_children():
            widget.destroy()

        if not self.reconocido:
            ctk.CTkLabel(
                self.estado_frame, text="⬛",
                font=ctk.CTkFont(size=70)
            ).pack(pady=(0, 20))

            ctk.CTkLabel(
                self.estado_frame, text="Escaneando código QR...",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color=COLOR_AZUL_OSCURO
            ).pack()

            ctk.CTkLabel(
                self.estado_frame, text="Acerca tu credencial QR al lector del tótem",
                font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO_GRIS_CLARO
            ).pack(pady=(4, 30))

            # Por ahora, como no hay cámara conectada, este botón simula la lectura
            ctk.CTkButton(
                self.estado_frame, text="ESCANEAR QR",
                width=220, height=48, corner_radius=8,
                fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
                text_color=COLOR_BLANCO, font=ctk.CTkFont(size=13, weight="bold"),
                command=self.on_escanear
            ).pack()
        else:
            ctk.CTkLabel(
                self.estado_frame, text="✓",
                width=70, height=70, corner_radius=35,
                fg_color=COLOR_VERDE, text_color=COLOR_BLANCO,
                font=ctk.CTkFont(size=30, weight="bold")
            ).pack(pady=(0, 20))

            ctk.CTkLabel(
                self.estado_frame, text="Código QR reconocido",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color=COLOR_AZUL_OSCURO
            ).pack()

            ctk.CTkLabel(
                self.estado_frame, text=ESTUDIANTE_EJEMPLO,
                font=ctk.CTkFont(size=13), text_color=COLOR_TEXTO_GRIS
            ).pack(pady=(2, 30))

            ctk.CTkButton(
                self.estado_frame, text="CONTINUAR →",
                width=220, height=48, corner_radius=8,
                fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
                text_color=COLOR_BLANCO, font=ctk.CTkFont(size=13, weight="bold"),
                command=self.on_continuar
            ).pack()

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
    def on_escanear(self):
        # Simulación: en el futuro aquí se conecta la cámara real y la
        # búsqueda del estudiante dueño del código QR escaneado
        self.reconocido = True
        self._dibujar_estado()

    def on_continuar(self):
        from screens.bienvenida import BienvenidaScreen
        self.controller.mostrar_pantalla(BienvenidaScreen, nombre_estudiante=ESTUDIANTE_EJEMPLO)

    def on_volver(self):
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)