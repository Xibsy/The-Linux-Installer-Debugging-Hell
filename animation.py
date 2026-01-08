# https://ezgif.com/sprite-cutter/
import math
from pathlib import Path

from attrs import define, field

from sprite import Sprite, SPRITES_FOLDER
from observer import Event, OnEventSubscriber
from mathematics.vector import Vector2Int


@define
class Animation:
    @classmethod
    def load(cls, folder: Path | str, frames_count: int, period: float, pivot: Vector2Int = Vector2Int.zero()):
        folder = Path(folder)
        full_folder = SPRITES_FOLDER / folder
        assert full_folder.exists() and full_folder.is_dir()

        frames = list[Sprite]()
        for index in range(frames_count):
            filename = folder / f"tile{str(index).rjust(3, "0")}.png"
            frames.append(Sprite.load_raw_image(filename, pivot))

        return cls(frames, period)

    _frames: list[Sprite]
    _period: float
    _progress: float = field(init=False, default=0)

    _has_ended: Event[None] = field(init=False, factory=Event)

    @property
    def has_ended(self) -> OnEventSubscriber[None]:
        return self._has_ended.subscriber

    @property
    def current_frame(self) -> Sprite:
        assert self._progress < self._period
        return self._frames[self._current_frame_index]

    @property
    def _current_frame_index(self) -> int:
        return math.floor(self._progress / self._period * len(self._frames))

    def update(self, dt: float) -> None:
        self._progress += dt
        if self._progress <= self._period:
            return

        self._progress = self._period
        self._has_ended.invoke()
