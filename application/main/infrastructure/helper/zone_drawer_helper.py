import cv2
import numpy as np
import copy

class ZoneDrawerHelper():
    def __init__(self) -> None:
        self.custom_green = (2, 115, 36)
        self.font = cv2.FONT_HERSHEY_DUPLEX
    def draw(self, im0:np.ndarray, frame_width,frame_height:int, upper_ratio=1/2.65, lower_ratio=7/8):
        
        # top zone
        x, y, x1, y1 = 0,0, frame_width, int(frame_height*upper_ratio)
        zone = im0[y:y1, x:x1]
        overlay = copy.deepcopy(zone)

        cv2.rectangle(overlay, (0, 0), (x1, y1), (0, 0, 200), -1)
        cv2.putText(overlay, "UNUSED ZONE", (x+25, y+35), self.font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        alpha = 0.5
        im0[y:y1, x:x1] = cv2.addWeighted(overlay, alpha, zone, 1 - alpha, 0)

        
        # bottom zone
        x, y, x1, y1 = 0,int(frame_height*lower_ratio), frame_width, frame_height
        zone = im0[y:y1, x:x1]
        overlay = copy.deepcopy(zone)

        cv2.rectangle(overlay, (0, 0), (overlay.shape[1], overlay.shape[0]), (0, 0, 200), -1)
        # cv2.putText(overlay, "UNUSED ZONE", (x+25, y+35), self.font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        alpha = 0.5
        im0[y:y1, x:x1] = cv2.addWeighted(overlay, alpha, zone, 1 - alpha, 0)

