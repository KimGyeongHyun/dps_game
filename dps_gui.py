import tkinter

if __name__ == '__main__':
    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    # 윈도우 창의 제목
    window.title("DPS 강화하기 유즈맵 계산기")
    # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
    window.geometry('1000x400+100+100')
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
    user_spec_panedwindow.pack(side="top")

    # 유저 스펙 중 강화확률 을 기입할 paned window 를 유저 스펙 paned window 에 배치
    upgrade_rate_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(upgrade_rate_panedwindow)

    # 유저 레벨 라벨
    user_level_label = tkinter.Label(upgrade_rate_panedwindow,
                                     text="유저 레벨 : ",
                                     anchor='w')
    upgrade_rate_panedwindow.add(user_level_label)
    user_level_label.grid(row=0, column=0)

    # 유저 레벨 엔트리
    first_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    first_upgrade_entry.insert(2, '1000')
    upgrade_rate_panedwindow.add(first_upgrade_entry)
    first_upgrade_entry.grid(row=0, column=1)

    # +1 강화확률 라벨
    first_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                        text="+1 강화 확률 : ",
                                        anchor='w')
    upgrade_rate_panedwindow.add(first_upgrade_label)
    first_upgrade_label.grid(row=1, column=0)
    
    # +1 강화확률 엔트리
    first_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    first_upgrade_entry.insert(2, '0.0')
    upgrade_rate_panedwindow.add(first_upgrade_entry)
    first_upgrade_entry.grid(row=1, column=1)


    # +2 강화확률 라벨
    second_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                         text="+2 강화 확률 : ",
                                         anchor='w')
    upgrade_rate_panedwindow.add(second_upgrade_label)
    second_upgrade_label.grid(row=2, column=0)

    # +2 강화확률 엔트리
    second_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    second_upgrade_entry.insert(2, '0.0')
    upgrade_rate_panedwindow.add(second_upgrade_entry)
    second_upgrade_entry.grid(row=2, column=1)

    # +3 강화확률 라벨
    third_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                        text="+3 강화 확률 : ",
                                        anchor='w')
    upgrade_rate_panedwindow.add(third_upgrade_label)
    third_upgrade_label.grid(row=3, column=0)

    # +3 강화확률 엔트리
    third_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    third_upgrade_entry.insert(2, '0.0')
    upgrade_rate_panedwindow.add(third_upgrade_entry)
    third_upgrade_entry.grid(row=3, column=1)

    # % 라벨
    percent1 = tkinter.Label(upgrade_rate_panedwindow, text='%')
    percent2 = tkinter.Label(upgrade_rate_panedwindow, text='%')
    percent3 = tkinter.Label(upgrade_rate_panedwindow, text='%')

    upgrade_rate_panedwindow.add(percent1)
    upgrade_rate_panedwindow.add(percent2)
    upgrade_rate_panedwindow.add(percent3)

    percent1.grid(row=1, column=2)
    percent2.grid(row=2, column=2)
    percent3.grid(row=3, column=2)

    # 유저 스펙 중 보스 라운드와 파티플레이 여부를 체크할 paned window 를 유저 스펙 paned window 에 배치
    boss_and_multy = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(boss_and_multy)

    # 개인 보스 처치 레벨 라벨
    private_boss_label = tkinter.Label(boss_and_multy, text='개인 보스 처치 레벨')
    boss_and_multy.add(private_boss_label)
    private_boss_label.grid(row=0, column=0)

    # 개인 보스 라디오 버튼을 눌렀을 때 발동되는 함수
    def check():
        pass
    
    # 개인 보스 처치 최대 레벨
    private_boss_count = tkinter.IntVar()
    private_0_ratio = tkinter.Radiobutton(boss_and_multy, text='0', value=0, 
                                          variable=private_boss_count, command=check)
    private_1_ratio = tkinter.Radiobutton(boss_and_multy, text='1', value=1, 
                                          variable=private_boss_count, command=check)
    private_2_ratio = tkinter.Radiobutton(boss_and_multy, text='2', value=2, 
                                          variable=private_boss_count, command=check)
    private_3_ratio = tkinter.Radiobutton(boss_and_multy, text='3', value=3, 
                                          variable=private_boss_count, command=check)
    private_4_ratio = tkinter.Radiobutton(boss_and_multy, text='4', value=4, 
                                          variable=private_boss_count, command=check)
    private_5_ratio = tkinter.Radiobutton(boss_and_multy, text='5', value=5, 
                                          variable=private_boss_count, command=check)

    boss_and_multy.add(private_0_ratio)
    boss_and_multy.add(private_1_ratio)
    boss_and_multy.add(private_2_ratio)
    boss_and_multy.add(private_3_ratio)
    boss_and_multy.add(private_4_ratio)
    boss_and_multy.add(private_5_ratio)

    private_0_ratio.grid(row=0, column=1)
    private_1_ratio.grid(row=0, column=2)
    private_2_ratio.grid(row=0, column=3)
    private_3_ratio.grid(row=0, column=4)
    private_4_ratio.grid(row=0, column=5)
    private_5_ratio.grid(row=0, column=6)

    # 파티 보스 처치 레벨 라벨
    party_boss_label = tkinter.Label(boss_and_multy, text='파티 보스 처치 레벨')
    boss_and_multy.add(party_boss_label)
    party_boss_label.grid(row=1, column=0)
    
    # 파티 보스 처치 최대 레벨
    party_boss_count = tkinter.IntVar()
    party_0_ratio = tkinter.Radiobutton(boss_and_multy, text='0', value=0,
                                        variable=party_boss_count, command=check)
    party_1_ratio = tkinter.Radiobutton(boss_and_multy, text='1', value=1,
                                        variable=party_boss_count, command=check)
    party_2_ratio = tkinter.Radiobutton(boss_and_multy, text='2', value=2,
                                        variable=party_boss_count, command=check)
    party_3_ratio = tkinter.Radiobutton(boss_and_multy, text='3', value=3,
                                        variable=party_boss_count, command=check)
    party_4_ratio = tkinter.Radiobutton(boss_and_multy, text='4', value=4,
                                        variable=party_boss_count, command=check)
    party_5_ratio = tkinter.Radiobutton(boss_and_multy, text='5', value=5,
                                        variable=party_boss_count, command=check)

    boss_and_multy.add(party_0_ratio)
    boss_and_multy.add(party_1_ratio)
    boss_and_multy.add(party_2_ratio)
    boss_and_multy.add(party_3_ratio)
    boss_and_multy.add(party_4_ratio)
    boss_and_multy.add(party_5_ratio)

    party_0_ratio.grid(row=1, column=1)
    party_1_ratio.grid(row=1, column=2)
    party_2_ratio.grid(row=1, column=3)
    party_3_ratio.grid(row=1, column=4)
    party_4_ratio.grid(row=1, column=5)
    party_5_ratio.grid(row=1, column=6)

    # 파티 플레이 여부 레이블
    party_check_label = tkinter.Label(boss_and_multy, text='파티 플레이 버프 여부')
    boss_and_multy.add(party_check_label)
    party_check_label.grid(row=2, column=0)

    # 파티 플레이 여부 체크 박스
    party_check = tkinter.BooleanVar()
    party_check_button = tkinter.Checkbutton(boss_and_multy, text='', onvalue=True, offvalue=False,
                                             variable=party_check)
    boss_and_multy.add(party_check_button)
    party_check_button.grid(row=2, column=1)

    # 유닛 시작 레벨, 마지막 레벨, 판매권 수, 리얼 타임 진행 시간
    # 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
    unit_information = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(unit_information)

    # 유닛 시작 레벨 레이블
    unit_start_level_label = tkinter.Label(unit_information, text='유닛 시작 레벨 : ')
    unit_information.add(unit_start_level_label)
    unit_start_level_label.grid(row=0, column=0)

    # 유닛 시작 레벨 엔트리
    unit_start_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_start_level_entry.insert(1, '28')
    unit_information.add(unit_start_level_entry)
    unit_start_level_entry.grid(row=0, column=1)

    # 유닛 마지막 레벨 레이블
    unit_last_level_label = tkinter.Label(unit_information, text='유닛 마지막 레벨 : ')
    unit_information.add(unit_last_level_label)
    unit_last_level_label.grid(row=1, column=0)

    # 유닛 마지막 레벨 엔트리
    unit_last_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_last_level_entry.insert(1, '40')
    unit_information.add(unit_last_level_entry)
    unit_last_level_entry.grid(row=1, column=1)
    
    # 판매권 수 레이블
    sell_ticket_label = tkinter.Label(unit_information, text='판매권 개수 : ')
    unit_information.add(sell_ticket_label)
    sell_ticket_label.grid(row=2, column=0)
    
    # 판매권 수 엔트리
    sell_ticket_entry = tkinter.Entry(unit_information, width=3, justify='center')
    sell_ticket_entry.insert(1, '500')
    unit_information.add(sell_ticket_entry)
    sell_ticket_entry.grid(row=2, column=1)

    # 방치 시간 레이블
    playing_time_label = tkinter.Label(unit_information, text='리얼 타임 진행 시간 : ')
    playing_hour_label = tkinter.Label(unit_information, text=' 시간 ')
    playing_minute_label = tkinter.Label(unit_information, text=' 분 ')
    playing_second_label = tkinter.Label(unit_information, text=' 초')

    # 방치 시간 엔트리
    playing_hour_entry = tkinter.Entry(unit_information, width=3, justify='center')
    playing_minute_entry = tkinter.Entry(unit_information, width=3, justify='center')
    playing_second_entry = tkinter.Entry(unit_information, width=3, justify='center')

    playing_hour_entry.insert(1, '3')
    playing_minute_entry.insert(1, '0')
    playing_second_entry.insert(1, '0')

    unit_information.add(playing_time_label)
    unit_information.add(playing_hour_label)
    unit_information.add(playing_hour_entry)
    unit_information.add(playing_minute_label)
    unit_information.add(playing_minute_entry)
    unit_information.add(playing_second_label)
    unit_information.add(playing_second_entry)

    playing_time_label.grid(row=3, column=0)
    playing_hour_label.grid(row=3, column=2)
    playing_hour_entry.grid(row=3, column=1)
    playing_minute_label.grid(row=3, column=4)
    playing_minute_entry.grid(row=3, column=3)
    playing_second_label.grid(row=3, column=6)
    playing_second_entry.grid(row=3, column=5)

    # 플레이어 시작 레벨(디폴트는 현재 플레이어 레벨), 목표 레벨, 판매 유닛과 수
    # 의 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
    player_level_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(player_level_panedwindow)

    # 플레이어 시작 레벨 라벨
    player_start_level_label = tkinter.Label(player_level_panedwindow, text='플레이어 시작 레벨 : ')
    player_level_panedwindow.add(player_start_level_label)
    player_start_level_label.grid(row=0, column=0)

    # 플레이어 시작 레벨 엔트리
    player_start_level_entry = tkinter.Entry(player_level_panedwindow, width=7, justify='center')
    player_start_level_entry.insert(2, '1000')
    player_level_panedwindow.add(player_start_level_entry)
    player_start_level_entry.grid(row=0, column=1)

    # 플레이어 마지막 레벨 라벨
    player_end_level_label = tkinter.Label(player_level_panedwindow, text='플레이어 마지막 레벨 : ')
    player_level_panedwindow.add(player_end_level_label)
    player_end_level_label.grid(row=1, column=0)

    # 플레이어 마지막 레벨 엔트리
    player_end_level_entry = tkinter.Entry(player_level_panedwindow, width=7, justify='center')
    player_end_level_entry.insert(2, '2000')
    player_level_panedwindow.add(player_end_level_entry)
    player_end_level_entry.grid(row=1, column=1)

    # 판매 유닛 레벨 라벨
    sell_unit_level_label = tkinter.Label(player_level_panedwindow, text='판매할 유닛 레벨 : ')
    player_level_panedwindow.add(sell_unit_level_label)
    sell_unit_level_label.grid(row=2, column=0)

    # 판매 유닛 레벨 엔트리
    sell_unit_level_entry = tkinter.Entry(player_level_panedwindow, width=3, justify='center')
    sell_unit_level_entry.insert(1, '40')
    player_level_panedwindow.add(sell_unit_level_entry)
    sell_unit_level_entry.grid(row=2, column=1)

    # 판매 유닛 수량 라벨
    sell_unit_number_label = tkinter.Label(player_level_panedwindow, text='판매할 유닛 수량 : ')
    player_level_panedwindow.add(sell_unit_number_label)
    sell_unit_number_label.grid(row=3, column=0)

    # 판매 유닛 수량 엔트리
    sell_unit_number_entry = tkinter.Entry(player_level_panedwindow, width=7, justify='center')
    sell_unit_number_entry.insert(2, '500')
    player_level_panedwindow.add(sell_unit_number_entry)
    sell_unit_number_entry.grid(row=3, column=1)
    

    # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
    window.mainloop()

