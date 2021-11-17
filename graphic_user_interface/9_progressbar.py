import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Nado GUI")  # 프로그램 제목 설정
root.geometry("640x480")  # 창 크기 설정(가로 * 세로)

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')  # 종료지점이 정해지지 않은 작업을 표현할때 사용한다.
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar.start(10)  # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)  # maximum : 최대 수치, length : 바의 길이
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)  # 0.01 초 대기 후 다음 실행

        p_var2.set(i)  # progress bar 의 값 설정
        progressbar2.update()  # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()