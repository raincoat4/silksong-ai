from enum import Enum
from dataclasses import dataclass

class ActionType(Enum):
    """
    This enum defines ALL actions the agent can choose from.
    The agent never presses keys directly.
    """
    NO_OP = 0
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    JUMP = 3
    JUMP_LEFT = 4
    JUMP_RIGHT = 5


@dataclass(frozen=True)
class Action:
    """
    This describes what an action actually does.
    It is IMMUTABLE so actions can't change mid-execution.
    """
    action_type: ActionType
    duration_ms: int          # How long the action lasts
    description: str

ACTION_SPACE = {
    ActionType.NO_OP: Action(
        action_type=ActionType.NO_OP,
        duration_ms=100,
        description="Do nothing"
    ),

    ActionType.MOVE_LEFT: Action(
        action_type=ActionType.MOVE_LEFT,
        duration_ms=100,
        description="Move left"
    ),

    ActionType.MOVE_RIGHT: Action(
        action_type=ActionType.MOVE_RIGHT,
        duration_ms=100,
        description="Move right"
    ),

    ActionType.JUMP: Action(
        action_type=ActionType.JUMP,
        duration_ms=50,
        description="Jump"
    ),

    ActionType.JUMP_LEFT: Action(
        action_type=ActionType.JUMP_LEFT,
        duration_ms=100,
        description="Jump while moving left"
    ),

    ActionType.JUMP_RIGHT: Action(
        action_type=ActionType.JUMP_RIGHT,
        duration_ms=100,
        description="Jump while moving right"
    ),
}
