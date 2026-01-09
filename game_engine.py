import math
import arcade
from mathematics.vector import Vector2Int
from draw import Draw
import protocols as proto
from player_inputer import PlayerInputer


class GameEngine(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self.background_color = arcade.color.LIME_GREEN
        self._draw = draw
        self._player = player

        self._player_inputer = PlayerInputer()

        self._player_sprite_path = 'sprites/player.png'
        self._player_sprite = arcade.Sprite(self._player_sprite_path)

    @property
    def player_inputer(self) -> PlayerInputer:
        return self._player_inputer

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._player_inputer.register_press(symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self._player_inputer.unregister_press(symbol)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        diff_x = x - self._player.rigid_body.position.x
        diff_y = y - self._player.rigid_body.position.y
        angle_rad = math.atan2(diff_x, diff_y)
        a = math.degrees(angle_rad)
        self._player_sprite.angle = a

    def on_fixed_update(self, delta_time: float) -> None:
        self._player.update(delta_time)

    def on_draw(self) -> None:
        self.clear()
        self._draw.player(self._player, self._player_sprite)

