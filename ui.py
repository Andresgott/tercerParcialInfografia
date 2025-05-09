# ui.py

import tkinter as tk
from tkinter import ttk

class ColorFilterUI:
    def __init__(self, master, color_names, on_apply_filter, on_record):
        self.master = master
        self.master.title("Panel de Control - Filtro de Colores")

        # Lista de colores seleccionables (hasta 3)
        ttk.Label(master, text="Selecciona hasta 3 colores:").pack(pady=5)
        self.color_listbox = tk.Listbox(master, selectmode="multiple", height=10, exportselection=False)
        for color in color_names:
            self.color_listbox.insert(tk.END, color)
        self.color_listbox.pack(pady=5)

        # Entrada para duración del video
        ttk.Label(master, text="Duración (1-10 segundos):").pack(pady=(10, 2))
        self.duration_var = tk.IntVar(value=5)
        self.duration_spinbox = tk.Spinbox(master, from_=1, to=10, textvariable=self.duration_var, width=5)
        self.duration_spinbox.pack(pady=2)

        # Botón para aplicar filtro
        self.filter_button = ttk.Button(master, text="Aplicar Filtro", command=self.apply_filter)
        self.filter_button.pack(pady=10)

        # Botón para grabar video
        self.record_button = ttk.Button(master, text="Grabar Fragmento", command=self.record_video_with_duration)
        self.record_button.pack(pady=5)

        self.on_apply_filter = on_apply_filter
        self.on_record = on_record

    def apply_filter(self):
        selected_indices = self.color_listbox.curselection()
        selected_colors = [self.color_listbox.get(i) for i in selected_indices]
        if len(selected_colors) > 3:
            print("Selecciona solo hasta 3 colores.")
            return
        self.on_apply_filter(selected_colors)

    def record_video_with_duration(self):
        selected_indices = self.color_listbox.curselection()
        selected_colors = [self.color_listbox.get(i) for i in selected_indices]
        if len(selected_colors) > 3:
            print("Selecciona solo hasta 3 colores.")
            return
        duration = self.duration_var.get()
        self.on_record(selected_colors, duration)
