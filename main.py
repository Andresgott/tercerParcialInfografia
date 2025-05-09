# main.py

import cv2
import threading
from tkinter import Tk
from colorsDictionary import COLOR_RANGES
from ui import ColorFilterUI
from videoFilter import apply_color_filter
from recorder import record_video

selected_color_names = []
apply_filter_flag = False

def on_apply_filter(color_names):
    global selected_color_names, apply_filter_flag
    selected_color_names = color_names
    apply_filter_flag = True

def on_record(color_names, duration):
    threading.Thread(target=record_video, args=(color_names, duration), daemon=True).start()

def start_video():
    global apply_filter_flag
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video Original", frame)

        if apply_filter_flag and selected_color_names:
            filtered = apply_color_filter(frame, selected_color_names)
            cv2.imshow("Video Filtrado", filtered)

        key = cv2.waitKey(1)
        if key == 27:  # Esc para salir
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    root = Tk()
    ui = ColorFilterUI(root, list(COLOR_RANGES.keys()), on_apply_filter, on_record)
    threading.Thread(target=start_video, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
