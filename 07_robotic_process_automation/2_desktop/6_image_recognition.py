import pyautogui

file_menu = pyautogui.locateOnScreen("/Users/csh/jupytercreation/Python_Practice/RPA/basic/2_desktop/img/file_menu.png")
print(file_menu)
# pyautogui.click(file_menu)
pyautogui.moveTo(12,112)