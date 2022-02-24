from numpy import dtype
import pygame
import numpy as np


class AgentRenderer:
    def __init__(self, win, agent_image):
        self.win = win
        self.agent_image = agent_image

    def draw_agent(self, stt):
        if stt == 0:
            self.win.blit(self.agent_image, (151.25, 51.25))
        if stt == 1:
            self.win.blit(self.agent_image, (283.75, 51.25))
        if stt == 2:
            self.win.blit(self.agent_image, (416.25, 51.25))
        if stt == 3:
            self.win.blit(self.agent_image, (548.75, 51.25))
        if stt == 4:
            self.win.blit(self.agent_image, (151.25, 183.75))
        if stt == 5:
            self.win.blit(self.agent_image, (283.75, 183.75))
        if stt == 6:
            self.win.blit(self.agent_image, (416.25, 183.75))
        if stt == 7:
            self.win.blit(self.agent_image, (548.75, 183.75))
        if stt == 8:
            self.win.blit(self.agent_image, (151.25, 316.25))
        if stt == 9:
            self.win.blit(self.agent_image, (283.75, 316.25))
        if stt == 10:
            self.win.blit(self.agent_image, (416.25, 316.25))
        if stt == 11:
            self.win.blit(self.agent_image, (548.75, 316.25))
        if stt == 12:
            self.win.blit(self.agent_image, (151.25, 448.75))
        if stt == 13:
            self.win.blit(self.agent_image, (283.75, 316.25))
        if stt == 14:
            self.win.blit(self.agent_image, (416.25, 316.25))
        if stt == 15:
            self.win.blit(self.agent_image, (548.75, 316.25))
