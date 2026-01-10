import arcade.math
from mathematics.vector import Vector2Int

TITLE = 'ROOT-EXECUTION'
SCREEN_SHAPE = Vector2Int(1080, 720)

MAX_SPEED = 900
ACCELERATION = 1800

DRAG_RATION = 5

ide = arcade.Sprite('sprites/walk/ide.png')
walk1 = arcade.Sprite('sprites/walk/walk1.png')
walk2 = arcade.Sprite('sprites/walk/walk2.png')
walk3 = arcade.Sprite('sprites/walk/walk3.png')
walk4 = arcade.Sprite('sprites/walk/walk4.png')
walk5 = arcade.Sprite('sprites/walk/walk5.png')

PLAYER_WALK_SPRITES = arcade.SpriteList()

PLAYER_WALK_SPRITES.append(ide)
PLAYER_WALK_SPRITES.append(walk1)
PLAYER_WALK_SPRITES.append(walk2)
PLAYER_WALK_SPRITES.append(walk3)
PLAYER_WALK_SPRITES.append(walk4)
PLAYER_WALK_SPRITES.append(walk5)
