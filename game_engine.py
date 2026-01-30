import arcade

from guns.grep_sniper import GrepSniper
from camera import Camera
from constants import SCREEN_SHAPE
from mathematics.vector import Vector2Int, Vector2
from draw import Draw
import protocols as proto
from player_inputer import PlayerInputer


class GameEngine(arcade.Window):
    def __init__(self,
                 title: str,
                 screen_shape: Vector2Int,
                 draw: Draw,
                 player: proto.Player,
                 gun: proto.GrepSniper,
                 enemy_list: proto.EnemyList,
                 player_walk: proto.Animation,
                 enemy_walk: proto.Animation,
                 spawner: proto.Spawner) -> None:
        super().__init__(screen_shape.x, screen_shape.y, title, vsync=True)
        self.background_color = arcade.color.LIME_GREEN
        self._draw = draw
        self._player = player

        self._camera = Camera(arcade.Camera2D(), self._player)

        self._player_inputer = PlayerInputer()
        self._enemy_list = enemy_list

        self._gun = gun
        self._player_walk = player_walk
        self._enemy_walk = enemy_walk
        self._spawner = spawner

    @property
    def player_inputer(self) -> PlayerInputer:
        return self._player_inputer

    @property
    def direction_to_mouse(self) -> Vector2:
        mouse_position = Vector2(self._mouse_x, self._mouse_y)
        return mouse_position - SCREEN_SHAPE.as_vector2 * .5

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self._player_inputer.on_press(symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self._player_inputer.on_release(symbol)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        self._player_inputer.on_mouse_press(x, y, button)

    def on_update(self, delta_time: float) -> None:
        self._player_walk.update(delta_time)
        self._enemy_walk.update(delta_time)

    def on_fixed_update(self, delta_time: float) -> None:
        self._player.update(delta_time)
        self._spawner.update(delta_time, self._player.rigid_body.position)
        self._camera.update(delta_time)
        self._gun.update(delta_time, self._spawner.enemy_list, self._player)

    def on_draw(self) -> None:
        self.clear()
        self._camera.camera.use()
        self._draw.player(Vector2(self._mouse_x, self._mouse_y))
        self._draw.enemy(self._player.rigid_body.position, self._spawner.enemy_list)
        self._draw.bullets(self._gun.bullets)

