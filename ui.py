# ui.py

import tkinter as tk
from tkinter import ttk

class ColorFilterUI:
    def __init__(self, master, color_names, on_apply_filter, on_record):
        self.master = master
        self.master.title("Panel de Control - Filtro de Colores")

        # Label
        ttk.Label(master, text="Selecciona un color:").pack(pady=5)

        # Dropdown (combobox) de colores
        self.color_var = tk.StringVar()
        self.color_dropdown = ttk.Combobox(master, textvariable=self.color_var, values=color_names, state="readonly")
        self.color_dropdown.pack(pady=5)
        self.color_dropdown.current(0)  # Selecciona el primer color por defecto

        # Botón para aplicar filtro
        self.filter_button = ttk.Button(master, text="Aplicar Filtro", command=self.apply_filter)
        self.filter_button.pack(pady=10)

        # Botón para grabar video
        self.record_button = ttk.Button(master, text="Grabar Fragmento", command=on_record)
        self.record_button.pack(pady=5)

        # Callbacks
        self.on_apply_filter = on_apply_filter

    def apply_filter(self):
        selected_color = self.color_var.get()
        self.on_apply_filter(selected_color)
