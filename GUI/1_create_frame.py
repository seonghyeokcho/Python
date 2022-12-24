from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그램 제목 설정
root.geometry("640x480")  # 창 크기 설정(가로 * 세로)
# root.geometry("640x480+300+100")  # 창 크기 설정(가로 * 세로 + x좌표 + y좌표)

root.resizable(True, False)  # x(너비), y(높이) 값 변경 불가 설정


root.mainloop()