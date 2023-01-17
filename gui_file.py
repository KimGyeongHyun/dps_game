import tkinter

# 가장 상위 레벨의 윈도우 창 생성
window = tkinter.Tk()

# 윈도우 창의 제목
window.title("DPS 강화하기 유즈맵 계산기")
# 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
window.geometry('640x400+100+100')
# 윈도우 창 크기 조절 가능 여부 설정
window.resizable(True, True)

# # 윈도우 창에 Label 위젯 설정
# label = tkinter.Label(window, text="hello", width=10, height=5, fg="red", relief="solid")
# # 위젯 배치
# label.pack()


# # 버튼 사용
# count = 0
# # 버튼이 눌렸을 때 부를 메소드
# # 메소드가 실행되면 count에 +1 추가 후 label 의 text 내용을 count 로 바꿈
# def count_up():
#     global count
#     count += 1
#     label.config(text=str(count))
#
#
# label = tkinter.Label(window, text="0")
# label.pack()
#
# button = tkinter.Button(window, overrelief="solid", width=15,
#                         command=count_up, repeatdelay=1000,
#                         repeatinterval=100)
# button.pack()


# # entry(기입창) 사용
# # 텍스트를 입력 받거나 출력하기 위한 기입창 생성 가능
# # get() : 기입창의 텍스트를 문자열로 반환
# # eval() : 문자열로 이루어진 수식을 계산하여 반환
# def calc(event):
#     label.config(text="result=" + str(eval(entry.get())))
#
# # entry 생성
# entry = tkinter.Entry(window)
# # key, mouse 등의 이벤트를 처리하여 메소드 실행 가능
# entry.bind("<Return>", calc)
# entry.pack()
#
# label = tkinter.Label(window)
# label.pack()


# # Listbox 사용
# # 목록을 불러와 추가, 제거 또는 선택
# listbox = tkinter.Listbox(window, selectmode="extended", height=0)
# # 항목 추가
# listbox.insert(0, "number 1")
# listbox.insert(0, "number 2")
# listbox.insert(0, "number 2")
# listbox.insert(0, "number 2")
# listbox.insert(0, "number 3")
# # 항목 삭제
# # 1 번 인덱스 부터 2 번 인덱스 까지 삭제
# # 단일 인덱스 삭제 가능
# listbox.delete(1, 2)
# listbox.pack()


# # Checkbutton 사용
# # checkbutton1 이 파란색(체크버튼 옵션 중 activebackground 항목) 으로 2번 깜빡임
# # 3번째 체크버튼을 눌렀을 경우 메소드 실행
# def flash():
#     checkbutton1.flash()
#
# # 체크할 항목을 지정
# # 버튼 2개를 한꺼번에 체크 항목에 지정 가능
# CheckVariety_1 = tkinter.IntVar()
# CheckVariety_2 = tkinter.IntVar()
#
# # 마우스 버튼이 해당 버튼에 눌려 있을 경우 파란색으로 바뀜
# checkbutton1 = tkinter.Checkbutton(window, text="1", variable=CheckVariety_1,
#                                    activebackground="blue")
# # 버튼을 클릭, 박스가 체크 되었다면 3번째 박스도 체크됨
# # 반대로 3번째 박스를 클릭해도 2번째 박스 체크 바뀜
# checkbutton2 = tkinter.Checkbutton(window, text="2", variable=CheckVariety_2)
# # 버튼을 클릭, 첫번째 버튼이 파란색으로 두 번 깜빡임
# checkbutton3 = tkinter.Checkbutton(window, text="3", variable=CheckVariety_2,
#                                    command=flash)
#
# checkbutton1.pack()
# checkbutton2.pack()
# checkbutton3.pack()


# # Radiobutton
# # 옵션 단일 선택
# def check():
#     label.config(text="RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" +
#                  "RadioVariety_2 = " + str(RadioVariety_2.get()) + "\n\n" +
#                  "Total = " + str(RadioVariety_1.get() + RadioVariety_2.get()))
#
# # Radiobutton 안의 속성 중 value 값을 가져옴
# # 처음에는 0으로 초기화 됨
# # 라디오 버튼이 체크 될 경우 value 값을 가져옴
# # 같은 IntVar() 에 묶여있는 라디오 버튼끼리 상호작용 함
# RadioVariety_1 = tkinter.IntVar()
# RadioVariety_2 = tkinter.IntVar()
#
# # 라디오 버튼 생성
# # value : 라디오 버튼이 반환할 정보
# # 반환된 정보는 variable 에 할당된 변수로 전달됨
# # 같은 variable 을 할당받은 라디오 버튼끼리 상호작용
# radio1 = tkinter.Radiobutton(window, text="1", value=3, variable=RadioVariety_1,
#                              command=check)
# radio1.pack()
#
# # 만약 value 가 같은 라디오 버튼이 있다면 동시에 체크되고 해제됨
# radio2 = tkinter.Radiobutton(window, text="2(1)", value=3, variable=RadioVariety_1,
#                              command=check)
# radio2.pack()
#
# radio3 = tkinter.Radiobutton(window, text="3", value=9, variable=RadioVariety_1,
#                              command=check)
# radio3.pack()
#
# label = tkinter.Label(window, text="None", height=5)
# label.pack()
#
# radio4 = tkinter.Radiobutton(window, text="4", value=12, variable=RadioVariety_2,
#                             command=check)
# radio4.pack()
#
# radio5 = tkinter.Radiobutton(window, text="5", value=15, variable=RadioVariety_2,
#                             command=check)
# radio5.pack()


# # 메뉴 생성
# def close():
#     window.quit()
#     window.destroy()
#
# # 메뉴를 가지고 있는 바
# menubar = tkinter.Menu(window)
#
# # 메뉴바에 메뉴 생성
# menu_1 = tkinter.Menu(menubar, tearoff=0)
# # 메뉴를 눌렀을 때 나오는 서브 메뉴
# menu_1.add_command(label="하위 메뉴 1-1")
# menu_1.add_command(label="하위 메뉴 1-2")
# # 중간 분리
# menu_1.add_separator()
# # 서브 메뉴를 누르면 command 메소드가 실행됨
# menu_1.add_command(label="하위 메뉴 1-3", command=close)
# # 상위 메뉴와 하위 메뉴를 연결
# menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)
#
# menu_2 = tkinter.Menu(menubar, tearoff=0, selectcolor="red")
# # 서브 메뉴를 라디오 버튼처럼 사용
# # state="disable" : 메뉴가 회색으로 변하면서 클릭할 수 없게 됨
# menu_2.add_radiobutton(label="하위 메뉴 2-1", state="disable")
# menu_2.add_radiobutton(label="하위 메뉴 2-2")
# menu_2.add_radiobutton(label="하위 메뉴 2-3")
# menubar.add_cascade(label="상위 메뉴 2", menu=menu_2)
#
# menu_3 = tkinter.Menu(menubar, tearoff=0)
# # 서브 메뉴를 체크 버튼처럼 사용
# menu_3.add_checkbutton(label="하위 메뉴 3-1")
# menu_3.add_checkbutton(label="하위 메뉴 3-2")
# menubar.add_cascade(label="상위 메뉴 3", menu=menu_3)
#
# # 해당 윈도우 창에 메뉴 등록
# # pack() 대신 사용
# window.config(menu=menubar)


# # 메뉴 버튼 생성
# # 메뉴 바는 메뉴 여러 개를 한꺼번에 위쪽에 띄어 놓은 개념
# # 메뉴 버튼은 해당 버튼을 눌렀을 때 메뉴가 어려 개 나오는 개념
# menubutton = tkinter.Menubutton(window, text="메뉴 메뉴 버튼", relief="raised", direction="right")
# menubutton.pack()
#
# # 메뉴 생성
# menu = tkinter.Menu(menubutton, tearoff=0)
# menu.add_command(label="하위 메뉴 - 1")
# menu.add_separator()
# menu.add_command(label="하위 메뉴 - 2")
# menu.add_command(label="하위 메뉴 - 3")
#
# # 메뉴를 메뉴 버튼에 연결
# menubutton["menu"] = menu


# # pack
# # 가장 처음 선언한 pack 부터 배치
# b1 = tkinter.Button(window, text="top")
# b1_1 = tkinter.Button(window, text="top-1")
#
# b2 = tkinter.Button(window, text="bottom")
# b2_1 = tkinter.Button(window, text="bottom-1")
#
# b3 = tkinter.Button(window, text="left")
# b3_1 = tkinter.Button(window, text="left-1")
#
# b4 = tkinter.Button(window, text="right")
# b4_1 = tkinter.Button(window, text="right-1")
#
# b5 = tkinter.Button(window, text="center", bg="red")
#
# # 위에 배치
# b1.pack(side="top")
# # x축을 꽉 채워 위에 배치
# # b1 아래쪽에 배치
# b1_1.pack(side="top", fill="x")
#
# # 아래쪽에 배치
# b2.pack(side="bottom")
# # 맨 오른쪽에 붙혀서 배치
# # b2 위쪽에 배치
# b2_1.pack(side="bottom", anchor="e")
#
# # 왼쪽에 배치
# b3.pack(side="left")
# # y축을 꽉 채워 왼쪽에 배치
# # b3 오른쪽에 배치
# b3_1.pack(side="left", fill="y")
#
# # 오른쪽에 배치
# b4.pack(side="right")
# # 맨 아래쪽에 붙혀서 배치
# # b4 왼쪽에 배치
# b4_1.pack(side="right", anchor="s")
#
# # expand : 미사용 공간 확보 / boolean
# # fill : 할당된 공간에 대한 크기 맞춤 / both 면 x, y 둘 다 맞춤
# b5.pack(expand=True, fill="both")


# # grid
# # 행과 열로 그리드를 나누어 배치
# b1 = tkinter.Button(window, text="(0, 0)")
# b2 = tkinter.Button(window, text="(0, 1)", width=20)
# b3 = tkinter.Button(window, text="(0, 2)",)
#
# b4 = tkinter.Button(window, text="(1, 0)")
# b5 = tkinter.Button(window, text="(1, 1)")
# b6 = tkinter.Button(window, text="(1, 3)")
#
# b7 = tkinter.Button(window, text="(2, 1)")
# b8 = tkinter.Button(window, text="(2, 2)")
# b9 = tkinter.Button(window, text="(2, 4)")
#
# # row : 행위치, column : 열위치
# b1.grid(row=0, column=0)
# b2.grid(row=0, column=1)
# b3.grid(row=0, column=2)
#
# # rowspan : 행 위치 조정, columnspan : 열 위치 조정
# b4.grid(row=1, column=0, rowspan=2)
# b5.grid(row=1, column=1, columnspan=3)
# b6.grid(row=1, column=3)
#
# # sticky : 할당된 공간 내에서 위치 조정
# b7.grid(row=2, column=1, sticky="w")
# b8.grid(row=2, column=2)
# # 그 전 grid 에서 최대 column 값이 3 였으므로 자동적으로 4로 할당
# b9.grid(row=2, column=99)


# # place
# # 좌표값으로 배치
# b1 = tkinter.Button(window, text="(50, 50)")
# b2 = tkinter.Button(window, text="(50, 100)")
# b3 = tkinter.Button(window, text="(100, 150)")
# b4 = tkinter.Button(window, text="(0, 200)")
# b5 = tkinter.Button(window, text="(0, 300)")
# b6 = tkinter.Button(window, text="(0, 300)")
#
# b1.place(x=50, y=50)
# b2.place(x=50, y=100, width=50, height=50)
# b3.place(x=100, y=150, bordermode="inside")
# # relwidth : 위젯의 너비 비율
# b4.place(x=0, y=200, relwidth=0.5)
# # relx : x 좌표 배치 비율
# b5.place(x=0, y=300, relx=0.5)
# # anchor : 위젯의 기준 위치
# b6.place(x=0, y=300, relx=0.5, anchor="s")


# # frame
# # 윈도우 바로 하위 영역으로 나누는 개념인듯
# # 다른 위젯 포함 가능
# # relief : 프레임 테두리 모양
# frame1 = tkinter.Frame(window, relief="solid")
# frame1.pack(side="left", fill="both", expand=True)
#
# frame2 = tkinter.Frame(window, relief="solid", bd=2)
# frame2.pack(side="right", fill="both", expand=True)
#
# # window 에 넣는 대신 frame 에 넣음
# button1 = tkinter.Button(frame1, text="frame1")
# button1.pack(side="right")
# button2 = tkinter.Button(frame2, text="frame2")
# button2.pack(side="left")


# # message
# # 여러 줄의 문자열을 포함
# message = tkinter.Message(window, text="메세지입니다.", width=100, relief="solid")
# message.pack()


# # canvas
# # 그림판같은 개념
# canvas = tkinter.Canvas(window, relief="solid", bd=2)
#
# line = canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill="red")
# polygon = canvas.create_polygon(50, 50, 170, 170, 100, 170, outline="yellow")
# oval = canvas.create_oval(100, 200, 150, 230, fill="blue", width=3)
# arc = canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill="red")
#
# canvas.pack()


# # scroll bar
# frame = tkinter.Frame(window)
#
# # 스크롤 바를 프레임 오른쪽에 배치
# scrollbar = tkinter.Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")
#
# # yscrollcommand : 스크롤 막대로 제어되게 함
# listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
# for line in range(1, 1001):
#     listbox.insert(line, str(line) + "/1000")
# listbox.pack(side="left")
#
# # 스크롤 바와 리스트 박스를 연결
# scrollbar["command"] = listbox.yview
#
# frame.pack()


# # scale
# # 수치 조정 바
# # 수평으로 바를 움직여 값을 빠르게 고를 수 있음
#
# # scale 바가 움직이면 해당 값을 가져와 label 에 출력
# def select(self):
#     value = "값 : " + str(scale.get())
#     label.config(text=value)
#
# var = tkinter.IntVar()
#
# # showvalue : 바 상단에 현재 값을 출력
# # tickinterval : 표현할 숫자 간격
# # to : 마지막 값
# scale = tkinter.Scale(window, variable=var, command=select, orient="horizontal",
#                       showvalue=False, tickinterval=50, to=500, length=300)
# scale.pack()
#
# label = tkinter.Label(window, text="값 : 0")
# label.pack()


# # text
# # 여러 줄의 문자열 출력
# text = tkinter.Text(window)
#
# text.insert(tkinter.CURRENT, "안녕하세요.\n")
# text.insert("current", "반습니다.")
# # 두번째 줄 1번째 인덱스에 str 삽입
# text.insert(2.1, "갑")
#
# text.pack()
#
# # 1번째 줄 0 ~ (6-1)번 인덱스 "강조" 라는 속성 표현
# text.tag_add("강조", "1.0", "1.6")
# # "강조" 속성 설정
# text.tag_config("강조", background="yellow")
# # 1번째 줄 1 ~ (2-1)번까지 "강조" 속성 제거
# # 1번 인덱스만 속성 제거됨
# text.tag_remove("강조", "1.1", "1.2")


# # label frame
# # 다른 위젯들을 포함, 캡션 존재
# # 소규모의 체크 박스나 라디오 버튼을 구성하는 데 좋음
#
# # 라디오 버튼이 눌렸다면 해당 value 를 가져와 label 에 출력
# def check():
#     label.config(text=RadioVariety_1.get())
#
# labelframe = tkinter.LabelFrame(window, text="플랫폼 선택")
# labelframe.pack()
#
# # value 를 string 으로 가짐
# RadioVariety_1 = tkinter.StringVar()
# RadioVariety_1.set("미선택")
#
# radio1 = tkinter.Radiobutton(labelframe, text="Python", value="가능", variable=RadioVariety_1,
#                              command=check)
# radio1.pack()
# radio2 = tkinter.Radiobutton(labelframe, text="C/C++", value="부분 가능", variable=RadioVariety_1,
#                              command=check)
# radio2.pack()
# radio3 = tkinter.Radiobutton(labelframe, text="JSON", value="불가능", variable=RadioVariety_1,
#                              command=check)
# radio3.pack()
# label = tkinter.Label(labelframe, text="None")
# label.pack()


# # paned window
# # 위젯 포함, 구역 나눌 수 있는 내부 윈도우 생성 가능
# # label 2개와 panedwindow 1개를 저장할 panedwindow 생성
# panedwindow1 = tkinter.PanedWindow(relief="raised", bd=2)
# panedwindow1.pack(expand=True)
#
# left = tkinter.Label(panedwindow1, text="내부윈도우-1 (좌측)")
# panedwindow1.add(left)
#
# # label 2개를 가지는 panedwindow
# # 상위 panedwindow 안으로 들어감
# panedwindow2 = tkinter.PanedWindow(panedwindow1, orient="vertical", relief="groove", bd=3)
# panedwindow1.add(panedwindow2)
#
# right = tkinter.Label(panedwindow1, text="내부윈도우-2 (우측)")
# panedwindow1.add(right)
#
# top = tkinter.Label(panedwindow2, text="내부윈도우-3 (상단)")
# panedwindow2.add(top)
#
# bottom = tkinter.Label(panedwindow2, text="내부윈도우-4 (하단)")
# panedwindow2.add(bottom)


# # font
# import tkinter.font
#
# # 폰트 설정
# font = tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
#
# # 라벨에 폰트 설정 적용
# label = tkinter.Label(window, text="파이썬 3.6", font=font)
# label.pack()


# # photo image
# # 위젯 공간에 이미지 설정
# image = tkinter.PhotoImage(file="gang.png")
#
# label = tkinter.Label(window, image=image)
# label.pack()


# # bind
# # 위젯의 이벤트가 작동할 때 실행할 함수를 설정 가능
# # bind 는 중복 가능
# # 마우스 휠로 width 를 조절하고, width 두깨의 팬으로 캔버스에 그림
#
# width = 1
#
# # 마우스를 누를 때 캔버스에 칠함
# def drawing(event):
#     if width > 0:
#         x1 = event.x-1
#         y1 = event.y-1
#         x2 = event.x+1
#         y2 = event.y+1
#         canvas.create_oval(x1, y1, x2, y2, fill="blue", width=width)
#
# # 마우스 휠을 돌리면 width 를 바꿈
# def scroll(event):
#     global width
#     if event.delta == 120:      # 업스크롤
#         width += 1
#     if event.delta == -120:     # 다운스크롤
#         width -= 1
#     label.config(text=str(width))
#
# canvas = tkinter.Canvas(window, relief="solid", bd=2)
# canvas.pack(expand=True, fill="both")
# canvas.bind("<B1-Motion>", drawing)
# canvas.bind("<MouseWheel>", scroll)
#
# label = tkinter.Label(window, text=str(width))
# label.pack()


# # top level
# # 위젯들을 포함하는 외부 윈도우
# menubar = tkinter.Menu(window)
#
# menu_1 = tkinter.Menu(menubar, tearoff=0)
# menu_1.add_command(label="하위 메뉴 1-1")
# menu_1.add_command(label="하위 메뉴 1-2")
# menu_1.add_separator()
# menu_1.add_command(label="하위 메뉴 1-3")
# menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)
#
# # 위에서 만든 메뉴바를 포함하여 top level 생성
# toplevel = tkinter.Toplevel(window, menu=menubar)
# toplevel.geometry("320x200+820+100")
#
# # top level 에 추가되는 label
# label = tkinter.Label(toplevel, text="YUN DAE HEE")
# label.pack()


# spin box
# 수치를 조정하고 입력받는 창
label = tkinter.Label(window, text="숫자를 입력하세요.", height=3)
label.pack()

# 올바른 값이 존재하는지 체크 (유효성 검사)
def value_check(self):
    label.config(text="숫자를 입력하세요.")
    valid = False
    if self.isdigit():
        if (int(self) <= 50 and int(self) >= 0):
            valid = True
    elif self == '':
        valid = True
    return valid

# 에러 출력
def value_error(self):
    label.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

# spin box 에 사용할 함수를 가져옴
validate_command = (window.register(value_check), '%P')
invalid_command = (window.register(value_error), '%P')

spinbox = tkinter.Spinbox(window, from_=0, to=50, validate='all',
                          validatecommand=validate_command, invalidcommand=invalid_command)
spinbox.pack()


# 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
window.mainloop()
