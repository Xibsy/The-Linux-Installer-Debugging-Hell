import math


def get_sprite_degrees(x: int, y: int, player_x: float, player_y: float) -> float:
    diff_x = x - player_x
    diff_y = y - player_y
    angle_rad = math.atan2(diff_x, diff_y)
    return math.degrees(angle_rad)