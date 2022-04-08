import os
from tkinter import * # GUI 프로그래밍을 위해 tkinter 라이브러리가 필요함
root = Tk()
root.title("제목 없음 - Windows 메모장") # 창 제목 설정
root.geometry('640x480') # 창 크기 설정 ()
filename = "mynote.txt" # 저장하거나 열 파일의 이름

# 창 내부 모습

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y") # 스크롤바를 만들고 창(root)의 오른쪽에 배치한 다음 해당 위치 y축 전체를 차지함
txt = Text(root, yscrollcommand=scrollbar.set) # 텍스트를 입력할 공간을 만듦. (scrollbar를 통해 y축 이동 가능) 
txt.pack(side="left", fill="both", expand=True) # 창 왼쪽 공간을 차지하고 x,y축 전체를 차지하고 expand해서 화면을 꽉 채움
scrollbar.config(command=txt.yview) # 스크롤바의 위치를 이동시키면 해당하는 텍스트 공간 위치를 볼 수 있게됨

# 메뉴의 기능을 위한 함수 정의

def open_file(): # 열기 옵션을 누르면 이 기능이 동작함.
    if os.path.isfile(filename): # 파일이 없으면 아무 동작도 하지 않지만, 파일이 존재하면 실행됨.
        with open("mynote.txt", "r", encoding="utf8") as file: # 파일을 읽음
            txt.delete("1.0", END) # 먼저 이미 써져있는 내용을 지우고
            txt.insert(END, file.read()) # 파일에 있는 내용으로 다시 써내려감

def save_file(): # 저장 옵션을 누르면 이 기능이 동작함
    with open("mynote.txt", 'w', encoding='utf8') as file: # 파일을 쓰기 시작
        file.write(txt.get('1.0', END)) # 파일의 내용은 텍스트 공간 전체에 있는 내용들
# 자동으로 파일이 닫히면서 저장의 기능을 하게됨

# 창(root)의 메뉴를 설정해줌

menu = Menu(root, tearoff=0) # 창(root)의 메뉴를 만듦

menu_file = Menu(menu, tearoff=0) # 파일이라는 메뉴를 만들거임
menu_file.add_command(label="열기", command=open_file) # 파일 메뉴 안에는 열기 기능이 있고, open_file 함수와 연결됨
menu_file.add_command(label="저장", command=save_file) # 파일 메뉴 안에는 저장 기능이 있고, save_file 함수와 연결됨
menu_file.add_separator() # 옵션간의 분리를 위해 선을 그어놓음
menu_file.add_command(label="종료", command=root.quit) # 종료를 누르면 창(root)이 종료됨

menu.add_cascade(label="파일", menu=menu_file) # 메뉴에 파일 메뉴를 추가함, 파일 메뉴의 기능을 쓸 수 있음.
menu.add_cascade(label="편집") # 메뉴에 편집 메뉴를 추가함. 기능은 없음.
menu.add_cascade(label="서식") # 메뉴에 서식 메뉴를 추가함. 기능은 없음.
menu.add_cascade(label="보기") # 메뉴에 보기 메뉴를 추가함. 기능은 없음. 
menu.add_cascade(label="도움말") # 메뉴에 도움말 메뉴를 추가함. 기능은 없음.
root.config(menu=menu) # 창(root)의 메뉴 설정을 우리가 만들었던 메뉴로 설정함

root.mainloop() # 직접 창을 종료하기 전까지, 우리는 창을 사용하기 위해 유지시켜야 함.