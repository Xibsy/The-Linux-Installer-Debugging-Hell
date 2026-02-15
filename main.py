import arcade

import constants as const
from animation import Animation
from enemy_draw import EnemyListDraw
from player import Player
from draw import Draw
from game_engine import GameEngine
from player_draw import PlayerDraw
from enemy_list import *
from spawners_list import SpawnersList
from sprite import Sprite
from guns.player_grep_sniper import PlayerGrepSniper


def main() -> None:
    player_walk = Animation.load('player_walk', 6, 1.5, 1.5)
    enemy_walk = Animation.load('enemy_walk', 6, 1.5, 1.5)

    player_ide = Sprite.load_raw_image('player_ide.png', 1.5)
    enemy_ide = Sprite.load_raw_image('enemy_ide.png', 1.5)

    player = Player(RigidBody(const.SCREEN_SHAPE.as_vector2 * .5, Vector2.zero(),
                              const.MAX_PLAYER_SPEED, Vector2(48, 38)))
    gun = PlayerGrepSniper(player)
    player.set_gun(gun)
    spawner_list = SpawnersList()
    spawner_list.spawn()

    engine = GameEngine(const.TITLE, const.SCREEN_SHAPE,
                        Draw(PlayerDraw(player, player_walk, player_ide), EnemyListDraw(enemy_walk, enemy_ide)),
                        player, player_walk, enemy_walk, spawner_list)

    (engine.player_inputer.keyboard_state_changed
     .subscribe(lambda keys: player.set_direction(_keys_to_player_direction(keys, engine.direction_to_mouse))))

    engine.player_inputer.mouse_clicked.subscribe(lambda pos: _on_mouse_click(pos, gun))

    engine.run()


def _on_mouse_click(position: Vector2, gun: PlayerGrepSniper) -> None:
    direction = (position - const.SCREEN_SHAPE.as_vector2 * .5).normalize

    gun.try_shoot(direction)


def _keys_to_player_direction(keys: set[int], direction_to_mouse: Vector2) -> Vector2:
    d_is_pressed = arcade.key.D in keys
    a_is_pressed = arcade.key.A in keys
    w_is_pressed = arcade.key.W in keys
    s_is_pressed = arcade.key.S in keys
    x = direction_to_mouse.as_90 * (d_is_pressed - a_is_pressed)
    y = direction_to_mouse * (w_is_pressed - s_is_pressed)
    c = x + y


    direction = c

    return direction.normalize if direction.length > 0 else direction


if __name__ == "__main__":
    main()
