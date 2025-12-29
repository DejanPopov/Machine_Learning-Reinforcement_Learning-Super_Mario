# Imports
import gym_super_mario_bros as mario
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Environment maps
mario_maps = {
    "level1": "SuperMarioBros-v0",
    "level2": "SuperMarioBros-v1",
    "level3": "SuperMarioBros-v2",
    "level4": "SuperMarioBros-v3",
    "level5": "SuperMarioBros2-v0",
    "level6": "SuperMarioBros2-v1",
}

# Setup environment
env = mario.make(mario_maps["level1"])
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# Environment retrun result
env.observation_space.shape # 240 X 256 pixels game
env.action_space # (7 actions => up.down.A,B, etc..)

done = True
tries = 10000

for step in range (tries):
    if done:
        env.reset()
