from environment import SilksongEnv    
from agent import RandomAgent

env = SilksongEnv()
agent = RandomAgent()

while True:
    action = agent.act()

    env.step(action)
    print(action)