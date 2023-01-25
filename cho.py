class Cho:

    def __init__(self, level):
        self.level = level
        self.next_price = 1000  # 다음 레벨

    def __str__(self):
        return "{}레벨에서 다음 레벨로 넘어가는 예상 비용은 {} 입니다.".format(self.level, self.next_price)


class ChoCalc:

    def __init__(self, prev_cho, cho):
        self.prev_cho = prev_cho
        self.cho = cho

    def set_next_price(self, price_dict, ratio_dict):
        # 실패 시 복구하는 데 들어가는 비용
        prev_total = self.prev_cho.next_price * ratio_dict[self.cho.level][2]
        # 강화가 유지될 때 들어가는 비용
        curr_total = price_dict[self.cho.level] * ratio_dict[self.cho.level][1]
        # 다음 레벨 넘어가는 예상 비용
        # 기본 강화 비용 + 실패 시 복구하는 데 들어가는 비용 + 강화가 유지될 때 들어가는 비용
        self.cho.next_price = prev_total + curr_total + price_dict[self.cho.level]
        print("{}, {}, {}, {}".format(self.cho.level, prev_total, curr_total, self.cho.next_price))


if __name__ == "__main__":

    price = {}
    ratio = {}

    for i in range(10):
        price[i] = i * 1000 + 1000
        ratio[i] = (round(1 - 0.1 * i, 2), round(0.1 * i * (1 - 0.1 * i), 3), round(0.1 * i * (0.1 * i), 3))

    print(price, ratio)

    cho_dict = {}

    for i in range(10):
        cho_dict[i] = Cho(i)

    for i in range(1, 10):
        cho_calc = ChoCalc(cho_dict[i-1], cho_dict[i])
        cho_calc.set_next_price(price, ratio)

    cho_sum = 0
    for i in range(10):
        print(cho_dict[i])
        cho_sum += cho_dict[i].next_price

    print(cho_sum)





