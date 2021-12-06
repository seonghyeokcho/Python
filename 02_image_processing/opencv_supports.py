import cv2

def close_opencv_window_for_macOS():
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.waitKey(1)