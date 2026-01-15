import math
import random
from abc import ABC, abstractmethod
from mathematics.vector import Vector2


class Weapon(ABC):
    def __init__(self, name: str, damage: float, fire_rate: float, ammo: int) -> None:
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.ammo = ammo
        self.max_ammo = ammo
        self.last_shot_time = 0.0

    @abstractmethod
    def shoot(self, shooter_pos: Vector2, shooter_shape: Vector2, target_pos: Vector2, current_time: float) -> bool:
        pass

    def can_shoot(self, current_time: float) -> bool:
        return (current_time - self.last_shot_time) >= (1.0 / self.fire_rate) and self.ammo > 0

    def reload(self) -> None:
        self.ammo = self.max_ammo


class RmRfShotgun(Weapon):
    def __init__(self) -> None:
        super().__init__(name="rm -rf", damage=100.0, fire_rate=1.0, ammo=8)
        self.spread_angle = 0.3
        self.range = 200.0

    def shoot(
        self,
        shooter_pos: Vector2,
        shooter_shape: Vector2,
        target_pos: Vector2,
        current_time: float
    ) -> bool:
        if not self.can_shoot(current_time):
            return False

        self.ammo -= 1
        self.last_shot_time = current_time

        muzzle_pos = shooter_pos + Vector2(shooter_shape.x / 2, shooter_shape.y)

        direction = (target_pos - muzzle_pos).normalize

        for _ in range(6):
            angle_offset = random.uniform(-self.spread_angle, self.spread_angle)
            cos_a = math.cos(angle_offset)
            sin_a = math.sin(angle_offset)
            dx = direction.x * cos_a - direction.y * sin_a
            dy = direction.x * sin_a + direction.y * cos_a
            bullet_dir = Vector2(dx, dy).normalize

            self.spawn_bullet(muzzle_pos, bullet_dir, self.damage)

        return True

    def spawn_bullet(self, start: Vector2, direction: Vector2, damage: float) -> None:
        pass


class GrepSniper(Weapon):
    def __init__(self) -> None:
        super().__init__(name="grep -P", damage=150.0, fire_rate=0.5, ammo=5)
        self.range = 1200.0

    def shoot(
        self,
        shooter_pos: Vector2,
        shooter_shape: Vector2,
        target_pos: Vector2,
        current_time: float
    ) -> bool:
        if not self.can_shoot(current_time):
            return False

        self.ammo -= 1
        self.last_shot_time = current_time

        muzzle_pos = shooter_pos + Vector2(shooter_shape.x / 2, shooter_shape.y)
        direction = (target_pos - muzzle_pos).normalize
        end_point = muzzle_pos + direction * self.range

        self.spawn_bullet(muzzle_pos, end_point, self.damage)

        return True

    def spawn_bullet(self, start: Vector2, end: Vector2, damage: float, is_critical: bool = False) -> None:
        pass