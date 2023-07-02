import pygame

pygame.font.init()
# Game Variable
GAME_NAME = "Figther"
INTRO_COUNT = 3
LAST_COUNT_UPDATE = pygame.time.get_ticks()
# player score [p1, p2]
SCORE = [0, 0]
ROUND_OVER = False
ROUND_OVER_COOLDOWN = 2000

# Game Resolution with bg an FPS
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
FRAMERATE = 60
BG_IMAGE = "assets/images/background/background.jpg"

# COLORS
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Icons

VICTORY_IMG = "assets/images/icons/victory.png"

# FONT

COUNT_FONT = pygame.font.Font("assets/fonts/turok.ttf", 80)
SCORE_FONT = pygame.font.Font("assets/fonts/turok.ttf", 30)

# MuSIC AND SOUND

MUSIC = "assets/audio/music.mp3"
SWORD = "assets/audio/sword.wav"
MAGIC = "assets/audio/magic.wav"


# PLAYER assets, size and steps
WARRIOR = 'assets/images/warrior/Sprites/warrior.png'
WIZARD = 'assets/images/wizard/Sprites/wizard.png'
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
