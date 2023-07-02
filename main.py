import pygame
from pygame import mixer

from Data.Screen import data
from Data.Fighter.fighter import Fighter

pygame.init()
mixer.init()

screen = pygame.display.set_mode((data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
pygame.display.set_caption(data.GAME_NAME)

# set framrate
clock = pygame.time.Clock()

# load music and sound

pygame.mixer.music.load(data.MUSIC)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

sword_fx = pygame.mixer.Sound(data.SWORD)
sword_fx.set_volume(0.5)

magic_fx = pygame.mixer.Sound(data.MAGIC)
magic_fx.set_volume(0.75)

# load bg image
bg_image = pygame.image.load(data.BG_IMAGE).convert_alpha()

# load sprite sheets
warrior_sheet = pygame.image.load(data.WARRIOR).convert_alpha()
wizard_sheet = pygame.image.load(data.WIZARD).convert_alpha()

# load victory img
victory_img = pygame.image.load(data.VICTORY_IMG).convert_alpha()

# join Font


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)

    screen.blit(img, (x, y))


# function for join bg
def draw_bg():
    scaled_bg = pygame.transform.scale(
        bg_image, (data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function health bar
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, data.WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, data.RED, (x, y, 400, 30))
    pygame.draw.rect(screen, data.YELLOW, (x, y, 400 * ratio, 30))

 # check for player defeat


def count():
    if data.INTRO_COUNT <= 0:
        # move fighters
        fighter_1.move(fighter_2)
        fighter_2.move(fighter_1)
    else:
        # display count timer
        draw_text(str(data.INTRO_COUNT), data.COUNT_FONT,
                  data.RED, data.SCREEN_WIDTH / 2, data.SCREEN_HEIGHT / 3)
        # update count timer
        if (pygame.time.get_ticks() - data.LAST_COUNT_UPDATE) >= 1000:
            data.INTRO_COUNT -= 1
            data.LAST_COUNT_UPDATE = pygame.time.get_ticks()


#  create an instance of fighters
fighter_1 = Fighter(1, 200, 410, False, data.WARRIOR_DATA,
                    warrior_sheet, data.WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 410, True, data.WIZARD_DATA,
                    wizard_sheet, data.WIZARD_ANIMATION_STEPS, magic_fx)

# game loop
run = True
while True:

    clock.tick(data.FRAMERATE)

    draw_bg()

    # SHow player Health
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 660, 20)
    draw_text("P1: " + str(data.SCORE[0]), data.SCORE_FONT, data.RED, 20, 60)
    draw_text("P2: " + str(data.SCORE[1]), data.SCORE_FONT, data.RED, 660, 60)

    # update countdown
    count()

    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    if data.ROUND_OVER == False:
        if fighter_1.alive == False:
            data.SCORE[1] += 1
            data.ROUND_OVER = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            data.SCORE[0] += 1
            data.ROUND_OVER = True
            round_over_time = pygame.time.get_ticks()
            print(data.SCORE)
    else:
        # display victory img
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > data.ROUND_OVER_COOLDOWN:
            data.ROUND_OVER = False
            data.INTRO_COUNT = 3
            fighter_1 = Fighter(1, 200, 410, False, data.WARRIOR_DATA,
                                warrior_sheet, data.WARRIOR_ANIMATION_STEPS, sword_fx)
            fighter_2 = Fighter(2, 700, 410, True, data.WIZARD_DATA,
                                wizard_sheet, data.WIZARD_ANIMATION_STEPS, magic_fx)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
# update display
pygame.quit()
