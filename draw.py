import arcade
from attrs import define
import protocols as proto
from constants import PLAYER_COLOR


@define
class Draw:
    def player(self, player: proto.Player) -> None:
        position = player.rigid_body.position
        rect = arcade.rect.LBWH(*position.tuple, *player.rigid_body.shape.tuple)
        arcade.draw_rect_filled(rect, PLAYER_COLOR)