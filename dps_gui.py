import tkinter

if __name__ == '__main__':
    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    # 윈도우 창의 제목
    window.title("DPS 강화하기 유즈맵 계산기")
    # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
    window.geometry('640x400+100+100')
    # 윈도우 창 크기 조절 가능 여부 설정
    window.resizable(True, True)

    ###########################
    # 여기에 위젯 추가

    # 처음 안내문
    first_information_label = tkinter.Label(window, text="유저 정보를 입력하시기 바랍니다.",
                                            anchor='w')
    first_information_label.pack(side="top", fill="x")

    # 유저 스펙을 기입할 paned window 를 상단에 배치
    user_spec_panedwindow = tkinter.PanedWindow(relief="solid", bd=2)
    user_spec_panedwindow.pack(side="top", fill="x")

    # 유저 스펙 중 강화확률 을 기입할 paned window 를 유저 스펙 paned window 에 배치
    upgrade_rate_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(upgrade_rate_panedwindow)

    first_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                        text="+1 강화 확률 : ",
                                        anchor='w')
    upgrade_rate_panedwindow.add(first_upgrade_label)

    first_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=10)
    upgrade_rate_panedwindow.add(first_upgrade_entry)

    # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
    window.mainloop()

