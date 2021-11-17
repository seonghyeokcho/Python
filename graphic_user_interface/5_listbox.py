from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그램 제목 설정
root.geometry("640x480")  # 창 크기 설정(가로 * 세로)

listbox = Listbox(root, selectmode='extended', height=0)  # extended : 다중 선택, single : 단일 선택
# height 0 : 리스트 전부를 노출, height n : 리스트의 n번째까지만 노출
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 리스트 항록 삭제
    # listbox.delete(0)  # 맨 앞에 항복을 삭제
    # listbox.delete(END)  # 맨 뒤에 항복을 삭제

    # 리스트 항목 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 리스트 항목 내용확인(시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 리스트 항목 확인(idx 위치로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()