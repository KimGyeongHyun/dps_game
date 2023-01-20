FRAME_RATE = 24
BEST_FRAME_RATE = 77

# 유닛 기본 강화 확률, dps, 경험치 / key : level, value : (+1, +2, +3 강화 확률, dps, exp)
unit_information = {
    1: (0.6, 0.06, 0.006, 1, 0),
    2: (0.6, 0.06, 0.006, 3, 0),
    3: (0.575, 0.0575, 0.00575, 7, 0),
    4: (0.543, 0.0543, 0.00543, 10, 0),
    5: (0.5, 0.05, 0.005, 15, 0),
    6: (0.5, 0.05, 0.005, 25, 0),
    7: (0.5, 0.05, 0.005, 40, 0),
    8: (0.5, 0.05, 0.005, 60, 0),
    9: (0.47, 0.047, 0.0047, 80, 0),
    10: (0.465, 0.0465, 0.00465, 125, 0),
    11: (0.463, 0.0463, 0.00463, 167, 0),
    12: (0.452, 0.0452, 0.00452, 200, 0),
    13: (0.45, 0.045, 0.0045, 275, 0),
    14: (0.45, 0.045, 0.0045, 333, 0),
    15: (0.44, 0.044, 0.0044, 433, 1),
    16: (0.44, 0.044, 0.0044, 500, 2),
    17: (0.44, 0.044, 0.0044, 560, 5),
    18: (0.43, 0.043, 0.0043, 900, 10),
    19: (0.42, 0.042, 0.0042, 1_146, 15),
    20: (0.38, 0.038, 0.0038, 2_000, 27),
    21: (0.38, 0.038, 0.0038, 2_700, 45),
    22: (0.36, 0.036, 0.0036, 3_500, 80),
    23: (0.36, 0.036, 0.0036, 5_000, 160),
    24: (0.35, 0.035, 0.0035, 6500, 335),
    25: (0.3, 0.03, 0.003, 9550, 750),
    26: (0.25, 0.025, 0.0025, 10, 7_500),
    27: (0.25, 0.025, 0.0025, 15, 10_500),
    28: (0.25, 0.025, 0.0025, 20, 18_750),
    29: (0.25, 0.025, 0.0025, 30, 30_000),
    30: (0.25, 0.025, 0.0025, 50, 51_000),
    31: (0.25, 0.025, 0.0025, 80, 94_000),
    32: (0.20, 0.02, 0.002, 150, 150_000),
    33: (0.20, 0.02, 0.002, 233, 250_000),
    34: (0.20, 0.02, 0.002, 350, 500_000),
    35: (0.20, 0.022, 0.0, 600, 800_000),
    36: (0.1776, 0.0, 0.0, 1_000, 2_000_000),
    37: (0.1332, 0.0, 0.0, 2_000, 4_000_000),
    38: (0.111, 0.0, 0.0, 4_000, 6_000_000),
    39: (0.0555, 0.0, 0.0, 6_685, 10_000_000),
    40: (0.0, 0.0, 0.0, 16_685, 25_000_000)
}


class UserSpec:
    """보스와 멀티플레이 환경에 따라 강화 확률 조정하여 유저 스펙으로 저장"""

    def __init__(self, player_level, first, second, third,
                 user_damage_up_rate, private_boss, party_boss, multi_player):
        # 유저 스펙에서 사용하지 않는 self 변수는 혹시 출력할 일이 생길 때 사용하기 위해 남겨 놓음

        self.first = first  # +1 강화 확률
        self.second = second  # +2 강화 확률
        self.third = third  # +3 강화 확률
        self.private_boss = private_boss  # 개인 보스 잡은 최대 레벨
        self.party_boss = party_boss  # 파티 보스 잡은 최대 레벨
        self.multi_player = multi_player  # 멀티 플레이 여부

        self.damage_up_rate = 1.0 + user_damage_up_rate  # 데미지 조정 비율
        self.exp_up_rate = 1.0  # 경험치 조정 비율

        # 개인 보스 조건에 따라 유저 스펙 갱신
        if private_boss >= 1:
            self.first += 0.01
        if private_boss >= 2:
            self.first += 0.01
        if private_boss >= 3:
            self.first += 0.01
            self.damage_up_rate += 0.5
        if private_boss >= 4:
            self.damage_up_rate += 0.5
            self.exp_up_rate += 0.1
        if private_boss >= 5:
            self.damage_up_rate += 0.5
            self.exp_up_rate += 0.1

        # 파티 보스 조건에 따라 유저 스펙 갱신
        if party_boss >= 1:
            self.first += 0.01
        if party_boss >= 2:
            self.first += 0.01
            self.damage_up_rate += 0.5
        if party_boss >= 3:
            self.exp_up_rate += 0.3
        if party_boss >= 4:
            self.damage_up_rate += 0.5

        # 멀티 플레이 여부에 따라 유저 스펙 갱신
        if multi_player:
            self.first += 0.01
            self.damage_up_rate += 1.5

        # 레벨 1000 미만일 경우 경험치 비율 추가
        if player_level < 1000:
            self.exp_up_rate += 1

        self.damage_up_rate = round(self.damage_up_rate, 1)
        self.exp_up_rate = round(self.exp_up_rate, 1)
        self.first = round(self.first, 3)
        self.second = round(self.second, 3)
        self.third = round(self.third, 3)

    def return_123(self):
        """유저 스펙의 +1, +2, +3 강화 확률을 반환"""
        return self.first, self.second, self.third

    def return_damage_up_rate(self):
        """유저 스펙의 데미지 조정 비율을 반환"""
        return self.damage_up_rate

    def return_exp_up_rate(self):
        """유저 스펙의 경험치 조정 비율을 반환"""
        return self.exp_up_rate

    def __str__(self):
        """유저 스펙을 반환"""
        return '+1 강화확률 : %.1f%% , +2 강화확률 : %.1f%% , +3 강화확률 : %.1f%%, ' % \
               (self.first * 100, self.second * 100, self.third * 100) + \
               '데미지 조정 비율 : {}% , '.format(int(self.damage_up_rate * 100)) + \
               '경험치 조정 비율 : {}%\n'.format(int(self.exp_up_rate * 100))


class Unit:
    """
    특정 level 의 유닛 정보를 담는 클래스

    level, dps, expected_next_dps_rate, exp, expected_next_exp_rate, +1, +2, +3 강화 확률 정보 가짐

    next_dps_rate, next_exp_rate 는 Calculator 클래스 객체로 계산 후 갱신
    """

    def __init__(self, user_spec, level, one, two, three, dps=0, exp=0):

        self.level = level  # 유닛 레벨
        self.dps = int(dps * user_spec.return_damage_up_rate())  # 조정된 dps
        self.exp = exp * user_spec.return_exp_up_rate()  # 조정된 exp
        self.next_dps_rate = 0  # 강화했을 때 예상되는 dps 비율
        self.next_exp_rate = 0  # 강화했을 때 예상되는 exp 비율
        self.one = one  # +1 강화 확률
        self.two = two  # +2 강화 확률
        self.three = three  # +3 강화 확률

        first, second, third = user_spec.return_123()  # 유저 스펙으로 추가되는 +1, +2, +3 강화 확률

        # 레벨 조건에 맞게 유저 스펙으로 올라가는 강화 확률을 +1, +2, +3 강화 확률에 분배
        self.one += first

        if self.level > 35:
            self.one += second
        else:
            self.two += second

        if self.level == 35:
            self.two += third
        elif self.level >= 36:
            self.one += third
        else:
            self.three += third

    def __str__(self):
        """특정 레벨의 유닛의 강화 확률을 반환"""
        return '{:2d}강 / +1 : {:.2f}% , +2 : {:.2f}% , +3 : {:.2f}%'.format(self.level, self.one * 100,
                                                                            self.two * 100, self.three * 100)

    def print_unit_dps(self):
        """특정 레벨의 유닛의 dps 정보를 반환"""
        if self.level == 25:
            return '{:2d}강 / dps : {:7,} , (두번째 사냥터로 넘어갑니다)'.format(self.level, self.dps)
        else:
            return '{:2d}강 / dps : {:7,} , 강화 시 dps 변화 비율 : {:.3f}'.format(self.level,
                                                                       self.dps, self.next_dps_rate)

    def print_unit_exp(self):
        """특정 레벨의 유닛의 exp 정보를 반환"""
        return '{:2d}강 / 판매경험치 : {:12,} , 강화 시 판매경험치 변화 비율: {:.3f}'.format(self.level,
                                                                           self.exp, self.next_exp_rate)

    def get_unit_exp(self):
        return self.exp


class UnitCalculator:
    """유저 스펙으로 조정된 유닛 정보를 받아 다양하게 정보를 처리하는 클래스"""

    def __init__(self, user_spec, input_unit_dict):
        self.first, self.second, self.third = user_spec.return_123()  # 유저 스펙 +1, +2, +3 강화 확률
        self.damage_up_rate = user_spec.return_damage_up_rate()  # 데미지 조정 비율
        self.exp_up_rate = user_spec.return_exp_up_rate()  # 경험치 조정 비율
        # key : level, value : instance of Unit class
        self.unit_dict = input_unit_dict

    @staticmethod
    def div_time(input_seconds):

        calc_hours = 0
        calc_minutes = 0
        calc_seconds = input_seconds

        if calc_seconds >= 60:
            calc_minutes = calc_seconds // 60
            calc_seconds %= 60

        if calc_minutes >= 60:
            calc_hours = calc_minutes // 60
            calc_minutes %= 60

        return calc_hours, calc_minutes, calc_seconds

    # def print_all_units(self):
    #     """모든 유닛의 강화 확률을 출력"""
    #
    #     print('-----unit upgrade rate information-----')
    #
    #     for level, value in self.unit_dict.items():
    #         print(value)
    #     print()

    def set_next_dps_expected_rate(self):
        """
        유닛을 강화했을 때 예상되는 dps 변화 비율을 갱신

        계산된 값은 유닛 딕셔러니의 각 유닛 인스턴스에 갱신됨
        """

        # 유닛 레벨 수만큼 반복
        for i in range(len(self.unit_dict)):

            curr_level = i + 1  # 값을 찾을 레벨
            curr_unit = self.unit_dict[curr_level]  # 해당 레벨의 유닛 인스턴스 가져옴
            curr_unit.next_dps_rate = 0  # 해당 유닛을 강화했을 때 예상되는 dps 변화 비율 초기화

            if curr_level == 25:
                continue

            if curr_level == 24:
                curr_unit.next_dps_rate += curr_unit.one * self.unit_dict[curr_level + 1].dps
                curr_unit.next_dps_rate += curr_unit.two * self.unit_dict[curr_level + 1].dps
                curr_unit.next_dps_rate += curr_unit.three * self.unit_dict[curr_level + 1].dps
                curr_unit.next_dps_rate /= curr_unit.dps
                continue

            if curr_level == 23:
                curr_unit.next_dps_rate += curr_unit.one * self.unit_dict[curr_level + 1].dps
                curr_unit.next_dps_rate += curr_unit.two * self.unit_dict[curr_level + 2].dps
                curr_unit.next_dps_rate += curr_unit.three * self.unit_dict[curr_level + 2].dps
                curr_unit.next_dps_rate /= curr_unit.dps
                continue

            # 40 레벨이면 값을 0으로 남겨놓고 갱신 종료
            if curr_level >= 40:
                break

            # 39 레벨 이하의 유닛 +1 강화했을 때 예상되는 dps 비율 추가
            curr_unit.next_dps_rate += curr_unit.one * self.unit_dict[curr_level + 1].dps

            # 39 레벨이면 값을 갱신, 넘어감
            if curr_level == 39:
                curr_unit.next_dps_rate /= curr_unit.dps
                continue

            # 38 레벨 이하의 유닛 +2 강화했을 때 예상되는 dps 비율 추가
            curr_unit.next_dps_rate += curr_unit.two * self.unit_dict[curr_level + 2].dps

            # 38 레벨이면 값을 갱신, 넘어감
            if curr_level == 38:
                curr_unit.next_dps_rate /= curr_unit.dps
                continue

            # 37 레벨 이하의 유닛 +3 강화했을 때 예상되는 dps 비율 추가
            curr_unit.next_dps_rate += curr_unit.three * self.unit_dict[curr_level + 3].dps

            # 37 레벨 이하의 유닛에 계산된 값 갱신
            curr_unit.next_dps_rate /= curr_unit.dps

    def set_next_exp_expected_rate(self, input_start_level=15):
        """유닛을 강화 했을 때 기대되는 exp 변화량 계산"""

        # 총 유닛 레벨 수만큼 반복
        for i in range(len(self.unit_dict)):

            start_level = input_start_level  # 갱신을 시작할 레벨

            curr_level = i + start_level  # 값을 찾을 레벨
            curr_unit = self.unit_dict[curr_level]  # 해당 레벨의 유닛 인스턴스 가져옴
            curr_unit.next_exp_rate = 0  # 해당 유닛을 강화했을 때 예상되는 exp 변화 비율 초기화

            # 40 레벨이면 값을 0으로 남겨놓고 갱신 종료
            if curr_level >= 40:
                break

            # 39 레벨 이하의 유닛 +1 강화했을 때 예상되는 exp 비율 추가
            curr_unit.next_exp_rate += curr_unit.one * self.unit_dict[curr_level + 1].exp

            # 39 레벨이면 값을 갱신, 넘어감
            if curr_level == 39:
                curr_unit.next_exp_rate /= curr_unit.exp
                continue

            # 38 레벨 이하의 유닛 +2 강화했을 때 예상되는 exp 비율 추가
            curr_unit.next_exp_rate += curr_unit.two * self.unit_dict[curr_level + 2].exp

            # 38 레벨이면 값을 갱신, 넘어감
            if curr_level == 38:
                curr_unit.next_exp_rate /= curr_unit.exp
                continue

            # 37 레벨 이하의 유닛 +3 강화했을 때 예상되는 exp 비율 추가
            curr_unit.next_exp_rate += curr_unit.three * self.unit_dict[curr_level + 3].exp

            # 37 레벨 이하의 유닛에 계산된 값 갱신
            curr_unit.next_exp_rate /= curr_unit.exp

    # def print_unit_dps_information(self, start_level=1):
    #     """start level 부터 유닛의 level, dps, expected next dps rate 를 출력"""
    #
    #     print('-----unit dps information-----')
    #
    #     for level, value in self.unit_dict.items():
    #         if level >= start_level:
    #             print(value.print_unit_dps())
    #     print()
    #
    # def print_unit_exp_information(self, start_level=15):
    #     """start level 부터 유닛의 level, exp, expected next exp rate 를 출력"""
    #
    #     print('-----unit exp information-----')
    #
    #     for level, value in self.unit_dict.items():
    #         if level >= start_level:
    #             print(value.print_unit_exp())
    #     print()

    # 제거 예정
    # def find_all_dps_increase_rate_and_print(self, first_input_index=26, last_input_index=40):
    #     """
    #     first_input_index 를 시작으로 last_input_index 레벨까지 모든 dps 기댓값 비율을 출력
    #     """
    #
    #     start_index = first_input_index
    #     last_index = last_input_index
    #     start_rate = 1.0
    #     print('-----find all dps increase rate-----')
    #     print('start level : {}, end level : {}'.format(start_index, last_index))
    #
    #     for i in range(start_index, last_index):
    #         start_rate *= self.unit_dict[i].next_dps_rate
    #         print('level : {} -> {} / expected dps rate : {:.3f}'.format(start_index, i + 1, start_rate))
    #
    #     print()
    #
    # # 제거 유무 확인
    # def find_best_dps_increase_and_print(self, first_input_index=26, last_input_index=40):
    #     """
    #     first_input_index 으로 들어오는 레벨 기준으로 last_input_index 레벨까지 비교해서
    #
    #     어느 레벨까지 강화 하는 것이 dps 기댓값이 제일 높을지 출력
    #     """
    #
    #     start_index = first_input_index
    #     last_index = last_input_index
    #     start_rate = 1.0
    #     rate_list = [1.0]
    #
    #     for i in range(start_index, last_index):
    #         start_rate *= self.unit_dict[i].next_dps_rate
    #         rate_list.append(start_rate)
    #
    #     best_index = rate_list.index(max(rate_list)) + start_index
    #     print('-----find best dps increase level-----')
    #     print('start level : {} / end level : {} / best dps level : {}'.format(start_index, last_index, best_index))
    #
    #     print()
    #
    # # 제거 유무 확인
    # def find_best_exp_increase_and_print(self, first_input_index=15, last_input_index=40):
    #     """
    #         first_input_index 으로 들어오는 레벨 기준으로 last_input_index 레벨까지 비교해서
    #
    #         어느 레벨까지 강화 하는 것이 exp 기댓값이 제일 높을지 출력
    #         """
    #
    #     start_index = first_input_index
    #     last_index = last_input_index
    #     start_rate = 1.0
    #     rate_list = [1.0]
    #
    #     for i in range(start_index, last_index):
    #         start_rate *= self.unit_dict[i].next_exp_rate
    #         rate_list.append(start_rate)
    #
    #     best_index = rate_list.index(max(rate_list)) + start_index
    #     print('-----find best exp increase level-----')
    #     print('{}강에서 시작, {}강까지 비교한 결과 {}강까지 강화해서 파는 것이 판매경험치 효율이 제일 좋습니다'.format(start_index,
    #                                                                              last_index, best_index))
    #     print()

    def return_number_level_to_level(self, first_input_index=30, last_input_index=40):
        """마지막 레벨 한 마리를 만들기 위한 시작 레벨 유닛 갯수 반환"""

        temp_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0,
            16: 0,
            17: 0,
            18: 0,
            19: 0,
            20: 0,
            21: 0,
            22: 0,
            23: 0,
            24: 0,
            25: 0,
            26: 0,
            27: 0,
            28: 0,
            29: 0,
            30: 0,
            31: 0,
            32: 0,
            33: 0,
            34: 0,
            35: 0,
            36: 0,
            37: 0,
            38: 0,
            39: 0,
            40: 0,
            41: 0,
            42: 0,
            43: 0,
        }
        if type(first_input_index) != int:
            print("ERROR. need int type value in first_input_index parameter")
            return
        else:
            temp_dict[first_input_index] = 1.0  # 시작 레벨 1마리가 있다고 가정

        # 마지막 레벨에 도달할 때까지 계산 반복
        for i in range(first_input_index, last_input_index):
            curr_number = temp_dict[i]  # 해당 레벨에 유닛 수
            temp_dict[i + 1] += curr_number * self.unit_dict[i].one  # +1 레벨에 유닛 추가
            temp_dict[i + 2] += curr_number * self.unit_dict[i].two  # +2 레벨에 유닛 추가
            temp_dict[i + 3] += curr_number * self.unit_dict[i].three  # +3 레벨에 유닛 추가

        numbers_of_unit = int(1 / temp_dict[last_input_index])  # 마지막 레벨 한 마리를 만들기 위해서 필요한 시작 레벨 유닛 수

        return numbers_of_unit

    def return_time_level_to_level(self, first_input_index=30, last_input_index=40):
        """시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간 반환"""

        numbers_of_unit = self.return_number_level_to_level(first_input_index, last_input_index)

        # 시작 레벨을 최대 가속인 상태에서 무한 생산하는 경우를 가정
        # 마지막 레벨 1마리를 뽑기 위해서 필요한 시간
        seconds = numbers_of_unit / BEST_FRAME_RATE  # 필요한 시간 = 필요한 유닛 / 유닛을 뽑는 속도
        return seconds

    def return_str_number_level_to_level(self, first_input_index=30, last_input_index=40):
        """마지막 레벨 한 마리를 만들기 위한 시작 레벨 유닛 갯수 출력"""

        numbers_of_unit = self.return_number_level_to_level(first_input_index, last_input_index)

        # 마지막 level 하나를 만들기 위해 필요한 시작 level 유닛의 개수를 출력
        return '{}강 하나를 만들기 위해선 {}강이 평균 {:,}마리가 필요합니다'.format(last_input_index, first_input_index,
                                                            numbers_of_unit)

    def return_str_time_level_to_level(self, first_input_index=30, last_input_index=40):
        """시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간 출력"""

        seconds = self.return_time_level_to_level(first_input_index, last_input_index)

        # 시, 분, 초로 변환
        hours, minutes, seconds = self.div_time(seconds)

        days = hours // 24
        hours %= 24

        months = days // 30
        days %= 30

        years = months // 12
        months %= 12

        acc_time = BEST_FRAME_RATE / FRAME_RATE  # 게임 최대 가속

        temp_string = ""

        # 마지막 레벨 하나를 만들기 위해 필요한 시간 출력
        temp_string += '----만약 {}강을 최대 시간 가속 비율({:.2f}배)에서 끊임 없이 생산 중이라면----\n\n'.format(first_input_index,
                                                                                         acc_time)
        temp_string += '{}강 하나를 만들기 위해 리얼 타임 평균 : '.format(last_input_index)

        if years > 0:
            temp_string += '{}년 '.format(int(years))
        if months > 0:
            temp_string += '{}달 '.format(int(months))
        if days > 0:
            temp_string += '{}일 '.format(int(days))
        if hours > 0:
            temp_string += '{}시간 '.format(int(hours))
        if minutes > 0:
            temp_string += '{}분 '.format(int(minutes))
        temp_string += '{:.2f}초'.format(seconds)

        # if hours != 0:
        #     temp_string += '{}시간 '.format(int(hours))
        #     temp_string += '{}분 '.format(int(minutes))
        # else:
        #     if minutes != 0:
        #         temp_string += '{}분 '.format(int(minutes))
        # temp_string += '{:.2f}초'.format(seconds)
        # temp_string += '의 시간이 필요합니다'

        return temp_string

    def return_str_sell_time_level_to_level(self, first_input_index=30, last_input_index=40, sell_number=500):
        """판매 티켓을 특정 갯수 팔기 위해 필요한 시간 출력"""
        numbers_of_unit, seconds = self.return_number_level_to_level(first_input_index, last_input_index), \
                                   self.return_time_level_to_level(first_input_index, last_input_index)
        seconds *= sell_number

        # 시, 분, 초로 변환
        hours, minutes, seconds = self.div_time(seconds)

        days = hours // 24
        hours %= 24

        months = days // 30
        days %= 30

        years = months // 12
        months %= 12

        # 마지막 level 하나를 만들기 위해 필요한 시작 level 유닛의 개수를 출력

        temp_string = ""

        temp_string += '{}강을 {}마리 판매하기 위해 리얼 타임 평균 '.format(last_input_index, sell_number)
        if years > 0:
            temp_string += '{}년 '.format(int(years))
        if months > 0:
            temp_string += '{}달 '.format(int(months))
        if days > 0:
            temp_string += '{}일 '.format(int(days))
        if hours > 0:
            temp_string += '{}시간 '.format(int(hours))
        if minutes > 0:
            temp_string += '{}분 '.format(int(minutes))
        temp_string += '{:.2f}초'.format(seconds)
        temp_string += '의 시간이 필요합니다'

        return temp_string

    def return_str_level_to_level(self, first_input_index=30, last_input_index=40, sell_number=500):
        """
        마지막 레벨 한 마리를 만들기 위한 시작 레벨 유닛 갯수 출력\n
        시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간 출력\n
        판매 티켓을 특정 갯수 팔기 위해 필요한 시간 출력
        """

        temp_string = ""
        temp_string += self.return_str_number_level_to_level(first_input_index, last_input_index)
        temp_string += "\n\n"
        temp_string += self.return_str_time_level_to_level(first_input_index, last_input_index)
        temp_string += "\n\n"
        temp_string += self.return_str_sell_time_level_to_level(first_input_index, last_input_index, sell_number)

        return temp_string

    def return_sell_number_level_to_level(self, first_input_index=30, last_input_index=40, input_seconds=0):
        """특정 시간을 방치했을 때 소모되는 판매티켓 갯수 반환"""

        seconds = input_seconds
        time_one_unit = self.return_time_level_to_level(first_input_index, last_input_index)

        return int(seconds / time_one_unit)

    def return_str_sell_number_level_to_level(self, first_input_index=30, last_input_index=40,
                                              input_hours=0, input_minutes=0, input_seconds=0):
        """특정 시간을 방치했을 때 소모되는 판매티켓 갯수 출력"""

        seconds = 3600 * input_hours + 60 * input_minutes + input_seconds
        ticket_number = self.return_sell_number_level_to_level(first_input_index, last_input_index, seconds)

        temp_string = ""

        hours, minutes, seconds = self.div_time(seconds)
        temp_string += '{}강의 유닛을 리얼 타임 '.format(last_input_index)
        if hours != 0:
            temp_string += '{}시간 '.format(hours)
            temp_string += '{}분 '.format(minutes)
        else:
            if minutes != 0:
                temp_string += '{}분 '.format(minutes)
        temp_string += '{}초 동안 팔 경우'.format(seconds)
        temp_string += '평균 {:,}개의 유닛이 판매됩니다'.format(ticket_number)

        return temp_string


class ExpOfLevel:
    """플레이어 레벨을 받고 레벨 업에 필요한 경험치를 계산"""

    def __init__(self, level):
        self.level = level
        self.need_exp = 0
        self.total_exp = 0

    def set_need_exp(self):
        """레벨 업에 필요한 경험치 계산"""
        self.need_exp = 3 * self.level * self.level - 3 * self.level + 10

    def set_total_exp(self):
        l = self.level - 1
        self.total_exp = int(3 * l * (l + 1) * (2 * l + 1) / 6 - 3 * l * (l + 1) / 2 + 10 * l)

    def get_need_exp(self):
        """레벨 업에 필요한 경험치 반환"""
        return self.need_exp

    def get_total_exp(self):
        return self.total_exp


class PlayerLevelCalculator:
    """플레이어 레벨 경험치 관련 계산 클래스"""

    def __init__(self, unit_dictionary):
        self.unit_dictionary = unit_dictionary

    @staticmethod
    def return_str_exp_to_level_up(level=1):
        """해당 레벨에서 레벨 업에 필요한 경험치 출력"""

        if level < 1 or level > 10000:
            print('ERROR. invalid player level')
            return

        exp_of_level = ExpOfLevel(level)
        exp_of_level.set_need_exp()
        return '플레이어 레벨 : {}, 레벨업에 필요한 경험치 : {:,}'.format(level, exp_of_level.get_need_exp())

    @staticmethod
    def calculate_exp_to_level_up(start_level=5000, end_level=6000):
        """시작 -> 마지막 레벨까지 필요한 경험치 계산 후 반환"""

        # 등비수열 합공식으로 계산 줄임

        # sum_exp = 0
        #
        # if start_level < 1 or end_level > 10000 or start_level >= end_level:
        #     return
        #
        # for curr_level in range(start_level, end_level):
        #     exp_of_level = ExpOfLevel(curr_level)
        #     exp_of_level.set_need_exp()
        #     sum_exp += exp_of_level.get_need_exp()
        #
        # return sum_exp

        st = ExpOfLevel(start_level)
        en = ExpOfLevel(end_level)
        st.set_total_exp()
        en.set_total_exp()

        return en.get_total_exp() - st.get_total_exp()

    def return_str_need_number_of_unit_to_level_up(self, start_level=1, end_level=10_000):
        """
        시작 -> 마지막 레벨까지 필요한 경험치 계산 후 출력\n
        이에 따른 레벨 37, 38, 39, 40 유닛 갯수 출력
        """

        sum_exp = self.calculate_exp_to_level_up(start_level, end_level)
        if start_level < 1 or end_level > 10000 or start_level > end_level:
            print('ERROR. invalid player level')
            return

        level_25 = int(sum_exp / self.unit_dictionary[25].get_unit_exp()) + 1
        level_26 = int(sum_exp / self.unit_dictionary[26].get_unit_exp()) + 1
        level_37 = int(sum_exp / self.unit_dictionary[37].get_unit_exp()) + 1
        level_38 = int(sum_exp / self.unit_dictionary[38].get_unit_exp()) + 1
        level_39 = int(sum_exp / self.unit_dictionary[39].get_unit_exp()) + 1
        level_40 = int(sum_exp / self.unit_dictionary[40].get_unit_exp()) + 1

        temp_string = ""

        temp_string += '플레이어 레벨 {} -> {} 에 필요한 경험치 : {:,}\n\n'.format(start_level, end_level, sum_exp)
        temp_string += '25강 갯수 : {:,}\n'.format(level_25)
        temp_string += '26강 갯수 : {:,}\n'.format(level_26)
        temp_string += '37강 갯수 : {:,}\n'.format(level_37)
        temp_string += '38강 갯수 : {:,}\n'.format(level_38)
        temp_string += '39강 갯수 : {:,}\n'.format(level_39)
        temp_string += '40강 갯수 : {:,}\n\n'.format(level_40)

        return temp_string

    def return_str_final_level_with_units(self, player_level=1, unit_level=40, unit_number=0):
        """유닛을 팔았을 때 레벨을 계산하고 출력"""

        get_exp = self.unit_dictionary[unit_level].get_unit_exp() * unit_number
        sum_exp = 0
        level = player_level
        while get_exp >= sum_exp:
            exp_of_level = ExpOfLevel(level)
            exp_of_level.set_need_exp()
            sum_exp += exp_of_level.get_need_exp()
            level += 1

        level -= 1

        return '플레이어 레벨 {} -> {}'.format(player_level, level)


class Game:
    """
    게임 클래스\n
    모든 클래스를 사용하여 모든 동작을 구현
    """

    def __init__(self):
        # self.player_level = 1
        # self.first = 0.0
        # self.second = 0.0
        # self.third = 0.0
        # self.user_damage = 0.0
        # self.private_boss = 0
        # self.party_boss = 0
        # self.multi_player = False
        self.unit_dict = {}
        self.user = None
        self.unit_calc = None
        self.player_calc = None

    def set_value(self, player_level, first, second, third, user_damage,
                  private_boss, party_boss, multi_player):
        """
        값을 받고 user, unit_dict, unit_calc 를 구성\n
        next dps, exp rate 갱신
        """
        # self.player_level = player_level
        # self.first = first
        # self.second = second
        # self.third = third
        # self.user_damage = user_damage
        # self.private_boss = private_boss
        # self.party_boss = party_boss
        # self.multi_player = multi_player

        # 유저 스펙을 보스와 멀티 플레이 환경에 맞게 저장
        self.user = UserSpec(player_level, first, second, third, user_damage,
                             private_boss, party_boss, multi_player)

        # key 를 level, value 를 Unit 으로 초기화
        # Unit class 는 각 level 의 dps, exp, +1, +2, +3 강화 확률 가짐
        # 유닛 강화 변화 수치를 user 에서 받음
        # 35, 36 이상 level : 예외 조건에 따라 +2, +3 강화 확률 수치가 +1 에 적용됨
        for j in range(len(unit_information)):
            current_level = j + 1
            self.unit_dict[current_level] = Unit(self.user, current_level, unit_information[current_level][0],
                                                 unit_information[current_level][1],
                                                 unit_information[current_level][2],
                                                 unit_information[current_level][3],
                                                 unit_information[current_level][4])

        self.unit_calc = UnitCalculator(self.user, self.unit_dict)
        self.player_calc = PlayerLevelCalculator(self.unit_dict)

        self.unit_calc.set_next_dps_expected_rate()
        self.unit_calc.set_next_exp_expected_rate()

    def return_user_spec(self):
        return self.user.__str__()

    def return_unit_info(self):
        """유닛 강화 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.__str__()
            temp_str += "\n"

        return temp_str

    def return_unit_dps_info(self):
        """유닛 dps 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.print_unit_dps()
            temp_str += "\n"

        return temp_str

    def return_unit_exp_info(self):
        """유닛 exp 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.print_unit_exp()
            temp_str += "\n"

        return temp_str

    def get_sell_number_return_str_play_time_and_player_level(self, unit_start_level, unit_last_level,
                                                              sell_number,
                                                              player_start_level):

        temp_string = ""

        temp_string += self.unit_calc.return_str_time_level_to_level(unit_start_level, unit_last_level)
        temp_string += "\n"
        self.unit_calc.return_str_number_level_to_level(unit_start_level, unit_last_level)
        temp_string += "\n"
        temp_string += self.unit_calc.return_str_sell_time_level_to_level(unit_start_level, unit_last_level,
                                                                          sell_number)
        temp_string += "\n"
        temp_string += self.player_calc.return_str_final_level_with_units(player_start_level, unit_last_level,
                                                                          sell_number)
        temp_string += "\n"

        return temp_string

    def get_play_time_return_str_sell_number_and_player_level(self, unit_start_level, unit_last_level,
                                                              hours, minutes, seconds,
                                                              player_start_level):

        temp_string = ""
        sell_ticket = self.unit_calc.return_sell_number_level_to_level(unit_start_level, unit_last_level,
                                                                       hours * 3_600 + minutes * 60 + seconds)

        temp_string += self.unit_calc.return_str_sell_number_level_to_level(unit_start_level, unit_last_level,
                                                                            hours, minutes, seconds)
        temp_string += "\n"
        temp_string += self.player_calc.return_str_final_level_with_units(player_start_level, unit_last_level,
                                                                          sell_ticket)
        temp_string += "\n"

        return temp_string


if __name__ == '__main__':
    game = Game()

    player_level = 5000
    first = 0.1
    second = 0.05
    third = 0.03
    deal_upgrade = 5.0
    private_boss = 5
    party_boss = 5
    multi_player = True

    game.set_value(player_level, first, second, third, deal_upgrade, private_boss, party_boss, multi_player)
    print(game.return_unit_info())
    print(game.return_unit_dps_info())
    print(game.return_unit_exp_info())

    unit_start_level = 30
    unit_last_level = 40
    sell_number = 500
    play_hours = 3

    print(game.unit_calc.return_str_level_to_level(unit_start_level, unit_last_level, sell_number))
    print()
    print(game.unit_calc.return_str_sell_number_level_to_level(unit_start_level, unit_last_level, play_hours))

    player_start_level = 5000
    player_last_level = 6000
    sell_unit_level = 40
    sell_unit_number = 500

    print(game.player_calc.return_str_exp_to_level_up(player_start_level))
    print()
    print(game.player_calc.return_str_need_number_of_unit_to_level_up(player_start_level, player_last_level))
    print()
    print(game.player_calc.return_str_final_level_with_units(player_start_level, sell_unit_level, sell_unit_number))

    print(game.get_sell_number_return_str_play_time_and_player_level(unit_start_level, unit_last_level, sell_number,
                                                                     player_start_level))
    print(game.get_play_time_return_str_sell_number_and_player_level(unit_start_level, unit_last_level,
                                                                     play_hours, 0, 0, player_start_level))
