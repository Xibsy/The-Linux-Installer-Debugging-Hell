from attrs import define
import protocols as proto
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
import constants as const


@define
class PlayerDraw:
    _player: proto.Player

    def draw(self, mouse: Vector2) -> None:
        const.PLAYER_WALK_ANIMATION.has_ended.subscribe(lambda: const.PLAYER_WALK_ANIMATION.set_progress(0.))
        position = self._player.rigid_body.position
        direction = self._player.direction
        angle = get_sprite_degrees(*mouse.tuple, *position.tuple)
        if direction.length != 0:
           animate = const.PLAYER_WALK_ANIMATION
           animate.current_frame.blit_at(position, angle - 90)
           return
        sprite = const.PLAYER_IDE_SPRITE
        const.WALK = False
        sprite.with_pivot(position)
        sprite.blit_at(position, angle - 90)

