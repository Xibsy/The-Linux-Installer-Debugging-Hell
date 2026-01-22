from attrs import define
from mathematics.vector import Vector2
from observer import Event, OnEventSubscriber
import arcade


@define
class PlayerInputer:
    pressed_keys: set[int] = set()

    _mouse_clicked_left = Event[Vector2, None]()
    _key_pressed = Event[int, None]()
    _keyboard_state_changed = Event[set[int], None]()

    @property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber

    @property
    def key_pressed(self) -> OnEventSubscriber[int, None]:
        return self._key_pressed.subscriber

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def on_key_press(self, symbol: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

        self._key_pressed.invoke(symbol)

    def on_key_release(self, symbol: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def on_mouse_press(self, x: float, y: float, button: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            mouse_pos = Vector2(x, y)
            self._mouse_clicked_left.invoke(mouse_pos)