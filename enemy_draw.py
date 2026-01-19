from attrs import define
import protocols as proto
from enemy_list import EnemyList
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
import constants as const


@define
class EnemyListDraw:
    _enemy_walk: proto.Animation
    _enemy_ide: proto.Sprite

    def draw(self, player_position: Vector2, enemy_list: EnemyList) -> None:
        self._enemy_walk.has_ended.subscribe(lambda: self._enemy_walk.set_progress(0.))
        for enemy in enemy_list:
            position = enemy.rigid_body.position
            direction = enemy.direction
            angle = get_sprite_degrees(*player_position.tuple, *position.tuple)
            if direction.length != 0:
                animate = self._enemy_walk
                animate.current_frame.blit_at(position, angle - 90)
                continue
            sprite = self._enemy_ide
            sprite.with_pivot(position)
            sprite.blit_at(position, angle - 90)