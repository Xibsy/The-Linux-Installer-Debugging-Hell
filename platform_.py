

import protocols as proto


class Platform(proto.Platform):
    _rigid_body: proto.RigidBody

    @property
    def rigid_body(self) -> proto.RigidBody:
        return self._rigid_body

    def update(self, dt: float) -> None:
        ...
