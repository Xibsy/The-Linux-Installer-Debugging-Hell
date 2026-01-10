from rigid_body import RigidBody
import arcade


class SudoBerserk:
    def __init__(self, duration: float = 5.0, cooldown: float = 30.0) -> None:
        self.duration = duration
        self.cooldown = cooldown
        self.active_until = 0.0
        self.last_used = -cooldown
        self.owner: 'RigidBody' = None

    def set_owner(self, owner: 'RigidBody') -> None:
        self.owner = owner

    def activate(self, current_time: float) -> bool:
        if current_time - self.last_used < self.cooldown:
            return False
        self.active_until = current_time + self.duration
        self.last_used = current_time
        # arcade.play_sound(arcade.Sound(":resources:sounds/upgrade4.wav"))
        return True

    def is_active(self, current_time: float) -> bool:
        return current_time < self.active_until

    # def get_bonus_damage(self) -> float:
    #     return 100.0 if self.is_active(arcade.time) else 0.0

    # def is_invulnerable(self) -> bool:
    #     return self.is_active(arcade.time)