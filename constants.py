from animation import Animation
from mathematics.vector import Vector2Int
from sprite import Sprite

TITLE = 'ROOT-EXECUTION'
SCREEN_SHAPE = Vector2Int(1080, 720)

MAX_PLAYER_SPEED = 900
MAX_ENEMY_SPEED = 450
ACCELERATION = 1800

DRAG_RATION = 5

PLAYER_WALK_ANIMATION = Animation.load('player_walk', 6, 1.5, 1.5)
ENEMY_WALK_ANIMATION = Animation.load('enemy_walk', 6, 1.5, 1.5)

PLAYER_IDE_SPRITE = Sprite.load_raw_image('player_ide.png', 1.5)
ENEMY_IDE_SPRITE = Sprite.load_raw_image('enemy_ide.png', 1.5)

WALK = 'walk'
IDE = 'ide'
RUN = 'run'
