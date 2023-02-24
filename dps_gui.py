import tkinter
import tkinter.messagebox
import dps_upgrade
from static_info.static_info import *
import time


class MainWindow:
    """최상단 윈도우"""

    def __init__(self):
        self.main_window = tkinter.Tk()

        # 윈도우 창의 제목
        self.main_window.title("DPS 강화하기 v2.12 유즈맵 계산기    version 2.5.18 made by - ddeerraa")
        # 윈도우 창의 너비와 높이, 초기 화면 위치의 x, y 좌표 설정
        # 14인치 : 1366 * 768
        # 15인치 : 1600 * 900
        # 16인치 : 1920 * 1080
        self.main_window.geometry('1400x770+100+100')
        # 윈도우 창 크기 조절 가능 여부 설정
        self.main_window.resizable(False, False)

        # 여기에 위젯 추가
        self.game_info = dps_upgrade.GameInfo()

        # 처음 안내문
        first_information_label = tkinter.Label(self.main_window,
                                                text="1) 먼저 플레이어 레벨과 고유 유닛 단 수를 입력하고 엔터를 눌러주세요.  "
                                                "그러면 유저 스펙, 고유 유닛 스펙, 플레이어 목표 레벨이 자동 갱신됩니다.\n"
                                                "2) 유저 스펙과 고유 유닛 스펙을 수정하고 엔터를 눌러주세요.  ->  "
                                                "3) 보스 처치 레벨과 파티 플레이 버프 여부를 선택하세요.  ->  "
                                                "4) 보고 싶은 정보를 입력하고 엔터를 눌러주세요.\n\n"
                                                "보고 싶은 정보의 계산 결과는 맨 아래쪽에 '유닛 레벨 계산 결과'칸과, "
                                                "'플레이어 레벨 계산 결과'칸에 나타납니다.\n"
                                                "25/26강 사이 돈 버는 비율 차이 (mps)는 미네랄 64배, 가스 1배 기준이고,  "
                                                "40/41강 사이 mps 는 가스 64배 기준입니다.\n"
                                                "계산 결과는 최종 스펙이 적용된 유닛의 강화확률 기반으로 계산됩니다.\n"
                                                "",
                                                anchor='w',
                                                justify='left')
        first_information_label.pack(side="top", fill="x")

        input_panedwindow = InputPanedWindow(self)
        self.user_spec_frame = input_panedwindow.user_spec_frame
        self.wraith_frame = input_panedwindow.wraith_frame
        self.bosses_frame = input_panedwindow.bosses_frame
        self.out_parameters_frame = input_panedwindow.out_parameters_frame

        # 유저 최종 스펙 레이블
        self.user_exact_spec_label = tkinter.Label(self.main_window, font=('Arial', 10), foreground='#9900cc')
        self.user_exact_spec_label.pack(side="top")

        self.unit_info_panedwindow = UnitInfoPanedWindow()

        self.print_panedwindow = PrintPanedWindow()

        self.get_value_calculate_print_all()

        # 해당 윈도우 창을 윈도우가 종료될 때 까지 실행
        self.main_window.mainloop()

    def get_value_calculate_print_all(self):
        """모든 수치를 받아 계산 후 모두 출력"""
        start = time.time()

        try:
            user_level = int(self.user_spec_frame.user_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유저 레벨 오류",
                                        "유저 레벨은 정수 값을 입력해야 합니다.")
            return

        try:
            user_damage = int(self.user_spec_frame.user_damage_upgrade_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유저 공업 오류",
                                        "유저 공업은 정수 값을 입력해야 합니다.")
            return

        try:
            unit_start_level = int(self.out_parameters_frame.unit_start_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유닛 시작 레벨 오류",
                                        "유닛 시작 레벨은 정수 값을 입력해야 합니다.")
            return

        try:
            unit_last_level = int(self.out_parameters_frame.unit_last_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유닛 마지막 레벨 오류",
                                        "유닛 마지막 레벨은 정수 값을 입력해야 합니다.")
            return

        try:
            sell_ticket = int(self.out_parameters_frame.sell_ticket_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유닛 판매 개수 오류",
                                        "유닛 판매 개수는 0을 포함한 자연수를 입력해야 합니다.")
            return

        try:
            hour = int(self.out_parameters_frame.playing_hour_entry.get())
            minute = int(self.out_parameters_frame.playing_minute_entry.get())
            seconds = int(self.out_parameters_frame.playing_second_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("시간 오류",
                                        "시간은 0을 포함한 자연수를 입력해야 합니다.")
            return

        try:
            player_last_level = int(self.out_parameters_frame.player_end_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("플레이어 목표 레벨 오류",
                                        "플레이어 목표 레벨은 정수 값을 입력해야 합니다.")
            return

        # 타입 유효성 검사
        try:
            first = float(self.user_spec_frame.first_upgrade_entry.get()) / 100
            second = float(self.user_spec_frame.second_upgrade_entry.get()) / 100
            third = float(self.user_spec_frame.third_upgrade_entry.get()) / 100
            special_upgrade_rate = float(self.user_spec_frame.special_upgrade_rate_entry.get()) / 100
            zero = float(self.user_spec_frame.prevent_del_rate_entry.get()) / 100
            another_first = float(self.user_spec_frame.another_first_entry.get()) / 100
            another_second = float(self.user_spec_frame.another_second_entry.get()) / 100
            another_third = float(self.user_spec_frame.another_third_entry.get()) / 100
            max_hunting = float(self.user_spec_frame.max_hunting_entry.get()) / 100
            private_boss = int(self.bosses_frame.private_boss_count.get())
            party_boss = int(self.bosses_frame.party_boss_count.get())
            multy_player = bool(self.bosses_frame.party_check.get())
            w_exp_rate = float(self.wraith_frame.w_exp_rate_entry.get()) / 100
            w_another_first = float(self.wraith_frame.w_another_first_entry.get()) / 100
            w_special_upgrade = float(self.wraith_frame.w_special_entry.get()) / 100
            w_zero = float(self.wraith_frame.w_zero_entry.get()) / 100
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

        if unit_start_level < 1 or unit_start_level > UNIT_MAX_LEVEL:
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
            tkinter.messagebox.showinfo("유닛 판매 개수 오류",
                                        "유닛 판매 개수는 0을 포함한 자연수를 입력해야 합니다.")
            return

        if hour < 0:
            tkinter.messagebox.showinfo("시간 오류 (시)",
                                        "시간은 0을 포함한 자연수를 입력해야 합니다.")
            return

        if minute < 0:
            tkinter.messagebox.showinfo("시간 오류 (분)",
                                        "시간은 0을 포함한 자연수를 입력해야 합니다.")
            return

        if seconds < 0:
            tkinter.messagebox.showinfo("시간 오류 (초)",
                                        "시간은 0을 포함한 자연수를 입력해야 합니다.")
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
            tkinter.messagebox.showinfo("고유 유닛 경험치 증가량 오류",
                                        "고유 유닛 경험치 증가량은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(W_EXP_RATE_MAX))
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

        if max_hunting < 0 or max_hunting > MAX_HUNTING_MAX / 100:
            tkinter.messagebox.showinfo("MAX 사냥터 돈 증가량 오류",
                                        "MAX 사냥터 돈 증가량은 0 % ~ {} % 사이의 값을 입력해야 합니다.".format(MAX_HUNTING_MAX))
            return

        # 유저 스펙 파라미터
        parameters = dps_upgrade.UserSpecParameter(user_level, first, second, third, zero, user_damage,
                                                   private_boss, party_boss, multy_player,
                                                   special_upgrade_rate, another_first, another_second, another_third,
                                                   w_exp_rate, w_another_first, w_special_upgrade, w_zero,
                                                   max_hunting)

        # 외부 파라미터
        out_parameters = dps_upgrade.OutParameter(unit_start_level,
                                                  unit_last_level,
                                                  sell_ticket,
                                                  hour, minute, seconds,
                                                  user_level,
                                                  player_last_level)

        # 모든 파라미터를 받아 GameInfo 인스턴스 초기화
        self.game_info.init_game_info(parameters, out_parameters)

        self.unit_info_panedwindow.unit_info_frame.unit_info_listbox.delete(0, UNIT_MAX_LEVEL)
        self.unit_info_panedwindow.unit_dps_frame.unit_info_listbox.delete(0, UNIT_MAX_LEVEL)
        self.unit_info_panedwindow.unit_exp_frame.unit_info_listbox.delete(0, UNIT_MAX_LEVEL)

        # 유저 최종 스펙 출력
        self.user_exact_spec_label.config(text=self.game_info.return_str_user_spec())

        # 리스트 박스에 유닛 정보 출력
        for i in range(len(self.game_info.unit_dict)):
            unit_level = i + 1
            self.unit_info_panedwindow.unit_info_frame.\
                unit_info_listbox.insert(unit_level, self.game_info.unit_dict[unit_level].__str__())
            self.unit_info_panedwindow.unit_dps_frame.\
                unit_info_listbox.insert(unit_level, self.game_info.unit_dict[unit_level].print_unit_dps())
            if self.game_info.unit_dict[unit_level].exp != 0:
                self.unit_info_panedwindow.unit_exp_frame.\
                    unit_info_listbox.insert(unit_level, self.game_info.unit_dict[unit_level].print_unit_exp())

        self.unit_info_panedwindow.unit_info_frame.unit_info_listbox.see(UNIT_MAX_LEVEL)
        self.unit_info_panedwindow.unit_dps_frame.unit_info_listbox.see(UNIT_MAX_LEVEL)
        self.unit_info_panedwindow.unit_exp_frame.unit_info_listbox.see(UNIT_MAX_LEVEL)

        # 유닛 레벨 관련 정보 출력
        self.print_panedwindow.level_to_level_label.config(text=self.game_info.return_str_unit_label())

        # 플레이어 레벨 관련 정보 출력
        self.print_panedwindow.player_calc_label.config(text=self.game_info.return_str_player_label())

        self.print_panedwindow.player_calc_25_40.config(text=self.game_info.player_calc.return_str_25_40_number())
        self.print_panedwindow.player_calc_41_44.config(text=self.game_info.player_calc.return_str_41_44_number())

        end = time.time()
        print('=========================')
        print('inner run time = {:.2f}ms'.format(1000 * (end - start)))

    def get_entry_value_calculate_print_all(self, event):
        """모든 수치를 받아 모두 출력"""
        self.get_value_calculate_print_all()

    def set_expected_upgrade_rate_and_deal_upgrade(self, event):
        """유저 레벨에 따라 +1, +2, +3, 공업, 특수 강화 확률, 파괴 방지 확률, 추가 +1, +2, +3 확률 갱신"""

        start = time.time()

        # 유저 레벨 유효성 검사
        try:
            user_level = int(self.user_spec_frame.user_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("유저 레벨 오류",
                                        "유저 레벨은 정수 값을 입력해야 합니다.")
            return

        # 포인트 총합
        points = int(self.user_spec_frame.user_level_entry.get()) * 5

        # 갱신할 엔트리 값 초기화
        self.user_spec_frame.first_upgrade_entry.delete(0, 10)
        self.user_spec_frame.first_upgrade_entry.insert(0, "0.0")
        self.user_spec_frame.second_upgrade_entry.delete(0, 10)
        self.user_spec_frame.second_upgrade_entry.insert(0, "0.0")
        self.user_spec_frame.third_upgrade_entry.delete(0, 10)
        self.user_spec_frame.third_upgrade_entry.insert(0, "0.0")
        self.user_spec_frame.user_damage_upgrade_entry.delete(0, 10)
        self.user_spec_frame.user_damage_upgrade_entry.insert(0, "0")
        self.user_spec_frame.special_upgrade_rate_entry.delete(0, 10)
        self.user_spec_frame.special_upgrade_rate_entry.insert(0, "0.0")
        self.user_spec_frame.prevent_del_rate_entry.delete(0, 10)
        self.user_spec_frame.prevent_del_rate_entry.insert(0, "0.0")
        self.user_spec_frame.another_first_entry.delete(0, 10)
        self.user_spec_frame.another_first_entry.insert(0, "0.0")
        self.user_spec_frame.max_hunting_entry.delete(0, 10)
        self.user_spec_frame.max_hunting_entry.insert(0, "0.0")
        self.user_spec_frame.another_second_entry.delete(0, 10)
        self.user_spec_frame.another_second_entry.insert(0, "0.0")
        self.user_spec_frame.another_third_entry.delete(0, 10)
        self.user_spec_frame.another_third_entry.insert(0, "0.0")

        # 플레이어 목표 레벨 디폴트 값 지정
        self.out_parameters_frame.player_end_level_entry.delete(0, 10)
        if user_level >= PLAYER_MAX_LEVEL:
            self.out_parameters_frame.player_end_level_entry.insert(0, str(PLAYER_MAX_LEVEL))
        else:
            self.out_parameters_frame.player_end_level_entry.insert(0, "{}".format((user_level // 500 + 1) * 500))

        # +1 강화 확률 디폴트 값 지정
        self.user_spec_frame.first_upgrade_entry.delete(0, 10)
        if points <= 10 * 100:
            self.user_spec_frame.first_upgrade_entry.insert(0, "{:.1f}".format((points // 10) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.first_upgrade_entry.insert(0, "10.0")
        points -= 10 * 100

        # 유저 공업 디폴트 값 지정
        self.user_spec_frame.user_damage_upgrade_entry.delete(0, 10)
        if points <= 20 * 50:
            self.user_spec_frame.user_damage_upgrade_entry.insert(0, "{}".format(points // 20))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.user_damage_upgrade_entry.insert(0, "50")
        points -= 20 * 50

        if points < 0:
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return

        # +2 강화 확률 디폴트 값 지정
        self.user_spec_frame.second_upgrade_entry.delete(0, 10)
        if points <= 200 * 50:
            self.user_spec_frame.second_upgrade_entry.insert(0, "{:.1f}".format((points // 200) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.second_upgrade_entry.insert(0, "5.0")
        points -= 200 * 50

        # +3 강화 확률 디폴트 값 지정
        self.user_spec_frame.third_upgrade_entry.delete(0, 10)
        if points <= 1_000 * 30:
            self.user_spec_frame.third_upgrade_entry.insert(0, "{:.1f}".format((points // 1_000) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.third_upgrade_entry.insert(0, "3.0")
        points -= 1_000 * 30

        # 추가 +1 강화 확률 디폴트 값 지정
        self.user_spec_frame.another_first_entry.delete(0, 10)
        if points <= 1_000 * 50:
            self.user_spec_frame.another_first_entry.insert(0, "{:.1f}".format((points // 1_000) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.another_first_entry.insert(0, "5.0")
        points -= 1_000 * 50

        # 특수 강화 확률 디폴트 값 지정
        self.user_spec_frame.special_upgrade_rate_entry.delete(0, 10)
        if points <= 500 * 100:
            self.user_spec_frame.special_upgrade_rate_entry.insert(0, "{:.1f}".format((points // 500) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.special_upgrade_rate_entry.insert(0, "10.0")
        points -= 500 * 100

        # 파괴 방지 확률 디폴트 값 지정
        self.user_spec_frame.prevent_del_rate_entry.delete(0, 10)
        if points <= 250 * 300:
            self.user_spec_frame.prevent_del_rate_entry.insert(0, "{:.1f}".format((points // 250) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.prevent_del_rate_entry.insert(0, "30.0")
        points -= 250 * 300

        # LV.MAX 허수아비 돈 수급량 디폴트 값 지정
        self.user_spec_frame.max_hunting_entry.delete(0, 10)
        if points <= 100 * 100:
            self.user_spec_frame.max_hunting_entry.insert(0, "{:.1f}".format((points // 100) / 1))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.max_hunting_entry.insert(0, "100.0")
        points -= 100 * 100

        # 추가 +2 강화 확률 디폴트 값 지정
        self.user_spec_frame.another_second_entry.delete(0, 10)
        if points <= 2_500 * 20:
            self.user_spec_frame.another_second_entry.insert(0, "{:.1f}".format((points // 2_500) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.another_second_entry.insert(0, "2.0")
        points -= 2_500 * 20

        # 추가 +3 강화 확률 디폴트 값 지정
        self.user_spec_frame.another_third_entry.delete(0, 10)
        if points <= 5_000 * 10:
            self.user_spec_frame.another_third_entry.insert(0, "{:.1f}".format((points // 5_000) / 10))
            self.get_value_calculate_print_all()
            end = time.time()
            print('run time = {:.2f}ms'.format(1000 * (end - start)))
            return
        self.user_spec_frame.another_third_entry.insert(0, "1.0")
        points -= 5_000 * 10

        # 갱신된 값을 받아 계산 후 모두 출력
        self.get_value_calculate_print_all()

        end = time.time()
        print('run time = {:.2f}ms'.format(1000 * (end - start)))


class InputPanedWindow:
    """정보를 입력할 팬윈도우"""
    
    def __init__(self, main_window):
        # 유저 스펙을 기입할 paned window 를 상단에 배치
        self.input_panedwindow = tkinter.PanedWindow(relief="solid", bd=1)
        self.input_panedwindow.pack(side="top")

        # 유저 스펙 레이블 표시
        user_spec_label = tkinter.Label(self.input_panedwindow, text="유저 스펙")
        cho_label = tkinter.Label(self.input_panedwindow, text="고유 유닛 스펙")
        boss_and_multi_label = tkinter.Label(self.input_panedwindow, text="보스 최대 레벨, 파티플레이 버프 여부")
        unit_level_calculate_label = tkinter.Label(self.input_panedwindow, text="보고 싶은 정보")

        # 유저 스펙 레이블 배치
        user_spec_label.grid(row=0, column=0)
        cho_label.grid(row=0, column=1)
        boss_and_multi_label.grid(row=0, column=2)
        unit_level_calculate_label.grid(row=0, column=3)

        self.user_spec_frame = UserSpecFrame(main_window, self.input_panedwindow)
        self.wraith_frame = WraithFrame(main_window, self.input_panedwindow)
        self.bosses_frame = BossesFrame(main_window, self.input_panedwindow)
        self.out_parameters_frame = OutParametersFrame(main_window, self.input_panedwindow)

        self.user_spec_frame.upgrade_rate_frame.grid(row=1, column=0)
        self.wraith_frame.w_frame.grid(row=1, column=1)
        self.bosses_frame.boss_and_multy.grid(row=1, column=2)
        self.out_parameters_frame.unit_information.grid(row=1, column=3)


class UserSpecFrame:
    """유저 스펙을 입력할 프레임"""

    def __init__(self, main_window, input_panedwindow):
        # 유저 스펙 중 강화확률과 공업, 특수 강화확률, 파괴 방지 확률, +1 추가 강화 확률을 기입할 frame 을 유저 스펙 paned window 에 배치
        self.upgrade_rate_frame = tkinter.Frame(input_panedwindow, padx=15)
        input_panedwindow.add(self.upgrade_rate_frame)

        # 유저 레벨 레이블
        user_level_label = tkinter.Label(self.upgrade_rate_frame,
                                         text="유저 레벨 : ")
        user_level_label.grid(row=0, column=0)

        # 유저 레벨 엔트리
        self.user_level_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.user_level_entry.bind("<Return>", main_window.set_expected_upgrade_rate_and_deal_upgrade)
        self.user_level_entry.insert(2, '1')
        self.user_level_entry.grid(row=0, column=1)

        # +1 강화확률 레이블
        first_upgrade_label = tkinter.Label(self.upgrade_rate_frame,
                                            text="+1 강화 확률 : ")
        first_upgrade_label.grid(row=1, column=0)

        # +1 강화확률 엔트리
        self.first_upgrade_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.first_upgrade_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.first_upgrade_entry.insert(2, '0.0')
        self.first_upgrade_entry.grid(row=1, column=1)

        # +2 강화확률 레이블
        second_upgrade_label = tkinter.Label(self.upgrade_rate_frame,
                                             text="+2 강화 확률 : ")
        second_upgrade_label.grid(row=2, column=0)

        # +2 강화확률 엔트리
        self.second_upgrade_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.second_upgrade_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.second_upgrade_entry.insert(2, '0.0')
        self.second_upgrade_entry.grid(row=2, column=1)

        # +3 강화확률 레이블
        third_upgrade_label = tkinter.Label(self.upgrade_rate_frame,
                                            text="+3 강화 확률 : ")
        third_upgrade_label.grid(row=3, column=0)

        # +3 강화확률 엔트리
        self.third_upgrade_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.third_upgrade_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.third_upgrade_entry.insert(2, '0.0')
        self.third_upgrade_entry.grid(row=3, column=1)

        # 유저 공격력 업그레이드 레이블
        user_damage_upgrade_label = tkinter.Label(self.upgrade_rate_frame,
                                                  text="유저 공업 : ")
        user_damage_upgrade_label.grid(row=4, column=0)

        # 유저 공격력 업그레이드 엔트리
        self.user_damage_upgrade_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.user_damage_upgrade_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.user_damage_upgrade_entry.insert(2, '0')
        self.user_damage_upgrade_entry.grid(row=4, column=1)

        # 특수 강화확률 레이블
        special_upgrade_rate_label = tkinter.Label(self.upgrade_rate_frame, text="특수 강화 확률 : ")
        special_upgrade_rate_label.grid(row=0, column=3)

        # 특수 강화확률 엔트리
        self.special_upgrade_rate_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.special_upgrade_rate_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.special_upgrade_rate_entry.insert(2, '0.0')
        self.special_upgrade_rate_entry.grid(row=0, column=4)

        # 파괴 방지 확률 레이블
        prevent_del_rate_label = tkinter.Label(self.upgrade_rate_frame, text="파괴 방지 확률 : ")
        prevent_del_rate_label.grid(row=1, column=3)

        # 파괴 방지 확률 엔트리
        self.prevent_del_rate_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.prevent_del_rate_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.prevent_del_rate_entry.insert(2, '0.0')
        self.prevent_del_rate_entry.grid(row=1, column=4)

        # 추가 +1 강화 확률 레이블
        another_first_label = tkinter.Label(self.upgrade_rate_frame, text="추가 +1 강화 확률 : ")
        another_first_label.grid(row=2, column=3)

        # 추가 +1 강화 확률 엔트리
        self.another_first_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.another_first_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.another_first_entry.insert(2, '0.0')
        self.another_first_entry.grid(row=2, column=4)

        # 추가 +2 강화 확률 레이블
        another_second_label = tkinter.Label(self.upgrade_rate_frame, text="추가 +2 강화 확률 : ")
        another_second_label.grid(row=3, column=3)

        # 추가 +2 강화 확률 엔트리
        self.another_second_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.another_second_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.another_second_entry.insert(2, '0.0')
        self.another_second_entry.grid(row=3, column=4)

        # 추가 +3 강화 확률 레이블
        another_third_label = tkinter.Label(self.upgrade_rate_frame, text="추가 +3 강화 확률 : ")
        another_third_label.grid(row=4, column=3)

        # 추가 +3 강화 확률 엔트리
        self.another_third_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.another_third_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.another_third_entry.insert(2, '0.0')
        self.another_third_entry.grid(row=4, column=4)

        # MX 사냥터 돈 증가량 획득량 레이블
        max_hunting_label = tkinter.Label(self.upgrade_rate_frame, text="MX 사냥터 돈 증가량 : ")
        max_hunting_label.grid(row=5, column=3)

        # MX 사냥터 돈 증가량 획득량 엔트리
        self.max_hunting_entry = tkinter.Entry(self.upgrade_rate_frame, width=7, justify='center')
        self.max_hunting_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.max_hunting_entry.insert(2, '0.0')
        self.max_hunting_entry.grid(row=5, column=4)

        # % 레이블
        p1 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p2 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p3 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p4 = tkinter.Label(self.upgrade_rate_frame, text='회')
        p5 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p6 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p7 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p8 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p9 = tkinter.Label(self.upgrade_rate_frame, text='%')
        p10 = tkinter.Label(self.upgrade_rate_frame, text='%')

        p1.grid(row=1, column=2)
        p2.grid(row=2, column=2)
        p3.grid(row=3, column=2)
        p4.grid(row=4, column=2)
        p5.grid(row=0, column=5)
        p6.grid(row=1, column=5)
        p7.grid(row=2, column=5)
        p8.grid(row=3, column=5)
        p9.grid(row=4, column=5)
        p10.grid(row=5, column=5)


class WraithFrame:
    """고유 유닛 스펙을 입력할 프레임"""
    def __init__(self, main_window, input_panedwindow):
        # 유저 스펙 중 고유 유닛 스펙 Frame 을 유저 스펙 paned window 에 배치
        self.main_window = main_window
        self.w_frame = tkinter.Frame(input_panedwindow, padx=15)
        input_panedwindow.add(self.w_frame)

        # 고유 유닛 단 수 레이블
        w_level_label = tkinter.Label(self.w_frame, text="고유 유닛 단 수 : ")
        w_level_label.grid(row=0, column=0)

        # 고유 유닛 단 수 엔트리
        self.w_level_entry = tkinter.Entry(self.w_frame, width=7, justify='center')
        self.w_level_entry.bind("<Return>", self.set_expected_wraith_upgrade)
        self.w_level_entry.insert(2, '0')
        self.w_level_entry.grid(row=0, column=1)

        # 고유 유닛 경험치 증가량 레이블
        w_exp_rate_label = tkinter.Label(self.w_frame, text="경험치 증가량 : ")
        w_exp_rate_label.grid(row=1, column=0)

        # 고유 유닛 경험치 증가량 엔트리
        self.w_exp_rate_entry = tkinter.Entry(self.w_frame, width=7, justify='center')
        self.w_exp_rate_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.w_exp_rate_entry.insert(2, '0.0')
        self.w_exp_rate_entry.grid(row=1, column=1)

        # 추가 +1 강화 확률 레이블
        w_another_first_label = tkinter.Label(self.w_frame, text="추가 +1 강화 확률 : ")
        w_another_first_label.grid(row=2, column=0)

        # 추가 +1 강화 확률 엔트리
        self.w_another_first_entry = tkinter.Entry(self.w_frame, width=7, justify='center')
        self.w_another_first_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.w_another_first_entry.insert(2, '0.0')
        self.w_another_first_entry.grid(row=2, column=1)

        # 특수 강화 확률 레이블
        w_special_label = tkinter.Label(self.w_frame, text="특수 강화 확률 : ")
        w_special_label.grid(row=3, column=0)

        # 특수 강화 확률 엔트리
        self.w_special_entry = tkinter.Entry(self.w_frame, width=7, justify='center')
        self.w_special_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.w_special_entry.insert(2, '0.0')
        self.w_special_entry.grid(row=3, column=1)

        # 파괴 방지 확률 레이블
        w_zero_label = tkinter.Label(self.w_frame, text="파괴 방지 확률 : ")
        w_zero_label.grid(row=4, column=0)

        # 파괴 방지 확률 엔트리
        self.w_zero_entry = tkinter.Entry(self.w_frame, width=7, justify='center')
        self.w_zero_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.w_zero_entry.insert(2, '0.0')
        self.w_zero_entry.grid(row=4, column=1)

        # % 레이블
        dan = tkinter.Label(self.w_frame, text='단')
        p1 = tkinter.Label(self.w_frame, text='%')
        p2 = tkinter.Label(self.w_frame, text='%')
        p3 = tkinter.Label(self.w_frame, text='%')
        p4 = tkinter.Label(self.w_frame, text='%')

        dan.grid(row=0, column=2)
        p1.grid(row=1, column=2)
        p2.grid(row=2, column=2)
        p3.grid(row=3, column=2)
        p4.grid(row=4, column=2)

    def set_expected_wraith_upgrade(self, event):
        """레이스 단 수에 따라 레이스 스펙 갱신"""

        wraith_level = 0

        # 레이스 단 수 유효성 검사
        try:
            wraith_level = int(self.w_level_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo("레이스 단수 오류",
                                        "레이스 단수는 정수 값을 입력해야 합니다.")

        self.w_exp_rate_entry.delete(0, 10)
        self.w_exp_rate_entry.insert(0, "0.0")
        self.w_another_first_entry.delete(0, 10)
        self.w_another_first_entry.insert(0, "0.0")
        self.w_special_entry.delete(0, 10)
        self.w_special_entry.insert(0, "0.0")
        self.w_zero_entry.delete(0, 10)
        self.w_zero_entry.insert(0, "0.0")

        # 고유 유닛 추가 +1 강화 확률 디폴트 값 지정
        self.w_another_first_entry.delete(0, 10)
        if wraith_level < 20:
            self.w_another_first_entry.insert(0, "{:.2f}".format(wraith_level / 4))
            self.main_window.get_value_calculate_print_all()
            return
        self.w_another_first_entry.insert(0, "5.0")
        wraith_level -= 20

        # 특수 강화 확률 디폴트 값 지정
        self.w_special_entry.delete(0, 10)
        if wraith_level < 10:
            self.w_special_entry.insert(0, "{:.1f}".format(wraith_level / 2))
            self.main_window.get_value_calculate_print_all()
            return
        self.w_special_entry.insert(0, "5.0")
        wraith_level -= 10

        # 추가 경험치 보너스 디폴트 값 지정
        self.w_exp_rate_entry.delete(0, 10)
        if wraith_level < 5:
            self.w_exp_rate_entry.insert(0, "{:.1f}".format(20 * wraith_level))
            self.main_window.get_value_calculate_print_all()
            return
        self.w_exp_rate_entry.insert(0, "100.0")
        wraith_level -= 5

        # 공업, 공속, 사냥터
        wraith_level -= 27

        if wraith_level < 0:
            self.main_window.get_value_calculate_print_all()
            return

        # 파괴 방지 확률 디폴트 값 지정
        self.w_zero_entry.delete(0, 10)
        if wraith_level < 200:
            self.w_zero_entry.insert(0, "{:.1f}".format(wraith_level / 10))
            self.main_window.get_value_calculate_print_all()
            return
        self.w_zero_entry.insert(0, "20.0")

        # 갱신된 값을 받아 계산 후 모두 출력
        self.main_window.get_value_calculate_print_all()


class BossesFrame:
    """보스 단계를 입력할 프레임"""
    def __init__(self, main_window, input_panedwindow):
        # 유저 스펙 중 보스 라운드와 파티플레이 여부를 체크할 frame 을 유저 스펙 paned window 에 배치
        self.boss_and_multy = tkinter.Frame(input_panedwindow, padx=15)
        input_panedwindow.add(self.boss_and_multy)

        # 개인 보스 처치 레벨 레이블
        private_boss_label = tkinter.Label(self.boss_and_multy, text='개인 보스 처치 레벨')
        private_boss_label.grid(row=0, column=0)

        # 개인 보스 처치 최대 레벨
        self.private_boss_count = tkinter.IntVar()
        self.private_0_ratio = tkinter.Radiobutton(self.boss_and_multy, text='0', value=0,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_1_ratio = tkinter.Radiobutton(self.boss_and_multy, text='1', value=1,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_2_ratio = tkinter.Radiobutton(self.boss_and_multy, text='2', value=2,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_3_ratio = tkinter.Radiobutton(self.boss_and_multy, text='3', value=3,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_4_ratio = tkinter.Radiobutton(self.boss_and_multy, text='4', value=4,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_5_ratio = tkinter.Radiobutton(self.boss_and_multy, text='5', value=5,
                                                   variable=self.private_boss_count,
                                                   command=main_window.get_value_calculate_print_all)
        self.private_5_ratio.select()

        self.private_0_ratio.grid(row=0, column=1)
        self.private_1_ratio.grid(row=0, column=2)
        self.private_2_ratio.grid(row=0, column=3)
        self.private_3_ratio.grid(row=0, column=4)
        self.private_4_ratio.grid(row=0, column=5)
        self.private_5_ratio.grid(row=0, column=6)

        # 파티 보스 처치 레벨 레이블
        party_boss_label = tkinter.Label(self.boss_and_multy, text='파티 보스 처치 레벨')
        party_boss_label.grid(row=1, column=0)

        # 파티 보스 처치 최대 레벨
        self.party_boss_count = tkinter.IntVar()
        self.party_0_ratio = tkinter.Radiobutton(self.boss_and_multy, text='0', value=0,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_1_ratio = tkinter.Radiobutton(self.boss_and_multy, text='1', value=1,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_2_ratio = tkinter.Radiobutton(self.boss_and_multy, text='2', value=2,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_3_ratio = tkinter.Radiobutton(self.boss_and_multy, text='3', value=3,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_4_ratio = tkinter.Radiobutton(self.boss_and_multy, text='4', value=4,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_5_ratio = tkinter.Radiobutton(self.boss_and_multy, text='5', value=5,
                                                 variable=self.party_boss_count,
                                                 command=main_window.get_value_calculate_print_all)
        self.party_5_ratio.select()

        self.party_0_ratio.grid(row=1, column=1)
        self.party_1_ratio.grid(row=1, column=2)
        self.party_2_ratio.grid(row=1, column=3)
        self.party_3_ratio.grid(row=1, column=4)
        self.party_4_ratio.grid(row=1, column=5)
        self.party_5_ratio.grid(row=1, column=6)

        # 파티 플레이 여부 레이블
        party_check_label = tkinter.Label(self.boss_and_multy, text='파티 플레이 버프 여부')
        party_check_label.grid(row=2, column=0)

        # 파티 플레이 여부 체크 박스
        self.party_check = tkinter.BooleanVar()
        self.party_check_button = tkinter.Checkbutton(self.boss_and_multy, text='', onvalue=True, offvalue=False,
                                                      variable=self.party_check,
                                                      command=main_window.get_value_calculate_print_all)
        self.party_check_button.select()
        self.party_check_button.grid(row=2, column=1)


class OutParametersFrame:
    """외부 변수를 입력할 프레임"""
    def __init__(self, main_window, input_panedwindow):
        # 유닛 시작 레벨, 마지막 레벨, 판매권 수, 리얼 타임 진행 시간
        # 정보를 가지는 paned window 를 유저 스펙 paned window 에 배치
        self.unit_information = tkinter.Frame(input_panedwindow, padx=15)
        input_panedwindow.add(self.unit_information)

        # 유닛 시작 레벨 레이블
        unit_start_level_label = tkinter.Label(self.unit_information, text='유닛 시작 레벨 : ')
        unit_start_level_label.grid(row=0, column=0)

        # 유닛 시작 레벨 엔트리
        self.unit_start_level_entry = tkinter.Entry(self.unit_information, width=3, justify='center')
        self.unit_start_level_entry.insert(1, '1')
        self.unit_start_level_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.unit_start_level_entry.grid(row=0, column=1)

        # 유닛 마지막 레벨 레이블
        unit_last_level_label = tkinter.Label(self.unit_information, text='유닛 마지막 레벨 : ')
        unit_last_level_label.grid(row=1, column=0)

        # 유닛 마지막 레벨 엔트리
        self.unit_last_level_entry = tkinter.Entry(self.unit_information, width=3, justify='center')
        self.unit_last_level_entry.insert(1, '40')
        self.unit_last_level_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.unit_last_level_entry.grid(row=1, column=1)

        # 판매권 수 레이블
        sell_ticket_label = tkinter.Label(self.unit_information, text='마지막 레벨 유닛 판매 수 : ')
        sell_ticket_label.grid(row=2, column=0)

        # 판매권 수 엔트리
        self.sell_ticket_entry = tkinter.Entry(self.unit_information, width=6, justify='center')
        self.sell_ticket_entry.insert(1, '500')
        self.sell_ticket_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.sell_ticket_entry.grid(row=2, column=1)

        # 방치 시간 레이블
        playing_time_label = tkinter.Label(self.unit_information, text='리얼 타임 진행 시간 : ')
        playing_hour_label = tkinter.Label(self.unit_information, text=' 시간 ')
        playing_minute_label = tkinter.Label(self.unit_information, text=' 분 ')
        playing_second_label = tkinter.Label(self.unit_information, text=' 초')

        # 방치 시간 엔트리
        self.playing_hour_entry = tkinter.Entry(self.unit_information, width=5, justify='center')
        self.playing_minute_entry = tkinter.Entry(self.unit_information, width=3, justify='center')
        self.playing_second_entry = tkinter.Entry(self.unit_information, width=3, justify='center')

        self.playing_hour_entry.insert(1, '3')
        self.playing_minute_entry.insert(1, '0')
        self.playing_second_entry.insert(1, '0')

        self.playing_hour_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.playing_minute_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.playing_second_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)

        playing_time_label.grid(row=3, column=0)
        playing_hour_label.grid(row=3, column=2)
        self.playing_hour_entry.grid(row=3, column=1)
        playing_minute_label.grid(row=3, column=4)
        self.playing_minute_entry.grid(row=3, column=3)
        playing_second_label.grid(row=3, column=6)
        self.playing_second_entry.grid(row=3, column=5)

        # 플레이어 목표 레벨 레이블
        player_end_level_label = tkinter.Label(self.unit_information, text='플레이어 목표 레벨 : ')
        player_end_level_label.grid(row=4, column=0)

        # 플레이어 목표 레벨 엔트리
        self.player_end_level_entry = tkinter.Entry(self.unit_information, width=7, justify='center')
        self.player_end_level_entry.insert(2, '150')
        self.player_end_level_entry.bind("<Return>", main_window.get_entry_value_calculate_print_all)
        self.player_end_level_entry.grid(row=4, column=1)


class UnitInfoPanedWindow:
    """유닛 정보를 보여줄 팬윈도우"""
    def __init__(self):
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

        self.unit_info_frame = UnitFrame(unit_information_panedwindow, 'upgrade-rate')
        self.unit_dps_frame = UnitFrame(unit_information_panedwindow, 'dps')
        self.unit_exp_frame = UnitFrame(unit_information_panedwindow, 'exp')

        self.unit_info_frame.unit_info_frame.grid(row=1, column=0)
        self.unit_dps_frame.unit_info_frame.grid(row=1, column=1)
        self.unit_exp_frame.unit_info_frame.grid(row=1, column=2)


class UnitFrame:
    """유닛 강화확률, dps, exp 정보를 보여줄 프레임"""
    def __init__(self, unit_info_panedwindow, mod):
        # 유닛 강화 확률 정보를 담을 frame 을 유닛 정보를 담을 paned window 에 배치
        self.unit_info_frame = tkinter.Frame(unit_info_panedwindow, padx=15, pady=5)

        unit_info_scrollbar = tkinter.Scrollbar(self.unit_info_frame)
        unit_info_scrollbar.pack(side='right', fill='y')

        w = 62

        if mod == 'upgrade-rate':
            w = 38
        elif mod == 'dps':
            w = 45
        elif mod == 'exp':
            w = 62

        self.unit_info_listbox = tkinter.Listbox(self.unit_info_frame,
                                                 yscrollcommand=unit_info_scrollbar.set,
                                                 width=w, height=10)
        self.unit_info_listbox.pack(side='left')

        unit_info_scrollbar["command"] = self.unit_info_listbox.yview


class PrintPanedWindow:
    """계산 결과를 보여줄 팬윈도우"""
    def __init__(self):
        # 나머지 정보들을 담을 paned window
        the_other_panedwindow = tkinter.PanedWindow()
        the_other_panedwindow.pack(side='top', pady=5)

        # level to level 제목 레이블
        level_to_level_title_lable = tkinter.Label(the_other_panedwindow, padx=75)
        level_to_level_title_lable.config(text="===============유닛 레벨 계산 결과===============\n")
        level_to_level_title_lable.grid(row=0, column=0)

        # level to level 레이블을 나머지 정보들을 담을 paned window 에 추가
        self.level_to_level_label = tkinter.Label(the_other_panedwindow)
        self.level_to_level_label.grid(row=1, column=0)

        # player level calc 제목 레이블
        player_calc_title_label = tkinter.Label(the_other_panedwindow, padx=75)
        player_calc_title_label.config(text="===============플레이어 레벨 계산 결과===============\n")
        player_calc_title_label.grid(row=0, column=1)

        # player level calc frame 을 나머지 정보들을 담을 paned window 에 추가
        player_calc_frame = tkinter.Frame(the_other_panedwindow)
        player_calc_frame.grid(row=1, column=1)

        self.player_calc_label = tkinter.Label(player_calc_frame)
        self.player_calc_label.pack(side='top')

        player_calc_unit_number_frame = tkinter.Frame(player_calc_frame)
        player_calc_unit_number_frame.pack(side='top')

        self.player_calc_25_40 = tkinter.Label(player_calc_unit_number_frame, padx=10)
        self.player_calc_25_40.grid(row=0, column=0)

        self.player_calc_41_44 = tkinter.Label(player_calc_unit_number_frame, padx=10)
        self.player_calc_41_44.grid(row=0, column=1)


if __name__ == '__main__':
    main = MainWindow()
