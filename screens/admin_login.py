"""
CET CHILE - Sistema de Asistencia
screens/admin_login.py - Pantalla 5: Acceso Administrador
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO,
    COLOR_BORDE, COLOR_ROJO
)


class AdminLoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller
        self.mostrar_password = False

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

        contenido = ctk.CTkFrame(body, fg_color=COLOR_FONDO, width=420)
        contenido.pack(pady=(40, 0))

        top_row = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        top_row.pack(fill="x", pady=(0, 5))

        back_btn = ctk.CTkButton(
            top_row, text="←", width=36, height=36, corner_radius=18,
            fg_color=COLOR_FONDO, hover_color="#E5E5E5",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.on_volver_inicio
        )
        back_btn.pack(side="left")

        titulo = ctk.CTkLabel(
            contenido, text="Acceso Administrador",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(anchor="w", pady=(5, 2))

        subtitulo = ctk.CTkLabel(
            contenido, text="Inicia sesión con tu cuenta institucional",
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXTO_GRIS
        )
        subtitulo.pack(anchor="w", pady=(0, 25))

        # Campo correo
        ctk.CTkLabel(contenido, text="👤  Correo institucional", font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w").pack(fill="x")
        self.correo_entry = ctk.CTkEntry(
            contenido, width=420, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1,
            text_color=COLOR_AZUL_OSCURO
        )
        self.correo_entry.pack(pady=(5, 18))

        # Campo contraseña
        ctk.CTkLabel(contenido, text="🔒  Contraseña", font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w").pack(fill="x")

        pass_row = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        pass_row.pack(fill="x", pady=(5, 5))

        self.password_entry = ctk.CTkEntry(
            pass_row, width=380, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1,
            text_color=COLOR_AZUL_OSCURO, show="*"
        )
        self.password_entry.pack(side="left")

        self.eye_btn = ctk.CTkButton(
            pass_row, text="👁", width=36, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, hover_color="#EDEDED",
            text_color=COLOR_TEXTO_GRIS,
            border_width=1, border_color=COLOR_BORDE,
            command=self.toggle_password
        )
        self.eye_btn.pack(side="left", padx=(8, 0))

        # Mensaje de error (oculto al inicio)
        self.error_label = ctk.CTkLabel(
            contenido, text="", font=ctk.CTkFont(size=11),
            text_color=COLOR_ROJO
        )
        self.error_label.pack(anchor="w", pady=(5, 0))

        # Botón ingresar
        ingresar_btn = ctk.CTkButton(
            contenido, text="INGRESAR",
            width=420, height=48, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.on_ingresar
        )
        ingresar_btn.pack(pady=(15, 10))

        volver_link = ctk.CTkButton(
            contenido, text="← Volver al inicio",
            width=420, height=25,
            fg_color=COLOR_FONDO, hover_color=COLOR_FONDO,
            text_color=COLOR_TEXTO_GRIS,
            font=ctk.CTkFont(size=12),
            command=self.on_volver_inicio
        )
        volver_link.pack()

    def toggle_password(self):
        self.mostrar_password = not self.mostrar_password
        self.password_entry.configure(show="" if self.mostrar_password else "*")

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
    def on_ingresar(self):
        correo = self.correo_entry.get().strip()
        password = self.password_entry.get().strip()

        # Validación simulada: cualquier correo/contraseña no vacíos funciona por ahora
        if not correo or not password:
            self.error_label.configure(text="Por favor completa ambos campos")
            return

        from screens.admin_panel import AdminPanelScreen
        self.controller.mostrar_pantalla(AdminPanelScreen)

    def on_volver_inicio(self):
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)