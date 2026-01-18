import random
from typing import Callable

from attrs import frozen, field
import protocols as proto
from constants import SCREEN_SHAPE, MAX_ENEMY_SPEED
from enemy import Enemy
from mathematics.vector import Vector2
from rigid_body import RigidBody


def _generate_position() -> Vector2:
    x = random.randint(30, SCREEN_SHAPE.x - 30)
    y = random.randint(51, SCREEN_SHAPE.y - 51)
    return Vector2(x, y)


@frozen
class EnemyList(proto.EnemyList):
    _enemy_list: list[proto.Enemy] = field(init=False, factory=list)

    @property
    def list(self) -> list[proto.Enemy]:
        return self._enemy_list

    def spawn(self, velocity: Vector2) -> None:
        enemy = Enemy(RigidBody(_generate_position(), velocity, MAX_ENEMY_SPEED, Vector2(53, 31)))
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
        return enemy.health <= 0.0

