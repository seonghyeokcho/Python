import pyautogui
# pyautogui.FAILSAFE = False  # 어떠한 경우에도 중지되지 않음
# pyautogui.mouseInfo()
pyautogui.PAUSE = 1  # 모든 동작에 1초식 sleep 적용

# pyautogui.sleep(3)
for i in range(10):
    pyautogui.move(100,100)
    # pyautogui.sleep(1)