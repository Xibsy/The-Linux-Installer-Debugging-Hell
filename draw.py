import arcade
from attrs import define
import protocols as proto


@define
class Draw:
    def player(self, player: proto.Player, player_sprite: arcade.Sprite) -> None:
        position = player.rigid_body.position
        player_sprite.center_x = position.x - player.rigid_body.shape.x
        player_sprite.center_y = position.y - player.rigid_body.shape.y
        player_sprite_list = arcade.SpriteList()
        player_sprite_list.append(player_sprite)
        player_sprite_list.draw()