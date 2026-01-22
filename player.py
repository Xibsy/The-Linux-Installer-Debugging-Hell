from attrs import define, field
import protocols as proto
from constants import ACCELERATION, MAX_PLAYER_SPEED, DRAG_RATION
from mathematics.vector import Vector2
from guns import RmRfShotgun, GrepSniper
from bullet import Bullet


@define
class Player(proto.Player):
    _rigid_body: proto.RigidBody
    _direction: Vector2 = field(init=False, default=Vector2.zero())
    _state: str = field(init=False, default="idle")

    _weapons: dict[int, proto.Weapon] = field(init=False)
    _current_weapon_id: int = field(init=False, default=1)

    def weapon(self):
        self._weapons = {
            1: RmRfShotgun(),
            2: GrepSniper()
        }

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
        acceleration -= self._rigid_body.velocity * DRAG_RATION
        self._rigid_body.update(acceleration, dt)

        velocity = self._rigid_body.velocity
        if velocity.length > MAX_PLAYER_SPEED:
            self._rigid_body.set_velocity(velocity.normalize * MAX_PLAYER_SPEED)

    def switch_weapon(self, weapon_id: int) -> None:
        if weapon_id in self._weapons:
            self._current_weapon_id = weapon_id

    def shoot(self, target: Vector2, current_time: float) -> list[Bullet]:
        weapon = self._weapons[self._current_weapon_id]
        return weapon.shoot(
            shooter_pos=self._rigid_body.position,
            shooter_shape=self._rigid_body.shape,
            target_pos=target,
            current_time=current_time
        )



