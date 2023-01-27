FRAME_RATE = 24         # 게임 내 1초 프레임
BEST_FRAME_RATE = 77    # dps 강화하기 게임 내 최대 프레임

FIRST_MAX_LEVEL = 25    # 첫번째 사냥터 유닛 최대 레벨
SECOND_MAX_LEVEL = 40   # 두번째 사냥터 유닛 최대 레벨

PLAYER_MAX_LEVEL = 50_000   # 플레이어 최대 레벨

MPS_40 = 285 / 207

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
    40: (-0.09, 0.0, 0.0, 16_685, 25_000_000),
    41: (-0.12, 0.0, 0.0, 25, 90_000_000),
    42: (-0.2, 0.0, 0.0, 35, 225_000_000),
    43: (-0.25, 0.0, 0.0, 117, 1_200_000_000),
    44: (0.0, 0.0, 0.0, 768, 6_000_000_000),
}

UNIT_MAX_LEVEL = len(unit_information)     # 유닛 최대 레벨

#################################################################################

FIRST_MAX = 10.0            # +1 강화 확률 최댓값
SECOND_MAX = 5.0            # +1 강화 확률 최댓값
THIRD_MAX = 3.0             # +1 강화 확률 최댓값
USER_DAMAGE_MAX = 50        # 최대 공업
SPECIAL_UPGRADE_MAX = 10.0  # 특수 강화 확률 최댓값
ZERO_MAX = 50.0             # 파괴 방지 확률 최댓값
ANOTHER_FIRST_MAX = 5.0     # 추가 +1 강화 확률 최댓값