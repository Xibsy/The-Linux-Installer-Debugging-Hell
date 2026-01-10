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