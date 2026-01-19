from attrs import define
import protocols as proto
from animation import Animation
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
import constants as const
from sprite import Sprite


@define
class PlayerDraw:
    _player: proto.Player
    _player_walk: proto.Animation
    _player_ide: proto.Sprite

    def draw(self, mouse: Vector2) -> None:
        self._player_walk.has_ended.subscribe(lambda: self._player_walk.set_progress(0.))
        position = self._player.rigid_body.position
        direction = self._player.direction
        angle = get_sprite_degrees(*mouse.tuple, *position.tuple)
        if direction.length != 0:
           animate = self._player_walk
           animate.current_frame.blit_at(position, angle - 90)
           return
        sprite = self._player_ide
        const.WALK = False
        sprite.with_pivot(position)
        sprite.blit_at(position, angle - 90)

