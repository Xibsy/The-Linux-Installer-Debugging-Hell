import arcade
from attrs import define
import protocols as proto
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
from player_draw import PlayerDraw


@define
class Draw:
    _player_draw: PlayerDraw
    def player(self, mouse: Vector2) -> None:
        self._player_draw.draw(mouse)