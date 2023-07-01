import pygame

from Data.Screen import data


class Fighter():
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = False
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0:idle 1:run 2:jump 3:attack1 4:attack2 5:hit 6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * self.size, y * self.size, self.size, self.size)

                temp_img_list.append(pygame.transform.scale(
                    temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)

        # print(animation_list)
        return animation_list

    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # get pressed

        key = pygame.key.get_pressed()

        # can only perform other action of not currently attacking
        if self.attacking == False:

            # movement
            if key[pygame.K_LEFT]:
                dx = -SPEED

            if key[pygame.K_RIGHT]:
                dx = SPEED

            # jump
            if key[pygame.K_UP] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            # attack
            if key[pygame.K_q] or key[pygame.K_r]:
                self.attack(surface, target)
                # determine wichattack type used
                if key[pygame.K_q]:
                    self.attack_type = 1
                if key[pygame.K_r]:
                    self.attack_type = 2

        # apply gravity
        self.vel_y += GRAVITY

        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left

        if self.rect.right + dx > data.SCREEN_WIDTH:
            dx = data.SCREEN_WIDTH - self.rect.right

        if self.rect.bottom + dy > data.SCREEN_HEIGHT - 130:
            self.vel_y = 0
            self.jump = False
            dy = data.SCREEN_HEIGHT - 130 - self.rect.bottom

        # ensure player face each other

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

    # update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(
            self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (self.rect.x -
                     (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
