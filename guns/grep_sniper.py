from attrs import define
import protocols as proto
from guns.bullets import Bullets
from mathematics.vector import Vector2


@define
class GrepSniper:
    _owner: proto.Enemy | proto.Player
    _bullets: proto.Bullets = Bullets()
    _last_shoot: float = 0
    _period: float = 180
    _damage: float = 125

    @property
    def owner(self) -> proto.Enemy | proto.Player:
        return self._owner

    @property
    def bullets(self) -> proto.Bullets:
        return self._bullets

    def try_shoot(self, bullet_direction: Vector2, player_pos: Vector2) -> None:
        self._bullets.spawn(bullet_direction, player_pos)

    def update(self, dt: float, enemy_list: proto.EnemyList, player: proto.Player) -> None:
        self._bullets.update(dt, enemy_list, player)
        self._last_shoot += dt
