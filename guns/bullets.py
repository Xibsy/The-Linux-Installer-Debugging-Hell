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

    def spawn(self, direction: Vector2, owner_pos: Vector2) -> None:
        bullet = Bullet(RigidBody(owner_pos, Vector2(10, 10), 200, Vector2(6, 6)),
                        direction, 100, 1250, owner_pos)
        self._bullets.append(bullet)

    def kill(self, bullet: proto.Bullet) -> None:
        assert bullet in self._bullets

        self._bullets.remove(bullet)

    def apply(self, function: Callable[[proto.Bullet], None]) -> None:
        for bullet in self._bullets:
            function(bullet)

    def update(self, dt: float, enemy_list: proto.EnemyList, player: proto.Player,
               owner: proto.Player | proto.Enemy) -> None:
        for bullet in self._bullets:
            bullet.update(dt, enemy_list, player, owner, self)
            if self._is_alive(bullet) and bullet in self._bullets:
                self.kill(bullet)

    @staticmethod
    def _is_alive(bullet: proto.Bullet) -> bool:
        road = bullet.rigid_body.position - bullet.start_position
        return road.length >= bullet.max_distance

    def __iter__(self):
        return iter(self._bullets)