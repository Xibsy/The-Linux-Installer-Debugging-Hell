from attrs import define, field
import protocols as proto
from constants import ACCELERATION
from mathematics.vector import Vector2


@define
class Player(proto.Player):
    _rigid_body: proto.RigidBody
    _direction: Vector2 = field(init=False, default=Vector2.zero())

    @property
    def rigid_body(self) -> proto.RigidBody:
        return self._rigid_body

    @property
    def direction(self) -> Vector2:
        return self._direction

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1.00001
        self._direction = direction

    def update(self, dt: float):
        acceleration = self._direction * ACCELERATION
        self._rigid_body.update(acceleration, dt)



