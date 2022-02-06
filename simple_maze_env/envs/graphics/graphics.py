import pygame
import sys
import os
import os.path as path
from simple_maze_env.envs.graphics.agent_renderer import AgentRenderer


class VisualRenderer():
    def __init__(self, state):
        self.win = pygame.display.set_mode((800, 600))
        maze_file_path = path.dirname(path.abspath(__file__)) + '/images/maze.png'
        self.maze_background = pygame.image.load(maze_file_path)
        agent_file_path = path.dirname(path.abspath(__file__)) + '/images/agent.png'
        self.agent_image = pygame.image.load(agent_file_path)
        self.agent_renderer = AgentRenderer(self.win, self.agent_image)
        self.win.fill((64, 224, 208))
        self.win.blit(self.maze_background, (135, 35))
        self.agent_renderer.draw_agent(state)
        
    
    def render(self, state):
        pygame.display.set_caption("Simple Maze Environment")
        pygame.display.flip()
        self.win.fill((64, 224, 208))
        self.win.blit(self.maze_background, (135, 35))
        self.agent_renderer.draw_agent(state)
        


# class Py:
#     def __init__(self):
#         self.paused = True
#         self.stepper = False
#         self.trm = False
#         self.run = True
#         self.runall = True

#     def trainAgent(self, env, win, agent, qAgent, grid):
#         for i in range(5):
#             win.fill((64, 224, 208))
#             win.blit(grid, (135, 35))
#             agent.drawStt(stt)
#             pygame.display.flip()

#             win.fill((64, 224, 208))
#             win.blit(grid, (135, 35))
#             agent.drawStt(stt)
#             pygame.display.flip()
#             if env.dark:
#                 env.dark = False
#                 print("Fell into cliff!!")

#             print("State: ", stt, "\n")

#             while self.run and self.runall:
#                 if trm:
#                     self.paused = True

#                 pygame.time.delay(1)
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         self.run = False
#                         self.runall = False
#                         sys.exit()

#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_p:
#                             if self.paused:
#                                 self.paused = False
#                             elif not self.paused:
#                                 self.paused = True

#                         if event.key == pygame.K_SPACE:
#                             if self.stepper:
#                                 self.stepper = False
#                             if not self.stepper:
#                                 self.stepper = True

#                 if not self.paused or self.stepper:
#                     if self.trm:
#                         self.run = False

#                     act = qAgent.agent_step(rew, stt)
#                     if act == 0:
#                         actWord = "Up!"
#                     elif act == 1:
#                         actWord = "Left!"
#                     elif act == 2:
#                         actWord = "Down!"
#                     elif act == 3:
#                         actWord = "Right!"
#                     print("Action: ", actWord)

#                     rew, stt, self.trm = env.env_step(act)
#                     agent.drawStt(stt)
#                     if env.dark:
#                         env.dark = False
#                         # self.paused = True # This makes the agent paused at when it fell into cliff
#                         print("Fell into cliff!!")

#                     print("State: ", stt, "\n")

#                     if self.trm:
#                         # self.paused = True
#                         print("Termination, iteration number:", i + 1, "\n", "Step taken:", steps, "\n")

#                     win.fill((64, 224, 208))
#                     win.blit(grid, (135, 35))
#                     agent.drawStt(stt)
#                     pygame.display.flip()
#                     steps += 1
#                     self.stepper = False

#         # sys.exit(0)