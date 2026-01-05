from mathematics.mathematics import sign

from attrs import define

from mathematics.vector import Vector2
import protocols as proto


@define
class RigidBody(proto.RigidBody):
    _position: Vector2
    _velocity: Vector2
    _max_speed: Vector2

    _shape: Vector2

    @property
    def position(self) -> Vector2:
        return self._position

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @property
    def shape(self) -> Vector2:
        return self._shape

    def is_contain(self, point: Vector2) -> bool:
        x, y = self.position.tuple
        width, height = self.shape.tuple
        return ((x <= point.x <= x + width) and
                (y <= point.y <= y + height))

    def is_collided_with(self, other: "RigidBody", _is_inner=False) -> bool:
        x, y = self.position.tuple
        width, height = self.shape.tuple
        corners = [
            Vector2(x, y),
            Vector2(x + width, y),
            Vector2(x, y + height),
            Vector2(x + width, y + height),
        ]
        result = any(other.is_contain(point) for point in corners)
        if result:
            return True
        if not _is_inner:
            return other.is_collided_with(self, _is_inner=True)
        return False


    def set_position(self, position: Vector2) -> None:
        self._position = position

    def set_velocity(self, velocity: Vector2) -> None:
        self._velocity = velocity

    def update(self, acceleration: Vector2, dt: float) -> None:
        delta_position = self.velocity * dt + (acceleration * dt**2) * .5
        delta_velocity = acceleration * dt

        self._position += delta_position
        self._velocity += delta_velocity
