from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")
default_label = "원하는 값을 입력하세요! (단, 공백은 불가)"
label = Label(root, text=default_label)
label.pack()
e = Entry(root, width=30)
e.insert(END, "리스트에 추가할 항목을 입력하세요")
listbox = Listbox(root, selectmode="extended", height=0) # selectmode, single or extended : 얼마나 선택할 수 있는가? height(몇 줄을 보여줄 것인가?, 0이면 전체 줄 공개)
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박') # list.append()와 비슷함
listbox.insert(END, '포도')
listbox.pack()
def btncmd():
    # listbox.delete(END) # 리스트박스 안에 있는 맨 뒤의 값을 제거. (인덱스 값을 넣으면 해당 위치의 값을 제거)
    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요.")
    # 항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2)) # 마지막 2를 포함하는 거임.
    # 선택된 항목 확인
    # print("선택된 항목 :", listbox.curselection()) # 인덱스 값으로 가져옴
    a = e.get()
    if a == "" or a == " ":
        label.config(text="너 어디 아프냐?", fg='red')
        return
    listbox.insert(END, a)
    label.config(text="\"{}\"가 성공적으로 추가되었습니다.".format(e.get()), fg = 'blue')
    e.delete(0, END)
def btncmd2():
    label.config(text="\"{}\"가 성공적으로 제거되었습니다.".format(listbox.get(listbox.curselection())), fg='red')
    listbox.delete(listbox.curselection())
e.pack()
btn = Button(root, text="ADD", command=btncmd)
btn2 = Button(root, text="DEL", command=btncmd2)
btn.pack()
btn2.pack()
root.mainloop()