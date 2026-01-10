import random

import arcade
from arcade import schedule
from arcade import SpriteList
from attrs import define
import protocols as proto
from mathematics.get_sprite_degrees import get_sprite_degrees
from mathematics.vector import Vector2
import constants as const


@define
class PlayerDraw:
    _player: proto.Player
    _last_walk_sprite: int = 0

    def switch_sprite(self, dt: float) -> None:
        self._last_walk_sprite += 1
        if self._last_walk_sprite > 5:
            self._last_walk_sprite = 0

    def draw(self, mouse: Vector2) -> None:
        position = self._player.rigid_body.position
        direction = self._player.direction
        finish_sprite_list = SpriteList()
        sprite = const.PLAYER_WALK_SPRITES[0]
        if direction.length != 0:
           sprite = const.PLAYER_WALK_SPRITES[self._last_walk_sprite]
           schedule(self.switch_sprite, 0.1)
        sprite.center_x = position.x
        sprite.center_y = position.y
        sprite.angle = get_sprite_degrees(*mouse.tuple, *position.tuple)
        finish_sprite_list.append(sprite)
        finish_sprite_list.draw()