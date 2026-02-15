import arcade
from attrs import define

from enemy_draw import EnemyListDraw
from enemy_list import EnemyList
from guns.enemy_bullets import EnemyBullets
from mathematics.vector import Vector2
from player_draw import PlayerDraw
from guns.player_bullets import PlayerBullets
from spawners_list import SpawnersList

PLATFORM_COLOR = arcade.color.GREEN

@define
class Draw:
    _player_draw: PlayerDraw
    _enemy_draw: EnemyListDraw

    def player(self, mouse: Vector2) -> None:
        self._player_draw.draw(mouse)

    def enemy(self, player_pos: Vector2, enemy_list: EnemyList) -> None:
        self._enemy_draw.draw(player_pos, enemy_list)

    def spawners_list(self, spawners_list: SpawnersList, player_pos: Vector2) -> None:
        for spawner in spawners_list:
            self.enemy(player_pos, spawner.enemy_list)

    def bullets(self, bullets: EnemyBullets | PlayerBullets) -> None:
        for bullet in bullets:
            arcade.draw_circle_filled(*bullet.rigid_body.position.tuple, 3, arcade.color.BLACK)