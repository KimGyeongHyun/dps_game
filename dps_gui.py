import tkinter
import tkinter.messagebox
import dps_upgrade
from static_info.static_info import *


if __name__ == '__main__':
    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    # 윈도우 창의 제목
    window.title("DPS 강화하기 v2.10 유즈맵 계산기    version 2.4.2 by-vigene")
    # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
    # 14인치 : 1366 * 768
    # 15인치 : 1600 * 900
    # 16인치 : 1920 * 1080
    window.geometry('1400x750+100+100')
    # 윈도우 창 크기 조절 가능 여부 설정
    window.resizable(False, False)

    ###########################
    # 여기에 위젯 추가
    game_info = dps_upgrade.GameInfo()

    # 모든 엔트리, 보스, 파티 플레이 여부 상태가 바뀌었을 때 실행
    # 처음 실행할 때도 실행
    # 엔트리 값, 체크 박스, 라디오 박스 정보를 받아 다시 갱신하여 모두 출력
    def get_value_calculate_print_all():
        """모든 수치를 받아 계산 후 모두 출력"""

        # 타입 유효성 검사
        try:
            user_level = int(user_level_entry.get())
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
            player_last_level = int(player_end_level_entry.get())
            special_upgrade_rate = float(special_upgrade_rate_entry.get()) / 100
            zero = float(prevent_del_rate_entry.get()) / 100
            another_first = float(another_first_entry.get()) / 100
            another_second = float(another_second_entry.get()) / 100
            another_third = float(another_third_entry.get()) / 100
            w_exp_rate = float(w_exp_rate_entry.get()) / 100
            w_another_first = float(w_another_first_entry.get()) / 100
            w_special_upgrade = float(w_special_entry.get()) / 100
            w_zero = float(w_zero_entry.get()) / 100
        except ValueError:
            print('ValueError in user spec input parameter')
            return

        # 숫자 범위 유효성 검사
        if user_level < 1 or user_level > PLAYER_MAX_LEVEL:
            tkinter.messagebox.showinfo("유저 레벨 오류",
                                        "유저 레벨은 1 ~ {} 사이의 정수 값을 입력해야 합니다.".format(PLAYER_MAX_LEVEL))
            return

        if first < 0 or first > FIRST_MAX / 100:
            tkinter.messagebox.showinfo("+1 강화 확률 오류",
                                        "+1 강화 확률은 0.0 % ~ {} % 사이의 값을 입력해야 합니다.".format(FIRST_MAX))
            return

        if second < 0 or second > SECOND_MAX / 100:
            tkinter.messagebox.showinfo("+2 강화 확률 오류",
                                        "+2 강화 확률은 0.0 % ~ {} % 사이의 값을 입력해야 합니다.".format(SECOND_MAX))
            return

        if third < 0 or third > THIRD_MAX / 100:
            tkinter.messagebox.showinfo("+3 강화 확률 오류",
                                        "+3 강화 확률은 0.0 % ~ {} % 사이의 값을 입력해야 합니다.".format(THIRD_MAX))
            return

        if user_damage < 0 or user_damage > USER_DAMAGE_MAX:
            tkinter.messagebox.showinfo("유저 공업 오류",
                                        "유저 공업은 0 ~ {} 사이의 정수 값을 입력해야 합니다.".format(USER_DAMAGE_MAX))
            return

        if unit_start_level < 1 or unit_last_level > UNIT_MAX_LEVEL:
            tkinter.messagebox.showinfo("유닛 시작 레벨 오류",
                                        "유닛 시작 레벨은 1 ~ {} 사이의 정수 값을 입력해야 합니다.".format(UNIT_MAX_LEVEL))
            return

        if unit_last_level < 1 or unit_last_level > UNIT_MAX_LEVEL:
            tkinter.messagebox.showinfo("유닛 마지막 레벨 오류",
                                        "유닛 마지막 레벨은 1 ~ {} 사이의 정수 값을 입력해야 합니다.".format(UNIT_MAX_LEVEL))
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

        if player_last_level < 1 or player_last_level > PLAYER_MAX_LEVEL:
            tkinter.messagebox.showinfo("플레이어 목표 레벨 오류",
                                        "플레이어 목표 레벨은 1 ~ {} 사이의 정수 값을 입력해야 합니다.".format(PLAYER_MAX_LEVEL))
            return

        if user_level > player_last_level:
            tkinter.messagebox.showinfo("플레이어 목표 레벨 오류",
                                        "플레이어 목표 레벨은 플레이어 레벨보다 같거나 커야 합니다.")
            return

        if special_upgrade_rate < 0 or special_upgrade_rate > SPECIAL_UPGRADE_MAX / 100:
            tkinter.messagebox.showinfo("특수 강화 확률 오류",
                                        "특수 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(SPECIAL_UPGRADE_MAX))
            return

        if zero < 0 or zero > ZERO_MAX / 100:
            tkinter.messagebox.showinfo("파괴 방지 확률 오류",
                                        "파괴 방지 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(ZERO_MAX))
            return

        if another_first < 0 or another_first > ANOTHER_FIRST_MAX / 100:
            tkinter.messagebox.showinfo("추가 +1 강화 확률 오류",
                                        "추가 +1 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(ANOTHER_FIRST_MAX))
            return
            
        if another_second < 0 or another_second > ANOTHER_SECOND_MAX / 100:
            tkinter.messagebox.showinfo("추가 +2 강화 확률 오류",
                                        "추가 +2 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(ANOTHER_SECOND_MAX))
            return
        
        if another_third < 0 or another_third > ANOTHER_SECOND_MAX / 100:
            tkinter.messagebox.showinfo("추가 +3 강화 확률 오류",
                                        "추가 +3 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(ANOTHER_THIRD_MAX))
            return

        if w_exp_rate < 0 or w_exp_rate > W_EXP_RATE_MAX / 100:
            tkinter.messagebox.showinfo("고유 유닛 경험치 증가량 확률 오류",
                                        "고유 유닛 경험치 증가량 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(W_EXP_RATE_MAX))
            return

        if w_another_first < 0 or w_another_first > W_ANOTHER_FIRST_MAX / 100:
            tkinter.messagebox.showinfo("고유 유닛 추가 +1 강화 확률 오류",
                                        "고유 유닛 추가 +1 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(W_ANOTHER_FIRST_MAX))
            return

        if w_special_upgrade < 0 or w_special_upgrade > W_SPECIAL_UPGRADE_MAX / 100:
            tkinter.messagebox.showinfo("고유 유닛 특수 강화 확률 오류",
                                        "고유 유닛 특수 강화 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(W_SPECIAL_UPGRADE_MAX))
            return

        if w_zero < 0 or w_zero > W_ZERO_MAX / 100:
            tkinter.messagebox.showinfo("고유 유닛 파괴 방지 확률 오류",
                                        "고유 유닛 파괴 방지 확률은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(W_ZERO_MAX))
            return

        user_damage = user_damage * 0.1

        # 유저 스펙 파라미터
        parameters = dps_upgrade.UserSpecParameter(user_level, first, second, third, zero, user_damage,
                                                   private_boss, party_boss, multy_player,
                                                   special_upgrade_rate, another_first, another_second, another_third,
                                                   w_exp_rate, w_another_first, w_special_upgrade, w_zero)

        # 외부 파라미터
        out_parameters = dps_upgrade.OutParameter(unit_start_level,
                                                  unit_last_level,
                                                  sell_ticket,
                                                  hour, minute, seconds,
                                                  user_level,
                                                  player_last_level)

        # 모든 파라미터를 받아 GameInfo 인스턴스 초기화
        game_info.init_game_info(parameters, out_parameters)

        unit_upgrade_rate_listbox.delete(0, UNIT_MAX_LEVEL)
        unit_dps_listbox.delete(0, UNIT_MAX_LEVEL)
        unit_exp_listbox.delete(0, UNIT_MAX_LEVEL)

        # 유저 최종 스펙 출력
        user_exact_spec_label.config(text=game_info.return_str_user_spec())

        # 리스트 박스에 유닛 정보 출력
        for i in range(len(game_info.unit_dict)):
            unit_level = i + 1
            unit_upgrade_rate_listbox.insert(unit_level, game_info.unit_dict[unit_level].__str__())
            unit_upgrade_rate_listbox.see(UNIT_MAX_LEVEL)

            unit_dps_listbox.insert(unit_level, game_info.unit_dict[unit_level].print_unit_dps())
            unit_dps_listbox.see(UNIT_MAX_LEVEL)

            if game_info.unit_dict[unit_level].exp != 0:
                unit_exp_listbox.insert(unit_level, game_info.unit_dict[unit_level].print_unit_exp())
            unit_exp_listbox.see(UNIT_MAX_LEVEL)

        # 유닛 레벨 관련 정보 출력
        level_to_level_label.config(text=game_info.unit_calc.return_str_number_unit_level_to_level()
                                    + "\n\n"
                                    + game_info.return_str_final_player_level_with_units()
                                    + "\n"
                                    + game_info.return_str_final_player_level_with_time())

        # 플레이어 레벨 관련 정보 출력
        player_calc_label.config(text=game_info.player_calc.return_str_exp_to_player_level_up()
                                 + "\n\n"
                                 + game_info.player_calc.return_str_player_level_to_level())


    def get_entry_value_calculate_print_all(event):
        """모든 수치를 받아 모두 출력"""
        get_value_calculate_print_all()


    def set_expected_upgrade_rate_and_deal_upgrade(event):
        """유저 레벨에 따라 +1, +2, +3, 공업, 유닛 시작, 마지막 레벨 , 특수 강화 확률, 파괴 방지 확률, +1 추가 확률 디폴트 값 갱신"""

        # 유저 레벨 유효성 검사
        try:
            user_level = int(user_level_entry.get())
        except ValueError:
            print('ValueError in user spec input parameter')
            return

        # 포인트 총합
        points = int(user_level_entry.get()) * 5

        unit_start_level_entry.delete(0, 10)
        unit_last_level_entry.delete(0, 10)

        # 유저 레벨에 따라 유닛 시작, 마지막 레벨 엔트리 값 초기화
        if user_level <= 100:
            unit_start_level_entry.insert(0, "15")
            unit_last_level_entry.insert(0, "18")

        elif user_level <= 500:
            unit_start_level_entry.insert(0, "18")
            unit_last_level_entry.insert(0, "25")

        elif user_level <= 1_000:
            unit_start_level_entry.insert(0, "20")
            unit_last_level_entry.insert(0, "25")

        elif user_level <= 1_500:
            unit_start_level_entry.insert(0, "24")
            unit_last_level_entry.insert(0, "25")

        else:
            unit_start_level_entry.insert(0, "30")
            unit_last_level_entry.insert(0, "39")

        # 갱신할 엔트리 값 초기화
        first_upgrade_entry.delete(0, 10)
        first_upgrade_entry.insert(0, "0.0")
        second_upgrade_entry.delete(0, 10)
        second_upgrade_entry.insert(0, "0.0")
        third_upgrade_entry.delete(0, 10)
        third_upgrade_entry.insert(0, "0.0")
        user_damage_upgrade_entry.delete(0, 10)
        user_damage_upgrade_entry.insert(0, "0")
        special_upgrade_rate_entry.delete(0, 10)
        special_upgrade_rate_entry.insert(0, "0.0")
        prevent_del_rate_entry.delete(0, 10)
        prevent_del_rate_entry.insert(0, "0.0")
        another_first_entry.delete(0, 10)
        another_first_entry.insert(0, "0.0")
        another_second_entry.delete(0, 10)
        another_second_entry.insert(0, "0.0")
        another_third_entry.delete(0, 10)
        another_third_entry.insert(0, "0.0")

        # 플레이어 목표 레벨 디폴트 값 지정
        player_end_level_entry.delete(0, 10)
        if user_level >= PLAYER_MAX_LEVEL:
            player_end_level_entry.insert(0, str(PLAYER_MAX_LEVEL))
        else:
            player_end_level_entry.insert(0, "{}".format((user_level // 500 + 1) * 500))

        # +1 강화 확률 디폴트 값 지정
        first_upgrade_entry.delete(0, 10)
        if points <= 10 * 100:
            first_upgrade_entry.insert(0, "{:.1f}".format((points // 10) / 10))
            get_value_calculate_print_all()
            return
        first_upgrade_entry.insert(0, "10.0")
        points -= 10 * 100

        # 유저 공업 디폴트 값 지정
        user_damage_upgrade_entry.delete(0, 10)
        if points <= 20 * 50:
            user_damage_upgrade_entry.insert(0, "{}".format(points // 20))
            get_value_calculate_print_all()
            return
        user_damage_upgrade_entry.insert(0, "50")
        points -= 20 * 50

        # +2 강화 확률 디폴트 값 지정
        second_upgrade_entry.delete(0, 10)
        if points <= 200 * 50:
            second_upgrade_entry.insert(0, "{:.1f}".format((points // 200) / 10))
            get_value_calculate_print_all()
            return
        second_upgrade_entry.insert(0, "5.0")
        points -= 200 * 50

        # +3 강화 확률 디폴트 값 지정
        third_upgrade_entry.delete(0, 10)
        if points <= 1_000 * 30:
            third_upgrade_entry.insert(0, "{:.1f}".format((points // 1_000) / 10))
            get_value_calculate_print_all()
            return
        third_upgrade_entry.insert(0, "3.0")
        points -= 1_000 * 30

        # 추가 +1 강화 확률 디폴트 값 지정
        another_first_entry.delete(0, 10)
        if points <= 1_000 * 50:
            another_first_entry.insert(0, "{:.1f}".format((points // 1_000) / 10))
            get_value_calculate_print_all()
            return
        another_first_entry.insert(0, "5.0")
        points -= 1_000 * 50

        # 특수 강화 확률 디폴트 값 지정
        special_upgrade_rate_entry.delete(0, 10)
        if points <= 500 * 100:
            special_upgrade_rate_entry.insert(0, "{:.1f}".format((points // 500) / 10))
            get_value_calculate_print_all()
            return
        special_upgrade_rate_entry.insert(0, "10.0")
        points -= 500 * 100

        # 파괴 방지 확률 디폴트 값 지정
        prevent_del_rate_entry.delete(0, 10)
        if points <= 150 * 500:
            prevent_del_rate_entry.insert(0, "{:.1f}".format((points // 150) / 10))
            get_value_calculate_print_all()
            return
        prevent_del_rate_entry.insert(0, "50.0")
        points -= 150 * 500

        # 추가 +2 강화 확률 디폴트 값 지정
        another_second_entry.delete(0, 10)
        if points <= 2_500 * 20:
            another_second_entry.insert(0, "{:.1f}".format((points // 2_500) / 10))
            get_value_calculate_print_all()
            return
        another_second_entry.insert(0, "2.0")
        points -= 2_500 * 20

        # 추가 +3 강화 확률 디폴트 값 지정
        another_third_entry.delete(0, 10)
        if points <= 5_000 * 10:
            another_third_entry.insert(0, "{:.1f}".format((points // 5_000) / 10))
            get_value_calculate_print_all()
            return
        another_third_entry.insert(0, "1.0")
        points -= 5_000 * 10

        # 갱신된 값을 받아 계산 후 모두 출력
        get_value_calculate_print_all()

    ###################################################################################################################
    # 처음 안내문
    first_information_label = tkinter.Label(window, text="1) 먼저 플레이어 레벨을 입력하고 엔터를 눌러주세요.\n"
                                                         "플레이어 레벨을 입력하고 엔터를 누르면 +1, +2, +3 강화 확률과 공업, "
                                                         "특수 강화, 파괴 방지, 추가 +1 강화 확률, "
                                                         "플레이어 목표 레벨이 어림짐작으로 자동 갱신됩니다.\n"
                                                         "2) 이후 유저 스펙을 수정하고 엔터를 눌러주세요.\n"
                                                         "3) 보스 처치 레벨과 파티 플레이 버프 여부를 선택하세요\n"
                                                         "4) 보고 싶은 정보를 입력하고 엔터를 눌러주세요.\n"
                                                         "보고 싶은 정보의 계산 결과는 맨 아래쪽에 '유닛 레벨 계산 결과'칸과, "
                                                         "'플레이어 레벨 계산 결과'칸에 나타납니다.\n"
                                                         "모든 계산은 최종 스펙이 적용된 유닛의 강화확률 기반으로 비교됩니다.\n"
                                                         "",
                                            anchor='w',
                                            justify='left')
    first_information_label.pack(side="top", fill="x")

    ###################################################################################################################
    ###################################################################################################################
    # 유저 스펙을 기입할 paned window 를 상단에 배치
    user_spec_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
    user_spec_panedwindow.pack(side="top")

    # 유저 스펙 레이블 표시
    user_spec_label = tkinter.Label(user_spec_panedwindow, text="유저 스펙")
    cho_label = tkinter.Label(user_spec_panedwindow, text="고유 유닛 스펙")
    boss_and_multi_label = tkinter.Label(user_spec_panedwindow, text="보스 최대 레벨, 파티플레이 버프 여부")
    unit_level_calculate_label = tkinter.Label(user_spec_panedwindow, text="보고 싶은 정보")

    # 유저 스펙 레이블 배치
    user_spec_label.grid(row=0, column=0)
    cho_label.grid(row=0, column=1)
    boss_and_multi_label.grid(row=0, column=2)
    unit_level_calculate_label.grid(row=0, column=3)

    ###################################################################################################################
    # 유저 스펙 중 강화확률과 공업, 특수 강화확률, 파괴 방지 확률, +1 추가 강화 확률을 기입할 frame 을 유저 스펙 paned window 에 배치
    upgrade_rate_frame = tkinter.Frame(user_spec_panedwindow, padx=15)
    user_spec_panedwindow.add(upgrade_rate_frame)
    upgrade_rate_frame.grid(row=1, column=0)

    # 유저 레벨 레이블
    user_level_label = tkinter.Label(upgrade_rate_frame,
                                     text="유저 레벨 : ")
    user_level_label.grid(row=0, column=0)

    # 유저 레벨 엔트리
    user_level_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    user_level_entry.bind("<Return>", set_expected_upgrade_rate_and_deal_upgrade)
    user_level_entry.insert(2, '8500')
    user_level_entry.grid(row=0, column=1)

    # +1 강화확률 레이블
    first_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                        text="+1 강화 확률 : ")
    first_upgrade_label.grid(row=1, column=0)

    # +1 강화확률 엔트리
    first_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    first_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    first_upgrade_entry.insert(2, '10.0')
    first_upgrade_entry.grid(row=1, column=1)

    # +2 강화확률 레이블
    second_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                         text="+2 강화 확률 : ")
    second_upgrade_label.grid(row=2, column=0)

    # +2 강화확률 엔트리
    second_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    second_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    second_upgrade_entry.insert(2, '5.0')
    second_upgrade_entry.grid(row=2, column=1)

    # +3 강화확률 레이블
    third_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                        text="+3 강화 확률 : ")
    third_upgrade_label.grid(row=3, column=0)

    # +3 강화확률 엔트리
    third_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    third_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    third_upgrade_entry.insert(2, '3.0')
    third_upgrade_entry.grid(row=3, column=1)

    # 유저 공격력 업그레이드 레이블
    user_damage_upgrade_label = tkinter.Label(upgrade_rate_frame,
                                              text="유저 공업 : ")
    user_damage_upgrade_label.grid(row=4, column=0)

    # 유저 공격력 업그레이드 엔트리
    user_damage_upgrade_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    user_damage_upgrade_entry.bind("<Return>", get_entry_value_calculate_print_all)
    user_damage_upgrade_entry.insert(2, '50')
    user_damage_upgrade_entry.grid(row=4, column=1)
    
    # 특수 강화확률 레이블
    special_upgrade_rate_label = tkinter.Label(upgrade_rate_frame, text="특수 강화 확률 : ")
    special_upgrade_rate_label.grid(row=0, column=3)
    
    # 특수 강화확률 엔트리
    special_upgrade_rate_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    special_upgrade_rate_entry.bind("<Return>", get_entry_value_calculate_print_all)
    special_upgrade_rate_entry.insert(2, '0.0')
    special_upgrade_rate_entry.grid(row=0, column=4)
    
    # 파괴 방지 확률 레이블
    prevent_del_rate_label = tkinter.Label(upgrade_rate_frame, text="파괴 방지 확률 : ")
    prevent_del_rate_label.grid(row=1, column=3)

    # 파괴 방지 확률 엔트리
    prevent_del_rate_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    prevent_del_rate_entry.bind("<Return>", get_entry_value_calculate_print_all)
    prevent_del_rate_entry.insert(2, '0.0')
    prevent_del_rate_entry.grid(row=1, column=4)

    # 추가 +1 강화 확률 레이블
    another_first_label = tkinter.Label(upgrade_rate_frame, text="추가 +1 강화 확률 : ")
    another_first_label.grid(row=2, column=3)

    # 추가 +1 강화 확률 엔트리
    another_first_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    another_first_entry.bind("<Return>", get_entry_value_calculate_print_all)
    another_first_entry.insert(2, '0.0')
    another_first_entry.grid(row=2, column=4)

    # 추가 +2 강화 확률 레이블
    another_second_label = tkinter.Label(upgrade_rate_frame, text="추가 +2 강화 확률 : ")
    another_second_label.grid(row=3, column=3)

    # 추가 +2 강화 확률 엔트리
    another_second_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    another_second_entry.bind("<Return>", get_entry_value_calculate_print_all)
    another_second_entry.insert(2, '0.0')
    another_second_entry.grid(row=3, column=4)

    # 추가 +3 강화 확률 레이블
    another_third_label = tkinter.Label(upgrade_rate_frame, text="추가 +3 강화 확률 : ")
    another_third_label.grid(row=4, column=3)

    # 추가 +3 강화 확률 엔트리
    another_third_entry = tkinter.Entry(upgrade_rate_frame, width=7, justify='center')
    another_third_entry.bind("<Return>", get_entry_value_calculate_print_all)
    another_third_entry.insert(2, '0.0')
    another_third_entry.grid(row=4, column=4)

    # % 레이블
    percent1 = tkinter.Label(upgrade_rate_frame, text='%')
    percent2 = tkinter.Label(upgrade_rate_frame, text='%')
    percent3 = tkinter.Label(upgrade_rate_frame, text='%')
    percent4 = tkinter.Label(upgrade_rate_frame, text='강')
    percent5 = tkinter.Label(upgrade_rate_frame, text='%')
    percent6 = tkinter.Label(upgrade_rate_frame, text='%')
    percent7 = tkinter.Label(upgrade_rate_frame, text='%')
    percent8 = tkinter.Label(upgrade_rate_frame, text='%')
    percent9 = tkinter.Label(upgrade_rate_frame, text='%')

    percent1.grid(row=1, column=2)
    percent2.grid(row=2, column=2)
    percent3.grid(row=3, column=2)
    percent4.grid(row=4, column=2)
    percent5.grid(row=0, column=5)
    percent6.grid(row=1, column=5)
    percent7.grid(row=2, column=5)
    percent8.grid(row=3, column=5)
    percent9.grid(row=4, column=5)

    ###################################################################################################################
    # 유저 스펙 중 고유 유닛 스펙 Frame 을 유저 스펙 paned window 에 배치
    w_frame = tkinter.Frame(user_spec_panedwindow, padx=15)
    user_spec_panedwindow.add(w_frame)
    w_frame.grid(row=1, column=1)

    # 고유 유닛 경험치 증가량 레이블
    w_exp_rate_label = tkinter.Label(w_frame, text="경험치 증가량 : ")
    w_exp_rate_label.grid(row=0, column=0)

    # 고유 유닛 경험치 증가량 엔트리
    w_exp_rate_entry = tkinter.Entry(w_frame, width=7, justify='center')
    w_exp_rate_entry.bind("<Return>", get_entry_value_calculate_print_all)
    w_exp_rate_entry.insert(2, '0.0')
    w_exp_rate_entry.grid(row=0, column=1)

    # 추가 +1 강화 확률 레이블
    w_another_first_label = tkinter.Label(w_frame, text="추가 +1 강화 확률 : ")
    w_another_first_label.grid(row=1, column=0)

    # 추가 +1 강화 확률 엔트리
    w_another_first_entry = tkinter.Entry(w_frame, width=7, justify='center')
    w_another_first_entry.bind("<Return>", get_entry_value_calculate_print_all)
    w_another_first_entry.insert(2, '0.0')
    w_another_first_entry.grid(row=1, column=1)

    # 특수 강화 확률 레이블
    w_special_label = tkinter.Label(w_frame, text="특수 강화 확률 : ")
    w_special_label.grid(row=2, column=0)

    # 특수 강화 확률 엔트리
    w_special_entry = tkinter.Entry(w_frame, width=7, justify='center')
    w_special_entry.bind("<Return>", get_entry_value_calculate_print_all)
    w_special_entry.insert(2, '0.0')
    w_special_entry.grid(row=2, column=1)

    # 파괴 방지 확률 레이블
    w_zero_label = tkinter.Label(w_frame, text="파괴 방지 확률 : ")
    w_zero_label.grid(row=3, column=0)

    # 파괴 방지 확률 엔트리
    w_zero_entry = tkinter.Entry(w_frame, width=7, justify='center')
    w_zero_entry.bind("<Return>", get_entry_value_calculate_print_all)
    w_zero_entry.insert(2, '0.0')
    w_zero_entry.grid(row=3, column=1)

    # % 레이블
    percent8 = tkinter.Label(w_frame, text='%')
    percent9 = tkinter.Label(w_frame, text='%')
    percent10 = tkinter.Label(w_frame, text='%')
    percent11 = tkinter.Label(w_frame, text='%')

    percent8.grid(row=0, column=2)
    percent9.grid(row=1, column=2)
    percent10.grid(row=2, column=2)
    percent11.grid(row=3, column=2)

    ###################################################################################################################
    # 유저 스펙 중 보스 라운드와 파티플레이 여부를 체크할 frame 을 유저 스펙 paned window 에 배치
    boss_and_multy = tkinter.Frame(user_spec_panedwindow, padx=15)
    user_spec_panedwindow.add(boss_and_multy)
    boss_and_multy.grid(row=1, column=2)

    # 개인 보스 처치 레벨 레이블
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

    # 파티 보스 처치 레벨 레이블
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

    ###################################################################################################################
    # 유닛 시작 레벨, 마지막 레벨, 판매권 수, 리얼 타임 진행 시간
    # 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
    unit_information = tkinter.Frame(user_spec_panedwindow, padx=15)
    user_spec_panedwindow.add(unit_information)
    unit_information.grid(row=1, column=3)

    # 유닛 시작 레벨 레이블
    unit_start_level_label = tkinter.Label(unit_information, text='유닛 시작 레벨 : ')
    unit_start_level_label.grid(row=0, column=0)

    # 유닛 시작 레벨 엔트리
    unit_start_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_start_level_entry.insert(1, '30')
    unit_start_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    unit_start_level_entry.grid(row=0, column=1)

    # 유닛 마지막 레벨 레이블
    unit_last_level_label = tkinter.Label(unit_information, text='유닛 마지막 레벨 : ')
    unit_last_level_label.grid(row=1, column=0)

    # 유닛 마지막 레벨 엔트리
    unit_last_level_entry = tkinter.Entry(unit_information, width=3, justify='center')
    unit_last_level_entry.insert(1, '39')
    unit_last_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    unit_last_level_entry.grid(row=1, column=1)

    # 판매권 수 레이블
    sell_ticket_label = tkinter.Label(unit_information, text='마지막 레벨 유닛 판매 수 : ')
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

    # 플레이어 목표 레벨 레이블
    player_end_level_label = tkinter.Label(unit_information, text='플레이어 목표 레벨 : ')
    player_end_level_label.grid(row=4, column=0)

    # 플레이어 목표 레벨 엔트리
    player_end_level_entry = tkinter.Entry(unit_information, width=7, justify='center')
    player_end_level_entry.insert(2, '9000')
    player_end_level_entry.bind("<Return>", get_entry_value_calculate_print_all)
    player_end_level_entry.grid(row=4, column=1)

    ##################################################################################################################
    ##################################################################################################################
    # 유저 최종 스펙 레이블
    user_exact_spec_label = tkinter.Label(window, font=('Arial', 10), foreground='#9900cc')
    user_exact_spec_label.pack(side="top")

    ###################################################################################################################
    ###################################################################################################################
    # 유닛 정보를 담을 paned window 생성
    unit_information_panedwindow = tkinter.PanedWindow()
    unit_information_panedwindow.pack(side="top", pady=0)

    # 유닛 정보 레이블
    unit_upgrade_rate_label = tkinter.Label(unit_information_panedwindow, text="유닛 강화 확률")
    unit_dps_label = tkinter.Label(unit_information_panedwindow, text="유닛 dps 정보")
    unit_exp_label = tkinter.Label(unit_information_panedwindow, text="유닛 exp 정보")

    unit_upgrade_rate_label.grid(row=0, column=0)
    unit_dps_label.grid(row=0, column=1)
    unit_exp_label.grid(row=0, column=2)

    ###################################################################################################################
    # 유닛 강화 확률 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_upgrade_rate_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_upgrade_rate_scrollbar = tkinter.Scrollbar(unit_upgrade_rate_frame)
    unit_upgrade_rate_scrollbar.pack(side='right', fill='y')

    unit_upgrade_rate_listbox = tkinter.Listbox(unit_upgrade_rate_frame,
                                                yscrollcommand=unit_upgrade_rate_scrollbar.set,
                                                width=38, height=10)
    unit_upgrade_rate_listbox.pack(side='left')

    unit_upgrade_rate_scrollbar["command"] = unit_upgrade_rate_listbox.yview

    unit_upgrade_rate_frame.grid(row=1, column=0)

    ###################################################################################################################
    # 유닛 dps 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_dps_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_dps_scrollbar = tkinter.Scrollbar(unit_dps_frame)
    unit_dps_scrollbar.pack(side='right', fill='y')

    unit_dps_listbox = tkinter.Listbox(unit_dps_frame,
                                       yscrollcommand=unit_dps_scrollbar.set,
                                       width=42, height=10)
    unit_dps_listbox.pack(side='left')

    unit_dps_scrollbar["command"] = unit_dps_listbox.yview

    unit_dps_frame.grid(row=1, column=1)

    ###################################################################################################################
    # 유닛 exp 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
    unit_exp_frame = tkinter.Frame(unit_information_panedwindow, padx=15, pady=5)

    unit_exp_scrollbar = tkinter.Scrollbar(unit_exp_frame)
    unit_exp_scrollbar.pack(side='right', fill='y')

    unit_exp_listbox = tkinter.Listbox(unit_exp_frame,
                                       yscrollcommand=unit_exp_scrollbar.set,
                                       width=62, height=10)
    unit_exp_listbox.pack(side='left')

    unit_exp_scrollbar["command"] = unit_exp_listbox.yview

    unit_exp_frame.grid(row=1, column=2)

    ###################################################################################################################
    ###################################################################################################################
    # 나머지 정보들을 담을 paned window
    the_other_panedwindow = tkinter.PanedWindow()
    the_other_panedwindow.pack(side='top', pady=5)

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

    # 모든 엔트리에 디폴트 값 출력
    get_value_calculate_print_all()

    # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
    window.mainloop()
