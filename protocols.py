from abc import ABC, abstractmethod
from typing import Callable

from mathematics.vector import Vector2

class Player(ABC):
    @property
    @abstractmethod
    def rigid_body(self) -> "RigidBody":
        ...

    @property
    @abstractmethod
    def direction(self) -> Vector2:
        ...

    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...


class RigidBody(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector2:
        ...

    @property
    @abstractmethod
    def velocity(self) -> Vector2:
        ...

    @abstractmethod
    def set_position(self, position: Vector2) -> None:
        ...

    @abstractmethod
    def set_velocity(self, velocity: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, acceleration: Vector2, dt: float) -> None:
        ...

class Enemy(ABC):
    @property
    @abstractmethod
    def rigid_body(self) -> RigidBody:
        ...

    @property
    @abstractmethod
    def direction(self) -> Vector2:
        ...

    @property
    @abstractmethod
    def health(self) -> float:
        ...

    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, player_position: Vector2):
        ...

class EnemyList(ABC):
    @property
    @abstractmethod
    def list(self) -> list[Enemy]:
        ...

    @abstractmethod
    def spawn(self, velocity: Vector2) -> None:
        ...

    @abstractmethod
    def kill(self, enemy: Enemy) -> None:
        ...

    @abstractmethod
    def apply(self, function: Callable[[Enemy], None]) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, player_position: Vector2) -> None:
        ...

    @abstractmethod
    def _is_enemy_kill(self, enemy: Enemy) -> bool:
        ...