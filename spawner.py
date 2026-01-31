from attrs import define

import protocols as proto
from enemy_list import EnemyList
from mathematics.random_enemy_count import random_enemy_count
from mathematics.vector import Vector2


@define
class Spawner(proto.Spawner):
    _position: Vector2
    _period: float
    _last_use: float = 0
    _enemy_list: EnemyList = EnemyList()

    @property
    def enemy_list(self) -> EnemyList:
        return self._enemy_list

    def spawn(self) -> None:
        for _ in range(random_enemy_count()):
            self._enemy_list.spawn(self._position)

    def update(self, dt: float, player: proto.Player)-> None:
        self._enemy_list.update(dt, player)
        self._last_use += dt
        if self._last_use <= self._period:
            return

        self._last_use = 0
        self.spawn()

