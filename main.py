import pygame

from Data.Screen import data
from Data.Fighter.fighter import Fighter

pygame.init()

screen = pygame.display.set_mode((data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
pygame.display.set_caption(data.GAME_NAME)

# set framrate
clock = pygame.time.Clock()


# load bg image

bg_image = pygame.image.load(data.BG_IMAGE).convert_alpha()

# load sprite sheets
warrior_sheet = pygame.image.load(data.WARRIOR).convert_alpha()
wizard_sheet = pygame.image.load(data.WIZARD).convert_alpha()


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


#  create an instance of fighters
fighter_1 = Fighter(200, 410, data.WARRIOR_DATA,
                    warrior_sheet, data.WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 410, data.WIZARD_DATA,
                    wizard_sheet, data.WIZARD_ANIMATION_STEPS)

# game loop
run = True
while True:

    clock.tick(data.FRAMERATE)

    draw_bg()

    # SHow player Health
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 660, 20)

    # move fighters
    fighter_1.move(screen, fighter_2)
    # fighter_2.move()

    # draw fighter

    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
# update display


pygame.quit()
