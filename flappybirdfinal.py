import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *
from pygame import mixer

FPS = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WIN_WIDTH = 284 * 2     # BG image size: 284x512 px; tiled twice
WIN_HEIGHT = 512