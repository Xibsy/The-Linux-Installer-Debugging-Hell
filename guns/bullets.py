from typing import Callable

from attrs import define, field

import constants as const
import protocols as proto
from guns.bullet import Bullet
from mathematics.vector import Vector2
from rigid_body import RigidBody


@define
class Bullets:
    _bullets: list[proto.Bullet] = field(init=False, factory=list)

    def spawn(self, direction: Vector2) -> None:
        bullet = Bullet(RigidBody(const.SCREEN_SHAPE.as_vector2 * .5, Vector2.zero(), 200, Vector2(10, 10)),
                        direction, 100, 1250)
        self._bullets.append(bullet)

    def kill(self, bullet: proto.Bullet) -> None:
        assert bullet in self._bullets

        self._bullets.remove(bullet)

    def apply(self, function: Callable[[proto.Bullet], None]) -> None:
        for bullet in self._bullets:
            function(bullet)

    def update(self, dt: float, enemy_list: proto.EnemyList, player: proto.Player) -> None:
        for bullet in self._bullets:
            bullet.update(dt, enemy_list, player)
            if self._is_alive(bullet):
                self.kill(bullet)

    def _is_alive(self, bullet: proto.Bullet) -> bool:
        return bullet.direction.length <= bullet.max_distance

    def __iter__(self):
        return iter(self._bullets)