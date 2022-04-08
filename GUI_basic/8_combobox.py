import tkinter.ttk as ttk
from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

values = [str(i)+"일" for i in range(1, 31+1)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결재일") # 최초 목록 제목 설정 뿐 아니라 버튼 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # state 키워드 매개변수에 "readonly"를 넣으면 콤보박스의 값을 변경할 수 없다.
readonly_combobox.current(0) # 미리 0번째 인덱스의 값을 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()