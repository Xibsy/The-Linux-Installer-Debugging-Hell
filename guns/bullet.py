from attrs import define
from mathematics.vector import Vector2
from constants import ACCELERATION, MAX_PLAYER_SPEED
import protocols as proto
from rigid_body import RigidBody
from player import Player


@define
class Bullet:
    _rigid_body: RigidBody
    _direction: Vector2
    _damage: float
    _max_distance: float
    _start_position: Vector2

    @property
    def rigid_body(self) -> proto.RigidBody:
        return self._rigid_body

    @property
    def direction(self) -> Vector2:
        return self._direction

    @property
    def damage(self) -> float:
        return self._damage

    @property
    def max_distance(self) -> float:
        return self._max_distance

    @property
    def start_position(self) -> Vector2:
        return self._start_position

    def update(self, dt: float, enemy_list: proto.EnemyList, player: proto.Player,
               owner: proto.Enemy | proto.Player) -> None:
        acceleration = self._direction * ACCELERATION
        self._rigid_body.update(acceleration, dt)

        velocity = self._rigid_body.velocity
        if velocity.length > MAX_PLAYER_SPEED:
            self._rigid_body.set_velocity(velocity.normalize * MAX_PLAYER_SPEED)

        types = type(owner)
        if type(owner) == Player:
            self._check_enemy_hit(enemy_list)
        else:
            self._check_player_hit(player)


    def _intersects_aabb(self, other_rigid_boy: RigidBody) -> bool:
        b_x1, b_y1 = self._rigid_body.position.tuple
        b_x2, b_y2 = b_x1 + self._rigid_body.shape.x, b_y1 + self._rigid_body.shape.y

        o_x1, o_y1 = other_rigid_boy.position.tuple
        o_x2, o_y2 = o_x1 + other_rigid_boy.shape.x, o_y1 + other_rigid_boy.shape.y

        return not (
                b_x2 < o_x1 or
                b_x1 > o_x2 or
                b_y2 < o_y1 or
                b_y1 > o_y2
        )

    def _check_enemy_hit(self, enemy_list: proto.EnemyList) -> None:
        for enemy in enemy_list:
            if self._intersects_aabb(enemy.rigid_body):
                enemy.hit(self._damage)

    def _check_player_hit(self, player: proto.Player) -> None:
        if self._intersects_aabb(player.rigid_body):
            player.hit(self._damage)
