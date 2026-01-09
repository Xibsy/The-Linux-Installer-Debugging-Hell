import arcade.math
from mathematics.vector import Vector2Int, Vector2

TITLE = 'ROOT-EXECUTION'
SCREEN_SHAPE = Vector2Int(1080, 720)

SHAPE = Vector2(40, 60)

SHOOT_FREQUENCY = 3
SHOOT_DELTA = SHAPE * .5

MAX_SPEED = 300
ACCELERATION = 100

PLAYER_COLOR = arcade.color.GRAPE