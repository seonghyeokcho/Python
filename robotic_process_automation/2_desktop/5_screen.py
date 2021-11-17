import pyautogui
from PIL import ImageGrab

# 스크린샷 찍기
# img = pyautogui.screenshot()
# # png 파일로 스크린샷 저장
# img.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/2_desktop/img/screenshot.png")

pyautogui.sleep(3)
# 첫 번째 방법
# screen = ImageGrab.grab()
# print(screen.getpixel(pyautogui.position()), pyautogui.position())
# 두 번째 방법
# screen = pyautogui.screenshot()
# print(screen.getpixel(pyautogui.position()), pyautogui.position())
# 세 번째 방법
print(pyautogui.position())
pixel = pyautogui.pixel(378, 508)
print(pixel)

# # print(pyautogui.pixelMatchesColor(378, 508, (26,26,26,255)))
# print(pyautogui.pixelMatchesColor(378, 508, pixel))