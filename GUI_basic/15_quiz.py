import os
from tkinter import *
root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry('640x480')
filename = "mynote.txt"

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

def open_file():
    if os.path.isfile(filename):
        with open("mynote.txt", "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open("mynote.txt", 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END))

menu = Menu(root, tearoff=0)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="종료", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)

root.mainloop()