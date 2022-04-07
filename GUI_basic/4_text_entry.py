from tkinter import *
root = Tk()
root.geometry("640x480")
root.title("My first GUI")

txt = Text(root, width=30, height=5) # 텍스트 위젯 생성
txt.pack()
txt.insert(END, "글자를 입력하세요\n뒤지기 싫으면") # 여러줄에 걸쳐 텍스트 입력 가능
e = Entry(root, width=30) # Text()와의 차이점 : Entry()는 한 줄만 입력 가능
e.pack()
e.insert(END, "한 줄만 입력하세요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫 번째 라인, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="CLICK", command=btncmd)
btn.pack()

root.mainloop()