import random
from typing import Callable

from attrs import frozen, field
import protocols as proto
from constants import SCREEN_SHAPE, MAX_ENEMY_SPEED
from enemy import Enemy
from mathematics.vector import Vector2
from rigid_body import RigidBody


def _generate_position(spawner_position: Vector2) -> Vector2:
    int_x = int(spawner_position.x)
    int_y = int(spawner_position.y)
    x = random.randint(int_x - 200, int_x + 200)
    y = random.randint(int_y - 200, int_y + 200)
    return Vector2(x, y)


@frozen
class EnemyList(proto.EnemyList):
    _enemy_list: list[proto.Enemy] = field(init=False, factory=list)

    def spawn(self, spawner_position: Vector2) -> None:
        enemy = Enemy(RigidBody(_generate_position(spawner_position), Vector2.zero(), MAX_ENEMY_SPEED, Vector2(53, 31)))
        self._enemy_list.append(enemy)

    def kill(self, enemy: proto.Enemy) -> None:
        assert enemy in self._enemy_list

        self._enemy_list.remove(enemy)

    def apply(self, function: Callable[[proto.Enemy], None]) -> None:
        for enemy in self._enemy_list:
            function(enemy)

    def update(self, dt: float, player_position: Vector2) -> None:
        for enemy in self._enemy_list:
            enemy.update(dt, player_position)
            if self._is_enemy_kill(enemy):
                self.kill(enemy)

    def _is_enemy_kill(self, enemy: proto.Enemy) -> bool:
        return not True #((0 <= enemy.rigid_body.position.x <= 2000) and (0 <= enemy.rigid_body.position.y <= 2000))

    def __iter__(self):
        return iter(self._enemy_list)

