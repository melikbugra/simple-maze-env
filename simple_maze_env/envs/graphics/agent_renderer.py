from numpy import dtype
import pygame
import numpy as np


class AgentRenderer:
    def __init__(self, win, agent_image):
        self.win = win
        self.agent_image = agent_image

    def draw_agent(self, stt):
        if list(map(int, stt)) == [0, 0]:
            self.win.blit(self.agent_image, (151.25, 51.25))
        if list(map(int, stt)) == [0, 1]:
            self.win.blit(self.agent_image, (283.75, 51.25))
        if list(map(int, stt)) == [0, 2]:
            self.win.blit(self.agent_image, (416.25, 51.25))
        if list(map(int, stt)) == [0, 3]:
            self.win.blit(self.agent_image, (548.75, 51.25))
        if list(map(int, stt)) == [1, 0]:
            self.win.blit(self.agent_image, (151.25, 183.75))
        if list(map(int, stt)) == [1, 1]:
            self.win.blit(self.agent_image, (283.75, 183.75))
        if list(map(int, stt)) == [1, 2]:
            self.win.blit(self.agent_image, (416.25, 183.75))
        if list(map(int, stt)) == [1, 3]:
            self.win.blit(self.agent_image, (548.75, 183.75))
        if list(map(int, stt)) == [2, 0]:
            self.win.blit(self.agent_image, (151.25, 316.25))
        if list(map(int, stt)) == [2, 1]:
            self.win.blit(self.agent_image, (283.75, 316.25))
        if list(map(int, stt)) == [2, 2]:
            self.win.blit(self.agent_image, (416.25, 316.25))
        if list(map(int, stt)) == [2, 3]:
            self.win.blit(self.agent_image, (548.75, 316.25))
        if list(map(int, stt)) == [3, 0]:
            self.win.blit(self.agent_image, (151.25, 448.75))
        if list(map(int, stt)) == [3, 1]:
            self.win.blit(self.agent_image, (283.75, 316.25))
        if list(map(int, stt)) == [3, 2]:
            self.win.blit(self.agent_image, (416.25, 316.25))
        if list(map(int, stt)) == [3, 3]:
            self.win.blit(self.agent_image, (548.75, 316.25))
