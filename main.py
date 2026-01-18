import math
from math import cos

import arcade

import constants as const
from enemy_draw import EnemyListDraw
from player import Player
from draw import Draw
from game_engine import GameEngine
from player_draw import PlayerDraw
from enemy_list import *


def main() -> None:
    player = Player(RigidBody(const.SCREEN_SHAPE.as_vector2 * .5, Vector2.zero(),
                              const.MAX_PLAYER_SPEED, Vector2(48, 38)))
    enemy_list = EnemyList()

    engine = GameEngine(const.TITLE, const.SCREEN_SHAPE, Draw(PlayerDraw(player),
                                                              EnemyListDraw()), player, enemy_list)

    (engine.player_inputer.keyboard_state_changed
     .subscribe(lambda keys: player.set_direction(_keys_to_player_direction(keys, engine.tests))))

    engine.player_inputer.keyboard_state_changed.subscribe(lambda keys:
                                                           enemy_list.spawn(Vector2.zero())
                                                           if arcade.key.L in keys else None)

    engine.run()


#def _on_mouse_click(position: Vector2, player: Player) -> None:
#    direction = (position - player.rigid_body.position).normalize
#    player.gun.try_shoot(player.rigid_body.position, direction)
#
#
def _keys_to_player_direction(keys: set[int], a: float) -> Vector2:
    d_is_pressed = arcade.key.D in keys
    a_is_pressed = arcade.key.A in keys
    w_is_pressed = arcade.key.W in keys
    s_is_pressed = arcade.key.S in keys
    x = d_is_pressed - a_is_pressed
    y = w_is_pressed - s_is_pressed

    direction = Vector2(x, y)

    return direction.normalize if direction.length > 0 else direction


if __name__ == "__main__":
    main()

