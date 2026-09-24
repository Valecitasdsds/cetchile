"""
CET CHILE - Sistema de Asistencia
screens/configuracion_qr.py - Configuración QR (activar/desactivar y regenerar código)
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO,
    COLOR_BORDE, COLOR_VERDE
)

# Estado "global" simulado (en un futuro esto vendría de una base de datos real)
CONFIGURACION_QR = {
    "activo": True,
    "codigo_actual": "CET-QR-A83F21",
}


class ConfiguracionQRScreen(ctk.CTkFrame):
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
            top_row, text="Configuración QR",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        titulo.pack(side="left", padx=(10, 0))

        contenido = ctk.CTkFrame(body, fg_color=COLOR_FONDO, width=500)
        contenido.pack(fill="x")

        # ---- Tarjeta: activar / desactivar ----
        switch_card = ctk.CTkFrame(
            contenido, fg_color=COLOR_BLANCO, corner_radius=12,
            border_width=1, border_color=COLOR_BORDE
        )
        switch_card.pack(fill="x", pady=(0, 15))

        switch_row = ctk.CTkFrame(switch_card, fg_color=COLOR_BLANCO)
        switch_row.pack(fill="x", padx=20, pady=18)

        text_col = ctk.CTkFrame(switch_row, fg_color=COLOR_BLANCO)
        text_col.pack(side="left")

        ctk.CTkLabel(
            text_col, text="Inicio de sesión por código QR",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_AZUL_OSCURO, anchor="w"
        ).pack(anchor="w")

        self.estado_texto = ctk.CTkLabel(
            text_col, text="", font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w"
        )
        self.estado_texto.pack(anchor="w", pady=(2, 0))

        self.switch_var = ctk.BooleanVar(value=CONFIGURACION_QR["activo"])
        self.switch = ctk.CTkSwitch(
            switch_row, text="", variable=self.switch_var,
            onvalue=True, offvalue=False,
            progress_color=COLOR_VERDE,
            command=self.on_toggle_qr
        )
        self.switch.pack(side="right")

        self._actualizar_estado_texto()

        # ---- Tarjeta: código actual ----
        codigo_card = ctk.CTkFrame(
            contenido, fg_color=COLOR_BLANCO, corner_radius=12,
            border_width=1, border_color=COLOR_BORDE
        )
        codigo_card.pack(fill="x", pady=(0, 15))

        codigo_inner = ctk.CTkFrame(codigo_card, fg_color=COLOR_BLANCO)
        codigo_inner.pack(fill="x", padx=20, pady=18)

        ctk.CTkLabel(
            codigo_inner, text="Código QR institucional actual",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_AZUL_OSCURO, anchor="w"
        ).pack(anchor="w")

        self.codigo_label = ctk.CTkLabel(
            codigo_inner, text=CONFIGURACION_QR["codigo_actual"],
            font=ctk.CTkFont(size=13), text_color=COLOR_TEXTO_GRIS,
            anchor="w"
        )
        self.codigo_label.pack(anchor="w", pady=(4, 12))

        self.regenerar_btn = ctk.CTkButton(
            codigo_inner, text="🔄  REGENERAR CÓDIGO",
            width=220, height=42, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO, font=ctk.CTkFont(size=12, weight="bold"),
            command=self.on_regenerar_codigo
        )
        self.regenerar_btn.pack(anchor="w")

        # Mensaje de confirmación (aparece al regenerar)
        self.mensaje_label = ctk.CTkLabel(
            contenido, text="", font=ctk.CTkFont(size=12),
            text_color=COLOR_VERDE
        )
        self.mensaje_label.pack(anchor="w")

        self._actualizar_estado_boton_regenerar()

    def _actualizar_estado_texto(self):
        if self.switch_var.get():
            self.estado_texto.configure(text="Activo — los estudiantes pueden ingresar con QR")
        else:
            self.estado_texto.configure(text="Desactivado — los estudiantes no podrán usar QR para ingresar")

    def _actualizar_estado_boton_regenerar(self):
        # Si el QR está desactivado, no tiene sentido regenerar el código
        if self.switch_var.get():
            self.regenerar_btn.configure(state="normal")
        else:
            self.regenerar_btn.configure(state="disabled")

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
    def on_toggle_qr(self):
        CONFIGURACION_QR["activo"] = self.switch_var.get()
        self._actualizar_estado_texto()
        self._actualizar_estado_boton_regenerar()
        self.mensaje_label.configure(text="")

    def on_regenerar_codigo(self):
        import random
        import string
        nuevo_codigo = "CET-QR-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        CONFIGURACION_QR["codigo_actual"] = nuevo_codigo
        self.codigo_label.configure(text=nuevo_codigo)
        self.mensaje_label.configure(text="✓ Código regenerado correctamente")

    def on_volver(self):
        from screens.admin_panel import AdminPanelScreen
        self.controller.mostrar_pantalla(AdminPanelScreen)