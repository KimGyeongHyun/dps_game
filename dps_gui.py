import tkinter
import dps_upgrade

if __name__ == '__main__':
    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    # 윈도우 창의 제목
    window.title("DPS 강화하기 유즈맵 계산기")
    # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
    window.geometry('1200x400+100+100')
    # 윈도우 창 크기 조절 가능 여부 설정
    window.resizable(True, True)

    ###########################
    # 여기에 위젯 추가
    game = dps_upgrade.Game()

    # 유저 스펙, 보스, 파티 플레이 여부 상태가 바뀌었을 때 실행
    # 처음 실행할 때도 실행
    # 모든 출력을 다시 갱신하여 출력
    def get_value_calculate_print_all():
        try:
            user_level = float(user_level_entry.get())
            first = float(first_upgrade_entry.get())/100
            second = float(second_upgrade_entry.get())/100
            third = float(third_upgrade_entry.get())/100
            user_damage = float(user_damage_upgrade_entry.get())/100
            private_boss = int(private_boss_count.get())
            party_boss = int(party_boss_count.get())
            multy_player = bool(party_check.get())
        except ValueError:
            return

        game.set_value(user_level, first, second, third, user_damage,
                       private_boss, party_boss, multy_player)
        print(game.return_user_spec())
        print(game.return_unit_info())

        unit_upgrade_rate_listbox.delete(0, 40)
        unit_dps_listbox.delete(0, 40)
        unit_exp_listbox.delete(0, 40)

        for i in range(len(game.unit_dict)):
            unit_level = i + 1
            unit_upgrade_rate_listbox.insert(unit_level, game.unit_dict[unit_level].__str__())
            unit_dps_listbox.insert(unit_level, game.unit_dict[unit_level].print_unit_dps())
            unit_exp_listbox.insert(unit_level, game.unit_dict[unit_level].print_unit_exp())

    def get_entry_value_calculate_print_all(event):
        get_value_calculate_print_all()

    # 처음 안내문
    first_information_label = tkinter.Label(window, text="유저 정보를 입력하고 엔터를 눌러주세요.",
                                            anchor='w')
    first_information_label.pack(side="top", fill="x")

    # 유저 스펙을 기입할 paned window 를 상단에 배치
    user_spec_panedwindow = tkinter.PanedWindow()
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
    user_level_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    user_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    user_level_entry.insert(2, '5000')
    upgrade_rate_panedwindow.add(user_level_entry)
    user_level_entry.grid(row=0, column=1)

    # +1 강화확률 라벨
    first_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                        text="+1 강화 확률 : ",
                                        anchor='w')
    upgrade_rate_panedwindow.add(first_upgrade_label)
    first_upgrade_label.grid(row=1, column=0)
    
    # +1 강화확률 엔트리
    first_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    first_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    first_upgrade_entry.insert(2, '10.0')
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
    second_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    second_upgrade_entry.insert(2, '5.0')
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
    third_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    third_upgrade_entry.insert(2, '3.0')
    upgrade_rate_panedwindow.add(third_upgrade_entry)
    third_upgrade_entry.grid(row=3, column=1)

    # 유저 공격력 업그레이드 라벨
    user_damage_upgrade_label = tkinter.Label(upgrade_rate_panedwindow,
                                              text="유저 공업 : ",
                                              anchor='w')
    upgrade_rate_panedwindow.add(user_damage_upgrade_label)
    user_damage_upgrade_label.grid(row=4, column=0)

    # 유저 공격력 업그레이드 엔트리
    user_damage_upgrade_entry = tkinter.Entry(upgrade_rate_panedwindow, width=7, justify='center')
    user_damage_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    user_damage_upgrade_entry.insert(2, '500')
    upgrade_rate_panedwindow.add(user_damage_upgrade_entry)
    user_damage_upgrade_entry.grid(row=4, column=1)

    # % 라벨
    percent1 = tkinter.Label(upgrade_rate_panedwindow, text='%')
    percent2 = tkinter.Label(upgrade_rate_panedwindow, text='%')
    percent3 = tkinter.Label(upgrade_rate_panedwindow, text='%')
    percent4 = tkinter.Label(upgrade_rate_panedwindow, text='%')

    upgrade_rate_panedwindow.add(percent1)
    upgrade_rate_panedwindow.add(percent2)
    upgrade_rate_panedwindow.add(percent3)
    upgrade_rate_panedwindow.add(percent4)

    percent1.grid(row=1, column=2)
    percent2.grid(row=2, column=2)
    percent3.grid(row=3, column=2)
    percent4.grid(row=4, column=2)

    # 유저 스펙 중 보스 라운드와 파티플레이 여부를 체크할 paned window 를 유저 스펙 paned window 에 배치
    boss_and_multy = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.add(boss_and_multy)

    # 개인 보스 처치 레벨 라벨
    private_boss_label = tkinter.Label(boss_and_multy, text='개인 보스 처치 레벨')
    boss_and_multy.add(private_boss_label)
    private_boss_label.grid(row=0, column=0)

    # 개인 보스 처치 최대 레벨
    private_boss_count = tkinter.IntVar()
    private_0_ratio = tkinter.Radiobutton(boss_and_multy, text='0', value=0, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_1_ratio = tkinter.Radiobutton(boss_and_multy, text='1', value=1, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_2_ratio = tkinter.Radiobutton(boss_and_multy, text='2', value=2, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_3_ratio = tkinter.Radiobutton(boss_and_multy, text='3', value=3, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_4_ratio = tkinter.Radiobutton(boss_and_multy, text='4', value=4, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_5_ratio = tkinter.Radiobutton(boss_and_multy, text='5', value=5, 
                                          variable=private_boss_count, command=get_value_calculate_print_all)
    private_5_ratio.select()

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
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_1_ratio = tkinter.Radiobutton(boss_and_multy, text='1', value=1,
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_2_ratio = tkinter.Radiobutton(boss_and_multy, text='2', value=2,
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_3_ratio = tkinter.Radiobutton(boss_and_multy, text='3', value=3,
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_4_ratio = tkinter.Radiobutton(boss_and_multy, text='4', value=4,
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_5_ratio = tkinter.Radiobutton(boss_and_multy, text='5', value=5,
                                        variable=party_boss_count, command=get_value_calculate_print_all)
    party_5_ratio.select()

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
                                             variable=party_check, command=get_value_calculate_print_all)
    boss_and_multy.add(party_check_button)
    party_check_button.select()
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

    # 유닛 정보를 담을 paned window 생성
    unit_information_panedwindow = tkinter.PanedWindow()
    unit_information_panedwindow.pack(side="top")

    # 유닛 강화 확률 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_upgrade_rate_frame = tkinter.Frame(unit_information_panedwindow, padx=5, pady=5)

    unit_upgrade_rate_scrollbar = tkinter.Scrollbar(unit_upgrade_rate_frame)
    unit_upgrade_rate_scrollbar.pack(side='right', fill='y')

    unit_upgrade_rate_listbox = tkinter.Listbox(unit_upgrade_rate_frame,
                                                yscrollcommand=unit_upgrade_rate_scrollbar.set,
                                                width=38)
    unit_upgrade_rate_listbox.pack(side='left')

    unit_upgrade_rate_scrollbar["command"] = unit_upgrade_rate_listbox.yview

    unit_upgrade_rate_frame.pack(side='left')

    # 유닛 dps 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_dps_frame = tkinter.Frame(unit_information_panedwindow, padx=5, pady=5)

    unit_dps_scrollbar = tkinter.Scrollbar(unit_dps_frame)
    unit_dps_scrollbar.pack(side='right', fill='y')

    unit_dps_listbox = tkinter.Listbox(unit_dps_frame,
                                       yscrollcommand=unit_dps_scrollbar.set,
                                       width=42)
    unit_dps_listbox.pack(side='left')

    unit_dps_scrollbar["command"] = unit_dps_listbox.yview

    unit_dps_frame.pack(side='left')

    # 유닛 exp 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_exp_frame = tkinter.Frame(unit_information_panedwindow, padx=5, pady=5)

    unit_exp_scrollbar = tkinter.Scrollbar(unit_exp_frame)
    unit_exp_scrollbar.pack(side='right', fill='y')

    unit_exp_listbox = tkinter.Listbox(unit_exp_frame,
                                       yscrollcommand=unit_exp_scrollbar.set,
                                       width=57)
    unit_exp_listbox.pack(side='left')

    unit_exp_scrollbar["command"] = unit_exp_listbox.yview

    unit_exp_frame.pack(side='left')


    # 처음 디폴트 출력
    get_value_calculate_print_all()

    # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
    window.mainloop()

