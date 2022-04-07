# 버튼은 이렇게 만든다.
from tkinter import *
root = Tk()
root.title("My first GUI")

btn1 = Button(root, text="버튼1")
btn2 = Button(root, padx=5, pady=10, text="버튼2") # pad는 크기의 절대값이 아니다. HTML의 padding과 비슷함.
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 크기 자체 설정
btn5 = Button(root, fg='red', bg='yellow', text="버튼5")

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

photo = PhotoImage(file="GUI_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Hello, World!")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()



root.mainloop()