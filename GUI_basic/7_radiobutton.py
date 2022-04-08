from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var) # 라디오 버튼은 서로 변수를 공유한다.
btn_burger1.select() # 기본값 선택
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var) # 하나를 선택하면 하나가 해제되는 것은 이러한 이유 때문이다.
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var) # 체크된 값을 burger_var가 갖는다.
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar() # 여기에 String형으로 값을 저장한다.
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var) # 라디오버튼의 그룹은 어떤 변수를 공유하는가에 따라 결정된다.
btn_drink1.select() # 기본값 선택, 이거 안하면 처음에 다 체크된 상태로 나옴.
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="우유", value="우유", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()