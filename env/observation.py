from dataclasses import dataclass


@dataclass
class Observation:
    """
    This is the agent's view of the world.
    Keep this SMALL and MEANINGFUL.
    """
    health: int       # 0 = dead, 5 = full
    is_grounded: bool
    horizontal_velocity: int   # -1 = left, 0 = idle, 1 = right
    time_since_damage: float
