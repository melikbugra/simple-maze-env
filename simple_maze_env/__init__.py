from gym.envs.registration import register

register(
    id='SimpleMaze-v1',
    entry_point='simple_maze_env.envs:SimpleMazeEnv',
)