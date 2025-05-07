# videoFilter.py

import cv2
import numpy as np
from colorsDictionary import COLOR_RANGES

def apply_color_filter(frame, color_name):
    # Convertir el frame a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtener rangos HSV del color seleccionado
    lower, upper = COLOR_RANGES[color_name]
    lower_np = np.array(lower, dtype=np.uint8)
    upper_np = np.array(upper, dtype=np.uint8)

    # Crear máscara y aplicarla al frame original
    mask = cv2.inRange(hsv, lower_np, upper_np)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result
