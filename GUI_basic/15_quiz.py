from tkinter import *
root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 본문

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
txt = Text(root, width=1920, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both")
scrollbar.config(command=txt.yview)

# 동작

def fopen():
    with open("mynote.txt", "r") as file:
        txt.delete("1.0", END)
        txt.insert(END, file.read())

def save():
    with open("mynote.txt", "w") as file:
        file.write(txt.get("1.0", END))

# 메뉴

menu = Menu(root, tearoff=0)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=fopen)
menu_file.add_command(label="저장", command=save)
menu_file.add_separator()
menu_file.add_command(label="종료", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
root.config(menu=menu)

root.mainloop()