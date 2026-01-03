from action import Action, ActionType, ACTION_SPACE
from observation import Observation
import pyautogui
import time

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
        pyautogui.keyDown("z")
        time.sleep(0.5)
        pyautogui.keyUp("z")
        pass

    def _jump_left(self):
        pyautogui.keyDown("z")
        pyautogui.keyDown("left")
        time.sleep(0.5)
        pyautogui.keyUp("z")
        pyautogui.keyUp("left")
        pass

    def _jump_right(self):
        pyautogui.keyDown("z")
        pyautogui.keyDown("right")
        time.sleep(0.5)
        pyautogui.keyUp("z")
        pyautogui.keyUp("right")
        pass

    def _move_left(self):
        pyautogui.keyDown("left")
        time.sleep(0.5)
        pyautogui.keyUp("left")
        pass

    def _move_right(self):
        pyautogui.keyDown("right")
        time.sleep(0.5)
        pyautogui.keyUp("right")
        pass

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
    