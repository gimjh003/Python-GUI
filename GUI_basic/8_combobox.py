from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

def btncmd():
    pass

btn = Button(root, text="CLICK", command=btncmd)
btn.pack()

root.mainloop()