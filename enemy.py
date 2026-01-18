from attrs import define, field

import protocols as proto
from constants import ACCELERATION, DRAG_RATION, MAX_ENEMY_SPEED
from mathematics.vector import Vector2


@define
class Enemy(proto.Enemy):
    _rigid_body: proto.RigidBody
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

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1.00001
        self._direction = direction

    def set_health(self, health: float) -> None:
        self._health = health

    def update(self, dt: float, player_position: Vector2):
        acceleration = self._direction * ACCELERATION
        acceleration -= self._rigid_body.velocity * DRAG_RATION
        self._rigid_body.update(acceleration, dt)

        velocity = self._rigid_body.velocity
        if velocity.length > MAX_ENEMY_SPEED:
            self._rigid_body.set_velocity(velocity.normalize * MAX_ENEMY_SPEED)

        direction = (player_position - self._rigid_body.position)

        a = direction.length

        self.set_direction(direction.normalize if direction.length >= 100 else Vector2.zero())