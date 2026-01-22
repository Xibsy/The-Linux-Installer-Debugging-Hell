from attrs import define
from mathematics.vector import Vector2


@define
class Bullet:
    _start_position: Vector2
    _direction: Vector2
    _speed: float
    _damage: float
    _knockback: float
    _max_distance: float

    _current_distance: float = 0.0
    _shape: Vector2 = Vector2(4.0, 4.0)

    @property
    def position(self) -> Vector2:
        return self._start_position + self._direction * self._current_distance

    @property
    def damage(self) -> float:
        return self._damage

    @property
    def knockback(self) -> float:
        return self._knockback

    def is_alive(self) -> bool:
        return self._current_distance < self._max_distance

    def update(self, dt: float) -> None:
        self._current_distance += self._speed * dt

    def intersects_aabb(self, other_pos: Vector2, other_shape: Vector2) -> bool:
        b_x1, b_y1 = self.position.tuple
        b_x2, b_y2 = b_x1 + self._shape.x, b_y1 + self._shape.y

        o_x1, o_y1 = other_pos.tuple
        o_x2, o_y2 = o_x1 + other_shape.x, o_y1 + other_shape.y

        return not (
                b_x2 < o_x1 or
                b_x1 > o_x2 or
                b_y2 < o_y1 or
                b_y1 > o_y2
        )

    def check_hit(self, enemies: list) -> tuple[bool, object | None]:

        for enemy in enemies:
            if self.intersects_aabb(enemy.position, enemy.shape):
                return True, enemy
        return False, None