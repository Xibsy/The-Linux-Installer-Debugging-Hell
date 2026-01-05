from attrs import define

from mathematics.vector import Vector2
from observer import Event, OnEventSubscriber


@define
class PlayerInputer:
    _pressed_keys = set[int]()
    _mouse_clicked_left = Event[Vector2, None]()
    _keyboard_state_changed = Event[set[int], None]()

    @property
    def pressed_keys(self) -> set[int]:
        return self._pressed_keys

    @property
    def keyboard_state(self) -> Event[set[int], None]:
        return self._keyboard_state_changed

    @property
    def clicked_left(self) -> Event[Vector2, None]:
        return self._mouse_clicked_left

    @property
    def mouse_clicked(self) -> OnEventSubscriber[Vector2, None]:
        return self._mouse_clicked_left.subscriber

    @property
    def keyboard_state_changed(self) -> OnEventSubscriber[set[int], None]:
        return self._keyboard_state_changed.subscriber
