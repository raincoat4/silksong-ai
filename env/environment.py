from action import Action, ActionType, ACTION_SPACE
from observation import Observation
import control.control_service as control

class SilksongEnv:
    def __init__(self):
        self.action_handlers = {
            ActionType.JUMP : self._jump,
            ActionType.JUMP_LEFT : self._jump_left,
            ActionType.JUMP_RIGHT : self._jump_right,
            ActionType.MOVE_LEFT : self._move_left,
            ActionType.MOVE_RIGHT : self._move_right,
            ActionType.NO_OP : self._no_op
        }
    
    def _jump(self):
        control.jump()

    def _jump_left(self):
        control.jump_left()

    def _jump_right(self):
        control.jump_right()

    def _move_left(self):
        control.move_left()

    def _move_right(self):
        control.move_right()

    def _no_op(self):
        pass

    def _execute_action(self, action):
        handler = self.action_handlers[action.action_type]
        if handler:
            handler()
        else:
            raise ValueError
    
    def _get_observation(self) -> Observation:
        pass
    
    def step(self, action_type: ActionType):
        action = ACTION_SPACE[action_type]
        self._execute_action(action)
    