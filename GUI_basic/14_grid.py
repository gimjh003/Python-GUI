from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

# pack이 쌓는 느낌이라면

# btn1.pack(side="left")
# btn2.pack(side="right") 

# grid는 좌표 어딘가에 배치하는 느낌

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 맨 윗줄

class Calculator(Button):
    def __init__(self, txt, row, column, wid=7, hei=3):
        Button.__init__(self, text=txt, width=wid, height=hei)
        self.grid(row=row, column=column, sticky=N+E+W+S, padx=3, pady=3) # 해당하는 방향의 그리드로 달라붙음 / 그리드 간의 간격 x, y

btn_f16 = Calculator("F16", 0, 0)
btn_f17 = Calculator("F17", 0, 1)
btn_f18 = Calculator("F18", 0, 2)
btn_f19 = Calculator("F17", 0, 3)
btn_clear = Calculator("clear", 1, 0)
btn_eq = Calculator("=", 1, 1)
btn_div = Calculator("/", 1, 2)
btn_times = Calculator("*", 1, 3)
btn_7 = Calculator("7", 2, 0)
btn_8 = Calculator("8", 2, 1)
btn_9 = Calculator("9", 2, 2)
btn_minus = Calculator("-", 2, 3)
btn_4 = Calculator("4", 3, 0)
btn_5 = Calculator("5", 3, 1)
btn_6 = Calculator("6", 3, 2)
btn_add = Calculator("+", 3, 3)
btn_1 = Calculator("1", 4, 0)
btn_2 = Calculator("2", 4, 1)
btn_3 = Calculator("3", 4, 2)
btn_enter = Calculator("enter", 4, 3)
btn_enter.grid(row=4, column=3, rowspan=2) # row 2개 공간을 차지하겠다. 
btn_0 = Calculator("0", 5, 0) # 가로로 합쳐짐
btn_point = Calculator(".", 5, 2)
btn_0.grid(row=5, column=0, columnspan=2) # 현재 위치로부터 오른쪽으로 몇 칸 더함
'''
btn_f16 = Button(root, text="F16") # N : 북, E : 동, W : 서, S : 남 (해당 방향 그리드로 달라붙음)
btn_f16.grid(row=0, column=0, sticky=N+E+W+S)
'''
root.mainloop()