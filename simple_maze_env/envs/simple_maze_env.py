import gym
from gym import spaces
import numpy as np
import pygame
import os.path as path


# Define actions
ACTION_UP = 0
ACTION_DOWN = 1
ACTION_LEFT = 2
ACTION_RIGHT = 3

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SimpleMazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, maze: list[list[int]]=None, cell_size: int=None):
        super().__init__()

        if not maze:
            self.maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 9, 9, 9, 9, 9, 9, 9, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 0, 9, 0, 9, 9, 0, 9, 9, 0, 9, 9, 9, 0, 9],
    [9, 0, 9, 0, 0, 9, 0, 9, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 0, 9, 0, 9, 0, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 9],
    [9, 9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 0, 9, 0, 0, 0, 0, 0, 2, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 0, 9, 0, 9, 9, 9, 9, 9],
    [9, 0, 9, 9, 9, 9, 9, 0, 9, 0, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]
        else:
            self.maze = maze

        # Set the dimensions of the maze
        self.cell_size = 1000/len(self.maze[0])
        self.maze_width = 1000
        self.maze_height = 1000
        
        
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=2, shape=(len(self.maze), len(self.maze[0])), dtype=np.int32)
        
        self.agent_x = 1
        self.agent_y = 1
        self.max_steps = 100
        self.steps = 0
        self.finished = False

        agent_file_path = path.dirname(path.abspath(__file__)) + '/images/agent.png'
        
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
        self.agent_image = pygame.image.load(agent_file_path).convert_alpha()
        self.agent_image = pygame.transform.scale(self.agent_image, (self.cell_size, self.cell_size))
    
    def reset(self):
        self.agent_x = 1
        self.agent_y = 1
        self.steps = 0
        self.finished = False
        return self._get_observation()
    
    def step(self, action):
        self.steps += 1
        
        if action == ACTION_UP and self.maze[self.agent_y - 1][self.agent_x] not in [8, 9]:
            self.agent_y -= 1
        elif action == ACTION_DOWN and self.maze[self.agent_y + 1][self.agent_x] not in [8, 9]:
            self.agent_y += 1
        elif action == ACTION_LEFT and self.maze[self.agent_y][self.agent_x - 1] not in [8, 9]:
            self.agent_x -= 1
        elif action == ACTION_RIGHT and self.maze[self.agent_y][self.agent_x + 1] not in [8, 9]:
            self.agent_x += 1
        
        observation = self._get_observation()
        reward = self._get_reward()
        done = self._is_done()
        info = {}
        
        return observation, reward, done, info
    
    def render(self, mode='human'):
        # Clear the screen
        self.screen.fill(BLACK)
        
        # Draw the maze
        self._draw_maze()
        
        # Draw the agent
        self.screen.blit(self.agent_image, (self.agent_x * self.cell_size, self.agent_y * self.cell_size))
        
        # Update the display
        pygame.display.flip()
        
        # Limit the frame rate
        self.clock.tick(60)
    
    def _get_observation(self):
        return np.array(self.maze)
    
    def _get_reward(self):
        if self.maze[self.agent_y][self.agent_x] == 2:
            self.finished = True
            return 1.0
        else:
            return 0.0
    
    def _is_done(self):
        return self.finished or self.steps >= self.max_steps
    
    def _draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 1:  # Start cell
                    pygame.draw.rect(self.screen, GREEN, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze[y][x] == 2:  # Finish cell
                    pygame.draw.rect(self.screen, BLUE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze[y][x] == 8:  # Inner Walls
                    pygame.draw.rect(self.screen, RED, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze[y][x] == 9:  # Outer Walls
                    pygame.draw.rect(self.screen, BLACK, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:  # Paths
                    pygame.draw.rect(self.screen, WHITE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, BLUE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), 1)


if __name__ == "__main__":
    env = MazeEnv()

    obs = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.render()

    env.close()
