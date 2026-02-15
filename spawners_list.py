from typing import Callable

from attrs import define, field

import protocols as proto
from spawner import Spawner
from mathematics.random_spawner_pos import random_spawner_position
from mathematics.random_spawner_period import random_spawner_period
from mathematics.random_spawer_count import random_spawner_count


@define
class SpawnersList:
    _spawners: list[proto.Spawner] = field(init=False, factory=list)

    def spawn(self) -> None:
        bullet = Spawner(random_spawner_position(), random_spawner_period())
        print(bullet)
        self._spawners.append(bullet)

    def kill(self, spawner: proto.Spawner) -> None:
        assert spawner in self._spawners

        self._spawners.remove(spawner)

    def apply(self, function: Callable[[proto.Spawner], None]) -> None:
        for bullet in self._spawners:
            function(bullet)

    def update(self, dt: float, player: proto.Player) -> None:
        for spawner in self._spawners:
            spawner.update(dt, player)
            if spawner.enemy_list.enemy_count == -1:
                self.kill(spawner)
                for _ in range(random_spawner_count()):
                    self.spawn()

    def __iter__(self):
        return iter(self._spawners)