from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable

import arcade

from mathematics.vector import Vector2, Vector2Int
from observer import OnEventSubscriber


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


class Sprite(ABC):
    @classmethod
    @abstractmethod
    def load_raw_image(cls, path: Path | str, shape: float = 1., pivot: Vector2Int = Vector2Int.zero()) -> "Sprite":
        ...

    @property
    @abstractmethod
    def shape(self) -> Vector2:
        ...

    @abstractmethod
    def get(self) -> arcade.Texture:
        ...

    @abstractmethod
    def blit_at(self, position: Vector2, angle: float=0.0) -> None:
        ...

    @abstractmethod
    def with_pivot(self, pivot: Vector2) -> "Sprite":
        ...

    @abstractmethod
    def with_pivot_from_ratios(self, ratio_x: float, ratio_y: float) -> "Sprite":
        ...

    @abstractmethod
    def reshape(self, shape: Vector2) -> "Sprite":
        ...

    @abstractmethod
    def resize(self, ratio: float) -> "Sprite":
        ...


class Animation(ABC):
    @classmethod
    @abstractmethod
    def load(cls, folder: Path | str, frames_count: int, period: float, shape: float, pivot: Vector2Int = Vector2Int.zero()):
        ...

    @property
    @abstractmethod
    def has_ended(self) -> OnEventSubscriber[None]:
        ...

    @property
    @abstractmethod
    def current_frame(self) -> Sprite:
        ...

    @property
    @abstractmethod
    def _current_frame_index(self) -> int:
        ...

    @abstractmethod
    def set_progress(self, progress: float) -> None:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...