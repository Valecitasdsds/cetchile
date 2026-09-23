"""
CET CHILE - Sistema de Asistencia
screens/admin_panel.py - Pantalla 6: Panel de administrador
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO, COLOR_BORDE
)


class AdminPanelScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller

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
        top_row.pack(fill="x", pady=(10, 25))

        back_btn = ctk.CTkButton(
            top_row, text="←", width=36, height=36, corner_radius=18,
            fg_color=COLOR_FONDO, hover_color="#E5E5E5",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.on_volver
        )
        back_btn.pack(side="left")

        titulo = ctk.CTkLabel(
            top_row, text="Panel de administrador",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(side="left", padx=(10, 0))

        # Opciones del menú
        self._menu_option(
            body, icono="🕒", titulo="Historial de llegadas",
            descripcion="Revisar asistencias y atrasos",
            command=self.on_historial
        )
        self._menu_option(
            body, icono="⚏", titulo="Configuración QR",
            descripcion="Activar o desactivar QR",
            command=self.on_configuracion_qr
        )
        self._menu_option(
            body, icono="👤", titulo="Nuevo estudiante",
            descripcion="Registrar un estudiante",
            command=self.on_nuevo_estudiante
        )

    def _menu_option(self, parent, icono, titulo, descripcion, command):
        card = ctk.CTkFrame(
            parent,
            fg_color=COLOR_BLANCO,
            border_width=1, border_color=COLOR_BORDE,
            corner_radius=12, height=78
        )
        card.pack(fill="x", pady=10)
        card.pack_propagate(False)

        content = ctk.CTkFrame(card, fg_color=COLOR_BLANCO)
        content.place(relx=0.04, rely=0.5, anchor="w")

        icon_circle = ctk.CTkLabel(
            content, text=icono, font=ctk.CTkFont(size=20),
            text_color=COLOR_AZUL_OSCURO,
            fg_color="#EFF2F6", corner_radius=22,
            width=44, height=44
        )
        icon_circle.pack(side="left", padx=(0, 16))

        text_col = ctk.CTkFrame(content, fg_color=COLOR_BLANCO)
        text_col.pack(side="left")

        ctk.CTkLabel(text_col, text=titulo, font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=COLOR_AZUL_OSCURO, anchor="w",
                     fg_color=COLOR_BLANCO).pack(anchor="w")
        ctk.CTkLabel(text_col, text=descripcion, font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w",
                     fg_color=COLOR_BLANCO).pack(anchor="w", pady=(2, 0))

        arrow = ctk.CTkLabel(card, text="›", font=ctk.CTkFont(size=24, weight="bold"),
                              text_color=COLOR_TEXTO_GRIS_CLARO, fg_color=COLOR_BLANCO)
        arrow.place(relx=0.95, rely=0.5, anchor="e")

        # Hacemos clicleable toda la tarjeta (frame, ícono, textos y flecha)
        clickable_widgets = [card, content, icon_circle, text_col, arrow] + text_col.winfo_children()
        for widget in clickable_widgets:
            widget.bind("<Button-1>", lambda e: command())
            widget.configure(cursor="hand2")
        # Efecto hover simple: cambia el color de fondo al pasar el mouse
        def on_enter(e):
            card.configure(fg_color="#F5F7FA")
            for w in [content, icon_circle, text_col] + text_col.winfo_children():
                if w is not icon_circle:
                    w.configure(fg_color="#F5F7FA")

        def on_leave(e):
            card.configure(fg_color=COLOR_BLANCO)
            for w in [content, icon_circle, text_col] + text_col.winfo_children():
                if w is not icon_circle:
                    w.configure(fg_color=COLOR_BLANCO)

        for widget in clickable_widgets:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

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
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)

    def on_historial(self):
        from screens.admin_historial import AdminHistorialScreen
        self.controller.mostrar_pantalla(AdminHistorialScreen)

    def on_configuracion_qr(self):
        print("Configuración QR -> pendiente (no estaba en las imágenes compartidas)")

    def on_nuevo_estudiante(self):
        from screens.nuevo_estudiante import NuevoEstudianteScreen
        self.controller.mostrar_pantalla(NuevoEstudianteScreen)