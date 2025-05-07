# recorder.py

import cv2
import time
from datetime import datetime
from colorsDictionary import COLOR_RANGES
from videoFilter import apply_color_filter
import os

def record_video(color_name, duration=5, output_folder="grabaciones"):
    # Asegurar que la carpeta existe
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Error: no se pudo acceder a la cámara.")
        return

    # Obtener tamaño de frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Preparar el nombre del archivo (.mp4)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_folder}/video_{color_name}_{timestamp}.mp4"

    # Codec y escritor de video (.mp4 con códec mp4v)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

    print(f"[INFO] Grabando video con filtro '{color_name}' durante {duration} segundos...")
    start_time = time.time()

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break

        filtered = apply_color_filter(frame, color_name)
        out.write(filtered)

        # Mostrar grabación en tiempo real
        cv2.imshow("Grabando...", filtered)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    out.release()
    cv2.destroyWindow("Grabando...")

    print(f"[INFO] Grabación guardada como {filename}")
