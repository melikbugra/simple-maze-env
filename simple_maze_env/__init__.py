from gym.envs.registration import register

register(
    id='SimpleMaze-v0',
    entry_point='gym_foo.envs:FooEnv',
)