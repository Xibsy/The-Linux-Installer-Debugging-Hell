# from mathematics.mathematics import sign

from attrs import define
from mathematics.vector import Vector2
import protocols as proto


@define
class RigidBody(proto.RigidBody):
    _position: Vector2
    _velocity: Vector2
    _max_speed: float
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

    def set_position(self, position: Vector2) -> None:
        self._position = position

    def set_velocity(self, velocity: Vector2) -> None:
        if velocity.length > self._max_speed:
            velocity = velocity.normalize * self._max_speed
        self._velocity = velocity

    def update(self, acceleration: Vector2, dt: float) -> None:
        new_velocity = self._velocity + acceleration * dt
        if new_velocity.length > self._max_speed:
            new_velocity = new_velocity.normalize * self._max_speed
        self._velocity = new_velocity
        self._position += self._velocity * dt

    def is_contain(self, point: Vector2) -> bool:
        x, y = self._position.tuple
        w, h = self._shape.tuple
        return (x <= point.x <= x + w) and (y <= point.y <= y + h)

    def constrain_to_screen(self, screen_width: float, screen_height: float) -> None:
        x, y = self._position.tuple
        w, h = self._shape.tuple

        if x < 0:
            self._position = Vector2(0, y)
            self._velocity = Vector2(0, self._velocity.y)
        elif x + w > screen_width:
            self._position = Vector2(screen_width - w, y)
            self._velocity = Vector2(0, self._velocity.y)

        if y < 0:
            self._position = Vector2(x, 0)
            self._velocity = Vector2(self._velocity.x, 0)
        elif y + h > screen_height:
            self._position = Vector2(x, screen_height - h)
            self._velocity = Vector2(self._velocity.x, 0)
