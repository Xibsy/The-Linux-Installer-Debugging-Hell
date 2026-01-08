import math
import random
from abc import ABC, abstractmethod

import arcade

from mathematics.vector import Vector2
from rigid_body import RigidBody


class Weapon(ABC):
    def __init__(self, name: str, damage: float, fire_rate: float, ammo: int) -> None:
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.ammo = ammo
        self.max_ammo = ammo
        self.last_shot_time = 0.0
        self.owner: 'RigidBody' = None

    def set_owner(self, owner: 'RigidBody') -> None:
        self.owner = owner

    @abstractmethod
    def shoot(self, target_pos: Vector2, current_time: float) -> bool:
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
        self.knockback = 200.0

    def shoot(self, target_pos: Vector2, current_time: float) -> bool:
        if not self.owner or not self.can_shoot(current_time):
            return False

        self.ammo -= 1
        self.last_shot_time = current_time

        owner_pos = self.owner.position + Vector2(0, self.owner.shape.y / 2)

        direction = (target_pos - owner_pos).normalize
        for _ in range(6):
            angle_offset = random.uniform(-self.spread_angle, self.spread_angle)
            dx = direction.x * math.cos(angle_offset) - direction.y * math.sin(angle_offset)
            dy = direction.x * math.sin(angle_offset) + direction.y * math.cos(angle_offset)
            bullet_dir = Vector2(dx, dy)

            self.spawn_bullet(owner_pos, bullet_dir * self.range, self.damage, self.knockback)

        # arcade.play_sound(arcade.Sound(":resources:sounds/laser2.wav"))
        return True

    def spawn_bullet(self, start: Vector2, end: Vector2, damage: float, knockback: float) -> None:
        pass


class GrepSniper(Weapon):
    def __init__(self):
        super().__init__(name="grep -P", damage=80.0, fire_rate=0.5, ammo=5)
        self.range = 1000.0
        self.knockback = 100.0
        self.zoom_factor = 0.3

    def shoot(self, target_pos: Vector2, current_time: float) -> bool:
        if not self.owner or not self.can_shoot(current_time):
            return False

        self.ammo -= 1
        self.last_shot_time = current_time

        owner_pos = self.owner.position + Vector2(0, self.owner.shape.y / 2)
        direction = (target_pos - owner_pos).normalize

        hit_point = owner_pos + direction * self.range

        self.spawn_bullet(owner_pos, hit_point, self.damage, self.knockback, is_critical=True)

        # arcade.play_sound(arcade.Sound(":resources:sounds/hit5.wav"))
        return True

    def spawn_bullet(self, start: Vector2, end: Vector2, damage: float, knockback: float, is_critical=False) -> None:
        pass
