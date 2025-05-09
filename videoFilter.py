# videoFilter.py

import cv2
import numpy as np
from colorsDictionary import COLOR_RANGES

def apply_color_filter(frame, color_names):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    combined_mask = None

    for color_name in color_names:
        lower, upper = COLOR_RANGES[color_name]
        mask = cv2.inRange(hsv, np.array(lower, dtype=np.uint8), np.array(upper, dtype=np.uint8))
        combined_mask = mask if combined_mask is None else cv2.bitwise_or(combined_mask, mask)

    result = cv2.bitwise_and(frame, frame, mask=combined_mask)
    return result
