import datetime

def build_timestamp(hour=0, minute=0, second=0, millis=0):
    return datetime.time(hour, minute, second, millis * 1000)

SEGMENTS = {
    "ll_01": {
        "stand_start": build_timestamp(hour=11, minute=35, second=21, millis=50),
        "stand_end": build_timestamp(hour=11, minute=35, second=22, millis=307),
        "turn1_start": build_timestamp(hour=11, minute=35, second=26, millis=22),
        "turn1_end": build_timestamp(hour=11, minute=35, second=27, millis=910),
        "turn2_start": build_timestamp(hour=11, minute=35, second=31, millis=6),
        "turn2_end": build_timestamp(hour=11, minute=35, second=32, millis=781),
        "sit_start": build_timestamp(hour=11, minute=35, second=32, millis=781),
        "sit_end": build_timestamp(hour=11, minute=35, second=34, millis=277)
    },
    "ll_02": {
        "stand_start": build_timestamp(hour=11, minute=35, second=43, millis=500),
        "stand_end": build_timestamp(hour=11, minute=35, second=44, millis=567),
        "turn1_start": build_timestamp(hour=11, minute=35, second=48, millis=739),
        "turn1_end": build_timestamp(hour=11, minute=35, second=50, millis=446),
        "turn2_start": build_timestamp(hour=11, minute=35, second=53, millis=437),
        "turn2_end": build_timestamp(hour=11, minute=35, second=55, millis=29),
        "sit_start": build_timestamp(hour=11, minute=35, second=55, millis=29),
        "sit_end": build_timestamp(hour=11, minute=35, second=56, millis=305)
    },
    "ll_03": {
        "stand_start": build_timestamp(hour=11, minute=36, second=6, millis=868),
        "stand_end": build_timestamp(hour=11, minute=36, second=8, millis=375),
        "turn1_start": build_timestamp(hour=11, minute=36, second=12, millis=682),
        "turn1_end": build_timestamp(hour=11, minute=36, second=14, millis=218),
        "turn2_start": build_timestamp(hour=11, minute=36, second=17, millis=526),
        "turn2_end": build_timestamp(hour=11, minute=36, second=19, millis=961),
        "sit_start": build_timestamp(hour=11, minute=36, second=19, millis=961),
        "sit_end": build_timestamp(hour=11, minute=36, second=21, millis=993)
    },
    "ll_04": {
        "stand_start": build_timestamp(hour=11, minute=36, second=40, millis=28),
        "stand_end": build_timestamp(hour=11, minute=36, second=41, millis=595),
        "turn1_start": build_timestamp(hour=11, minute=36, second=45, millis=937),
        "turn1_end": build_timestamp(hour=11, minute=36, second=47, millis=656),
        "turn2_start": build_timestamp(hour=11, minute=36, second=51, millis=154),
        "turn2_end": build_timestamp(hour=11, minute=36, second=53, millis=294),
        "sit_start": build_timestamp(hour=11, minute=36, second=53, millis=294),
        "sit_end": build_timestamp(hour=11, minute=36, second=54, millis=928)
    },
    "ll_05": {
        "stand_start": build_timestamp(hour=11, minute=37, second=5, millis=448),
        "stand_end": build_timestamp(hour=11, minute=37, second=7, millis=50),
        "turn1_start": build_timestamp(hour=11, minute=37, second=11, millis=448),
        "turn1_end": build_timestamp(hour=11, minute=37, second=12, millis=931),
        "turn2_start": build_timestamp(hour=11, minute=37, second=16, millis=747),
        "turn2_end": build_timestamp(hour=11, minute=37, second=18, millis=751),
        "sit_start": build_timestamp(hour=11, minute=37, second=18, millis=751),
        "sit_end": build_timestamp(hour=11, minute=37, second=20, millis=883)
    },
    "ll_06": {
        "stand_start": build_timestamp(hour=11, minute=37, second=48, millis=272),
        "stand_end": build_timestamp(hour=11, minute=37, second=49, millis=739),
        "turn1_start": build_timestamp(hour=11, minute=37, second=54, millis=355),
        "turn1_end": build_timestamp(hour=11, minute=37, second=56, millis=317),
        "turn2_start": build_timestamp(hour=11, minute=37, second=59, millis=456),
        "turn2_end": build_timestamp(hour=11, minute=38, second=1, millis=524),
        "sit_start": build_timestamp(hour=11, minute=38, second=1, millis=524),
        "sit_end": build_timestamp(hour=11, minute=38, second=3, millis=137)
    },
    "ll_07": {
        "stand_start": build_timestamp(hour=11, minute=38, second=19, millis=511),
        "stand_end": build_timestamp(hour=11, minute=38, second=21, millis=440),
        "turn1_start": build_timestamp(hour=11, minute=38, second=25, millis=648),
        "turn1_end": build_timestamp(hour=11, minute=38, second=27, millis=720),
        "turn2_start": build_timestamp(hour=11, minute=38, second=30, millis=968),
        "turn2_end": build_timestamp(hour=11, minute=38, second=33, millis=185),
        "sit_start": build_timestamp(hour=11, minute=38, second=33, millis=185),
        "sit_end": build_timestamp(hour=11, minute=38, second=34, millis=853)
    },
    "ll_08": {
        "stand_start": build_timestamp(hour=11, minute=39, second=27, millis=338),
        "stand_end": build_timestamp(hour=11, minute=39, second=28, millis=903),
        "turn1_start": build_timestamp(hour=11, minute=39, second=33, millis=528),
        "turn1_end": build_timestamp(hour=11, minute=39, second=35, millis=772),
        "turn2_start": build_timestamp(hour=11, minute=39, second=38, millis=590),
        "turn2_end": build_timestamp(hour=11, minute=39, second=40, millis=498),
        "sit_start": build_timestamp(hour=11, minute=39, second=40, millis=498),
        "sit_end": build_timestamp(hour=11, minute=39, second=42, millis=732)
    },
    "ll_09": {
        "stand_start": build_timestamp(hour=11, minute=39, second=56, millis=516),
        "stand_end": build_timestamp(hour=11, minute=39, second=58, millis=127),
        "turn1_start": build_timestamp(hour=11, minute=40, second=2, millis=253),
        "turn1_end": build_timestamp(hour=11, minute=40, second=3, millis=938),
        "turn2_start": build_timestamp(hour=11, minute=40, second=7, millis=382),
        "turn2_end": build_timestamp(hour=11, minute=40, second=9, millis=339),
        "sit_start": build_timestamp(hour=11, minute=40, second=9, millis=339),
        "sit_end": build_timestamp(hour=11, minute=40, second=11, millis=481)
    },
    "ll_10": {
        "stand_start": build_timestamp(hour=11, minute=40, second=32, millis=916),
        "stand_end": build_timestamp(hour=11, minute=40, second=34, millis=730),
        "turn1_start": build_timestamp(hour=11, minute=40, second=38, millis=843),
        "turn1_end": build_timestamp(hour=11, minute=40, second=40, millis=732),
        "turn2_start": build_timestamp(hour=11, minute=40, second=44, millis=615),
        "turn2_end": build_timestamp(hour=11, minute=40, second=46, millis=839),
        "sit_start": build_timestamp(hour=11, minute=40, second=46, millis=839),
        "sit_end": build_timestamp(hour=11, minute=40, second=48, millis=765)
    },
    "ll_11": {
        "stand_start": build_timestamp(hour=12, minute=9, second=6, millis=789),
        "stand_end": build_timestamp(hour=12, minute=9, second=8, millis=419),
        "turn1_start": build_timestamp(hour=12, minute=9, second=11, millis=915),
        "turn1_end": build_timestamp(hour=12, minute=9, second=13, millis=640),
        "turn2_start": build_timestamp(hour=12, minute=9, second=17, millis=120),
        "turn2_end": build_timestamp(hour=12, minute=9, second=18, millis=444),
        "sit_start": build_timestamp(hour=12, minute=9, second=18, millis=444),
        "sit_end": build_timestamp(hour=12, minute=9, second=19, millis=966)
    },
    "ll_12": {
        "stand_start": build_timestamp(hour=12, minute=9, second=29, millis=906),
        "stand_end": build_timestamp(hour=12, minute=9, second=31, millis=200),
        "turn1_start": build_timestamp(hour=12, minute=9, second=34, millis=902),
        "turn1_end": build_timestamp(hour=12, minute=9, second=36, millis=719),
        "turn2_start": build_timestamp(hour=12, minute=9, second=40, millis=271),
        "turn2_end": build_timestamp(hour=12, minute=9, second=41, millis=709),
        "sit_start": build_timestamp(hour=12, minute=9, second=41, millis=709),
        "sit_end": build_timestamp(hour=12, minute=9, second=43, millis=253)
    },
    "ll_13": {
        "stand_start": build_timestamp(hour=12, minute=9, second=50, millis=173),
        "stand_end": build_timestamp(hour=12, minute=9, second=51, millis=363),
        "turn1_start": build_timestamp(hour=12, minute=9, second=55, millis=946),
        "turn1_end": build_timestamp(hour=12, minute=9, second=57, millis=611),
        "turn2_start": build_timestamp(hour=12, minute=10, second=1, millis=277),
        "turn2_end": build_timestamp(hour=12, minute=10, second=2, millis=638),
        "sit_start": build_timestamp(hour=12, minute=10, second=2, millis=638),
        "sit_end": build_timestamp(hour=12, minute=10, second=4, millis=162)
    },
    "ll_14": {
        "stand_start": build_timestamp(hour=12, minute=10, second=16, millis=162),
        "stand_end": build_timestamp(hour=12, minute=10, second=17, millis=729),
        "turn1_start": build_timestamp(hour=12, minute=10, second=22, millis=115),
        "turn1_end": build_timestamp(hour=12, minute=10, second=23, millis=918),
        "turn2_start": build_timestamp(hour=12, minute=10, second=27, millis=456),
        "turn2_end": build_timestamp(hour=12, minute=10, second=28, millis=923),
        "sit_start": build_timestamp(hour=12, minute=10, second=28, millis=923),
        "sit_end": build_timestamp(hour=12, minute=10, second=30, millis=467)
    },
    "ll_15": {
        "stand_start": build_timestamp(hour=12, minute=10, second=40, millis=952),
        "stand_end": build_timestamp(hour=12, minute=10, second=42, millis=231),
        "turn1_start": build_timestamp(hour=12, minute=10, second=46, millis=655),
        "turn1_end": build_timestamp(hour=12, minute=10, second=48, millis=459),
        "turn2_start": build_timestamp(hour=12, minute=10, second=52, millis=340),
        "turn2_end": build_timestamp(hour=12, minute=10, second=53, millis=933),
        "sit_start": build_timestamp(hour=12, minute=10, second=53, millis=933),
        "sit_end": build_timestamp(hour=12, minute=10, second=55, millis=621)
    },
    "lr_01": {
        "stand_start": build_timestamp(hour=11, minute=27, second=43, millis=62),
        "stand_end": build_timestamp(hour=11, minute=27, second=44, millis=253),
        "turn1_start": build_timestamp(hour=11, minute=27, second=47, millis=679),
        "turn1_end": build_timestamp(hour=11, minute=27, second=49, millis=462),
        "turn2_start": build_timestamp(hour=11, minute=27, second=52, millis=185),
        "turn2_end": build_timestamp(hour=11, minute=27, second=54, millis=121),
        "sit_start": build_timestamp(hour=11, minute=27, second=54, millis=121),
        "sit_end": build_timestamp(hour=11, minute=27, second=55, millis=757)
    },
     "lr_02": {
        "stand_start": build_timestamp(hour=11, minute=28, second=24, millis=115),
        "stand_end": build_timestamp(hour=11, minute=28, second=25, millis=342),
        "turn1_start": build_timestamp(hour=11, minute=28, second=28, millis=727),
        "turn1_end": build_timestamp(hour=11, minute=28, second=30, millis=464),
        "turn2_start": build_timestamp(hour=11, minute=28, second=33, millis=309),
        "turn2_end": build_timestamp(hour=11, minute=28, second=35, millis=404),
        "sit_start": build_timestamp(hour=11, minute=28, second=35, millis=404),
        "sit_end": build_timestamp(hour=11, minute=28, second=36, millis=871)
    },
    "lr_03": {
        "stand_start": build_timestamp(hour=11, minute=29, second=6, millis=570),
        "stand_end": build_timestamp(hour=11, minute=29, second=7, millis=993),
        "turn1_start": build_timestamp(hour=11, minute=29, second=11, millis=263),
        "turn1_end": build_timestamp(hour=11, minute=29, second=12, millis=999),
        "turn2_start": build_timestamp(hour=11, minute=29, second=15, millis=876),
        "turn2_end": build_timestamp(hour=11, minute=29, second=18, millis=69),
        "sit_start": build_timestamp(hour=11, minute=29, second=18, millis=69),
        "sit_end": build_timestamp(hour=11, minute=29, second=19, millis=380)
    },
    "lr_04": {
        "stand_start": build_timestamp(hour=11, minute=29, second=51, millis=164),
        "stand_end": build_timestamp(hour=11, minute=29, second=53, millis=46),
        "turn1_start": build_timestamp(hour=11, minute=29, second=56, millis=382),
        "turn1_end": build_timestamp(hour=11, minute=29, second=58, millis=167),
        "turn2_start": build_timestamp(hour=11, minute=30, second=0, millis=933),
        "turn2_end": build_timestamp(hour=11, minute=30, second=3, millis=374),
        "sit_start": build_timestamp(hour=11, minute=30, second=3, millis=374),
        "sit_end": build_timestamp(hour=11, minute=30, second=4, millis=774)
    },
    "lr_05": {
        "stand_start": build_timestamp(hour=11, minute=31, second=3, millis=611),
        "stand_end": build_timestamp(hour=11, minute=31, second=5, millis=474),
        "turn1_start": build_timestamp(hour=11, minute=31, second=9, millis=81),
        "turn1_end": build_timestamp(hour=11, minute=31, second=10, millis=758),
        "turn2_start": build_timestamp(hour=11, minute=31, second=14, millis=114),
        "turn2_end": build_timestamp(hour=11, minute=31, second=16, millis=594),
        "sit_start": build_timestamp(hour=11, minute=31, second=16, millis=594),
        "sit_end": build_timestamp(hour=11, minute=31, second=18, millis=217)
    },
    "lr_06": {
        "stand_start": build_timestamp(hour=11, minute=31, second=51, millis=851),
        "stand_end": build_timestamp(hour=11, minute=31, second=53, millis=684),
        "turn1_start": build_timestamp(hour=11, minute=31, second=57, millis=725),
        "turn1_end": build_timestamp(hour=11, minute=31, second=59, millis=805),
        "turn2_start": build_timestamp(hour=11, minute=32, second=3, millis=908),
        "turn2_end": build_timestamp(hour=11, minute=32, second=5, millis=989),
        "sit_start": build_timestamp(hour=11, minute=32, second=5, millis=989),
        "sit_end": build_timestamp(hour=11, minute=32, second=7, millis=591)
    },
    "lr_07": {
        "stand_start": build_timestamp(hour=11, minute=32, second=19, millis=668),
        "stand_end": build_timestamp(hour=11, minute=32, second=21, millis=495),
        "turn1_start": build_timestamp(hour=11, minute=32, second=24, millis=985),
        "turn1_end": build_timestamp(hour=11, minute=32, second=27, millis=343),
        "turn2_start": build_timestamp(hour=11, minute=32, second=31, millis=375),
        "turn2_end": build_timestamp(hour=11, minute=32, second=33, millis=469),
        "sit_start": build_timestamp(hour=11, minute=32, second=33, millis=469),
        "sit_end": build_timestamp(hour=11, minute=32, second=35, millis=8)
    },
    "lr_08": {
        "stand_start": build_timestamp(hour=11, minute=32, second=51, millis=135),
        "stand_end": build_timestamp(hour=11, minute=32, second=53, millis=37),
        "turn1_start": build_timestamp(hour=11, minute=32, second=57, millis=318),
        "turn1_end": build_timestamp(hour=11, minute=32, second=58, millis=882),
        "turn2_start": build_timestamp(hour=11, minute=33, second=2, millis=203),
        "turn2_end": build_timestamp(hour=11, minute=33, second=4, millis=667),
        "sit_start": build_timestamp(hour=11, minute=33, second=4, millis=667),
        "sit_end": build_timestamp(hour=11, minute=33, second=6, millis=330)
    },
    "lr_09": {
        "stand_start": build_timestamp(hour=11, minute=33, second=31, millis=679),
        "stand_end": build_timestamp(hour=11, minute=33, second=33, millis=233),
        "turn1_start": build_timestamp(hour=11, minute=33, second=37, millis=710),
        "turn1_end": build_timestamp(hour=11, minute=33, second=39, millis=496),
        "turn2_start": build_timestamp(hour=11, minute=33, second=43, millis=462),
        "turn2_end": build_timestamp(hour=11, minute=33, second=45, millis=379),
        "sit_start": build_timestamp(hour=11, minute=33, second=45, millis=379),
        "sit_end": build_timestamp(hour=11, minute=33, second=47, millis=365)
    },
    "lr_10": {
        "stand_start": build_timestamp(hour=11, minute=34, second=49, millis=598),
        "stand_end": build_timestamp(hour=11, minute=34, second=51, millis=436),
        "turn1_start": build_timestamp(hour=11, minute=34, second=55, millis=634),
        "turn1_end": build_timestamp(hour=11, minute=34, second=57, millis=427),
        "turn2_start": build_timestamp(hour=11, minute=35, second=0, millis=878),
        "turn2_end": build_timestamp(hour=11, minute=35, second=2, millis=995),
        "sit_start": build_timestamp(hour=11, minute=35, second=2, millis=995),
        "sit_end": build_timestamp(hour=11, minute=35, second=4, millis=598)
    },
    "lr_11": {
        "stand_start": build_timestamp(hour=12, minute=5, second=2, millis=590),
        "stand_end": build_timestamp(hour=12, minute=5, second=3, millis=946),
        "turn1_start": build_timestamp(hour=12, minute=5, second=7, millis=666),
        "turn1_end": build_timestamp(hour=12, minute=5, second=9, millis=541),
        "turn2_start": build_timestamp(hour=12, minute=5, second=13, millis=74),
        "turn2_end": build_timestamp(hour=12, minute=5, second=15, millis=386),
        "sit_start": build_timestamp(hour=12, minute=5, second=15, millis=386),
        "sit_end": build_timestamp(hour=12, minute=5, second=16, millis=516)
    },
    "lr_12": {
        "stand_start": build_timestamp(hour=12, minute=5, second=27, millis=757),
        "stand_end": build_timestamp(hour=12, minute=5, second=28, millis=950),
        "turn1_start": build_timestamp(hour=12, minute=5, second=33, millis=5),
        "turn1_end": build_timestamp(hour=12, minute=5, second=34, millis=827),
        "turn2_start": build_timestamp(hour=12, minute=5, second=38, millis=519),
        "turn2_end": build_timestamp(hour=12, minute=5, second=40, millis=689),
        "sit_start": build_timestamp(hour=12, minute=5, second=40, millis=689),
        "sit_end": build_timestamp(hour=12, minute=5, second=42, millis=431)
    },
    "lr_13": {
        "stand_start": build_timestamp(hour=12, minute=5, second=52, millis=885),
        "stand_end": build_timestamp(hour=12, minute=5, second=54, millis=616),
        "turn1_start": build_timestamp(hour=12, minute=5, second=58, millis=541),
        "turn1_end": build_timestamp(hour=12, minute=6, second=0, millis=220),
        "turn2_start": build_timestamp(hour=12, minute=6, second=4, millis=93),
        "turn2_end": build_timestamp(hour=12, minute=6, second=6, millis=356),
        "sit_start": build_timestamp(hour=12, minute=6, second=6, millis=356),
        "sit_end": build_timestamp(hour=12, minute=6, second=7, millis=686)
    },
    "lr_14": {
        "stand_start": build_timestamp(hour=12, minute=6, second=17, millis=951),
        "stand_end": build_timestamp(hour=12, minute=6, second=19, millis=381),
        "turn1_start": build_timestamp(hour=12, minute=6, second=23, millis=455),
        "turn1_end": build_timestamp(hour=12, minute=6, second=25, millis=259),
        "turn2_start": build_timestamp(hour=12, minute=6, second=28, millis=883),
        "turn2_end": build_timestamp(hour=12, minute=6, second=30, millis=647),
        "sit_start": build_timestamp(hour=12, minute=6, second=30, millis=647),
        "sit_end": build_timestamp(hour=12, minute=6, second=32, millis=459)
    },
    "lr_15": {
        "stand_start": build_timestamp(hour=12, minute=6, second=39, millis=887),
        "stand_end": build_timestamp(hour=12, minute=6, second=41, millis=544),
        "turn1_start": build_timestamp(hour=12, minute=6, second=45, millis=428),
        "turn1_end": build_timestamp(hour=12, minute=6, second=47, millis=201),
        "turn2_start": build_timestamp(hour=12, minute=6, second=50, millis=893),
        "turn2_end": build_timestamp(hour=12, minute=6, second=52, millis=897),
        "sit_start": build_timestamp(hour=12, minute=6, second=52, millis=897),
        "sit_end": build_timestamp(hour=12, minute=6, second=54, millis=612)
    },
    "rl_01": {
        "stand_start": build_timestamp(hour=12, minute=24, second=35, millis=457),
        "stand_end": build_timestamp(hour=12, minute=24, second=36, millis=714),
        "turn1_start": build_timestamp(hour=12, minute=24, second=41, millis=70),
        "turn1_end": build_timestamp(hour=12, minute=24, second=42, millis=676),
        "turn2_start": build_timestamp(hour=12, minute=24, second=46, millis=448),
        "turn2_end": build_timestamp(hour=12, minute=24, second=48, millis=423),
        "sit_start": build_timestamp(hour=12, minute=24, second=48, millis=423),
        "sit_end": build_timestamp(hour=12, minute=24, second=50, millis=55)
    },
    "rl_02": {
        "stand_start": build_timestamp(hour=12, minute=24, second=55, millis=154),
        "stand_end": build_timestamp(hour=12, minute=24, second=56, millis=645),
        "turn1_start": build_timestamp(hour=12, minute=25, second=0, millis=715),
        "turn1_end": build_timestamp(hour=12, minute=25, second=2, millis=306),
        "turn2_start": build_timestamp(hour=12, minute=25, second=6, millis=131),
        "turn2_end": build_timestamp(hour=12, minute=25, second=7, millis=982),
        "sit_start": build_timestamp(hour=12, minute=25, second=7, millis=982),
        "sit_end": build_timestamp(hour=12, minute=25, second=9, millis=753)
    },
    "rl_03": {
        "stand_start": build_timestamp(hour=12, minute=25, second=17, millis=570),
        "stand_end": build_timestamp(hour=12, minute=25, second=19, millis=180),
        "turn1_start": build_timestamp(hour=12, minute=25, second=23, millis=443),
        "turn1_end": build_timestamp(hour=12, minute=25, second=24, millis=995),
        "turn2_start": build_timestamp(hour=12, minute=25, second=29, millis=232),
        "turn2_end": build_timestamp(hour=12, minute=25, second=30, millis=806),
        "sit_start": build_timestamp(hour=12, minute=25, second=30, millis=806),
        "sit_end": build_timestamp(hour=12, minute=25, second=32, millis=178)
    },
    "rl_04": {
        "stand_start": build_timestamp(hour=12, minute=25, second=40, millis=611),
        "stand_end": build_timestamp(hour=12, minute=25, second=42, millis=287),
        "turn1_start": build_timestamp(hour=12, minute=25, second=46, millis=562),
        "turn1_end": build_timestamp(hour=12, minute=25, second=48, millis=157),
        "turn2_start": build_timestamp(hour=12, minute=25, second=52, millis=108),
        "turn2_end": build_timestamp(hour=12, minute=25, second=53, millis=938),
        "sit_start": build_timestamp(hour=12, minute=25, second=53, millis=938),
        "sit_end": build_timestamp(hour=12, minute=25, second=55, millis=472)
    },
    "rl_05": {
        "stand_start": build_timestamp(hour=12, minute=26, second=3, millis=203),
        "stand_end": build_timestamp(hour=12, minute=26, second=4, millis=860),
        "turn1_start": build_timestamp(hour=12, minute=26, second=9, millis=36),
        "turn1_end": build_timestamp(hour=12, minute=26, second=10, millis=609),
        "turn2_start": build_timestamp(hour=12, minute=26, second=14, millis=462),
        "turn2_end": build_timestamp(hour=12, minute=26, second=16, millis=189),
        "sit_start": build_timestamp(hour=12, minute=26, second=16, millis=189),
        "sit_end": build_timestamp(hour=12, minute=26, second=17, millis=896)
    },
    "rl_06": {
        "stand_start": build_timestamp(hour=12, minute=26, second=23, millis=731),
        "stand_end": build_timestamp(hour=12, minute=26, second=25, millis=512),
        "turn1_start": build_timestamp(hour=12, minute=26, second=29, millis=717),
        "turn1_end": build_timestamp(hour=12, minute=26, second=31, millis=217),
        "turn2_start": build_timestamp(hour=12, minute=26, second=34, millis=999),
        "turn2_end": build_timestamp(hour=12, minute=26, second=36, millis=614),
        "sit_start": build_timestamp(hour=12, minute=26, second=36, millis=614),
        "sit_end": build_timestamp(hour=12, minute=26, second=38, millis=327)
    },
    "rl_07": {
        "stand_start": build_timestamp(hour=12, minute=26, second=44, millis=575),
        "stand_end": build_timestamp(hour=12, minute=26, second=46, millis=225),
        "turn1_start": build_timestamp(hour=12, minute=26, second=50, millis=441),
        "turn1_end": build_timestamp(hour=12, minute=26, second=51, millis=757),
        "turn2_start": build_timestamp(hour=12, minute=26, second=55, millis=686),
        "turn2_end": build_timestamp(hour=12, minute=26, second=57, millis=222),
        "sit_start": build_timestamp(hour=12, minute=26, second=57, millis=222),
        "sit_end": build_timestamp(hour=12, minute=26, second=58, millis=850)
    },
    "rl_08": {
        "stand_start": build_timestamp(hour=12, minute=27, second=5, millis=657),
        "stand_end": build_timestamp(hour=12, minute=27, second=7, millis=339),
        "turn1_start": build_timestamp(hour=12, minute=27, second=11, millis=535),
        "turn1_end": build_timestamp(hour=12, minute=27, second=12, millis=997),
        "turn2_start": build_timestamp(hour=12, minute=27, second=16, millis=969),
        "turn2_end": build_timestamp(hour=12, minute=27, second=18, millis=443),
        "sit_start": build_timestamp(hour=12, minute=27, second=18, millis=443),
        "sit_end": build_timestamp(hour=12, minute=27, second=20, millis=183)
    },
    "rl_09": {
        "stand_start": build_timestamp(hour=12, minute=27, second=30, millis=434),
        "stand_end": build_timestamp(hour=12, minute=27, second=32, millis=32),
        "turn1_start": build_timestamp(hour=12, minute=27, second=36, millis=206),
        "turn1_end": build_timestamp(hour=12, minute=27, second=37, millis=673),
        "turn2_start": build_timestamp(hour=12, minute=27, second=41, millis=737),
        "turn2_end": build_timestamp(hour=12, minute=27, second=43, millis=275),
        "sit_start": build_timestamp(hour=12, minute=27, second=43, millis=275),
        "sit_end": build_timestamp(hour=12, minute=27, second=44, millis=656)
    },
    "rl_10": {
        "stand_start": build_timestamp(hour=12, minute=27, second=52, millis=666),
        "stand_end": build_timestamp(hour=12, minute=27, second=54, millis=249),
        "turn1_start": build_timestamp(hour=12, minute=27, second=58, millis=458),
        "turn1_end": build_timestamp(hour=12, minute=28, second=59, millis=877),
        "turn2_start": build_timestamp(hour=12, minute=28, second=3, millis=904),
        "turn2_end": build_timestamp(hour=12, minute=28, second=5, millis=717),
        "sit_start": build_timestamp(hour=12, minute=28, second=5, millis=717),
        "sit_end": build_timestamp(hour=12, minute=28, second=7, millis=499)
    },
    "rl_11": {
        "stand_start": build_timestamp(hour=12, minute=28, second=17, millis=207),
        "stand_end": build_timestamp(hour=12, minute=28, second=18, millis=841),
        "turn1_start": build_timestamp(hour=12, minute=28, second=23, millis=142),
        "turn1_end": build_timestamp(hour=12, minute=28, second=24, millis=503),
        "turn2_start": build_timestamp(hour=12, minute=28, second=28, millis=425),
        "turn2_end": build_timestamp(hour=12, minute=28, second=29, millis=908),
        "sit_start": build_timestamp(hour=12, minute=28, second=29, millis=908),
        "sit_end": build_timestamp(hour=12, minute=28, second=31, millis=704)
    },
    "rl_12": {
        "stand_start": build_timestamp(hour=12, minute=28, second=44, millis=213),
        "stand_end": build_timestamp(hour=12, minute=28, second=45, millis=905),
        "turn1_start": build_timestamp(hour=12, minute=28, second=50, millis=172),
        "turn1_end": build_timestamp(hour=12, minute=28, second=51, millis=610),
        "turn2_start": build_timestamp(hour=12, minute=28, second=55, millis=503),
        "turn2_end": build_timestamp(hour=12, minute=28, second=57, millis=197),
        "sit_start": build_timestamp(hour=12, minute=28, second=57, millis=197),
        "sit_end": build_timestamp(hour=12, minute=28, second=58, millis=607)
    },
    "rl_13": {
        "stand_start": build_timestamp(hour=12, minute=29, second=7, millis=62),
        "stand_end": build_timestamp(hour=12, minute=29, second=8, millis=955),
        "turn1_start": build_timestamp(hour=12, minute=29, second=12, millis=954),
        "turn1_end": build_timestamp(hour=12, minute=29, second=14, millis=435),
        "turn2_start": build_timestamp(hour=12, minute=29, second=18, millis=486),
        "turn2_end": build_timestamp(hour=12, minute=29, second=20, millis=241),
        "sit_start": build_timestamp(hour=12, minute=29, second=20, millis=241),
        "sit_end": build_timestamp(hour=12, minute=29, second=21, millis=933)
    },
    "rl_14": {
        "stand_start": build_timestamp(hour=12, minute=29, second=55, millis=175),
        "stand_end": build_timestamp(hour=12, minute=29, second=56, millis=930),
        "turn1_start": build_timestamp(hour=12, minute=30, second=1, millis=45),
        "turn1_end": build_timestamp(hour=12, minute=30, second=2, millis=571),
        "turn2_start": build_timestamp(hour=12, minute=30, second=6, millis=542),
        "turn2_end": build_timestamp(hour=12, minute=30, second=8, millis=134),
        "sit_start": build_timestamp(hour=12, minute=30, second=8, millis=134),
        "sit_end": build_timestamp(hour=12, minute=30, second=9, millis=705)
    },
    "rl_15": {
        "stand_start": build_timestamp(hour=12, minute=30, second=16, millis=999),
        "stand_end": build_timestamp(hour=12, minute=30, second=18, millis=479),
        "turn1_start": build_timestamp(hour=12, minute=30, second=22, millis=953),
        "turn1_end": build_timestamp(hour=12, minute=30, second=24, millis=605),
        "turn2_start": build_timestamp(hour=12, minute=30, second=28, millis=696),
        "turn2_end": build_timestamp(hour=12, minute=30, second=30, millis=163),
        "sit_start": build_timestamp(hour=12, minute=30, second=30, millis=163),
        "sit_end": build_timestamp(hour=12, minute=30, second=31, millis=755)
    },
    "rr_01": {
        "stand_start": build_timestamp(hour=12, minute=14, second=11, millis=242),
        "stand_end": build_timestamp(hour=12, minute=14, second=13, millis=82),
        "turn1_start": build_timestamp(hour=12, minute=14, second=17, millis=28),
        "turn1_end": build_timestamp(hour=12, minute=14, second=18, millis=989),
        "turn2_start": build_timestamp(hour=12, minute=14, second=22, millis=594),
        "turn2_end": build_timestamp(hour=12, minute=14, second=24, millis=223),
        "sit_start": build_timestamp(hour=12, minute=14, second=24, millis=223),
        "sit_end": build_timestamp(hour=12, minute=14, second=26, millis=7)
    },
    "rr_02": {
        "stand_start": build_timestamp(hour=12, minute=14, second=34, millis=240),
        "stand_end": build_timestamp(hour=12, minute=14, second=35, millis=826),
        "turn1_start": build_timestamp(hour=12, minute=14, second=39, millis=772),
        "turn1_end": build_timestamp(hour=12, minute=14, second=41, millis=556),
        "turn2_start": build_timestamp(hour=12, minute=14, second=45, millis=352),
        "turn2_end": build_timestamp(hour=12, minute=14, second=47, millis=184),
        "sit_start": build_timestamp(hour=12, minute=14, second=47, millis=184),
        "sit_end": build_timestamp(hour=12, minute=14, second=48, millis=765)
    },
    "rr_03": {
        "stand_start": build_timestamp(hour=12, minute=14, second=56, millis=208),
        "stand_end": build_timestamp(hour=12, minute=14, second=57, millis=909),
        "turn1_start": build_timestamp(hour=12, minute=15, second=2, millis=396),
        "turn1_end": build_timestamp(hour=12, minute=15, second=4, millis=228),
        "turn2_start": build_timestamp(hour=12, minute=15, second=8, millis=417),
        "turn2_end": build_timestamp(hour=12, minute=15, second=10, millis=118),
        "sit_start": build_timestamp(hour=12, minute=15, second=10, millis=118),
        "sit_end": build_timestamp(hour=12, minute=15, second=11, millis=665)
    },
    "rr_04": {
        "stand_start": build_timestamp(hour=12, minute=15, second=18, millis=914),
        "stand_end": build_timestamp(hour=12, minute=15, second=20, millis=553),
        "turn1_start": build_timestamp(hour=12, minute=15, second=24, millis=983),
        "turn1_end": build_timestamp(hour=12, minute=15, second=26, millis=833),
        "turn2_start": build_timestamp(hour=12, minute=15, second=30, millis=668),
        "turn2_end": build_timestamp(hour=12, minute=15, second=32, millis=183),
        "sit_start": build_timestamp(hour=12, minute=15, second=32, millis=183),
        "sit_end": build_timestamp(hour=12, minute=15, second=33, millis=890)
    },
    "rr_05": {
        "stand_start": build_timestamp(hour=12, minute=15, second=41, millis=163),
        "stand_end": build_timestamp(hour=12, minute=15, second=43, millis=9),
        "turn1_start": build_timestamp(hour=12, minute=15, second=47, millis=329),
        "turn1_end": build_timestamp(hour=12, minute=15, second=49, millis=98),
        "turn2_start": build_timestamp(hour=12, minute=15, second=53, millis=62),
        "turn2_end": build_timestamp(hour=12, minute=15, second=54, millis=702),
        "sit_start": build_timestamp(hour=12, minute=15, second=54, millis=702),
        "sit_end": build_timestamp(hour=12, minute=15, second=56, millis=356)
    },
    "rr_06": {
        "stand_start": build_timestamp(hour=12, minute=16, second=3, millis=794),
        "stand_end": build_timestamp(hour=12, minute=16, second=5, millis=314),
        "turn1_start": build_timestamp(hour=12, minute=16, second=9, millis=657),
        "turn1_end": build_timestamp(hour=12, minute=16, second=11, millis=369),
        "turn2_start": build_timestamp(hour=12, minute=16, second=15, millis=218),
        "turn2_end": build_timestamp(hour=12, minute=16, second=16, millis=779),
        "sit_start": build_timestamp(hour=12, minute=16, second=16, millis=779),
        "sit_end": build_timestamp(hour=12, minute=16, second=18, millis=232)
    },
    "rr_07": {
        "stand_start": build_timestamp(hour=12, minute=16, second=27, millis=343),
        "stand_end": build_timestamp(hour=12, minute=16, second=28, millis=695),
        "turn1_start": build_timestamp(hour=12, minute=16, second=32, millis=894),
        "turn1_end": build_timestamp(hour=12, minute=16, second=34, millis=693),
        "turn2_start": build_timestamp(hour=12, minute=16, second=38, millis=869),
        "turn2_end": build_timestamp(hour=12, minute=16, second=40, millis=492),
        "sit_start": build_timestamp(hour=12, minute=16, second=40, millis=492),
        "sit_end": build_timestamp(hour=12, minute=16, second=42, millis=146)
    },
    "rr_08": {
        "stand_start": build_timestamp(hour=12, minute=16, second=51, millis=482),
        "stand_end": build_timestamp(hour=12, minute=16, second=52, millis=813),
        "turn1_start": build_timestamp(hour=12, minute=16, second=57, millis=67),
        "turn1_end": build_timestamp(hour=12, minute=16, second=58, millis=888),
        "turn2_start": build_timestamp(hour=12, minute=17, second=2, millis=812),
        "turn2_end": build_timestamp(hour=12, minute=17, second=4, millis=301),
        "sit_start": build_timestamp(hour=12, minute=17, second=4, millis=301),
        "sit_end": build_timestamp(hour=12, minute=17, second=5, millis=950)
    },
    "rr_09": {
        "stand_start": build_timestamp(hour=12, minute=17, second=47, millis=43),
        "stand_end": build_timestamp(hour=12, minute=17, second=48, millis=888),
        "turn1_start": build_timestamp(hour=12, minute=17, second=53, millis=189),
        "turn1_end": build_timestamp(hour=12, minute=17, second=54, millis=915),
        "turn2_start": build_timestamp(hour=12, minute=17, second=58, millis=884),
        "turn2_end": build_timestamp(hour=12, minute=18, second=0, millis=426),
        "sit_start": build_timestamp(hour=12, minute=18, second=0, millis=426),
        "sit_end": build_timestamp(hour=12, minute=18, second=2, millis=144)
    },
    "rr_10": {
        "stand_start": build_timestamp(hour=12, minute=18, second=10, millis=543),
        "stand_end": build_timestamp(hour=12, minute=18, second=12, millis=188),
        "turn1_start": build_timestamp(hour=12, minute=18, second=16, millis=493),
        "turn1_end": build_timestamp(hour=12, minute=18, second=18, millis=278),
        "turn2_start": build_timestamp(hour=12, minute=18, second=22, millis=419),
        "turn2_end": build_timestamp(hour=12, minute=18, second=24, millis=87),
        "sit_start": build_timestamp(hour=12, minute=18, second=24, millis=87),
        "sit_end": build_timestamp(hour=12, minute=18, second=25, millis=937)
    },
    "rr_11": {
        "stand_start": build_timestamp(hour=12, minute=18, second=35, millis=928),
        "stand_end": build_timestamp(hour=12, minute=18, second=37, millis=490),
        "turn1_start": build_timestamp(hour=12, minute=18, second=41, millis=817),
        "turn1_end": build_timestamp(hour=12, minute=18, second=43, millis=563),
        "turn2_start": build_timestamp(hour=12, minute=18, second=47, millis=350),
        "turn2_end": build_timestamp(hour=12, minute=18, second=48, millis=910),
        "sit_start": build_timestamp(hour=12, minute=18, second=48, millis=910),
        "sit_end": build_timestamp(hour=12, minute=18, second=50, millis=893)
    },
    "rr_12": {
        "stand_start": build_timestamp(hour=12, minute=18, second=58, millis=302),
        "stand_end": build_timestamp(hour=12, minute=18, second=59, millis=854),
        "turn1_start": build_timestamp(hour=12, minute=19, second=3, millis=941),
        "turn1_end": build_timestamp(hour=12, minute=19, second=5, millis=598),
        "turn2_start": build_timestamp(hour=12, minute=19, second=9, millis=381),
        "turn2_end": build_timestamp(hour=12, minute=19, second=11, millis=213),
        "sit_start": build_timestamp(hour=12, minute=19, second=11, millis=213),
        "sit_end": build_timestamp(hour=12, minute=19, second=12, millis=833)
    },
    "rr_13": {
        "stand_start": build_timestamp(hour=12, minute=19, second=21, millis=269),
        "stand_end": build_timestamp(hour=12, minute=19, second=23, millis=98),
        "turn1_start": build_timestamp(hour=12, minute=19, second=27, millis=268),
        "turn1_end": build_timestamp(hour=12, minute=19, second=28, millis=884),
        "turn2_start": build_timestamp(hour=12, minute=19, second=32, millis=428),
        "turn2_end": build_timestamp(hour=12, minute=19, second=34, millis=699),
        "sit_start": build_timestamp(hour=12, minute=19, second=34, millis=699),
        "sit_end": build_timestamp(hour=12, minute=19, second=36, millis=70)
    },
    "rr_14": {
        "stand_start": build_timestamp(hour=12, minute=19, second=43, millis=700),
        "stand_end": build_timestamp(hour=12, minute=19, second=45, millis=497),
        "turn1_start": build_timestamp(hour=12, minute=19, second=49, millis=859),
        "turn1_end": build_timestamp(hour=12, minute=19, second=51, millis=594),
        "turn2_start": build_timestamp(hour=12, minute=19, second=55, millis=714),
        "turn2_end": build_timestamp(hour=12, minute=19, second=57, millis=419),
        "sit_start": build_timestamp(hour=12, minute=19, second=57, millis=419),
        "sit_end": build_timestamp(hour=12, minute=19, second=59, millis=299)
    },
    "rr_15": {
        "stand_start": build_timestamp(hour=12, minute=20, second=6, millis=489),
        "stand_end": build_timestamp(hour=12, minute=20, second=8, millis=485),
        "turn1_start": build_timestamp(hour=12, minute=20, second=12, millis=901),
        "turn1_end": build_timestamp(hour=12, minute=20, second=14, millis=551),
        "turn2_start": build_timestamp(hour=12, minute=20, second=18, millis=482),
        "turn2_end": build_timestamp(hour=12, minute=20, second=19, millis=943),
        "sit_start": build_timestamp(hour=12, minute=20, second=19, millis=943),
        "sit_end": build_timestamp(hour=12, minute=20, second=21, millis=501)
    }
}