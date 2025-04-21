
import pygame
import os
from os.path import join
import random
import sys

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
            self.dice_timer(roll,Votes)
           
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','player.png')).convert_alpha()
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
       
def dice_timer(roll,Votes):
    global dice_rolling, dice, last_roll, rolls, redo
    dice_rolling = True
    dice = True
    last_roll = roll
    rolls += roll + 1  
    if rolls > 23:
        redo = True
        Votes = Votes + 20
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

    go1_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go1_rect = go_surf.get_frect(topleft = (861, 10))
    go1 = Space(all_spaces, go1_surf, go1_rect, (925, 80))

    for i in range(5, 10):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots[i] = pygame.transform.rotate(spots[i], 270)
        spots_rects.append(spots[i].get_frect(topleft = (861, 120 + 89*(i-5))))
        Space(all_spaces, spots[i], spots_rects[i], (925, 185 + 90*(i-5)))

    go2_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go2_rect = go_surf.get_frect(topleft = (861, 580))
    go2 = Space(all_spaces, go2_surf, go2_rect, (925, 640))

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


    player = Player(all_sprites)


   
pygame.init()
pygame.font.init()
# Setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Running = True
clock = pygame.time.Clock()
middle = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
dice_rolling = True
dice = True
last_roll = 0
rolls = 0
redo = False
Influence_points = 1500
property_cost = 0
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
height = 720
width = 1280
ROI = 0
global Brooky,Manly_Vale,Belrose,Terry_Hills,Dee_Why,Cromer,Forest,Alambie,Beacon_Hill,Sea_Forth,Curly,Freshy,Manly
Brooky = False
Manly_Vale = False
Belrose = False
Terry_Hills = False
Dee_Why = False
Cromer = False
Forest = False
Alambie = False
Beacon_Hill = False
Sea_Forth = False
Curly = False
Freshy = False
Manly = False
Votes = 0
houses = [1,2,4,5,7,10,11,13,14,16,19,20,22]
other = [0,3,6,8,9,12,15,17,18,21,23,24]
roll_button = pygame.Rect(50, WINDOW_HEIGHT - 130, 180, 80)
running = True
font = pygame.font.Font('Pixel.ttf')
text = font.render('PRESS TO ROLL', False, color)
text_rect = text.get_rect()

board_surf = pygame.Surface((703, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dices = [pygame.image.load(join('images', 'dice', f'dice{i}.png')).convert_alpha() for i in range(1, 7)]
dice_rect = dices[1].get_frect(center = middle)
properties_title = font.render('Properties Owned:' , True , color)
all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

Brooky_text = font.render('Brooky', False, (150,75,0))
Manly_Vale_text = font.render('Manly Vale', False, (150,75,0))
Belrose_text = font.render('Belrose', False, (100,216,255))
Terry_Hills_text = font.render('Terry Hills', False, (100,216,255))
Dee_Why_text = font.render('Dee Why', False, (255,165,0))
Cromer_text = font.render('Cromer', False, (255,192,240))
Forest_text = font.render('Forest', False, (255,192,240))
Alambie_text = font.render('Alambie', False, (255,0,0))
Beacon_Hill_text = font.render('Beacon Hill', False, (255,0,0))
Sea_Forth_text = font.render('Sea Forth', False, (255,215,0))
Curly_text = font.render('Curly', False, (160,140,255))
Freshy_text = font.render('Freshy', False, (160,140,255))
Manly_text = font.render('Manly', False, (0,0,255))

variable_setup()

roll_frames = [pygame.image.load(join('images', 'dice', 'roll',  f'{i}.png')).convert_alpha() for i in range(0, 8)]
buy_text = font.render('Buy Property: $'+ str(property_cost) , True , color)
while Running:
    dt = clock.tick(60) / 1000
    mouse = pygame.mouse.get_pos()
    Total_ROI_text = font.render('Total ROI: '+ str(ROI) , True , color)
    votes_text = font.render('Votes: '+ str(Votes) , True , color)
    influence_text = font.render('Influence Points: '+ str(Influence_points) , True , color)
   
    # Event loops
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            Running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width - 1230 <= mouse[0] <= width - 1050 and height - 130 <= mouse[1] <= height - 50:
                if dice_rolling:
                    dice = False
                    AnimatedDice(roll_frames, middle, all_sprites, dice_timer, last_roll)
                    dice_rolling = False
         #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            if width - 1230 <= mouse[0] <= width - 1050 and height - 230 <= mouse[1] <= height - 120:
                    if rolls == 1:
                        property_cost = 10
                        if Influence_points >= property_cost:
                            if Brooky == False:
                                Brooky = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
           
                    if rolls == 2:
                        property_cost = 10
                        if Influence_points >= property_cost:
                            if Manly_Vale == False:
                                Manly_Vale = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 4:
                        property_cost = 30
                        if Influence_points >= property_cost:
                            if Belrose == False:
                                Belrose = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 5:
                        property_cost = 40
                        if Influence_points >= property_cost:
                            if Terry_Hills == False:
                                Terry_Hills = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 7:
                        property_cost = 60
                        if Influence_points >= property_cost:
                            if Dee_Why == False:
                                Dee_Why = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 10:
                        property_cost = 80
                        if Influence_points >= property_cost:
                            if Cromer == False:
                                Cromer = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 11:
                        property_cost = 90
                        if Influence_points >= property_cost:
                            if Forest == False:
                                Forest = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 13:
                        property_cost = 110
                        if Influence_points >= property_cost:
                            if Alambie == False:
                                Alambie = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 14:
                        property_cost = 120
                        if Influence_points >= property_cost:
                            if Beacon_Hill == False:
                                Beacon_Hill = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 16:
                        property_cost = 130
                        if Influence_points >= property_cost:
                            if Sea_Forth == False:
                                Sea_Forth = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 19:
                        property_cost = 140
                        if Influence_points >= property_cost:
                            if Curly == False:
                                Curly = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 20:
                        property_cost = 140
                        if Influence_points >= property_cost:
                            if Freshy == False:
                                Freshy = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1
                    if rolls == 22:
                        property_cost = 150
                        if Influence_points >= property_cost:
                            if Manly == False:
                                Manly = True
                                Influence_points = Influence_points - property_cost
                                property_cost = -1

                   
               

    # Update sprites
    all_sprites.update(dt)

    # Drawing
    screen.fill('#892bad')
    pygame.draw.rect(screen,0,[10,height - 710,270,440])
    pygame.draw.rect(screen,0,[width - 280,height - 710,270,700])
    screen.blit(votes_text,(20,height - 700))
    screen.blit(influence_text,(20,height - 680))
    if width - 1230 <= mouse[0] <= width - 1050 and height - 230 <= mouse[1] <= height - 150:
        pygame.draw.rect(screen,color_light,[50,height - 230,180,80])

    else:
        pygame.draw.rect(screen,color_dark,[50,height - 230,180,80])
       
    if width - 1230 <= mouse[0] <= width - 1050 and height - 130 <= mouse[1] <= height - 50:
        pygame.draw.rect(screen,color_light, roll_button)
    else:
        pygame.draw.rect(screen,color_dark, roll_button)



    if width - 860 <= mouse[0] <= width - 775 and height - 710 <= mouse[1] <= height - 580:
        property_name = font.render('Brooky', False, 0)
        cost_text = font.render('Property Cost: $10', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 775 <= mouse[0] <= width - 685 and height - 710 <= mouse[1] <= height - 580:
        property_name = font.render('Manly Vale', False, 0)
        cost_text = font.render('Property Cost: $10', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 595 <= mouse[0] <= width - 505 and height - 710 <= mouse[1] <= height - 580:
        property_name = font.render('Belrose', False, 0)
        cost_text = font.render('Property Cost: $30', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 505 <= mouse[0] <= width - 415 and height - 710 <= mouse[1] <= height - 580:
        property_name = font.render('Terry Hills', False, 0)
        cost_text = font.render('Property Cost: $40', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 420 <= mouse[0] <= width - 290 and height - 580 <= mouse[1] <= height - 495:
        property_name = font.render('Dee Why', False, 0)
        cost_text = font.render('Property Cost: $60', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 420 <= mouse[0] <= width - 290 and height - 315 <= mouse[1] <= height - 225:
        property_name = font.render('Cromer', False, 0)
        cost_text = font.render('Property Cost: $80', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 420 <= mouse[0] <= width - 290 and height - 225 <= mouse[1] <= height - 140:
        property_name = font.render('Forest', False, 0)
        cost_text = font.render('Property Cost: $90', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 505 <= mouse[0] <= width - 420 and height - 140 <= mouse[1] <= height - 10:
        property_name = font.render('Alambie', False, 0)
        cost_text = font.render('Property Cost: $110', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 595 <= mouse[0] <= width - 505 and height - 140 <= mouse[1] <= height - 10:
        property_name = font.render('Beacon Hill', False, 0)
        cost_text = font.render('Property Cost: $120', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 775 <= mouse[0] <= width - 685 and height - 140 <= mouse[1] <= height - 10:
        property_name = font.render('Sea Forth', False, 0)
        cost_text = font.render('Property Cost: $130', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 990 <= mouse[0] <= width - 860 and height - 225 <= mouse[1] <= height - 140:
        property_name = font.render('Curl Curl', False, 0)
        cost_text = font.render('Property Cost: $140', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 990 <= mouse[0] <= width - 860 and height - 315 <= mouse[1] <= height - 225:
        property_name = font.render('Freshy', False, 0)
        cost_text = font.render('Property Cost: $140', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))
    elif width - 990 <= mouse[0] <= width - 860 and height - 495 <= mouse[1] <= height - 405:
        property_name = font.render('Manly', False, 0)
        cost_text = font.render('Property Cost: $150', False, 0)
        ROI_text = font.render('ROI:', False, 0)
        set_bonus_text = font.render('Set Bonus:', False, 0)
        pygame.draw.rect(screen,color_light,[20,height - 500,250,220])
        screen.blit(property_name,(30,height - 490))
        screen.blit(cost_text,(30,height - 470))
        screen.blit(ROI_text,(30,height - 450))
        screen.blit(set_bonus_text,(30,height - 430))

    else:
        pygame.draw.rect(screen,0,[10,height - 710,270,440])
        pygame.draw.rect(screen,0,[width - 280,height - 710,270,700])
        screen.blit(votes_text,(20,height - 700))
        screen.blit(influence_text,(20,height - 680))
   


    if rolls == 1:
        property_cost = 10
       
    if rolls == 2:
        property_cost = 10
    if rolls == 4:
        property_cost = 30
    if rolls == 5:
        property_cost = 40
    if rolls == 7:
        property_cost = 60
    if rolls == 10:
        property_cost = 80
    if rolls == 11:
        property_cost = 90
    if rolls == 13:
        property_cost = 110
    if rolls == 14:
        property_cost = 120
    if rolls == 16:
        property_cost = 130
    if rolls == 19:
        property_cost = 140
    if rolls == 20:
        property_cost = 140
    if rolls == 22:
        property_cost = 150


    if rolls in houses:
        buy_text = font.render('Buy Property: $'+ str(property_cost) , True , color)
        if property_cost < 0:
            buy_text = font.render('Buy Property:SOLD', True , color)
        screen.blit(buy_text , (width - 1220,height - 200))
    if rolls in other:
        buy_text = font.render('Can not Buy', True , color)
        screen.blit(buy_text , (width - 1195,height - 200))




    #pygame.draw.rect(screen, (255,0,0), roll_button)
    screen.blit(text, (roll_button.x + roll_button.width / 2 - text_rect.width / 2, roll_button.y + roll_button.height / 2 - text_rect.height / 2))
    # Draw the board and spaces
    screen.blit(board_surf, board_rect)
    screen.blit(properties_title , (width - 270,height - 700))
    screen.blit(Total_ROI_text , (width - 270,height - 45))
    if dice:
        screen.blit(dices[last_roll], dice_rect)


   
    if Brooky == True:
        screen.blit(Brooky_text , (width - 270,height - 670))
    if Manly_Vale == True:
        screen.blit(Manly_Vale_text , (width - 270,height - 640))
    if Belrose == True:
        screen.blit(Belrose_text , (width - 270,height - 610))
    if Terry_Hills == True:
        screen.blit(Terry_Hills_text , (width - 270,height - 580))
    if Dee_Why == True:
        screen.blit(Dee_Why_text , (width - 270,height - 550))
    if Cromer == True:
        screen.blit(Cromer_text , (width - 270,height - 520))
    if Forest == True:
        screen.blit(Forest_text , (width - 270,height - 490))
    if Alambie == True:
        screen.blit(Alambie_text , (width - 270,height - 460))
    if Beacon_Hill == True:
        screen.blit(Beacon_Hill_text , (width - 270,height - 430))
    if Sea_Forth == True:
        screen.blit(Sea_Forth_text , (width - 270,height - 400))
    if Curly == True:
        screen.blit(Curly_text , (width - 270,height - 370))
    if Freshy == True:
        screen.blit(Freshy_text , (width - 270,height - 340))
    if Manly == True:
        screen.blit(Manly_text , (width - 270,height - 310))
   
    all_spaces.draw(screen)
    all_sprites.draw(screen)
   

    pygame.display.update()
pygame.font.quit()
pygame.quit()
