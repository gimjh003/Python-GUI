# 레이블은 그냥 글자(text keyword argument)나 이미지(image keyword argument)만 보여준다.
from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="우웩")
def change2():
    global photo2
    photo2 = PhotoImage(file="GUI_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="CLICK", command=change)
btn.pack()
btn2 = Button(root, text="CLICK!!!", command=change2)
btn2.pack()

root.mainloop()