"""
CET CHILE - Sistema de Asistencia
screens/admin_historial.py - Pantalla 7: Historial de llegadas (vista administrador)
"""

import customtkinter as ctk
import json
import urllib.request
import calendar
from datetime import datetime
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_BLANCO, COLOR_BORDE, COLOR_VERDE
)


def obtener_fecha_chile_web():
    """Obtiene la fecha actual de Chile vía API REST Web."""
    try:
        url = "http://worldtimeapi.org/api/timezone/America/Santiago"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode())
            datetime_str = data["datetime"]
            dt = datetime.fromisoformat(datetime_str)
            return dt.strftime("%d/%m/%Y")
    except Exception:
        return datetime.now().strftime("%d/%m/%Y")


FECHA_ACTUAL_STR = obtener_fecha_chile_web()

HISTORIAL_ADMIN_EJEMPLO = [
    # 4°CPV
    {"estudiante": "Javiera Muñoz", "curso": "4CPV", "fecha": FECHA_ACTUAL_STR, "hora": "08:15", "estado": "Atraso"},
    {"estudiante": "Diego Fuentes", "curso": "4CPV", "fecha": FECHA_ACTUAL_STR, "hora": "07:50", "estado": "A tiempo"},
    {"estudiante": "Camila Soto", "curso": "4CPV", "fecha": FECHA_ACTUAL_STR, "hora": "08:05", "estado": "A tiempo"},
    {"estudiante": "Benjamín Torres", "curso": "4CPV", "fecha": FECHA_ACTUAL_STR, "hora": "08:32", "estado": "Atraso"},

    # 3°CMM
    {"estudiante": "Martina Vidal", "curso": "3CMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:45", "estado": "A tiempo"},
    {"estudiante": "Sebastián Rojas", "curso": "3CMM", "fecha": FECHA_ACTUAL_STR, "hora": "08:20", "estado": "Atraso"},
    {"estudiante": "Florencia Araya", "curso": "3CMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:58", "estado": "A tiempo"},
    {"estudiante": "Ignacio Herrera", "curso": "3CMM", "fecha": FECHA_ACTUAL_STR, "hora": "08:40", "estado": "Atraso"},
    {"estudiante": "Antonia Reyes", "curso": "3CMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:52", "estado": "A tiempo"},

    # 4°DPV
    {"estudiante": "Vicente Castro", "curso": "4DPV", "fecha": "22/09/2026", "hora": "08:10", "estado": "Atraso"},
    {"estudiante": "Josefa Morales", "curso": "4DPV", "fecha": "22/09/2026", "hora": "07:47", "estado": "A tiempo"},
    {"estudiante": "Tomás Silva", "curso": "4DPV", "fecha": "22/09/2026", "hora": "08:25", "estado": "Atraso"},

    # 4°DMM
    {"estudiante": "Emilia Pizarro", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:55", "estado": "A tiempo"},
    {"estudiante": "Maximiliano Flores", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "08:18", "estado": "Atraso"},
    {"estudiante": "Renata Contreras", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:49", "estado": "A tiempo"},
    {"estudiante": "Agustín Bravo", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "08:33", "estado": "Atraso"},
    {"estudiante": "Valentina Cárdenas", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "07:59", "estado": "A tiempo"},
    {"estudiante": "Cristóbal Espinoza", "curso": "4DMM", "fecha": FECHA_ACTUAL_STR, "hora": "08:44", "estado": "Atraso"},
]

CURSOS_DISPONIBLES = ["Todos los cursos"] + sorted(set(r["curso"] for r in HISTORIAL_ADMIN_EJEMPLO))


class AdminHistorialScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller

        ahora = datetime.now()
        self.cal_mes = ahora.month
        self.cal_anio = ahora.year

        self._build_header()
        self._build_body()
        self._build_footer()

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

        filtros_row1 = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        filtros_row1.pack(fill="x", pady=(0, 8))

        self.buscar_entry = ctk.CTkEntry(
            filtros_row1, width=240, height=36, corner_radius=8,
            placeholder_text="🔍  Buscar estudiante u hora...",
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.buscar_entry.pack(side="left")

        frame_fecha = ctk.CTkFrame(filtros_row1, fg_color="transparent")
        frame_fecha.pack(side="right")

        self.fecha_entry = ctk.CTkEntry(
            frame_fecha, width=110, height=36, corner_radius=8,
            placeholder_text="DD/MM/AAAA",
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.fecha_entry.insert(0, FECHA_ACTUAL_STR)
        self.fecha_entry.pack(side="left", padx=(0, 5))

        btn_cal = ctk.CTkButton(
            frame_fecha, text="📅", width=36, height=36, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1A2B4C",
            command=self.abrir_calendario_popup
        )
        btn_cal.pack(side="left")

        filtros_row2 = ctk.CTkFrame(body, fg_color=COLOR_FONDO)
        filtros_row2.pack(fill="x", pady=(0, 15))

        self.estado_filtro = ctk.CTkOptionMenu(
            filtros_row2, width=190, height=34, corner_radius=8,
            values=["Todos los estados", "Atraso", "A tiempo"],
            fg_color=COLOR_BLANCO, button_color=COLOR_BORDE,
            button_hover_color="#CCCCCC", text_color=COLOR_AZUL_OSCURO,
            dropdown_fg_color=COLOR_BLANCO,
            command=self.on_filtro_cambiado
        )
        self.estado_filtro.pack(side="left")

        self.curso_filtro = ctk.CTkOptionMenu(
            filtros_row2, width=190, height=34, corner_radius=8,
            values=CURSOS_DISPONIBLES,
            fg_color=COLOR_BLANCO, button_color=COLOR_BORDE,
            button_hover_color="#CCCCCC", text_color=COLOR_AZUL_OSCURO,
            dropdown_fg_color=COLOR_BLANCO,
            command=self.on_filtro_cambiado
        )
        self.curso_filtro.pack(side="left", padx=(10, 0))

        self.tabla_card = ctk.CTkFrame(
            body, fg_color=COLOR_BLANCO, corner_radius=10,
            border_width=1, border_color=COLOR_BORDE
        )
        self.tabla_card.pack(fill="both", expand=True)

        self.header_row = ctk.CTkFrame(self.tabla_card, fg_color=COLOR_BLANCO)
        self.header_row.pack(fill="x", padx=20, pady=(15, 5))

        ctk.CTkLabel(self.header_row, text="Estudiante", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=160, anchor="w").pack(side="left")
        ctk.CTkLabel(self.header_row, text="Curso", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=70, anchor="w").pack(side="left")
        ctk.CTkLabel(self.header_row, text="Fecha", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=100, anchor="w").pack(side="left")
        ctk.CTkLabel(self.header_row, text="Hora", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=80, anchor="w").pack(side="left")
        ctk.CTkLabel(self.header_row, text="Estado", font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=COLOR_TEXTO_GRIS, width=90, anchor="w").pack(side="left")

        separador = ctk.CTkFrame(self.tabla_card, fg_color=COLOR_BORDE, height=1)
        separador.pack(fill="x", padx=20)

        self.filas_scroll = ctk.CTkScrollableFrame(
            self.tabla_card, fg_color=COLOR_BLANCO,
            scrollbar_button_color=COLOR_BORDE,
            scrollbar_button_hover_color="#CCCCCC"
        )
        self.filas_scroll.pack(fill="both", expand=True, padx=5, pady=(0, 10))

        self._dibujar_tabla()

        self.buscar_entry.bind("<KeyRelease>", self.on_filtro_cambiado)
        self.fecha_entry.bind("<KeyRelease>", self.on_filtro_cambiado)

    # ----------CALENDARIO----------
    def abrir_calendario_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Seleccionar Fecha")
        popup.geometry("300x320")
        popup.grab_set()

        frame_nav = ctk.CTkFrame(popup, fg_color="transparent")
        frame_nav.pack(fill="x", padx=10, pady=10)

        lbl_mes = ctk.CTkLabel(
            frame_nav, 
            text=f"{calendar.month_name[self.cal_mes].capitalize()} {self.cal_anio}",
            font=ctk.CTkFont(size=14, weight="bold")
        )

        grid_frame = ctk.CTkFrame(popup, fg_color="transparent")

        def actualizar_calendario():
            lbl_mes.configure(text=f"{calendar.month_name[self.cal_mes].capitalize()} {self.cal_anio}")
            for w in grid_frame.winfo_children():
                w.destroy()

            dias = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"]
            for col, dia in enumerate(dias):
                ctk.CTkLabel(grid_frame, text=dia, font=ctk.CTkFont(size=10, weight="bold"), width=34).grid(row=0, column=col)

            cal_matriz = calendar.monthcalendar(self.cal_anio, self.cal_mes)

            def seleccionar_dia(dia_num):
                fecha_fmt = f"{dia_num:02d}/{self.cal_mes:02d}/{self.cal_anio}"
                self.fecha_entry.delete(0, "end")
                self.fecha_entry.insert(0, fecha_fmt)
                self._dibujar_tabla()
                popup.destroy()

            for r_idx, week in enumerate(cal_matriz):
                for c_idx, day in enumerate(week):
                    if day != 0:
                        btn = ctk.CTkButton(
                            grid_frame, 
                            text=str(day), 
                            width=34, 
                            height=28,
                            fg_color="transparent",
                            text_color=COLOR_AZUL_OSCURO,
                            hover_color=COLOR_AMARILLO,
                            command=lambda d=day: seleccionar_dia(d)
                        )
                        btn.grid(row=r_idx+1, column=c_idx, padx=1, pady=1)

        def mes_anterior():
            if self.cal_mes == 1:
                self.cal_mes = 12
                self.cal_anio -= 1
            else:
                self.cal_mes -= 1
            actualizar_calendario()

        def mes_siguiente():
            if self.cal_mes == 12:
                self.cal_mes = 1
                self.cal_anio += 1
            else:
                self.cal_mes += 1
            actualizar_calendario()

        btn_prev = ctk.CTkButton(frame_nav, text="◄", width=30, height=26, command=mes_anterior, fg_color=COLOR_AZUL_OSCURO)
        btn_prev.pack(side="left")

        lbl_mes.pack(side="left", expand=True)

        btn_next = ctk.CTkButton(frame_nav, text="►", width=30, height=26, command=mes_siguiente, fg_color=COLOR_AZUL_OSCURO)
        btn_next.pack(side="right")

        grid_frame.pack(padx=10, pady=5)
        actualizar_calendario()

    def _dibujar_tabla(self):
        for widget in self.filas_scroll.winfo_children():
            widget.destroy()

        registros_filtrados = self._obtener_registros_filtrados()

        if not registros_filtrados:
            ctk.CTkLabel(
                self.filas_scroll, text="No se encontraron resultados",
                font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO_GRIS
            ).pack(pady=20)
            return

        for registro in registros_filtrados:
            self._fila(
                self.filas_scroll, 
                registro["estudiante"], 
                registro["curso"],
                registro.get("fecha", FECHA_ACTUAL_STR),
                registro["hora"], 
                registro["estado"]
            )

    def _obtener_registros_filtrados(self):
        estado_seleccionado = self.estado_filtro.get()
        curso_seleccionado = self.curso_filtro.get()
        texto_busqueda = self.buscar_entry.get().strip().lower()
        fecha_busqueda = self.fecha_entry.get().strip().lower()

        resultado = []
        for registro in HISTORIAL_ADMIN_EJEMPLO:
            if estado_seleccionado != "Todos los estados" and registro["estado"] != estado_seleccionado:
                continue
            if curso_seleccionado != "Todos los cursos" and registro["curso"] != curso_seleccionado:
                continue
            if fecha_busqueda and fecha_busqueda not in registro.get("fecha", "").lower():
                continue
            if texto_busqueda:
                coincide_nombre = texto_busqueda in registro["estudiante"].lower()
                coincide_hora = texto_busqueda in registro["hora"].lower()
                if not (coincide_nombre or coincide_hora):
                    continue

            resultado.append(registro)
        return resultado

    def on_filtro_cambiado(self, event=None):
        self._dibujar_tabla()

    def _fila(self, parent, estudiante, curso, fecha, hora, estado):
        row = ctk.CTkFrame(parent, fg_color=COLOR_BLANCO)
        row.pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(row, text=estudiante, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=160, anchor="w").pack(side="left")
        ctk.CTkLabel(row, text=curso, font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS, width=70, anchor="w").pack(side="left")
        ctk.CTkLabel(row, text=fecha, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=100, anchor="w").pack(side="left")
        ctk.CTkLabel(row, text=hora, font=ctk.CTkFont(size=12),
                     text_color=COLOR_AZUL_OSCURO, width=80, anchor="w").pack(side="left")

        color_badge = COLOR_AMARILLO if estado == "Atraso" else COLOR_VERDE
        texto_color = COLOR_AZUL_OSCURO if estado == "Atraso" else COLOR_BLANCO

        badge = ctk.CTkLabel(
            row, text=estado, font=ctk.CTkFont(size=11, weight="bold"),
            text_color=texto_color, fg_color=color_badge,
            corner_radius=6, width=80, height=24
        )
        badge.pack(side="left")

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

    def on_volver(self):
        from screens.admin_panel import AdminPanelScreen
        self.controller.mostrar_pantalla(AdminPanelScreen)