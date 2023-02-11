from static_info.static_info import *


class UserSpecParameter:
    """UserSpec 파라미터로 사용되는 클래스"""

    def __init__(self, player_level, first, second, third, zero,
                 user_damage_up_rate, private_boss, party_boss, multi_player,
                 special_upgrade_rate, another_first, another_second, another_third,
                 w_exp_rate, w_another_first, w_special_rate, w_zero,
                 max_hunting_rate):
        self.player_level = player_level
        self.first = first + another_first
        self.second = second + another_second
        self.third = third + another_third
        self.zero = zero
        self.user_damage_up_rate = user_damage_up_rate
        self.private_boss = private_boss
        self.party_boss = party_boss
        self.multi_player = multi_player
        self.special_upgrade_rate = special_upgrade_rate
        self.w_exp_rate = w_exp_rate
        self.w_another_first = w_another_first
        self.w_special_rate = w_special_rate
        self.w_zero = w_zero
        self.max_hunting_rate = max_hunting_rate


class UserSpec:
    """스펙을 입력 받아 강화 확률을 계산하여 유저 스펙으로 저장"""

    def __init__(self, parameters):
        # 유저 스펙에서 사용하지 않는 self 변수는 혹시 출력할 일이 생길 때 사용하기 위해 남겨 놓음

        self.first = parameters.first  # +1 강화 확률
        self.second = parameters.second  # +2 강화 확률
        self.third = parameters.third  # +3 강화 확률
        self.zero = parameters.zero + parameters.w_zero  # 유지 확률
        self.private_boss = parameters.private_boss  # 개인 보스 잡은 최대 레벨
        self.party_boss = parameters.party_boss  # 파티 보스 잡은 최대 레벨
        self.multi_player = parameters.multi_player  # 멀티 플레이 여부
        self.special_upgrade_rate = parameters.special_upgrade_rate  # 40강 이후 특수 강화 확률

        self.damage_up_rate = 1.0 + parameters.user_damage_up_rate  # 데미지 조정 비율
        self.exp_up_rate = 1.0  # 경험치 조정 비율

        self.exp_up_rate += parameters.w_exp_rate  # 고유 유닛 경험치 증가량 확률 추가
        self.first += parameters.w_another_first  # 고유 유닛 추가 +1 강화 확률 추가
        self.special_upgrade_rate += parameters.w_special_rate  # 고유 유닛 특수 강화 확률 추가
        self.max_hunting_rate = 1.0 + parameters.max_hunting_rate   # MAX 허수아비 돈 수급량 증가량 추가

        # 개인 보스 조건에 따라 유저 스펙 갱신
        if parameters.private_boss >= 1:
            self.first += 0.01
        if parameters.private_boss >= 2:
            self.first += 0.01
        if parameters.private_boss >= 3:
            self.first += 0.01
            self.damage_up_rate += 0.5
        if parameters.private_boss >= 4:
            self.damage_up_rate += 0.5
            self.exp_up_rate += 0.1
        if parameters.private_boss >= 5:
            self.damage_up_rate += 0.5
            self.exp_up_rate += 0.1

        # 파티 보스 조건에 따라 유저 스펙 갱신
        if parameters.party_boss >= 1:
            self.first += 0.01
        if parameters.party_boss >= 2:
            self.first += 0.01
            self.damage_up_rate += 0.5
        if parameters.party_boss >= 3:
            self.exp_up_rate += 0.3
        if parameters.party_boss >= 4:
            self.damage_up_rate += 0.5

        # 멀티 플레이 여부에 따라 유저 스펙 갱신
        if parameters.multi_player:
            self.first += 0.01
            self.damage_up_rate += 1.5

        # 레벨 1000 이하일 경우 경험치 비율 추가
        if parameters.player_level <= 1000:
            self.exp_up_rate += 1

        # 형식 변화 중 길게 나오는 소숫점 제거
        self.damage_up_rate = round(self.damage_up_rate, 1)
        self.exp_up_rate = round(self.exp_up_rate, 1)
        self.first = round(self.first, 4)
        self.second = round(self.second, 4)
        self.third = round(self.third, 4)

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
        """유저 스펙 문자열 반환"""
        return '+1 강화확률 : %.2f%% , +2 강화확률 : %.2f%% , +3 강화확률 : %.2f%%, ' % \
               (self.first * 100, self.second * 100, self.third * 100) + \
               '파괴 방지 확률 : {:.2f}% , '.format(float(self.zero * 100)) + \
               '특수 강화 확률 : {:.2f}% , '.format(float(self.special_upgrade_rate * 100)) + \
               '데미지 조정 비율 : {}% , '.format(int(self.damage_up_rate * 100)) + \
               '경험치 조정 비율 : {}%\n'.format(int(self.exp_up_rate * 100))


class Unit:
    """
    특정 level 의 유닛 정보를 담는 클래스\n
    level, dps, expected_next_dps_rate, exp, expected_next_exp_rate, +1, +2, +3 강화 확률 정보 가짐\n
    next_dps_rate, next_exp_rate 는 Calculator 클래스 객체로 계산 후 갱신
    """

    def __init__(self, user_spec, level):

        self.level = level  # 유닛 레벨
        self.dps = int(unit_information[level][3] * user_spec.return_damage_up_rate())  # 조정된 dps
        self.exp = unit_information[level][4] * user_spec.return_exp_up_rate()  # 조정된 exp
        self.next_dps_rate = 0  # 강화했을 때 예상되는 dps 비율
        self.next_exp_rate = 0  # 강화했을 때 예상되는 exp 비율
        self.one = unit_information[level][0]  # +1 강화 확률
        self.two = unit_information[level][1]  # +2 강화 확률
        self.three = unit_information[level][2]  # +3 강화 확률
        self.zero = user_spec.zero  # 강화 유지 확률

        sum_of_upgrade_rate = user_spec.first + user_spec.second + user_spec.third + user_spec.special_upgrade_rate

        if level >= UNIT_MAX_LEVEL:  # 마지막 레벨의 유닛은 예외 처리
            self.one = 0.0
            self.two = 0.0
            self.three = 0.0
            return

        # 특수 강화 확률
        if level >= SECOND_MAX_LEVEL:
            self.one += user_spec.special_upgrade_rate

        # 유닛 레벨에 따른 +1, +2, +3 강화 확률 적용
        if level >= 36:
            self.one += user_spec.third
            self.one += user_spec.second
        else:
            self.two += user_spec.second
            if level == 35:
                self.two += user_spec.third
            else:
                self.three += user_spec.third

        self.one += user_spec.first

        # 강화 확률이 - 이면 0으로 바꿈
        if self.one < 0:
            self.one = 0.0

    def __str__(self):
        """
        특정 레벨의 유닛의 강화 확률 문자열 반환\n
        40강 이상이라면 +2, +3 강화확률 대신 유지 확률 반환
        """
        if self.level >= SECOND_MAX_LEVEL:
            return '{:2d}강 / +1 : {:.2f}% , 유지 확률 : {:.2f}%\n'.format(self.level, self.one * 100, self.zero * 100)
        else:
            return '{:2d}강 / +1 : {:.2f}% , +2 : {:.2f}% , +3 : {:.2f}%\n'.format(self.level, self.one * 100,
                                                                                  self.two * 100, self.three * 100)

    def print_unit_dps(self):
        """
        특정 레벨의 유닛의 dps 정보를 반환\n
        23, 24, 25, 40강 유닛은 강화했을 때 dps 변화 비율 대신 돈 증가 비율을 출력 (mps)\n
        """
        if self.level == SECOND_MAX_LEVEL or self.level == FIRST_MAX_LEVEL or \
                self.level == FIRST_MAX_LEVEL - 1 or self.level == FIRST_MAX_LEVEL - 2:
            return '{:2d}강 / dps : {:7,} , 강화 시 mps 변화 비율 : {:.3f}\n'.format(self.level,
                                                                             self.dps, self.next_dps_rate)
        else:
            return '{:2d}강 / dps : {:7,} , 강화 시 dps 변화 비율 : {:.3f}\n'.format(self.level,
                                                                             self.dps, self.next_dps_rate)

    def print_unit_exp(self):
        """특정 레벨의 유닛의 exp 정보를 반환"""
        return '{:2d}강 / 판매경험치 : {:12,} , 강화 시 판매경험치 변화 비율: {:.3f}\n'.format(self.level,
                                                                             self.exp, self.next_exp_rate)

    def get_unit_exp(self):
        return self.exp


class OutParameter:
    """유저 스펙 외의 정보를 담는 클래스"""

    def __init__(self, unit_start_level, unit_last_level, sell_unit_number,
                 hours, minutes, seconds, player_start_level, player_last_level):
        self.unit_start_level = unit_start_level
        self.unit_last_level = unit_last_level
        self.sell_unit_number = sell_unit_number
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.player_start_level = player_start_level
        self.player_last_level = player_last_level


class UnitCalculator:
    """유닛 관련 계산, 반환, 출력 담당 클래스"""

    def __init__(self, user_spec, input_unit_dict, out_parameters):
        self.first, self.second, self.third = user_spec.return_123()  # 유저 스펙 +1, +2, +3 강화 확률
        self.damage_up_rate = user_spec.return_damage_up_rate()  # 데미지 조정 비율
        self.exp_up_rate = user_spec.return_exp_up_rate()  # 경험치 조정 비율
        self.max_hunting_rate = user_spec.max_hunting_rate  # MX 사냥터 돈 획득량 증가량
        # key : level, value : instance of Unit class
        self.unit_dict = input_unit_dict  # Unit 인스턴스를 담은 딕셔너리
        self.zero = user_spec.zero  # 유지 확률
        self.out_parameters = out_parameters  # 외부 파라미터

    @staticmethod
    def div_time(input_seconds):
        """
        시간(초)을 입력받아 년, 달, 일, 시간, 분, 초로 나눠 반환\n
        입력 시간은 float 형식
        """

        seconds = input_seconds

        minutes = seconds // 60
        seconds %= 60

        hours = minutes // 60
        minutes %= 60

        days = hours // 24
        hours %= 24

        months = days // 30
        days %= 30

        years = months // 12
        months %= 12

        return years, months, days, hours, minutes, seconds

    @staticmethod
    def return_str_div_time(years, months, days, hours, minutes, seconds):
        """분리된 시간을 입력받아 str 형식으로 출력"""
        if years == 0 and months == 0 and days == 0 and hours == 0 and minutes == 0 and seconds == 0:
            return '0 초 '

        temp_string = ""

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
        if seconds > 0.0:
            temp_string += '{:.2f}초 '.format(seconds)

        return temp_string

    def set_next_dps_rate(self):
        """
        유닛을 강화했을 때 예상되는 dps 변화 비율을 갱신\n
        계산된 값은 유닛 딕셔러니의 각 유닛 인스턴스에 갱신됨
        """

        # 다음 유닛 레벨로 넘어갈 때 기대되는 mps(dps) 변화 비율 (성공 100% 가정)
        dps_rate_dict = {}

        for i in range(len(self.unit_dict) + 3):
            dps_rate_dict[i+1] = 0

        for i in range(len(self.unit_dict) - 1):
            curr_level = i + 1
            if curr_level == 25:
                dps_rate_dict[curr_level] = MPS_25
            elif curr_level == 40:
                dps_rate_dict[curr_level] = MPS_40 * self.max_hunting_rate
            elif curr_level >= UNIT_MAX_LEVEL:
                break
            else:
                dps_rate_dict[curr_level] = self.unit_dict[curr_level + 1].dps / self.unit_dict[curr_level].dps

        # 성공 100% dps 변화 비율에 강화 성공 확률 적용 / Unit 인스턴스에 next dps rate 계산 후 갱신
        # +3 증가의 성공 100% dps 변화 비율은 성공 100% dps 변화 비율을 차례대로 세번 곱하면 나옴
        for i in range(len(self.unit_dict)):

            curr_level = i + 1
            curr_unit = self.unit_dict[curr_level]
            curr_unit.next_dps_rate = 0

            if curr_level >= UNIT_MAX_LEVEL:
                break

            # 파괴 방지
            if curr_level >= SECOND_MAX_LEVEL:
                curr_unit.next_dps_rate += curr_unit.zero

            curr_multiply = dps_rate_dict[curr_level]
            curr_unit.next_dps_rate += curr_unit.one * curr_multiply

            if curr_unit.two == 0.0:
                continue

            curr_multiply *= dps_rate_dict[curr_level+1]
            curr_unit.next_dps_rate += curr_unit.two * curr_multiply

            if curr_unit.three == 0.0:
                continue

            curr_multiply *= dps_rate_dict[curr_level+2]
            curr_unit.next_dps_rate += curr_unit.three * curr_multiply

    def set_next_exp_rate(self, input_start_level=15):
        """유닛을 강화 했을 때 기대되는 exp 변화량 계산"""

        # 총 유닛 레벨 수만큼 반복
        for i in range(len(self.unit_dict)):

            start_level = input_start_level  # 갱신을 시작할 레벨

            curr_level = i + start_level  # 값을 찾을 레벨
            curr_unit = self.unit_dict[curr_level]  # 해당 레벨의 유닛 인스턴스 가져옴
            curr_unit.next_exp_rate = 0  # 해당 유닛을 강화했을 때 예상되는 exp 변화 비율 초기화

            # 마지막 레벨이면 값을 0으로 남겨놓고 갱신 종료
            if curr_level >= UNIT_MAX_LEVEL:
                break

            curr_unit.next_exp_rate += curr_unit.one * self.unit_dict[curr_level+1].exp

            if curr_unit.two == 0:
                curr_unit.next_exp_rate /= curr_unit.exp
                continue

            curr_unit.next_exp_rate += curr_unit.two * self.unit_dict[curr_level+2].exp

            if curr_unit.three == 0:
                curr_unit.next_exp_rate /= curr_unit.exp
                continue

            curr_unit.next_exp_rate += curr_unit.three * self.unit_dict[curr_level+3].exp
            curr_unit.next_exp_rate /= curr_unit.exp

    def return_number_unit_level_to_level(self):
        """
        유닛 시작 레벨부터 마지막 레벨 한 마리를 만들기 위한 시작 레벨 유닛 갯수 반환\n
        유닛을 만들 수 없다면 None 반환
        """

        # 유닛 레벨에 따른 비율을 담을 딕셔너리
        temp_dict = {}

        # 딕셔너리 초기화
        for i in range(self.out_parameters.unit_start_level, self.out_parameters.unit_last_level + 3):
            temp_dict[i] = 0

        temp_dict[self.out_parameters.unit_start_level] = 1.0  # 시작 레벨 1마리가 있다고 가정

        # 마지막 레벨에 도달할 때까지 계산 반복
        for i in range(self.out_parameters.unit_start_level, self.out_parameters.unit_last_level):
            curr_number = temp_dict[i]  # 해당 레벨에 유닛 수
            temp_dict[i + 1] += curr_number * self.unit_dict[i].one  # +1 레벨에 유닛 추가
            temp_dict[i + 2] += curr_number * self.unit_dict[i].two  # +2 레벨에 유닛 추가
            temp_dict[i + 3] += curr_number * self.unit_dict[i].three  # +3 레벨에 유닛 추가

            if i >= SECOND_MAX_LEVEL:  # 40강 이상이라면 유지 확률 적용    /   등비수열 총합 이론
                temp_dict[i + 1] /= 1 - self.unit_dict[i].zero
                temp_dict[i + 2] /= 1 - self.unit_dict[i].zero
                temp_dict[i + 3] /= 1 - self.unit_dict[i].zero

        if temp_dict[self.out_parameters.unit_last_level] == 0:  # 유닛을 만들 수 없다면 None 반환
            return None

        # 마지막 레벨 한 마리를 만들기 위해서 필요한 시작 레벨 유닛 수
        numbers_of_unit = int(1 / temp_dict[self.out_parameters.unit_last_level])

        return numbers_of_unit

    # need
    def return_str_number_unit_level_to_level(self):
        """마지막 레벨 한 마리를 만들기 위한 시작 레벨 유닛 갯수 출력"""

        # 마지막 레벨 유닛 한 마리를 만들기 위해 필요한 시작 레벨 유닛 갯수
        numbers_of_unit = self.return_number_unit_level_to_level()

        # 마지막 유닛을 만들 수 없을 때 예외 처리
        if numbers_of_unit is None:
            return '{}강 유닛은 만들 수 없습니다.\n'.format(self.out_parameters.unit_last_level)

        # 마지막 level 하나를 만들기 위해 필요한 시작 level 유닛의 개수를 출력
        return '{}강 하나를 만들기 위해선 {}강이 평균 {:,}마리가 필요합니다\n'.format(self.out_parameters.unit_last_level,
                                                                self.out_parameters.unit_start_level,
                                                                numbers_of_unit)

    def return_time_unit_level_to_level(self):
        """시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간 반환"""

        # 마지막 레벨 유닛 한 마리를 만들기 위해 필요한 시작 레벨 유닛 갯수
        numbers_of_unit = self.return_number_unit_level_to_level()

        # 마지막 유닛을 만들 수 없을 때 None 반환
        if numbers_of_unit is None:
            return None

        # 시작 레벨을 최대 가속인 상태에서 무한 생산하는 경우를 가정
        # 마지막 레벨 1마리를 뽑기 위해서 필요한 시간
        seconds = numbers_of_unit / BEST_FRAME_RATE  # 필요한 시간 = 필요한 유닛 / 유닛을 뽑는 속도
        return seconds

    # need
    def return_str_time_unit_level_to_level(self):
        """시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간 출력"""

        # 시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛 하나를 만드는 데 걸리는 시간
        seconds = self.return_time_unit_level_to_level()

        # 마지막 유닛을 만들 수 없으면 예외 처리
        if seconds is None:
            return ""

        # 시, 분, 초로 변환
        years, months, days, hours, minutes, seconds = self.div_time(seconds)

        acc_time = BEST_FRAME_RATE / FRAME_RATE  # 게임 최대 가속

        temp_string = ""

        # 마지막 레벨 하나를 만들기 위해 필요한 시간 출력
        temp_string += '----만약 {}강을 최대 시간 가속 비율({:.2f}배)에서 끊임 없이 생산 중이라면----\n\n'.format(
            self.out_parameters.unit_start_level,
            acc_time)
        temp_string += '{}강 하나를 만들기 위한 리얼 타임 평균 : '.format(self.out_parameters.unit_last_level)

        temp_string += self.return_str_div_time(years, months, days, hours, minutes, seconds)

        temp_string += "\n"

        return temp_string

    # need
    def return_str_time_with_sell_unit_level_to_level(self):
        """시작 레벨 유닛을 최대 속도로 생산한다고 가정, 마지막 유닛을 sell unit number 만큼 만드는 데 걸리는 시간 출력"""

        # 마지막 유닛 하나를 만들기 위한 시작 유닛 갯수, 걸리는 시간
        numbers_of_unit, seconds = self.return_number_unit_level_to_level(), self.return_time_unit_level_to_level()

        # 마지막 유닛을 만들 수 없으면 예외 처리
        if numbers_of_unit is None:
            return ""

        # 유닛을 특정 마리수 팔았을 때 걸리는 시간
        seconds *= self.out_parameters.sell_unit_number

        # 시, 분, 초로 변환
        years, months, days, hours, minutes, seconds = self.div_time(seconds)

        # 마지막 level 하나를 만들기 위해 필요한 시작 level 유닛의 개수를 출력

        temp_string = ""

        temp_string += '{}강을 {}마리 판매하기 위해 리얼 타임 평균 '.format(self.out_parameters.unit_last_level,
                                                            self.out_parameters.sell_unit_number)
        temp_string += self.return_str_div_time(years, months, days, hours, minutes, seconds)

        temp_string += '의 시간이 필요합니다\n'

        return temp_string

    def return_sell_number_with_time_unit_level_to_level(self):
        """특정 시간을 방치했을 때 판매되는 유닛 갯수 반환"""

        # 유닛 판매 특정 시간
        seconds = 3_600 * self.out_parameters.hours + 60 * self.out_parameters.minutes + self.out_parameters.seconds
        # 마지막 유닛을 하나 만드는 데 필요한 시간
        time_one_unit = self.return_time_unit_level_to_level()

        # 마지막 유닛을 만들 수 없다면 None 반환
        if time_one_unit is None:
            return None

        # 특정 시간 방치했을 때 판매되는 유닛 갯수 반환
        return int(seconds / time_one_unit)

    # need
    def return_str_sell_number_with_time_unit_level_to_level(self):
        """특정 시간을 방치했을 때 판매되는 유닛 갯수 출력"""

        # 유닛 판매 특정 시간, 특정 시간동안 판매되는 유닛 갯수
        seconds = 3600 * self.out_parameters.hours + 60 * self.out_parameters.minutes + self.out_parameters.seconds
        ticket_number = self.return_sell_number_with_time_unit_level_to_level()

        # 마지막 유닛을 만들 수 없다면 예외 처리
        if ticket_number is None:
            return ""

        temp_string = ""

        years, months, days, hours, minutes, seconds = self.div_time(seconds)
        temp_string += '{}강의 유닛을 리얼 타임 '.format(self.out_parameters.unit_last_level)
        temp_string += self.return_str_div_time(years, months, days, hours, minutes, seconds)
        temp_string += '동안 팔 경우 '.format(seconds)
        temp_string += '평균 {:,}개의 유닛이 판매됩니다\n'.format(ticket_number)

        return temp_string


class ExpOfLevel:
    """플레이어 레벨을 받고 레벨 업 경험치, 모인 경험치 계산, 반환 담당 클래스"""

    def __init__(self, level):
        self.level = level  # 플레이어 레벨
        self.need_exp = 0  # 레벨 업에 필요한 경험치
        self.total_exp = 0  # 해당 레벨까지 모인 경험치

    def set_need_exp(self):
        """레벨 업에 필요한 경험치 계산"""
        self.need_exp = 3 * self.level * self.level - 3 * self.level + 10

    def set_total_exp(self):
        """level 까지 모인 경험치 계산"""
        level = self.level - 1
        self.total_exp = int(3 * level * (level + 1) * (2 * level + 1) / 6 - 3 * level * (level + 1) / 2 + 10 * level)

    def get_need_exp(self):
        """레벨 업에 필요한 경험치 반환"""
        return self.need_exp

    def get_total_exp(self):
        """level 까지 모인 경험치 반환"""
        return self.total_exp


class PlayerLevelCalculator:
    """플레이어 레벨 경험치 관련 계산, 반환, 출력 담당 클래스"""

    def __init__(self, unit_dictionary, out_parameters):
        self.unit_dictionary = unit_dictionary  # Unit 인스턴스를 담은 딕셔너리
        self.out_parameters = out_parameters  # 외부 파라미터
        self.exp_level_to_level = 0
        self.set_exp_player_level_to_level()

    def return_str_exp_to_player_level_up(self):
        """해당 레벨에서 레벨 업에 필요한 경험치 출력"""

        # 레벨업에 필요한 경험치 계산 후 str 반환
        exp_of_level = ExpOfLevel(self.out_parameters.player_start_level)
        exp_of_level.set_need_exp()
        return '플레이어 레벨 : {:,}, 레벨업에 필요한 경험치 : {:,}\n'.format(self.out_parameters.player_start_level,
                                                              exp_of_level.get_need_exp())

    def set_exp_player_level_to_level(self):
        """시작 -> 마지막 레벨까지 필요한 경험치 계산 후 반환"""

        # 시작 레벨까지의 경험치, 마지막 레벨까지의 경험치 차이를 반환
        st = ExpOfLevel(self.out_parameters.player_start_level)
        en = ExpOfLevel(self.out_parameters.player_last_level)
        st.set_total_exp()
        en.set_total_exp()

        self.exp_level_to_level = en.get_total_exp() - st.get_total_exp()

    def return_str_25_40_number(self):
        """플레이어 목표 레벨까지 도달하기 위해 필요한 유닛 25, 26, 37, 38, 39, 40강 갯수"""
        sum_exp = self.exp_level_to_level

        # 해당 경험치까지 도달하기 위해 팔아야 하는 유닛
        level_25 = int(sum_exp / self.unit_dictionary[25].get_unit_exp()) + 1
        level_26 = int(sum_exp / self.unit_dictionary[26].get_unit_exp()) + 1
        level_37 = int(sum_exp / self.unit_dictionary[37].get_unit_exp()) + 1
        level_38 = int(sum_exp / self.unit_dictionary[38].get_unit_exp()) + 1
        level_39 = int(sum_exp / self.unit_dictionary[39].get_unit_exp()) + 1
        level_40 = int(sum_exp / self.unit_dictionary[40].get_unit_exp()) + 1

        temp_string = ""
        temp_string += '25강 갯수 : {:,}\n'.format(level_25)
        temp_string += '26강 갯수 : {:,}\n'.format(level_26)
        temp_string += '37강 갯수 : {:,}\n'.format(level_37)
        temp_string += '38강 갯수 : {:,}\n'.format(level_38)
        temp_string += '39강 갯수 : {:,}\n'.format(level_39)
        temp_string += '40강 갯수 : {:,}\n'.format(level_40)

        return temp_string

    def return_str_41_44_number(self):
        """플레이어 목표 레벨까지 도달하기 위해 필요한 유닛 41, 42, 43, 44강 갯수"""

        sum_exp = self.exp_level_to_level

        # 해당 경험치까지 도달하기 위해 팔아야 하는 유닛
        level_41 = int(sum_exp / self.unit_dictionary[41].get_unit_exp()) + 1
        level_42 = int(sum_exp / self.unit_dictionary[42].get_unit_exp()) + 1
        level_43 = int(sum_exp / self.unit_dictionary[43].get_unit_exp()) + 1
        level_44 = int(sum_exp / self.unit_dictionary[44].get_unit_exp()) + 1

        temp_string = ""
        temp_string += '41강 갯수 : {:,}\n'.format(level_41)
        temp_string += '42강 갯수 : {:,}\n'.format(level_42)
        temp_string += '43강 갯수 : {:,}\n'.format(level_43)
        temp_string += '44강 갯수 : {:,}\n'.format(level_44)

        return temp_string

    def return_str_player_level_to_level(self):
        """
        시작 -> 마지막 레벨까지 필요한 경험치 계산 후 출력
        """

        return '플레이어 레벨 {} -> {} 에 필요한 경험치 : {:,}\n'.format(self.out_parameters.player_start_level,
                                                              self.out_parameters.player_last_level,
                                                              self.exp_level_to_level)

    @staticmethod
    def return_final_player_level(player_start_level, get_exp):
        """플레이어 시작 레벨과 들어오는 경험치를 받아 최종 플레이어 레벨을 계산, 반환"""

        start_exp_of_level = ExpOfLevel(player_start_level)  # 플레이어 시작 레벨
        start_exp_of_level.set_total_exp()  # 플레이어 레벨까지 경험치 총합
        sum_exp = get_exp + start_exp_of_level.get_total_exp()  # 들어오는 경험치 더하기
        level = PLAYER_MAX_LEVEL  # 계산에 사용할 플레이어 시작 레벨
        last_level = PLAYER_MAX_LEVEL   # 계산에 사용할 마지막 플레이어 레벨

        # 계산에 활용할 ExpOfLevel 인스턴스
        temp_eol = ExpOfLevel(level)
        temp_eol.set_total_exp()

        # PLAYER_MAX_LEVEL 부터 4로 나누면서 시작 플레이어 레벨 찾음
        while temp_eol.total_exp > sum_exp:
            last_level = level
            level = int(level/4)
            temp_eol = ExpOfLevel(level)
            temp_eol.set_total_exp()

        temp_eol.set_need_exp()

        # 최종 플레이어 레벨 찾을 때까지 반복
        # 이분법 적용
        while temp_eol.total_exp > sum_exp or sum_exp >= temp_eol.total_exp + temp_eol.need_exp:

            # 최대 플레이어 레벨일 경우 예외처리
            if temp_eol.level == PLAYER_MAX_LEVEL:
                break

            # 플레이어 시작, 마지막 레벨의 중간 값 기준
            temp_eol = ExpOfLevel(int((level + last_level)/2))
            temp_eol.set_total_exp()

            # 중간 값 기준으로 반 나눠서 반복문 다시 적용
            if temp_eol.total_exp <= sum_exp:
                level += int((last_level - level)/2)
            else:
                last_level -= int((last_level - level)/2)

            temp_eol.set_need_exp()

        return level


class GameInfo:
    """
    게임 정보 클래스\n
    모든 클래스 사용, 모든 동작 구현
    """

    def __init__(self):
        self.unit_dict = {}  # Unit 인스턴스 저장할 딕셔너리
        self.user = None  # 유저 스펙
        self.unit_calc = None  # 유닛 레벨 계산기
        self.player_calc = None  # 플레이어 레벨 계산기
        self.out_parameters = None  # 외부 파라미터

    def init_game_info(self, parameters, out_parameters):
        """
        user, unit_dict, unit_calc, player_calc 구성\n
        next dps, exp rate 갱신
        """

        # 유저 스펙을 보스와 멀티 플레이 환경에 맞게 저장
        self.user = UserSpec(parameters)  # 유저 스펙 초기화
        self.out_parameters = out_parameters  # 외부 파라미터

        # key <- level / value <- Unit 으로 초기화
        # Unit 인스턴스를 가지는 딕셔너리
        for j in range(len(unit_information)):
            current_level = j + 1
            self.unit_dict[current_level] = Unit(self.user, current_level)

        self.unit_calc = UnitCalculator(self.user, self.unit_dict, out_parameters)  # 유닛 레벨 계산기 초기화
        self.player_calc = PlayerLevelCalculator(self.unit_dict, out_parameters)  # 플레이어 레벨 계산기 초기화

        self.unit_calc.set_next_dps_rate()  # 유닛 next dps rate 갱신
        self.unit_calc.set_next_exp_rate()  # 유닛 next exp rate 갱신

    def return_str_user_spec(self):
        """유저 스펙 반환"""
        return self.user.__str__()

    def return_str_unit_info(self):
        """유닛 강화 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.__str__()
            temp_str += "\n"

        return temp_str

    def return_str_unit_dps_info(self):
        """유닛 dps 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.print_unit_dps()
            temp_str += "\n"

        return temp_str

    def return_str_unit_exp_info(self):
        """유닛 exp 정보 반환"""

        temp_str = ""
        for level, value in self.unit_dict.items():
            temp_str += value.print_unit_exp()
            temp_str += "\n"

        return temp_str

    def return_str_final_level_with_units(self):
        """유닛을 특정 갯수를 팔았을 때 플레이어 레벨 계산하고 출력"""

        # 마지막 유닛을 뽑을 수 없다면 예외 처리
        if self.unit_calc.return_sell_number_with_time_unit_level_to_level() is None:
            return " "

        # 추가 되는 경험치
        get_exp = 0

        # 유저 레벨이 1000 을 넘어간다면 추가연산 필요 없음
        if self.player_calc.out_parameters.player_start_level > 1000:
            get_exp = self.player_calc.unit_dictionary[
                          self.out_parameters.unit_last_level].get_unit_exp() * self.out_parameters.sell_unit_number
        else:  # 유저 레벨이 1000 이하라면
            curr_user_level = ExpOfLevel(self.player_calc.out_parameters.player_start_level)
            thousand_level = ExpOfLevel(1001)

            curr_user_level.set_total_exp()
            thousand_level.set_total_exp()

            # 현재 유저 레벨 ~ 1000 레벨까지 남은 exp
            to_thousand_exp = thousand_level.total_exp - curr_user_level.total_exp

            # 들어온 경험치로 레벨 1000 을 못 찍는다면 그대로 진행
            if self.player_calc.unit_dictionary[self.out_parameters.unit_last_level].get_unit_exp() * \
                    self.out_parameters.sell_unit_number < to_thousand_exp:
                get_exp = self.player_calc.unit_dictionary[self.out_parameters.unit_last_level].get_unit_exp() * \
                          self.out_parameters.sell_unit_number
            else:  # 아니라면 레벨 1000 초과 후 발생하는 경험치 버프 손실을 적용

                # 1000 레벨까지 들어간 경험치
                get_exp += to_thousand_exp

                # 1000 레벨까지 들어간 경험치를 체우고 남은 유닛 갯수
                remain_number_unit = self.out_parameters.sell_unit_number - to_thousand_exp // \
                    self.player_calc.unit_dictionary[self.out_parameters.unit_last_level].get_unit_exp()

                # UserSpec 인스턴스 복사
                temp_user = self.user
                # UserSpec 인스턴스의 exp_up_rate 에서 초보자 경험치 버프를 제거
                temp_user.exp_up_rate -= 1
                # 초보자 경험치가 버프된 UnitSpec 인스턴스를 받는 Unit 인스턴스 생성
                temp_unit = Unit(temp_user, self.out_parameters.unit_last_level)

                # 초보자 버프가 제외된 유닛으로 경험치 계산
                get_exp += temp_unit.get_unit_exp() * remain_number_unit

        # 최종 플레이어 레벨
        level = self.player_calc.return_final_player_level(self.out_parameters.player_start_level, get_exp)

        return '플레이어 레벨 {} -> {}\n'.format(self.out_parameters.player_start_level, level)

    def return_str_final_player_level_with_units(self):
        """out_parameters 관련 유닛 정보, 유닛 판매 갯수에 따른 플레이어 최종 레벨 출력"""

        temp_string = ""

        temp_string += self.unit_calc.return_str_time_unit_level_to_level()
        temp_string += "\n"
        self.unit_calc.return_str_number_unit_level_to_level()
        temp_string += self.unit_calc.return_str_time_with_sell_unit_level_to_level()
        temp_string += self.return_str_final_level_with_units()

        return temp_string

    def return_str_final_level_with_times(self):
        """유닛을 특정 시간 팔았을 때 플레이어 레벨 계산하고 출력"""

        # 특정 시간 판매할 때 유닛 수
        sell_number = self.unit_calc.return_sell_number_with_time_unit_level_to_level()

        # 마지막 유닛을 못 생산한다면 예외 처리
        if sell_number is None:
            return " "

        # 추가 되는 경험치
        get_exp = 0

        # 유저 레벨이 1000 을 넘어간다면 추가연산 필요 없음
        if self.player_calc.out_parameters.player_start_level > 1000:
            get_exp = self.player_calc.unit_dictionary[
                          self.out_parameters.unit_last_level].get_unit_exp() * sell_number
        else:  # 유저 레벨이 1000 이하라면

            # 1000 레벨까지 남은 경험치 구함
            curr_user_level = ExpOfLevel(self.player_calc.out_parameters.player_start_level)
            thousand_level = ExpOfLevel(1001)

            curr_user_level.set_total_exp()
            thousand_level.set_total_exp()

            # 현재 유저 레벨 ~ 1000 레벨까지 남은 exp
            to_thousand_exp = thousand_level.total_exp - curr_user_level.total_exp

            # 들어온 경험치로 레벨 1000 을 못 찍는다면 그대로 진행
            if self.player_calc.unit_dictionary[
                    self.out_parameters.unit_last_level].get_unit_exp() * sell_number < to_thousand_exp:
                get_exp = self.player_calc.unit_dictionary[
                              self.out_parameters.unit_last_level].get_unit_exp() * sell_number
            else:  # 아니라면 레벨 1000 초과 후 발생하는 경험치 버프 손실을 적용

                # 1000 레벨까지 들어간 경험치
                get_exp += to_thousand_exp

                # 1000 레벨까지 들어간 경험치를 체우고 남은 유닛 갯수
                remain_number_unit = sell_number - to_thousand_exp // \
                    self.player_calc.unit_dictionary[self.out_parameters.unit_last_level].get_unit_exp()

                # UserSpec 인스턴스 복사
                temp_user = self.user
                # UserSpec 인스턴스의 exp_up_rate 에서 초보자 경험치 버프를 제거
                temp_user.exp_up_rate -= 1
                # 초보자 경험치가 버프된 UnitSpec 인스턴스를 받는 Unit 인스턴스 생성
                temp_unit = Unit(temp_user, self.out_parameters.unit_last_level)

                # 초보자 버프가 제외된 유닛으로 경험치 계산
                get_exp += temp_unit.get_unit_exp() * remain_number_unit

        level = self.player_calc.return_final_player_level(self.out_parameters.player_start_level, get_exp)

        return '플레이어 레벨 {} -> {}\n'.format(self.out_parameters.player_start_level, level)

    def return_str_final_player_level_with_time(self):
        """out_parameters 관련 유닛 판매 시간에 따른 플레이어 최종 레벨 출력"""

        temp_string = ""

        # 특정 시간을 방치했을 때 판매되는 유닛 갯수 출력
        temp_string += self.unit_calc.return_str_sell_number_with_time_unit_level_to_level()
        # 유닛을 특정 시간 팔았을 때 플레이어 레벨 계산하고 출력
        temp_string += self.return_str_final_level_with_times()

        return temp_string


if __name__ == '__main__':
    pass
