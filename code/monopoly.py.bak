import pygame
import os
from os.path import join
import random 

pygame.display.set_caption("Politician Monopoly")

class Space(pygame.sprite.Sprite):
    def __init__(self, groups, image, location, position):
        super().__init__(groups)
        self.image = image
        self.rect = location
        self.postion = position

    def get_position(self):
        return self.postion

class AnimatedDice(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups, dice_timer, roll_index):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=pos)
        self.dice_timer = dice_timer

    def update(self, dt):
        self.frame_index += 9 * dt 
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
            self.rect.centery += -100 * dt
            if self.frame_index > 5:
                self.rect.centery += 200 * dt
        
        else:
            self.kill()
            roll = random.randint(0, 5)
            self.dice_timer(roll) 
            
class Player(pygame.sprite.Sprite):
    def __init__(self, groups, hat):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', hat)).convert_alpha()
        self.rect = self.image.get_frect(center = (355, 80))
        self.speed = 200
        self.target_position = self.rect.center
        self.traveling = False 
        self.space_location = 0
        self.top_right = False
        self.bottom_right = False
        self.bottom_left = False
        self.top_left = False


    def update(self, dt):  
        if self.traveling:
            target_x, target_y = self.target_position
            direction = pygame.math.Vector2(int(target_x) - int(self.rect.centerx), int(target_y) - int(self.rect.centery))
            if direction.length() > 1:
                direction.normalize_ip()
                if self.top_right:
                    direction.x = 1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx >= target_x:
                        self.top_right = False

                elif self.bottom_right:
                    direction.y = 1
                    direction.x = 0
                    self.rect.centery += direction.y * self.speed * dt
                    if self.rect.centery >= target_y:
                        self.bottom_right = False

                elif self.bottom_left:
                    direction.x = -1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx <= target_x:
                        self.bottom_left = False

                elif self.top_left:
                    direction.y = -1
                    direction.x = 0
                    self.rect.centery += direction.y * self.speed * dt
                    if self.rect.centery <= target_y:
                        self.top_left = False
                        redo = False
                else:
                    self.rect.centerx += direction.x * self.speed * dt
                    self.rect.centery += direction.y * self.speed * dt
            else:
                self.traveling = False  # Stop moving once we reach the target

    def move_to_square(self, space_position):
        if space_position[0] > 920:
            self.top_right = True
        elif space_position[1] > 635:
            self.bottom_right = True
        elif space_position[0] < 360 and 100 < space_position[1] < 635:
            self.bottom_left = True
        elif redo:
            self.top_left = True
        else:
            self.top_right = False
            self.bottom_right = False
            self.bottom_left = False
            self.top_left = False
        self.target_position = space_position
        self.traveling = True
        
def dice_timer(roll):
    global dice_rolling, dice, last_roll, rolls, redo
    dice_rolling = True
    dice = True
    last_roll = roll
    rolls += roll + 1
    if rolls > 23:
        redo = True 
        rolls -= 24
    print(rolls, (all_spaces.sprites()[rolls]).get_position())
    player.move_to_square((all_spaces.sprites()[rolls]).get_position()) 
    
def variable_setup():
    global player, spots

    spots = []
    spots_rects = []

    go_surf = pygame.image.load(join('images', 'spaces' ,'go.png')).convert_alpha()
    go_rect = go_surf.get_frect(topleft = (288, 10))
    go = Space(all_spaces, go_surf, go_rect, (350, 80))

    for i in range(5):
        if i == 3 or 4:
            num = 89
        else:
            num = 90
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots_rects.append(spots[i].get_frect(topleft = ((398 + num*i), 10)))
        Space(all_spaces, spots[i], spots_rects[i], (460+90*i, 80))

    free_perk_surf = pygame.image.load(join('images', 'spaces' ,'free_perk.png')).convert_alpha()
    free_perk_rect = go_surf.get_frect(topleft = (861, 10))
    free_perk = Space(all_spaces, free_perk_surf, free_perk_rect, (925, 80))

    for i in range(5, 10):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots[i] = pygame.transform.rotate(spots[i], 270)
        spots_rects.append(spots[i].get_frect(topleft = (861, 120 + 89*(i-5))))
        Space(all_spaces, spots[i], spots_rects[i], (925, 185 + 90*(i-5)))

    go1_surf = pygame.image.load(join('images', 'spaces' ,'+1_go.png')).convert_alpha()
    go1_rect = go_surf.get_frect(topleft = (861, 580))
    go1 = Space(all_spaces, go1_surf, go1_rect, (925, 640))

    for i in range (10, 15):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots_rects.append(spots[i].get_frect(topleft = (752 - 89*(i-10), 580)))
        Space(all_spaces, spots[i], spots_rects[i], (815 - 90*(i-10), 640))

    go3_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go3_rect = go_surf.get_frect(topleft = (288, 580))
    go3 = Space(all_spaces, go3_surf, go3_rect, (350, 640))

    for i in range (15, 20):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots[i] = pygame.transform.rotate(spots[i], 90)
        spots_rects.append(spots[i].get_frect(topleft = (288, 470 - 89*(i-15))))
        Space(all_spaces, spots[i], spots_rects[i], (355, 535- 90*(i-15)))


    player = Player(all_sprites, hat)

pygame.init()
pygame.font.init()
# Setup 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()
middle = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
dice_rolling = True
dice = True
last_roll = 0
rolls = 0
redo = False
class_select = True
colour = "deepskyblue3"

liberal_surf = pygame.image.load(join('images', 'liberal.png')).convert_alpha()
liberal_rect = liberal_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

labor_surf = pygame.image.load(join('images', 'labor.png')).convert_alpha()
labor_rect = labor_surf.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2))

greens_surf = pygame.image.load(join('images', 'greens.png')).convert_alpha()
greens_rect = greens_surf.get_frect(center = (WINDOW_WIDTH * 0.75, WINDOW_HEIGHT / 2))

while class_select:
   
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            class_select = False
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if labor_rect.collidepoint(event.pos):
                hat = 'player_red.png'
                class_select = False
            if liberal_rect.collidepoint(event.pos):
                hat = 'player_blue.png'
                class_select = False
            if greens_rect.collidepoint(event.pos):
                hat = 'player_green.png'
                class_select = False

 


    screen.fill(colour)
    screen.blit(liberal_surf, liberal_rect)
    screen.blit(labor_surf, labor_rect)
    screen.blit(greens_surf, greens_rect)


    pygame.display.update()


roll_button = pygame.FRect(80, WINDOW_HEIGHT - 130, 170, 80)

font = pygame.font.Font('Pixel.ttf')
text = font.render('PRESS TO ROLL', False, 0)
text_rect = text.get_rect()

board_surf = pygame.Surface((703, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dices = [pygame.image.load(join('images', 'dice', f'dice{i}.png')).convert_alpha() for i in range(1, 7)]
dice_rect = dices[1].get_frect(center = middle)

all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

variable_setup()

roll_frames = [pygame.image.load(join('images', 'dice', 'roll',  f'{i}.png')).convert_alpha() for i in range(0, 8)]

while running:
    dt = clock.tick(60) / 1000

    # Event loops
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            running = False
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                if dice_rolling:
                    dice = False
                    AnimatedDice(roll_frames, middle, all_sprites, dice_timer, last_roll)
                    dice_rolling = False


    # Update sprites
    all_sprites.update(dt)

    # Drawing
    screen.fill('plum1')


    shadow_offset = 4
    shadow_rect = roll_button.move(shadow_offset, shadow_offset)
    pygame.draw.rect(screen, (180, 180, 180), shadow_rect, border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), roll_button, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), roll_button, width=3, border_radius=10)
    screen.blit(text, (roll_button.centerx - text_rect.width // 2, roll_button.centery - text_rect.height // 2))

    if dice:
        screen.blit(dices[last_roll], dice_rect)

    all_spaces.draw(screen) 
    all_sprites.draw(screen)

    pygame.display.update()
pygame.font.quit()
pygame.quit()
