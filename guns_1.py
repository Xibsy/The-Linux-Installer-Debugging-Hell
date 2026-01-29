import math
import random
from abc import ABC, abstractmethod

from constants import SCREEN_SHAPE
from mathematics.vector import Vector2
from guns.bullet import Bullet
import arcade
from rigid_body import RigidBody


class Weapon(ABC):
    def __init__(self, name: str, damage: float, fire_rate: float, ammo: int, texture_path: str) -> None:
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.ammo = ammo
        self.max_ammo = ammo
        self.last_shot_time = 0.0
        self.texture = arcade.load_texture(texture_path) if texture_path else None

    @abstractmethod
    def shoot(self, shooter_pos: Vector2, shooter_shape: Vector2, target_pos: Vector2, current_time: float) -> bool:
        pass

    def can_shoot(self, current_time: float) -> bool:
        return (current_time - self.last_shot_time) >= (1.0 / self.fire_rate) and self.ammo > 0

    def reload(self) -> None:
        self.ammo = self.max_ammo


class RmRfShotgun(Weapon):
    def __init__(self) -> None:
        super().__init__(name="rm -rf", damage=100.0, fire_rate=1.0, ammo=8, texture_path="path")
        self.spread_angle = 0.3
        self.range = 200.0

    def shoot(
            self,
            shooter_pos: Vector2,
            shooter_shape: Vector2,
            target_pos: Vector2,
            current_time: float
    ) -> list[Bullet]:
        if (current_time - self.last_shot_time) < (1.0 / self.fire_rate) or self.ammo <= 0:
            return []

        self.ammo -= 1
        self.last_shot_time = current_time

        muzzle_pos = shooter_pos + Vector2(shooter_shape.x * 0.5, shooter_shape.y)

        direction = (target_pos - muzzle_pos).normalize

        bullets = []
        pellet_count = 6
        spread_angle = 0.3
        bullet_speed = 600.0
        knockback = 150.0
        max_distance = 200.0

        for _ in range(pellet_count):
            angle_offset = random.uniform(-spread_angle, spread_angle)

            cos_a = math.cos(angle_offset)
            sin_a = math.sin(angle_offset)
            rotated_x = direction.x * cos_a - direction.y * sin_a
            rotated_y = direction.x * sin_a + direction.y * cos_a
            pellet_dir = Vector2(rotated_x, rotated_y).normalize

            bullet = Bullet(
                start_position=muzzle_pos,
                direction=pellet_dir,
                speed=bullet_speed,
                damage=self.damage,
                knockback=knockback,
                max_distance=max_distance
            )
            bullets.append(bullet)

        return bullets


class GrepSniper(Weapon):
    def __init__(self) -> None:
        super().__init__(name="grep -P", damage=80.0, fire_rate=0.5, ammo=5, texture_path="path")
        self.range = 1000.0
        self.zoom_factor = 0.3

    def shoot(
        self,
        shoter_rigid_body: RigidBody,
        target_pos: Vector2,
        current_time: float
    ) -> Bullet | None:
        if not self.can_shoot(current_time):
            return None

        self.ammo -= 1
        self.last_shot_time = current_time

        muzzle_pos = shooter_pos + Vector2(shooter_shape.x * 0.5, shooter_shape.y)

        direction = (target_pos - muzzle_pos).normalize

        bullet = Bullet(RigidBody(SCREEN_SHAPE.as_vector2 * .5, Vector2.zero(), 200, Vector2(10, 10)),
                        direction, 100, 1250)

        return bullet