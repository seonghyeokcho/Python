import pyautogui

# print(pyautogui.position())

# pyautogui.click(26, 72, duration=1)  # 1초 동안(26,72) 좌표로 이동 후 마우스 클릭
# pyautogui.click()

# 드래그 작업시 필요함
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()  # 더블 클릭
# pyautogui.click(clicks=2)  # 더블 클릭 효과

# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown()
# pyautogui.moveTo(200, 300)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1559, 41)
# pyautogui.drag(0, 241, button='left')  # 현재 마우스 커서 기준으로 x 300 만큼 드래그
# pyautogui.drag(0, 241, button='left', duration=0.25)
# pyautogui.dragTo(1559, 241, duration=0.25, button='left')  # 절대 좌표(1559, 41) 기준으로 (1559, 241)로 드래그

pyautogui.scroll(-10)
# 양수이면 위 방향으로, 음수이면 아래 방향으로 주어진 값만큼 스크롤