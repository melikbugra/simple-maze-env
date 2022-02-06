import gym
from gym import error, spaces, utils
from gym.utils import seeding
import time


class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.safe_path = [(0, 0), (0, 1), (0, 2), (0, 3),
                          (1, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0)]
        self.cliffs = [(1, 0), (1, 1), (1, 2), (3, 1), (3, 2), (3, 3)]
        self.start_loc = self.safe_path[0]
        self.trm_loc = self.safe_path[9]
        self.agent_loc = ()
        self.num_states = len(self.safe_path) + len(self.cliffs)
        self.state = 0
        self.reward = 0
        self.done = False
        self.info = "Info"
        self.temp_loc = ()

    def get_state_no(self, loc):
        return 4 * loc[0] + loc[1]

    def step(self, action):
        if action == 0:  # up
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0] - 1, self.agent_loc[1])
            if possible_next_loc[0] >= 0:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = (1, 0)  # go to a cliff
        elif action == 1:  # left
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0], self.agent_loc[1] - 1)
            if possible_next_loc[1] >= 0:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = (1, 0)  # go to a cliff
        elif action == 2:  # down
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0] + 1, self.agent_loc[1])
            if possible_next_loc[0] < 4:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = (1, 0)  # go to a cliff
        elif action == 3:  # right
            self.temp_loc = self.agent_loc
            possible_next_loc = (self.agent_loc[0], self.agent_loc[1] + 1)
            if possible_next_loc[1] < 4:  # check the agent within grid?
                # if within grid, current location is possible location
                self.agent_loc = possible_next_loc
            else:
                self.agent_loc = (1, 0)  # go to a cliff

        self.reward = 0  # initiate self.reward as -1,agent gets a -1 self.reward for its every step in safe path,so it does not stuck
        self.done = False  # holds the termination information

        if self.agent_loc == self.trm_loc:  # check the self.done is reached?
            self.reward = 100  # give 100 self.reward if it terminates the episode
            self.done = True  # bool of termination is true
            
        # check fell into cliffs?
        elif self.agent_loc in self.cliffs or (possible_next_loc in self.cliffs or possible_next_loc not in self.safe_path):
            self.reward = -10  # give -100 self.reward if it falls into the cliffs
            self.done = False  # bool of termination is true
            self.agent_loc = self.start_loc  # agent is sent to start state
        else:
            self.reward = -1  # default value
            self.done = False  # default value

        self.state = self.get_state_no(self.agent_loc)

        return [self.state, self.reward, self.done, self.info]

    def reset(self):
        self. reward = 0
        # agentLoc is the current location of the agent
        self.agent_loc = self.start_loc
        # state is state number as an int
        self.state = self.get_state_no(self.agent_loc)
        self.done = False
        return [self.state, self.reward, self.done, self.info]

    def render(self, mode='human', close=False):
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
