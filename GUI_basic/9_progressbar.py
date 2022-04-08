import time
import tkinter.ttk as ttk
from tkinter import *
root = Tk()
root.title("My first GUI")
root.geometry("640x480")

'''
#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # indeterminate : 끝을 알 수 없을 때
progressbar.start(10) # 10ms마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text="CLICK", command=btncmd)
btn.pack()
'''

p_var2 = DoubleVar() # 1.2%, 2.5% 처럼 실수도 반영하기 위해
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, mode="determinate", variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(100+1):
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()