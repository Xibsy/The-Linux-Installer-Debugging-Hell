from traceback import print_tb

from attrs import define

import protocols as proto
from enemy_list import EnemyList
from mathematics.random_enemy_count import random_enemy_count
from mathematics.vector import Vector2
from mathematics.random_spawner_limits import random_spawner_limit


@define
class Spawner(proto.Spawner):
    _position: Vector2
    _period: float
    _last_use: float = 0
    _enemy_list: EnemyList = EnemyList()
    _limit: int = random_spawner_limit()
    _spawns_enemies: int = 0

    @property
    def enemy_list(self) -> EnemyList:
        return self._enemy_list

    @property
    def limit(self) -> int:
        return self._limit

    def spawn(self) -> None:
        for _ in range(random_enemy_count()):
            self._enemy_list.spawn(self._position)
            self._spawns_enemies += 1


    def update(self, dt: float, player: proto.Player)-> None:
        self._enemy_list.update(dt, player, self._spawns_enemies >= self._limit)
        self._last_use += dt
        if self._last_use <= self._period:
            return

        self._last_use = 0
        self.spawn()
        print(self._spawns_enemies)
