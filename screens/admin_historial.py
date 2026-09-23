"""
CET CHILE - Sistema de Asistencia
screens/admin_historial.py - Pantalla 7: Historial de llegadas (vista administrador)
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_BLANCO, COLOR_BORDE, COLOR_VERDE
)

# Datos de ejemplo (luego vendrán de una base de datos real)
HISTORIAL_ADMIN_EJEMPLO = [
    {"estudiante": "Catalina Cortes", "hora": "08:30", "estado": "Atraso"},
    {"estudiante": "Pedro González", "hora": "07:54", "estado": "A tiempo"},
    {"estudiante": "Ana Pérez", "hora": "08:17", "estado": "Atraso"},
    {"estudiante": "Matías Rojas", "hora": "09:03", "estado": "A tiempo"},
]


class AdminHistorialScreen(ctk.CTkFrame):
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
        top_row.pack(fill="x", pady=(10, 15))

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

        # Fila de filtros: buscador + fecha
        filtros_row1 = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        filtros_row1.pack(fill="x", pady=(0, 8))

        self.buscar_entry = ctk.CTkEntry(
            filtros_row1, width=260, height=36, corner_radius=8,
            placeholder_text="🔍  Buscar estudiante...",
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.buscar_entry.pack(side="left")

        self.fecha_entry = ctk.CTkEntry(
            filtros_row1, width=140, height=36, corner_radius=8,
            placeholder_text="📅 Fecha",
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.fecha_entry.pack(side="right")

        # Fila de filtros: estado + curso
        filtros_row2 = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        filtros_row2.pack(fill="x", pady=(0, 15))

        self.estado_filtro = ctk.CTkOptionMenu(
            filtros_row2, width=190, height=34, corner_radius=8,
            values=["Todos los estados", "Atraso", "A tiempo"],
            fg_color=COLOR_BLANCO, button_color=COLOR_BORDE,
            button_hover_color="#CCCCCC", text_color=COLOR_AZUL_OSCURO,
            dropdown_fg_color=COLOR_BLANCO
        )
        self.estado_filtro.pack(side="left")

        self.curso_filtro = ctk.CTkOptionMenu(
            filtros_row2, width=190, height=34, corner_radius=8,
            values=["Todos los cursos"],
            fg_color=COLOR_BLANCO, button_color=COLOR_BORDE,
            button_hover_color="#CCCCCC", text_color=COLOR_AZUL_OSCURO,
            dropdown_fg_color=COLOR_BLANCO
        )
        self.curso_filtro.pack(side="left", padx=(10, 0))

        # Tabla
        tabla_card = ctk.CTkFrame(
            body, fg_color=COLOR_BLANCO, corner_radius=10,
            border_width=1, border_color=COLOR_BORDE
        )
        tabla_card.pack(fill="both", expand=True)

        header_row = ctk.CTkFrame(tabla_card, fg_color=COLOR_BLANCO)
        header_row.pack(fill="x", padx=20, pady=(15, 5))

        ctk.CTkLabel(header_row, text="Estudiante", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=220, anchor="w").pack(side="left")
        ctk.CTkLabel(header_row, text="Hora", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=120, anchor="w").pack(side="left")
        ctk.CTkLabel(header_row, text="Estado", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=100, anchor="w").pack(side="left")

        separador = ctk.CTkFrame(tabla_card, fg_color=COLOR_BORDE, height=1)
        separador.pack(fill="x", padx=20)

        for registro in HISTORIAL_ADMIN_EJEMPLO:
            self._fila(tabla_card, registro["estudiante"], registro["hora"], registro["estado"])

    def _fila(self, parent, estudiante, hora, estado):
        row = ctk.CTkFrame(parent, fg_color=COLOR_BLANCO)
        row.pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(row, text=estudiante, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=220, anchor="w").pack(side="left")
        ctk.CTkLabel(row, text=hora, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=120, anchor="w").pack(side="left")

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
        from screens.admin_panel import AdminPanelScreen
        self.controller.mostrar_pantalla(AdminPanelScreen)