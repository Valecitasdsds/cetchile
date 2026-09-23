"""
CET CHILE - Sistema de Asistencia
screens/nuevo_estudiante.py - Registro de nuevo estudiante (3 pasos)
"""

import customtkinter as ctk
from utils.theme import (
    COLOR_AZUL_OSCURO, COLOR_AMARILLO, COLOR_FONDO,
    COLOR_TEXTO_GRIS, COLOR_TEXTO_GRIS_CLARO, COLOR_BLANCO,
    COLOR_BORDE, COLOR_VERDE
)


class NuevoEstudianteScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLOR_FONDO)
        self.controller = controller

        # Datos que se van acumulando durante los 3 pasos
        self.datos = {
            "nombre": "",
            "correo": "",
            "password": "",
            "qr_registrado": False,
            "rostro_registrado": False,
        }
        self.mostrar_password = False

        self._build_header()

        # Contenedor que se limpia y reconstruye en cada paso
        self.body = ctk.CTkFrame(self, fg_color=COLOR_FONDO)
        self.body.pack(fill="both", expand=True)

        self._build_footer()

        self._ir_a_paso_1()

    # ---------- ENCABEZADO (fijo) ----------
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

    # ---------- PIE DE PÁGINA (fijo) ----------
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

    def _limpiar_body(self):
        for widget in self.body.winfo_children():
            widget.destroy()

    def _encabezado_paso(self, contenido, paso_texto, titulo, on_volver):
        top_row = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        top_row.pack(fill="x", pady=(0, 5))

        back_btn = ctk.CTkButton(
            top_row, text="←", width=36, height=36, corner_radius=18,
            fg_color=COLOR_FONDO, hover_color="#E5E5E5",
            text_color=COLOR_AZUL_OSCURO,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=on_volver
        )
        back_btn.pack(side="left")

        paso_label = ctk.CTkLabel(
            top_row, text=f"Nuevo estudiante {paso_texto}",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        )
        paso_label.pack(side="left", padx=(10, 0))

        ctk.CTkLabel(
            contenido, text=titulo, font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXTO_GRIS, anchor="w"
        ).pack(fill="x", pady=(15, 15))

    # ============================================================
    # PASO 1/3 — Datos del estudiante
    # ============================================================
    def _ir_a_paso_1(self):
        self._limpiar_body()
        contenido = ctk.CTkFrame(self.body, fg_color=COLOR_FONDO, width=420)
        contenido.pack(pady=(30, 0))

        self._encabezado_paso(contenido, "(1/3)", "Datos del estudiante", self.on_cancelar)

        ctk.CTkLabel(contenido, text="👤  Nombre completo", font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w").pack(fill="x")
        self.nombre_entry = ctk.CTkEntry(
            contenido, width=420, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.nombre_entry.insert(0, self.datos["nombre"])
        self.nombre_entry.pack(pady=(5, 15))

        ctk.CTkLabel(contenido, text="✉  Correo institucional", font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w").pack(fill="x")
        self.correo_entry = ctk.CTkEntry(
            contenido, width=420, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1
        )
        self.correo_entry.insert(0, self.datos["correo"])
        self.correo_entry.pack(pady=(5, 15))

        ctk.CTkLabel(contenido, text="🔒  Contraseña", font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, anchor="w").pack(fill="x")
        pass_row = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        pass_row.pack(fill="x", pady=(5, 25))

        self.password_entry = ctk.CTkEntry(
            pass_row, width=380, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, border_color=COLOR_BORDE, border_width=1, show="*"
        )
        self.password_entry.insert(0, self.datos["password"])
        self.password_entry.pack(side="left")

        self.eye_btn = ctk.CTkButton(
            pass_row, text="👁", width=36, height=42, corner_radius=8,
            fg_color=COLOR_BLANCO, hover_color="#EDEDED",
            text_color=COLOR_TEXTO_GRIS, border_width=1, border_color=COLOR_BORDE,
            command=self.toggle_password
        )
        self.eye_btn.pack(side="left", padx=(8, 0))

        self.error_label = ctk.CTkLabel(
            contenido, text="", font=ctk.CTkFont(size=11), text_color="#D9534F"
        )
        self.error_label.pack(anchor="w", pady=(0, 5))

        continuar_btn = ctk.CTkButton(
            contenido, text="CONTINUAR →",
            width=420, height=48, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.on_continuar_paso1
        )
        continuar_btn.pack()

    def toggle_password(self):
        self.mostrar_password = not self.mostrar_password
        self.password_entry.configure(show="" if self.mostrar_password else "*")

    def on_continuar_paso1(self):
        nombre = self.nombre_entry.get().strip()
        correo = self.correo_entry.get().strip()
        password = self.password_entry.get().strip()

        if not nombre or not correo or not password:
            self.error_label.configure(text="Completa todos los campos para continuar")
            return

        self.datos["nombre"] = nombre
        self.datos["correo"] = correo
        self.datos["password"] = password
        self._ir_a_paso_2_qr()

    # ============================================================
    # PASO 2/3 — Identificación QR
    # ============================================================
    def _ir_a_paso_2_qr(self):
        self._limpiar_body()
        contenido = ctk.CTkFrame(self.body, fg_color=COLOR_FONDO, width=420)
        contenido.pack(pady=(30, 0))

        self._encabezado_paso(contenido, "(2/3)", "Identificación QR", self._ir_a_paso_1)

        self.qr_estado_frame = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        self.qr_estado_frame.pack(pady=(10, 20))
        self._dibujar_estado_qr()

        self.qr_continuar_btn = ctk.CTkButton(
            contenido, text="CONTINUAR →",
            width=420, height=48, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            state="normal" if self.datos["qr_registrado"] else "disabled",
            command=self._ir_a_paso_2_facial
        )
        self.qr_continuar_btn.pack(pady=(10, 0))

    def _dibujar_estado_qr(self):
        for widget in self.qr_estado_frame.winfo_children():
            widget.destroy()

        if not self.datos["qr_registrado"]:
            ctk.CTkLabel(self.qr_estado_frame, text="⬛",
                         font=ctk.CTkFont(size=40)).pack(pady=(0, 10))
            ctk.CTkLabel(self.qr_estado_frame, text="Escanear código QR",
                         font=ctk.CTkFont(size=13, weight="bold"),
                         text_color=COLOR_AZUL_OSCURO).pack()
            ctk.CTkLabel(self.qr_estado_frame,
                         text="Acerca el código QR del estudiante\na la cámara.",
                         font=ctk.CTkFont(size=11), text_color=COLOR_TEXTO_GRIS_CLARO,
                         justify="center").pack(pady=(2, 15))
            ctk.CTkButton(
                self.qr_estado_frame, text="ESCANEAR QR",
                width=200, height=42, corner_radius=8,
                fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
                text_color=COLOR_BLANCO, font=ctk.CTkFont(size=12, weight="bold"),
                command=self.on_escanear_qr
            ).pack()
        else:
            ctk.CTkLabel(
                self.qr_estado_frame, text="✓",
                width=60, height=60, corner_radius=30,
                fg_color=COLOR_VERDE, text_color=COLOR_BLANCO,
                font=ctk.CTkFont(size=26, weight="bold")
            ).pack(pady=(0, 10))
            ctk.CTkLabel(self.qr_estado_frame, text="QR registrado correctamente",
                         font=ctk.CTkFont(size=13, weight="bold"),
                         text_color=COLOR_AZUL_OSCURO).pack()

    def on_escanear_qr(self):
        # Simulación: en un futuro aquí iría la lectura real de la cámara
        self.datos["qr_registrado"] = True
        self._dibujar_estado_qr()
        self.qr_continuar_btn.configure(state="normal")

    # ============================================================
    # PASO 2/3 — Reconocimiento facial
    # ============================================================
    def _ir_a_paso_2_facial(self):
        self._limpiar_body()
        contenido = ctk.CTkFrame(self.body, fg_color=COLOR_FONDO, width=420)
        contenido.pack(pady=(30, 0))

        self._encabezado_paso(contenido, "(2/3)", "Reconocimiento facial", self._ir_a_paso_2_qr)

        self.rostro_estado_frame = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        self.rostro_estado_frame.pack(pady=(10, 20))
        self._dibujar_estado_rostro()

        self.rostro_continuar_btn = ctk.CTkButton(
            contenido, text="CONTINUAR →",
            width=420, height=48, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            state="normal" if self.datos["rostro_registrado"] else "disabled",
            command=self._ir_a_completado
        )
        self.rostro_continuar_btn.pack(pady=(10, 0))

    def _dibujar_estado_rostro(self):
        for widget in self.rostro_estado_frame.winfo_children():
            widget.destroy()

        if not self.datos["rostro_registrado"]:
            ctk.CTkLabel(self.rostro_estado_frame, text="🙂",
                         font=ctk.CTkFont(size=40)).pack(pady=(0, 10))
            ctk.CTkLabel(self.rostro_estado_frame,
                         text="Captura el rostro del estudiante\npara su registro.",
                         font=ctk.CTkFont(size=11), text_color=COLOR_TEXTO_GRIS_CLARO,
                         justify="center").pack(pady=(2, 15))
            ctk.CTkButton(
                self.rostro_estado_frame, text="REGISTRAR ROSTRO",
                width=200, height=42, corner_radius=8,
                fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
                text_color=COLOR_BLANCO, font=ctk.CTkFont(size=12, weight="bold"),
                command=self.on_registrar_rostro
            ).pack()
        else:
            ctk.CTkLabel(
                self.rostro_estado_frame, text="✓",
                width=60, height=60, corner_radius=30,
                fg_color=COLOR_VERDE, text_color=COLOR_BLANCO,
                font=ctk.CTkFont(size=26, weight="bold")
            ).pack(pady=(0, 10))
            ctk.CTkLabel(self.rostro_estado_frame, text="Rostro registrado correctamente",
                         font=ctk.CTkFont(size=13, weight="bold"),
                         text_color=COLOR_AZUL_OSCURO).pack()

    def on_registrar_rostro(self):
        # Simulación: en un futuro aquí iría la captura real de la cámara
        self.datos["rostro_registrado"] = True
        self._dibujar_estado_rostro()
        self.rostro_continuar_btn.configure(state="normal")

    # ============================================================
    # COMPLETADO — Resumen final
    # ============================================================
    def _ir_a_completado(self):
        self._limpiar_body()
        contenido = ctk.CTkFrame(self.body, fg_color=COLOR_FONDO, width=420)
        contenido.pack(pady=(30, 0))

        top_row = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO)
        top_row.pack(fill="x", pady=(0, 5))
        ctk.CTkLabel(
            top_row, text="Nuevo estudiante - Completado",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        ).pack(side="left")

        ctk.CTkLabel(
            contenido, text="✓",
            width=60, height=60, corner_radius=30,
            fg_color=COLOR_VERDE, text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            contenido, text="ESTUDIANTE REGISTRADO",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color=COLOR_AZUL_OSCURO
        ).pack(pady=(0, 20))

        info_card = ctk.CTkFrame(
            contenido, fg_color=COLOR_BLANCO, corner_radius=10,
            border_width=1, border_color=COLOR_BORDE
        )
        info_card.pack(fill="x", pady=(0, 25))

        self._info_row(info_card, "👤", "Nombre", self.datos["nombre"])
        self._info_row(info_card, "✉", "Correo", self.datos["correo"])
        self._info_row(info_card, "⬛", "QR", "Registrado", check=True)
        self._info_row(info_card, "🙂", "Rostro", "Registrado", check=True)

        ctk.CTkButton(
            contenido, text="VOLVER AL INICIO",
            width=420, height=48, corner_radius=8,
            fg_color=COLOR_AZUL_OSCURO, hover_color="#1C3355",
            text_color=COLOR_BLANCO,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.on_volver_al_inicio
        ).pack()

    def _info_row(self, parent, icono, label, valor, check=False):
        row = ctk.CTkFrame(parent, fg_color=COLOR_BLANCO)
        row.pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(row, text=icono, font=ctk.CTkFont(size=13), width=20).pack(side="left")
        ctk.CTkLabel(row, text=label, font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXTO_GRIS_CLARO, width=100, anchor="w").pack(side="left", padx=(10, 0))

        texto = f"✓ {valor}" if check else valor
        color = COLOR_VERDE if check else COLOR_AZUL_OSCURO
        ctk.CTkLabel(row, text=texto, font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=color, anchor="w").pack(side="left")

    # ---------- ACCIONES GLOBALES ----------
    def on_cancelar(self):
        from screens.admin_panel import AdminPanelScreen
        self.controller.mostrar_pantalla(AdminPanelScreen)

    def on_volver_al_inicio(self):
        from screens.login import LoginScreen
        self.controller.mostrar_pantalla(LoginScreen)