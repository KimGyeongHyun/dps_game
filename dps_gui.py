import tkinter
import tkinter.messagebox
import dps_upgrade

END = 40

if __name__ == '__main__':
    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    # 윈도우 창의 제목
    window.title("DPS 강화하기 유즈맵 계산기")
    # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
    window.geometry('1300x800+100+100')
    # 윈도우 창 크기 조절 가능 여부 설정
    window.resizable(False, False)

    ###########################
    # 여기에 위젯 추가
    game = dps_upgrade.Game()


    # 유저 스펙, 보스, 파티 플레이 여부 상태가 바뀌었을 때 실행
    # 처음 실행할 때도 실행
    # 모든 출력을 다시 갱신하여 출력
    def get_value_calculate_print_all():

        # 타입 유효성 검사
        try:
            user_number = float(user_number_entry.get())
            first = float(first_upgrade_entry.get()) / 100
            second = float(second_upgrade_entry.get()) / 100
            third = float(third_upgrade_entry.get()) / 100
            user_damage = int(user_damage_upgrade_entry.get())
            private_boss = int(private_boss_count.get())
            party_boss = int(party_boss_count.get())
            multy_player = bool(party_check.get())
            unit_start_level = int(unit_start_level_entry.get())
            unit_last_level = int(unit_last_level_entry.get())
            sell_ticket = int(sell_ticket_entry.get())
            hour = int(playing_hour_entry.get())
            minute = int(playing_minute_entry.get())
            seconds = int(playing_second_entry.get())
            player_start_level = int(player_start_level_entry.get())
            player_last_level = int(player_end_level_entry.get())
            level_of_sell = int(sell_unit_level_entry.get())
            number_of_sell = int(sell_unit_number_entry.get())
        except ValueError:
            print('ValueError in user spec input parameter')
            return

        # 숫자 범위 유효성 검사
        if user_number < 1 or user_number > 10000:
            tkinter.messagebox.showinfo("유저 레벨 오류",
                                        "유저 레벨은 1 ~ 10000 사이의 정수 값을 입력해야 합니다.")
            return

        if first < 0 or first > 0.1:
            tkinter.messagebox.showinfo("+1 강화 확률 오류",
                                        "+1 강화 확률은 0.0 % ~ 10.0 % 사이의 값을 입력해야 합니다.")
            return

        if second < 0 or second > 0.05:
            tkinter.messagebox.showinfo("+2 강화 확률 오류",
                                        "+2 강화 확률은 0.0 % ~ 5.0 % 사이의 값을 입력해야 합니다.")
            return

        if third < 0 or third > 0.03:
            tkinter.messagebox.showinfo("+3 강화 확률 오류",
                                        "+3 강화 확률은 0.0 % ~ 3.0 % 사이의 값을 입력해야 합니다.")
            return

        if user_damage < 0 or user_damage > 50:
            tkinter.messagebox.showinfo("유저 공업 오류",
                                        "유저 공업은 0 ~ 50 사이의 정수 값을 입력해야 합니다.")
            return

        if unit_start_level < 1 or unit_last_level > 40:
            tkinter.messagebox.showinfo("유닛 시작 레벨 오류",
                                        "유닛 시작 레벨은 1 ~ 40 사이의 정수 값을 입력해야 합니다.")
            return

        if unit_last_level < 1 or unit_last_level > 40:
            tkinter.messagebox.showinfo("유닛 마지막 레벨 오류",
                                        "유닛 마지막 레벨은 1 ~ 40 사이의 정수 값을 입력해야 합니다.")
            return

        if unit_start_level > unit_last_level:
            tkinter.messagebox.showinfo("유닛 레벨 오류",
                                        "유닛 마지막 레벨이 유닛 시작 레벨보다 커야 합니다.")
            return

        if sell_ticket < 0:
            tkinter.messagebox.showinfo("판매권 개수",
                                        "판매권 개수는 자연수를 입력해야 합니다.")
            return

        if hour < 0:
            tkinter.messagebox.showinfo("시간 오류 (시)",
                                        "시간은 자연수를 입력해야 합니다.")
            return

        if minute < 0:
            tkinter.messagebox.showinfo("시간 오류 (분)",
                                        "시간은 자연수를 입력해야 합니다.")
            return

        if seconds < 0:
            tkinter.messagebox.showinfo("시간 오류 (초)",
                                        "시간은 자연수를 입력해야 합니다.")
            return

        if player_start_level < 1 or player_start_level > 10000:
            tkinter.messagebox.showinfo("플레이어 시작 레벨 오류",
                                        "플레이어 레벨은 1 ~ 10000 사이의 정수를 입력해야 합니다.")
            return

        if player_last_level < 1 or player_last_level > 10000:
            tkinter.messagebox.showinfo("플레이어 마지막 레벨 오류",
                                        "플레이어 레벨은 1 ~ 10000 사이의 정수를 입력해야 합니다.")
            return

        if player_start_level > player_last_level:
            tkinter.messagebox.showinfo("플레이어 레벨 오류",
                                        "플레이어 마지막 레벨은 플레이어 시작 레벨보다 커야 합니다.")
            return

        if level_of_sell < 1 or level_of_sell > 40:
            print(level_of_sell)
            tkinter.messagebox.showinfo("판매할 유닛 레벨 오류",
                                        "유닛 레벨은 1 ~ 40 사이의 정수 값을 입력해야 합니다.")
            return

        if number_of_sell < 0:
            tkinter.messagebox.showinfo("판매할 유닛 수량 오류",
                                        "유닛 수량은 자연수를 입력해야 합니다.")
            return

        user_damage = user_damage * 0.1

        game.set_value(user_number, first, second, third, user_damage,
                       private_boss, party_boss, multy_player)

        # print(game.return_user_spec())
        # print(game.return_unit_info())
        # print(game.return_unit_dps_info())
        # print(game.return_unit_exp_info())

        unit_upgrade_rate_listbox.delete(0, END)
        unit_dps_listbox.delete(0, END)
        unit_exp_listbox.delete(0, END)

        user_spec_label.config(text=game.return_user_spec())

        for i in range(len(game.unit_dict)):
            unit_number = i + 1
            unit_upgrade_rate_listbox.insert(unit_number, game.unit_dict[unit_number].__str__())
            unit_upgrade_rate_listbox.see(END)
            unit_dps_listbox.insert(unit_number, game.unit_dict[unit_number].print_unit_dps())
            unit_dps_listbox.see(END)
            unit_exp_listbox.insert(unit_number, game.unit_dict[unit_number].print_unit_exp())
            unit_exp_listbox.see(END)

        level_to_level_label.config(text=game.unit_calc.return_str_level_to_level(unit_start_level,
                                                                                  unit_last_level,
                                                                                  sell_ticket)
                                    + "\n\n"
                                    + game.unit_calc.return_str_sell_number_level_to_level(unit_start_level,
                                                                                           unit_last_level,
                                                                                           hour,
                                                                                           minute,
                                                                                           seconds))
        
        player_calc_label.config(text=game.player_calc.return_str_exp_to_level_up(player_start_level)
                                 + "\n\n"
                                 + game.player_calc.return_str_need_number_of_unit_to_level_up(player_start_level,
                                                                                               player_last_level)
                                 + game.player_calc.return_str_final_level_with_units(player_start_level,
                                                                                      level_of_sell,
                                                                                      number_of_sell))

    def get_entry_value_calculate_print_all(event):
        get_value_calculate_print_all()


    # 처음 안내문
    first_information_label = tkinter.Label(window, text="아무 칸에 숫자를 입력하고 엔터를 눌러주세요.\n"
                                                         "유닛 레벨 계산은 유저 스펙이 적용된 유닛의 강화확률 기반으로 비교됩니다.\n"
                                                         "",
                                            anchor='w',
                                            justify='left')
    first_information_label.pack(side="top", fill="x")

    # 유저 스펙을 기입할 paned window 를 상단에 배치
    user_spec_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.pack(side="top")

    # 유저 스펙 라벨 표시
    user_spec_label = tkinter.Label(user_spec_panedwindow, text="유저 스펙")
    boss_and_multi_label = tkinter.Label(user_spec_panedwindow, text="보스 최대 레벨, 파티플레이 버프 여부")
    unit_level_calculate_label = tkinter.Label(user_spec_panedwindow, text="유닛 레벨 계산")
    player_level_calculate_label = tkinter.Label(user_spec_panedwindow, text="플레이어 레벨 계산")

    user_spec_label.grid(row=0, column=0)
    boss_and_multi_label.grid(row=0, column=1)
    unit_level_calculate_label.grid(row=0, column=2)
    player_level_calculate_label.grid(row=0, column=3)

    # 유저 스펙 중 강화확률 을 기입할 paned window 를 유저 스펙 paned window 에 배치
    upgrade_rate_frame = tkinter.Frame(user_spec_panedwindow, padx=30)
    user_spec_panedwindow.add(upgrade_rate_frame)
    upgrade_rate_frame.grid(row=1, column=0)

    # 유저 레벨 라벨
    user_number_label = tkinter.Label(upgrade_rate_frame,
                                      text="유저 레벨 : ")
    user_number_label.grid(row=0, column=0)

    # 유저 레벨 엔트리
    user_number_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    user_number_entry.bind("<Return>", get_entry_value_calculate_print_all)
    user_number_entry.insert(2, '5000')
    user_number_entry.grid(row=0, column=1)

    # +1 강화확률 라벨
    first_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                        text="+1 강화 확률 : ")
    first_upgrade_label.grid(row=1, column=0)

    # +1 강화확률 엔트리
    first_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    first_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    first_upgrade_entry.insert(2, '10.0')
    first_upgrade_entry.grid(row=1, column=1)

    # +2 강화확률 라벨
    second_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                         text="+2 강화 확률 : ")
    second_upgrade_label.grid(row=2, column=0)

    # +2 강화확률 엔트리
    second_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    second_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    second_upgrade_entry.insert(2, '5.0')
    second_upgrade_entry.grid(row=2, column=1)

    # +3 강화확률 라벨
    third_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                        text="+3 강화 확률 : ")
    third_upgrade_label.grid(row=3, column=0)

    # +3 강화확률 엔트리
    third_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    third_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    third_upgrade_entry.insert(2, '3.0')
    third_upgrade_entry.grid(row=3, column=1)

    # 유저 공격력 업그레이드 라벨
    user_damage_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                              text="유저 공업 : ")
    user_damage_upgrade_label.grid(row=4, column=0)

    # 유저 공격력 업그레이드 엔트리
    user_damage_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    user_damage_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    user_damage_upgrade_entry.insert(2, '50')
    user_damage_upgrade_entry.grid(row=4, column=1)

    # % 라벨
    percent1 = tkinter.Label(upgrade_rate_frame, text='%')
    percent2 = tkinter.Label(upgrade_rate_frame, text='%')
    percent3 = tkinter.Label(upgrade_rate_frame, text='%')
    percent4 = tkinter.Label(upgrade_rate_frame, text='강')

    percent1.grid(row=1, column=2)
    percent2.grid(row=2, column=2)
    percent3.grid(row=3, column=2)
    percent4.grid(row=4, column=2)

    # 유저 스펙 중 보스 라운드와 파티플레이 여부를 체크할 paned window 를 유저 스펙 paned window 에 배치
    boss_and_multy = tkinter.Frame(user_spec_panedwindow, padx=30)
    user_spec_panedwindow.add(boss_and_multy)
    boss_and_multy.grid(row=1, column=1)

    # 개인 보스 처치 레벨 라벨
    private_boss_label = tkinter.Label(boss_and_multy, text='개인 보스 처치 레벨')
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

    private_0_ratio.grid(row=0, column=1)
    private_1_ratio.grid(row=0, column=2)
    private_2_ratio.grid(row=0, column=3)
    private_3_ratio.grid(row=0, column=4)
    private_4_ratio.grid(row=0, column=5)
    private_5_ratio.grid(row=0, column=6)

    # 파티 보스 처치 레벨 라벨
    party_boss_label = tkinter.Label(boss_and_multy, text='파티 보스 처치 레벨')
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

    party_0_ratio.grid(row=1, column=1)
    party_1_ratio.grid(row=1, column=2)
    party_2_ratio.grid(row=1, column=3)
    party_3_ratio.grid(row=1, column=4)
    party_4_ratio.grid(row=1, column=5)
    party_5_ratio.grid(row=1, column=6)

    # 파티 플레이 여부 레이블
    party_check_label = tkinter.Label(boss_and_multy, text='파티 플레이 버프 여부')
    party_check_label.grid(row=2, column=0)

    # 파티 플레이 여부 체크 박스
    party_check = tkinter.BooleanVar()
    party_check_button = tkinter.Checkbutton(boss_and_multy, text='', onvalue=True, offvalue=False,
                                             variable=party_check, command=get_value_calculate_print_all)
    party_check_button.select()
    party_check_button.grid(row=2, column=1)

    # 유저 스펙 레이블
    user_spec_label = tkinter.Label(window)
    user_spec_label.pack(side="top", pady=10)

    # 유닛 시작 레벨, 마지막 레벨, 판매권 수, 리얼 타임 진행 시간
    # 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
    unit_information = tkinter.Frame(user_spec_panedwindow, padx=30)
    user_spec_panedwindow.add(unit_information)
    unit_information.grid(row=1, column=2)

    # 유닛 시작 레벨 레이블
    unit_start_level_label = tkinter.Label(unit_information, text='유닛 시작 레벨 : ')
    unit_start_level_label.grid(row=0, column=0)

    # 유닛 시작 레벨 엔트리
    unit_start_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_start_level_entry.insert(1, '28')
    unit_start_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    unit_start_level_entry.grid(row=0, column=1)

    # 유닛 마지막 레벨 레이블
    unit_last_level_label = tkinter.Label(unit_information, text='유닛 마지막 레벨 : ')
    unit_last_level_label.grid(row=1, column=0)

    # 유닛 마지막 레벨 엔트리
    unit_last_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_last_level_entry.insert(1, '40')
    unit_last_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    unit_last_level_entry.grid(row=1, column=1)

    # 판매권 수 레이블
    sell_ticket_label = tkinter.Label(unit_information, text='판매권 개수 : ')
    sell_ticket_label.grid(row=2, column=0)

    # 판매권 수 엔트리
    sell_ticket_entry = tkinter.Entry(unit_information, width=6, justify='center')
    sell_ticket_entry.insert(1, '500')
    sell_ticket_entry.bind("<Return>", get_entry_value_calculate_print_all)
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

    playing_hour_entry.bind("<Return>", get_entry_value_calculate_print_all)
    playing_minute_entry.bind("<Return>", get_entry_value_calculate_print_all)
    playing_second_entry.bind("<Return>", get_entry_value_calculate_print_all)

    playing_time_label.grid(row=3, column=0)
    playing_hour_label.grid(row=3, column=2)
    playing_hour_entry.grid(row=3, column=1)
    playing_minute_label.grid(row=3, column=4)
    playing_minute_entry.grid(row=3, column=3)
    playing_second_label.grid(row=3, column=6)
    playing_second_entry.grid(row=3, column=5)

    # 플레이어 시작 레벨(디폴트는 현재 플레이어 레벨), 목표 레벨, 판매 유닛과 수
    # 의 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
    player_level_frame = tkinter.Frame(user_spec_panedwindow, padx=30)
    user_spec_panedwindow.add(player_level_frame)
    player_level_frame.grid(row=1, column=3)

    # 플레이어 시작 레벨 라벨
    player_start_level_label = tkinter.Label(player_level_frame, text='플레이어 시작 레벨 : ')
    player_start_level_label.grid(row=0, column=0)

    # 플레이어 시작 레벨 엔트리
    player_start_level_entry = tkinter.Entry(player_level_frame, width=7, justify='center')
    player_start_level_entry.insert(2, '1000')
    player_start_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    player_start_level_entry.grid(row=0, column=1)

    # 플레이어 마지막 레벨 라벨
    player_end_level_label = tkinter.Label(player_level_frame, text='플레이어 마지막 레벨 : ')
    player_end_level_label.grid(row=1, column=0)

    # 플레이어 마지막 레벨 엔트리
    player_end_level_entry = tkinter.Entry(player_level_frame, width=7, justify='center')
    player_end_level_entry.insert(2, '2000')
    player_end_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    player_end_level_entry.grid(row=1, column=1)

    # 판매 유닛 레벨 라벨
    sell_unit_level_label = tkinter.Label(player_level_frame, text='판매할 유닛 레벨 : ')
    sell_unit_level_label.grid(row=2, column=0)

    # 판매 유닛 레벨 엔트리
    sell_unit_level_entry = tkinter.Entry(player_level_frame, width=3, justify='center')
    sell_unit_level_entry.insert(1, '40')
    sell_unit_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    sell_unit_level_entry.grid(row=2, column=1)

    # 판매 유닛 수량 라벨
    sell_unit_number_label = tkinter.Label(player_level_frame, text='판매할 유닛 수량 : ')
    sell_unit_number_label.grid(row=3, column=0)

    # 판매 유닛 수량 엔트리
    sell_unit_number_entry = tkinter.Entry(player_level_frame, width=7, justify='center')
    sell_unit_number_entry.insert(2, '500')
    sell_unit_number_entry.bind("<Return>", get_entry_value_calculate_print_all)
    sell_unit_number_entry.grid(row=3, column=1)

    # 유닛 정보를 담을 paned window 생성
    unit_information_panedwindow = tkinter.PanedWindow()
    unit_information_panedwindow.pack(side="top", pady=30)

    # 유닛 정보 레이블
    unit_upgrade_rate_label = tkinter.Label(unit_information_panedwindow, text="유닛 강화 확률")
    unit_dps_label = tkinter.Label(unit_information_panedwindow, text="유닛 dps 정보")
    unit_exp_label = tkinter.Label(unit_information_panedwindow, text="유닛 exp 정보")

    unit_upgrade_rate_label.grid(row=0, column=0)
    unit_dps_label.grid(row=0, column=1)
    unit_exp_label.grid(row=0, column=2)

    # 유닛 강화 확률 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_upgrade_rate_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_upgrade_rate_scrollbar = tkinter.Scrollbar(unit_upgrade_rate_frame)
    unit_upgrade_rate_scrollbar.pack(side='right', fill='y')

    unit_upgrade_rate_listbox = tkinter.Listbox(unit_upgrade_rate_frame,
                                                yscrollcommand=unit_upgrade_rate_scrollbar.set,
                                                width=38, height=15)
    unit_upgrade_rate_listbox.pack(side='left')

    unit_upgrade_rate_scrollbar["command"] = unit_upgrade_rate_listbox.yview

    unit_upgrade_rate_frame.grid(row=1, column=0)

    # 유닛 dps 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_dps_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_dps_scrollbar = tkinter.Scrollbar(unit_dps_frame)
    unit_dps_scrollbar.pack(side='right', fill='y')

    unit_dps_listbox = tkinter.Listbox(unit_dps_frame,
                                       yscrollcommand=unit_dps_scrollbar.set,
                                       width=42, height=15)
    unit_dps_listbox.pack(side='left')

    unit_dps_scrollbar["command"] = unit_dps_listbox.yview

    unit_dps_frame.grid(row=1, column=1)

    # 유닛 exp 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_exp_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_exp_scrollbar = tkinter.Scrollbar(unit_exp_frame)
    unit_exp_scrollbar.pack(side='right', fill='y')

    unit_exp_listbox = tkinter.Listbox(unit_exp_frame,
                                       yscrollcommand=unit_exp_scrollbar.set,
                                       width=57, height=15)
    unit_exp_listbox.pack(side='left')

    unit_exp_scrollbar["command"] = unit_exp_listbox.yview

    unit_exp_frame.grid(row=1, column=2)

    # 나머지 정보들을 담을 paned window
    the_other_panedwindow = tkinter.PanedWindow()
    the_other_panedwindow.pack(side='top')

    # level to level 제목 레이블
    level_to_level_title_lable = tkinter.Label(the_other_panedwindow, padx=75)
    level_to_level_title_lable.config(text="===============유닛 레벨 계산 결과===============\n")
    level_to_level_title_lable.grid(row=0, column=0)

    # player level calc 제목 레이블
    player_calc_title_label = tkinter.Label(the_other_panedwindow, padx=75)
    player_calc_title_label.config(text="===============플레이어 레벨 계산 결과===============\n")
    player_calc_title_label.grid(row=0, column=1)

    # level to level 레이블을 나머지 정보들을 담을 paned window 에 추가
    level_to_level_label = tkinter.Label(the_other_panedwindow)
    level_to_level_label.grid(row=1, column=0)
    
    # player level calc 레이블을 나머지 정보들을 담을 paned window 에 추가
    player_calc_label = tkinter.Label(the_other_panedwindow)
    player_calc_label.grid(row=1, column=1)

    # 처음 디폴트 출력
    get_value_calculate_print_all()

    # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
    window.mainloop()
