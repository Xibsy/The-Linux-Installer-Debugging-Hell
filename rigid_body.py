# from mathematics.mathematics import sign

from attrs import define

from mathematics.vector import Vector2
import protocols as proto


@define
class RigidBody(proto.RigidBody):
    _position: Vector2
    _velocity: Vector2
    _max_speed: int

    @property
    def position(self) -> Vector2:
        return self._position

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    def set_position(self, position: Vector2) -> None:
        self._position = position

    def set_velocity(self, velocity: Vector2) -> None:
        self._velocity = velocity

    def update(self, acceleration: Vector2, dt: float) -> None:
        delta_position = self.velocity * dt + (acceleration * dt**2) * .5
        delta_velocity = acceleration * dt

        self._position += delta_position
        self._velocity += delta_velocity