from tkinter import * # tkinter를 이용한 GUI 프로그래밍
root = Tk() # Tk 인스턴스 생성
root.title("My first GUI") # title()함수로 문자열을 보내면 윈도우 창의 이름이 변경됨.
root.geometry("640x480")
#root.geometry("640x480+300+100") # root.geometry("너비x높이+X좌표+Y좌표")
root.resizable(False, False) # 너비, 높이 변경 불가능 (창 크기 조절)
root.mainloop() # pygame으로 게임을 만들었을 때 꺼지지 않도록 루프를 만들었던 것과 비슷하게 루프를 하는 것.
