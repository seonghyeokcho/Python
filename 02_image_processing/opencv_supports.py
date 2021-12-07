import cv2

imread_flags = {
    "color":cv2.IMREAD_COLOR,
    "grayscale":cv2.IMREAD_GRAYSCALE,
    "unchanged":cv2.IMREAD_UNCHANGED
    }

def load_image(src, flag = "color"):
    if flag not in imread_flags.keys():
        return print(f"This \"{flag}\" flag key is not in imread_flags dictionary.")
    
    matrix = cv2.imread(
        "/Users/csh/programming_language/001_Python/02_image_processing/images/" + src,
        imread_flags[flag]
        )
    return matrix

def close_opencv_window_for_macOS():
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.waitKey(1)