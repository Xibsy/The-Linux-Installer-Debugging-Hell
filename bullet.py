from mathematics.vector import Vector2
from attrs import define
from rigid_body import RigidBody


@define
class Bullet:
    _position: Vector2
    _velocity: Vector2
    _damage: float
    _lifetime: float
    _spawn_time: float
    _shape: Vector2 = Vector2(4, 4)

    @property
    def position(self) -> Vector2:
        return self._position

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @property
    def shape(self) -> Vector2:
        return self._shape

    @property
    def damage(self) -> float:
        return self._damage

    def is_alive(self, current_time: float) -> bool:
        return (current_time - self._spawn_time) < self._lifetime

    def update(self, dt: float) -> None:
        self._position += self._velocity * dt

    def intersects(self, other: RigidBody) -> bool:
        x, y = self._position.tuple
        w, h = self._shape.tuple
        bullet_corners = [
            Vector2(x, y),
            Vector2(x + w, y),
            Vector2(x, y + h),
            Vector2(x + w, y + h),
        ]
        return any(other.is_contain(pt) for pt in bullet_corners)