from gym.envs.registration import register

register(
    id='SimpleMaze-v0',
    entry_point='simple_maze_env.envs:SimpleMazeEnv',
)