import gym
from gym import spaces
import numpy as np
import pygame
import os.path as path
from copy import deepcopy


# Define actions
ACTION_UP = 0
ACTION_LEFT = 1
ACTION_DOWN = 2
ACTION_RIGHT = 3

MAX_SIZE = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, maze: list[list[int]]=None, cell_size: int=None, max_steps: int=200):
        super().__init__()

        if not maze:
            self.maze = [
                [9, 9, 9, 9, 9, 9],
                [9, 1, 0, 0, 0, 9],
                [9, 8, 8, 8, 0, 9],
                [9, 0, 0, 0, 0, 9],
                [9, 2, 9, 8, 9, 9],
                [9, 9, 9, 9, 9, 9]
            ]
        else:
            try:
                maze_np = np.array(maze)
            except:
                raise ValueError("Provide a valid maze!")

            if maze_np.shape[0] > MAX_SIZE or maze_np.shape[1] > MAX_SIZE:
                raise ValueError("Provide a valid maze (max size = 30)!")
            self.maze = maze

        # Set the dimensions of the maze
        if not cell_size:
            self.cell_size = 512/len(self.maze[0])
        else:
            self.cell_size = cell_size
        self.maze_width = len(self.maze[0])*self.cell_size
        self.maze_height = len(self.maze)*self.cell_size
        
        
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=2, shape=(2, len(self.maze), len(self.maze[0])), dtype=np.int32)
        
        self.agent_x = 1
        self.agent_y = 1
        self.max_steps = max_steps
        self.steps = 0
        self.finished = False

        self.pygame_init_switch = 0
        
    
    def reset(self):
        self.agent_x = 1
        self.agent_y = 1
        self.steps = 0
        self.finished = False
        return self._get_observation()
    
    def step(self, action):
        self.steps += 1
        
        if action == ACTION_UP and self.maze[self.agent_y - 1][self.agent_x] != 9:
            self.agent_y -= 1
        elif action == ACTION_DOWN and self.maze[self.agent_y + 1][self.agent_x] != 9:
            self.agent_y += 1
        elif action == ACTION_LEFT and self.maze[self.agent_y][self.agent_x - 1] != 9:
            self.agent_x -= 1
        elif action == ACTION_RIGHT and self.maze[self.agent_y][self.agent_x + 1] != 9:
            self.agent_x += 1
        
        observation = self._get_observation()
        reward = self._get_reward()
        done = self._is_done()
        info = {}
        
        return observation, reward, done, info
    
    def render(self, mode='human'):
        if self.pygame_init_switch == 0:
            self.agent_file_path = path.dirname(path.abspath(__file__)) + '/images/agent.png'
            self.start_file_path = path.dirname(path.abspath(__file__)) + '/images/start.png'
            self.finish_file_path = path.dirname(path.abspath(__file__)) + '/images/finish.png'
            self.wolf_file_path = path.dirname(path.abspath(__file__)) + '/images/wolf.png'
            # Initialize Pygame
            pygame.init()
            
            # Set up the screen
            self.screen = pygame.display.set_mode((self.maze_width, self.maze_height))
            pygame.display.set_caption("Maze Game")
            
            # Set up clock for frame rate
            self.clock = pygame.time.Clock()
            
            # Set up font for rendering text
            self.font = pygame.font.SysFont(None, 36)
            
            # Load the agent image
            self.agent_image = pygame.image.load(self.agent_file_path).convert_alpha()
            self.agent_image = pygame.transform.scale(self.agent_image, (self.cell_size, self.cell_size))
            # Load the start image
            self.start_image = pygame.image.load(self.start_file_path).convert_alpha()
            self.start_image = pygame.transform.scale(self.start_image, (self.cell_size, self.cell_size))
            # Load the finish image
            self.finish_image = pygame.image.load(self.finish_file_path).convert_alpha()
            self.finish_image = pygame.transform.scale(self.finish_image, (self.cell_size, self.cell_size))
            # Load the wolf image
            self.wolf_image = pygame.image.load(self.wolf_file_path).convert_alpha()
            self.wolf_image = pygame.transform.scale(self.wolf_image, (self.cell_size, self.cell_size))
            # Clear the screen
            self.screen.fill(BLACK)
            self.pygame_init_switch = 1
        
        # Draw the maze
        self._draw_maze()
        
        # Draw the agent
        self.screen.blit(self.agent_image, (self.agent_x * self.cell_size, self.agent_y * self.cell_size))
        
        # Update the display
        pygame.display.flip()
        
        # Limit the frame rate
        self.clock.tick(60)
    
    def _get_observation(self):
        agent_grid = np.zeros(np.array(self.maze).shape)
        agent_grid[self.agent_y][self.agent_x] = 1
        return np.array([self.maze, agent_grid])
    
    def _get_reward(self):
        if self.maze[self.agent_y][self.agent_x] == 2:
            self.finished = True
            return np.prod(np.array(self.maze).shape) + self.max_steps
        elif self.maze[self.agent_y][self.agent_x] == 8: # Fallen into cliff
            self.finished = True
            return -np.prod(np.array(self.maze).shape) - self.max_steps*2
        else:
            return -1.0
    
    def _is_done(self):
        return self.finished or self.steps >= self.max_steps
    
    def _draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 1:  # Start cell
                    pygame.draw.rect(self.screen, WHITE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    self.screen.blit(self.start_image, (x * self.cell_size, y * self.cell_size))
                elif self.maze[y][x] == 2:  # Finish cell
                    pygame.draw.rect(self.screen, WHITE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    self.screen.blit(self.finish_image, (x * self.cell_size, y * self.cell_size))
                elif self.maze[y][x] == 8:  # Wolfs
                    pygame.draw.rect(self.screen, RED, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    self.screen.blit(self.wolf_image, (x * self.cell_size, y * self.cell_size))
                elif self.maze[y][x] == 9:  # Outer Walls
                    pygame.draw.rect(self.screen, BLACK, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:  # Paths
                    pygame.draw.rect(self.screen, WHITE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, BLUE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), 1)


if __name__ == "__main__":
    env = SimpleMazeEnv()

    obs = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.render()

    env.close()
