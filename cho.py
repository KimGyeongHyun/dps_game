VAC = 100000


class Cho:

    def __init__(self, level, price, ratio):
        self.level = level
        self.price = price  # 강화 가격
        self.next_price = 1000
        self.next_ratio = ratio[0]
        self.curr_ratio = ratio[1]
        self.prev_ratio = ratio[2]
        self.vac = 0

    def __str__(self):
        return "level : {}, 강화시 들어가는 크래딧 갯수 : {}, 백신 사용했을 때 절약되는 크래딧 갯수 : {}".format(self.level, self.next_price, self.vac)


class ChoCalc:

    def __init__(self, prev_cho, cho):
        self.prev_cho = prev_cho
        self.cho = cho

    def set_next_price(self):
        # 만약 강화를 실패했다면 다시 올리기 위해 이전의 cho 의 next_price(강화 성공 기대 크레딧 갯수) 를 추가한다
        # 그러므로 강화를 실패했다면 기존 강화비용 + 이전 cho 의 next_price 만큼 크레딧이 들어간다
        # 또한 강화 실패의 경우는 강화 유지 상태에서 이전 cho 의 next_price 만큼의 추가 비용이 들어간다고 본다
        # 강화가 유지되었다면 기존 강화비용만 들어간다
        # 즉 강화 실패든 강화 유지든 강화 유지로 보며 강화 실패는 추가비용이 들어간다고 본다

        # 강화 유지시 들어가는 비용을 알았으니 강화 성공을 제외한 나머지 확률로 몇 번이 반복될지 정해야 한다
        # 나머지 확률을 1부터 계속 곱했을 때 50% 이하가 나오는 순간은, 성공할 확률이 반반이란 의미이다
        # 즉 나머지 확률을 1부터 곱했을 때 몇 번째에 50% 이하가 나오는지를 알아야 한다 -> m_number
        # m_number : 강화 성공을 하기 위해 강화를 몇 번할지 맞추는 변수
        # temp_ratio : 1.0 부터 강화 성공을 제외한 나머지 확률을 계속 곱할 변수

        # 현재 강화비용은 m_number 만큼 들어갈 것이며,
        # 강화 실패 / (강화 유지 + 강화 실패) 의 확률로 강화 실패에 대한 추가비용이 들어간다.
        # m_number * price + m_number * prev_cho_next_price * (강화 실패 / (강화 유지 + 강화 실패))

        # 강화기 백신을 사용할 경우 강화 실패시 추가비용이 들어가지 않는다
        # 즉 백신을 사용할 경우
        # m_number * prev_cho_next_price * (강화 실패 / (강화 유지 + 강화 실패)) - 강화기 백신 가격 * 강화 횟수
        # 개의 크래딧이 절약된다
        # - 라면 강화기 백신 가격에 대한 추가 크레딧이 들어가는 것 (손해)

        temp_ratio = 1.0
        m_number = 0

        while temp_ratio > 0.5:
            temp_ratio *= self.cho.prev_ratio + self.cho.curr_ratio
            m_number += 1

        self.cho.vac = int(m_number * self.prev_cho.next_price * (
                    self.cho.prev_ratio / (self.cho.prev_ratio + self.cho.curr_ratio))) - VAC * m_number

        self.cho.next_price = int(m_number * self.cho.price + m_number * self.prev_cho.next_price * (self.cho.prev_ratio / (self.cho.prev_ratio + self.cho.curr_ratio)))

        if self.cho.vac > 0:
            self.cho.next_price -= self.cho.vac


if __name__ == "__main__":

    price = {}
    ratio = {}

    for i in range(10):
        price[i] = i * 1000 + 1000
        ratio[i] = (round(1 - 0.1 * i, 2), round(0.1 * i * (1 - 0.1 * i), 3), round(0.1 * i * (0.1 * i), 3))

    # print(price, ratio)

    cho_dict = {}

    for i in range(10):
        cho_dict[i] = Cho(i, price[i], ratio[i])

    for i in range(1, 10):
        cho_calc = ChoCalc(cho_dict[i-1], cho_dict[i])
        cho_calc.set_next_price()

    cho_sum = 0
    for i in range(10):
        print(cho_dict[i])
        cho_sum += cho_dict[i].next_price

    # 승급 비용
    cho_sum += 1_000_000

    print(cho_sum)

    # 계산 결과 9 레벨에서 백신을 사용해야 하며, 총 크래딧 갯수는 2642459 개에서 2076052 개로 바뀜



