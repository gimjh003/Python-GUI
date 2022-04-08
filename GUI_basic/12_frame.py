from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# menu frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True) # expand를 쓰면 꽉 참

btn = Button(frame_burger, text="햄버거").pack()
btn2 = Button(frame_burger, text="치즈버거").pack()
btn3 = Button(frame_burger, text="치킨버거").pack()

# drink frame
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

btn4 = Button(frame_drink, text="물").pack()
btn5 = Button(frame_drink, text="우유").pack()
btn6 = Button(frame_drink, text="탄산수").pack()

root.mainloop()