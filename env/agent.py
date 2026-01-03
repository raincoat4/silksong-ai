from action import ActionType
import random

class RandomAgent:

    def __init__(self):
        pass

    def act(self):
        return random.choice(list(ActionType))