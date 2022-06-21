import gym
from gym import error, spaces, utils
from gym.utils import seeding
import time
import sys
from simple_maze_env.envs.graphics.graphics import VisualRenderer
import numpy as np

class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['cli', 'graphics']}

    def __init__(self):
        self.safe_path = [(0, 0), (0, 1), (0, 2), (0, 3),
                          (1, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0)]
        self.cliffs = [(1, 0), (1, 1), (1, 2), (3, 1), (3, 2), (3, 3)],
        low = np.array([0, 0], dtype=np.float32)
        high = np.array([3, 3], dtype=np.float32)
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low, high, dtype=np.float32)
        self.start_loc = self.safe_path[0]
        self.trm_loc = self.safe_path[9]
        self.agent_loc = ()
        self.num_states = len(self.safe_path) + len(self.cliffs)
        self.state = self.observation_space.low
        self.reward = 0
        self.done = False
        self.info = "Info"
        self.temp_loc = ()
        self.config = {"sleep": 1}
        self.length = 0

    def get_state_no(self, loc):
        return 4 * loc[0] + loc[1]

    def step(self, action):
        self.length += 1
        if action == 0:  # up
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0] - 1, self.agent_loc[1])
            if possible_next_loc[0] >= 0:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = self.temp_loc
        elif action == 1:  # left
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0], self.agent_loc[1] - 1)
            if possible_next_loc[1] >= 0:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = self.temp_loc
        elif action == 2:  # down
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0] + 1, self.agent_loc[1])
            if possible_next_loc[0] < 4:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = self.temp_loc
        elif action == 3:  # right
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0], self.agent_loc[1] + 1)
            if possible_next_loc[1] < 4:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = self.temp_loc

        self.reward = -10  # initiate self.reward as -1,agent gets a -1 self.reward for its every step in safe path,so it does not stuck
        self.done = False  # holds the termination information

        if self.agent_loc == self.trm_loc:  # check the self.done is reached?
            self.reward = 100000  # give 100 self.reward if it terminates the episode
            self.done = True  # bool of termination is true
            self.agent_loc = self.start_loc  # agent is sent to start state
            
        # check fell into cliffs?
        elif self.agent_loc in self.cliffs or (possible_next_loc in self.cliffs or possible_next_loc not in self.safe_path) or self.length >= 30:
            self.reward = -100  # give -100 self.reward if it falls into the cliffs
            if self.length >= 300:
                self.done = True
            else:
                self.done = False  # bool of termination is true
            self.agent_loc = self.temp_loc  # agent is sent to start state
            
        else:
            self.reward = -10  # default value
            self.done = False  # default value

        self.state = np.array(self.agent_loc, dtype=np.float32)

        return [self.state, self.reward, self.done, self.info]

    def reset(self):
        self.length = 0
        self. reward = 0
        # agentLoc is the current location of the agent
        self.agent_loc = self.start_loc
        # state is state number as an int
        self.state = np.array(self.agent_loc, dtype=np.float32)
        self.done = False
        return self.state

    def render(self, mode='cli', close=False):
        if mode=='cli':
            maze = [[".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ".", ".", "."]]

            def reset_maze():
                for safe in self.safe_path:
                    maze[safe[0]][safe[1]] = "-"

                for cliff in self.cliffs:
                    maze[cliff[0]][cliff[1]] = "X"

            reset_maze()

            maze[self.agent_loc[0]][self.agent_loc[1]] = "O"

            for k in range(4):
                print(maze[k])
            print("\n")
            time.sleep(1)
        elif mode=='graphics':
            self.visualiser = VisualRenderer(self.state)
            self.visualiser.render(self.state)
            time.sleep(self.config["sleep"])
            

