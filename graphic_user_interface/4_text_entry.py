from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그램 제목 설정
root.geometry("640x480")  # 창 크기 설정(가로 * 세로)

txt = Text(root, width=30, height=5)
txt.pack()  # 텍스트를 입력할 수 있는 빈 공간을 생성한다.
txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width=30)  # 한 줄로 입력받을때 사용(여러줄에 걸쳐 사용해야 할때는 텍스트를 사용)
e.pack()
e.insert(0, "한 줄만 입력해요")  # 값이 비어 있을때는 END를 써도 동일하다.

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 텍스트 상자의 line 1, 0번째 인덱스로부터 END까지의 텍스트를 모두 가져온다.
    # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())  # entry 의 모든 텍스트를 가져온다.

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()