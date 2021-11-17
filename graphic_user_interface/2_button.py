from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그램 제목 설정

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼222222222")  # 버튼 내 콘텐츠와 버튼 가장자리의 간격(padding)을 조정할 수 있다.
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼444444444444")  # 버튼 자체의 크기(고정된 값)를 조절할 수도 있다.
btn4.pack()

btn5 = Button(root, fg="red", bg='yellow', text="버튼5")  # 버튼 내 배경색과 버튼 내 텍스트 색을 지정할 수있다.
btn5.pack()

photo = PhotoImage(file="Python_Practice/GUIprogramming/GUI_basic/img.png")  # 이미지 버튼이 가능하다.
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요.")  # 버튼을 눌렀을 때 VScode 내에서 실행되는 코드

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()