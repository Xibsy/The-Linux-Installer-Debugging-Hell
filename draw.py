import arcade
from attrs import define

from enemy_draw import EnemyListDraw
from enemy_list import EnemyList
from guns.bullets import Bullets
from mathematics.vector import Vector2
from player_draw import PlayerDraw


@define
class Draw:
    _player_draw: PlayerDraw
    _enemy_draw: EnemyListDraw

    def player(self, mouse: Vector2) -> None:
        self._player_draw.draw(mouse)

    def enemy(self, mouse: Vector2, enemy_list: EnemyList) -> None:
        self._enemy_draw.draw(mouse, enemy_list)

    def bullets(self, bullets: Bullets) -> None:
        for bullet in bullets:
            arcade.draw_circle_filled(*bullet.rigid_body.position.tuple, 3, arcade.color.BLACK)