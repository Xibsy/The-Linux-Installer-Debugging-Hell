from attrs import define, field

import protocols as proto
from constants import ACCELERATION, DRAG_RATION, MAX_ENEMY_SPEED
from guns.grep_sniper import GrepSniper
from mathematics.vector import Vector2


@define
class Enemy(proto.Enemy):
    _rigid_body: proto.RigidBody
    _gun: GrepSniper | None = None
    _direction: Vector2 = field(init=False, default=Vector2.zero())
    _health: float = field(init=False, default=100.0)

    @property
    def rigid_body(self) -> proto.RigidBody:
        return self._rigid_body

    @property
    def direction(self) -> Vector2:
        return self._direction

    @property
    def health(self) -> float:
        return self._health

    @property
    def gun(self) -> GrepSniper | None:
        return self._gun

    def set_gun(self, gun: GrepSniper) -> None:
        self._gun = gun

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1.00001
        self._direction = direction

    def set_health(self, health: float) -> None:
        self._health = health

    def hit(self, health: float) -> None:
        self._health -= health

    def update(self, dt: float, enemy_list: proto.EnemyList, player: proto.Player) -> None:
        acceleration = self._direction * ACCELERATION
        acceleration -= self._rigid_body.velocity * DRAG_RATION
        self._rigid_body.update(acceleration, dt)

        velocity = self._rigid_body.velocity
        if velocity.length > MAX_ENEMY_SPEED:
            self._rigid_body.set_velocity(velocity.normalize * MAX_ENEMY_SPEED)

        direction = player.rigid_body.position - self._rigid_body.position

        self.set_direction(direction.normalize if direction.length >= 200 else Vector2.zero())
        if direction.length < 200:
            self._gun.try_shoot(direction.normalize)