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

    def shoot(self, target: Vector2, time: float) -> list["Bullet"]:
        ...

    def switch_weapon(self, weapon_id: int) -> None:
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

    @property
    @abstractmethod
    def shape(self) -> Vector2:
        ...

    @abstractmethod
    def is_contain(self, point: Vector2) -> bool:
        ...

    @abstractmethod
    def is_collided_with(self, other: "RigidBody") -> bool:
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

    @property
    @abstractmethod
    def gun(self) -> 'GrepSniper':
        ...

    @abstractmethod
    def set_gun(self, gun: "GrepSniper") -> None:
        ...

    @abstractmethod
    def set_direction(self, direction: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, enemy_list: "EnemyList", player: Player) -> None:
        ...

class EnemyList(ABC):
    @abstractmethod
    def spawn(self, spawner_position: Vector2) -> None:
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

    @abstractmethod
    def __iter__(self):
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


class Weapon(ABC):
    @abstractmethod
    def shoot(self, shooter_pos: Vector2, shooter_shape: Vector2, target_pos: Vector2,
              current_time: float) -> list["Bullet"]:
        ...

    @abstractmethod
    def can_shoot(self, current_time: float) -> bool:
        ...

    @abstractmethod
    def reload(self) -> None:
        ...

class Spawner(ABC):
    @property
    @abstractmethod
    def enemy_list(self) -> EnemyList:
        ...

    @abstractmethod
    def spawn(self) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, player: Player) -> None:
        ...

class Bullet(ABC):

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
    def damage(self) -> float:
        ...

    @property
    @abstractmethod
    def max_distance(self) -> float:
        ...

    @abstractmethod
    def update(self, dt: float, enemy_list: EnemyList, player: Player,
               owner: Enemy | Player, bullets: "Bullets") -> None:
        ...

    @abstractmethod
    def _intersects_aabb(self, other_rigid_boy: RigidBody) -> bool:
        ...

    @abstractmethod
    def _check_enemy_hit(self, enemy_list: EnemyList) -> None:
        ...

    @abstractmethod
    def _check_player_hit(self, player: Player) -> None:
        ...

class Bullets(ABC):
    @abstractmethod
    def spawn(self, direction: Vector2, player_pos: Vector2) -> None:
        ...

    @abstractmethod
    def kill(self, bullet: Bullet) -> None:
        ...

    @abstractmethod
    def apply(self, function: Callable[[Bullet], None]) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, enemy_list: EnemyList, player: Player) -> None:
        ...

    @abstractmethod
    def _is_alive(self, bullet: Bullet) -> bool:
        ...

    @abstractmethod
    def __iter__(self):
        ...


class GrepSniper(ABC):
    @property
    @abstractmethod
    def owner(self) -> Enemy | Player:
        ...

    @property
    @abstractmethod
    def bullets(self) -> Bullets:
        ...

    @abstractmethod
    def try_shoot(self, bullet_direction: Vector2, player_pos: Vector2) -> None:
        ...

    @abstractmethod
    def update(self, dt: float, enemy_list: EnemyList, player: Player) -> None:
        ...


class Platform(ABC):
    @property
    @abstractmethod
    def rigid_body(self) -> RigidBody:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...

class Platforms(ABC):
    @abstractmethod
    def get_touched(self, other: RigidBody) -> Platform | None:
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        ...

    @abstractmethod
    def apply(self, function: Callable[[Platform], None]) -> None:
        ...