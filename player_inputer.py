from attrs import define
from mathematics.vector import Vector2
from observer import Event, OnEventSubscriber


@define
class PlayerInputer:
    pressed_keys = set[int]()
    _mouse_clicked_left = Event[Vector2, None]()
    _keyboard_state_changed = Event[set[int], None]()

    @property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber

    def register_press(self, symbol: int) -> None:
        self.pressed_keys.add(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)

    def unregister_press(self, symbol: int) -> None:
        self.pressed_keys.discard(symbol)
        self._keyboard_state_changed.invoke(self.pressed_keys)
