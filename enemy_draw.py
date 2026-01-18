from attrs import define
from enemy_list import EnemyList
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
import constants as const


@define
class EnemyListDraw:
    def draw(self, player_position: Vector2, enemy_list: EnemyList) -> None:
        const.ENEMY_WALK_ANIMATION.has_ended.subscribe(lambda: const.ENEMY_WALK_ANIMATION.set_progress(0.))
        for enemy in enemy_list.list:
            position = enemy.rigid_body.position
            direction = enemy.direction
            angle = get_sprite_degrees(*player_position.tuple, *position.tuple)
            if direction.length != 0:
                animate = const.ENEMY_WALK_ANIMATION
                animate.current_frame.blit_at(position, angle - 90)
                continue
            sprite = const.ENEMY_IDE_SPRITE
            sprite.with_pivot(position)
            sprite.blit_at(position, angle - 90)