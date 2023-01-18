import math


def find_center(size):
    return round(size / 2, 2)


def get_area(ar_width, ar_height):
    # print(round(area_long_size * ar_hight, 2))
    return round(ar_width * ar_height, 2)


def get_remainder(area_size, tile_size):
    # Получить Остаток (ширина остатка(в см) от целой плитки, если класть от стены в крой)
    # print(round((area_size % tile_size), 2))
    return round((area_size % tile_size), 2)


def get_integral_part(area_size, tile_size):
    # Возвращает Расчетное количество целых частей
    # print(area_size // tile_size)
    return int(area_size // tile_size)


def get_tile_numb_for_area(ar_width, ar_height, tile_width, tile_height):
    # Возвращает количество целых плиток на плоскости, штук
    width_numb = math.ceil(ar_width / tile_width)
    height_numb = math.ceil(ar_height / tile_height)
    return width_numb * height_numb


def get_seam_numb(area_long_size, tile_long_size):
    # Возвращает количество швов на ширине с установкой их толщины, juncture_width
    number_tile = get_integral_part(area_long_size, tile_long_size)
    remainder = get_remainder(area_long_size, tile_long_size)
    if remainder <= 0.2:
        remainder = 0
    return math.ceil(number_tile + remainder) + 1


def distance_first_solid_tile(ar_height, tile_height, seam_thickness=1.5):
    # Для стен. Если начинаем целой плиткой от потолка. Размеры в (см), толщина шва в (мм)
    # Возвращает расстояние от пола до второго ряда, для начала кладки с целой плитки, в (см)
    integral_part = get_integral_part(ar_height, tile_height)
    all_seam_size = integral_part * (seam_thickness / 10)
    return round(ar_height - (integral_part * tile_height + all_seam_size),2)


def get_start(ar_width, tile_width):
    number_tile = get_integral_part(ar_width, tile_width) % 2
    remainder = get_remainder(ar_width, tile_width)
    if remainder <= 0.2:
        remainder = 0
    print(number_tile, remainder)
    if (number_tile == 0 and remainder == 0) or (number_tile == 1 and remainder):
        # "От центра в стороны"
        print("from_center_to_side")
        return "from_center_to_side"
    elif (number_tile == 1 and remainder == 0) or (number_tile == 0 and remainder):
        print("centers_match")
        return "centers_match"
    else:
        print("something wrong")
        return "something wrong"
