from attrs import define, field
import protocols as proto
from constants import ACCELERATION, MAX_PLAYER_SPEED, DRAG_RATION
from mathematics.vector import Vector2
from spawners_list import SpawnersList


@define
class Player(proto.Player):
    _rigid_body: proto.RigidBody
    _direction: Vector2 = field(init=False, default=Vector2.zero())
    _gun: proto.PlayerGrepSniper | None = None
    _state: str = field(init=False, default=str)
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
    def gun(self) -> proto.PlayerGrepSniper | None:
        return self._gun

    def set_direction(self, direction: Vector2) -> None:
        assert direction.length <= 1.00001
        self._direction = direction

    def set_health(self, health: float) -> None:
        self._health = health

    def set_gun(self, gun: proto.PlayerGrepSniper) -> None:
        self._gun = gun

    def hit(self, health: float) -> None:
        self._health -= health

    def update(self, dt: float, spawners_list: SpawnersList) -> None:
        acceleration = self._direction * ACCELERATION
        acceleration -= self._rigid_body.velocity * DRAG_RATION
        self._rigid_body.update(acceleration, dt)
        for spawner in spawners_list:
            self._gun.update(dt, spawner.enemy_list)

        velocity = self._rigid_body.velocity
        if velocity.length > MAX_PLAYER_SPEED:
            self._rigid_body.set_velocity(velocity.normalize * MAX_PLAYER_SPEED)


