import pygame,sys,random
from pygame.math import Vector2
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent / "assets"

class SNAKE:
    def __init__(self):
        self.body= [Vector2(5,10),Vector2(4,10)]
        self.direction =Vector2(1,0)
        self.new_block=False

        #images
        self.head_up=pygame.image.load(str(ASSETS_DIR / 'snake head up.png')).convert_alpha()
        self.head_down=pygame.image.load(str(ASSETS_DIR / 'snake head down.png')).convert_alpha()
        self.head_right=pygame.image.load(str(ASSETS_DIR / 'snake head right.png')).convert_alpha()
        self.head_left=pygame.image.load(str(ASSETS_DIR / 'snake head left.png')).convert_alpha()

        self.tail_up=pygame.image.load(str(ASSETS_DIR / 'tail down.png')).convert_alpha()
        self.tail_down=pygame.image.load(str(ASSETS_DIR / 'tail up.png')).convert_alpha()
        self.tail_right=pygame.image.load(str(ASSETS_DIR / 'tail left.png')).convert_alpha()
        self.tail_left=pygame.image.load(str(ASSETS_DIR / 'tail right.png')).convert_alpha()

        self.body_vertical=pygame.image.load(str(ASSETS_DIR / 'snake body2.png')).convert_alpha()
        self.body_horizontal=pygame.image.load(str(ASSETS_DIR / 'snake body 1.png')).convert_alpha()
        
        self.body_tr=pygame.image.load(str(ASSETS_DIR / 'new (1).png')).convert_alpha()
        self.body_tl=pygame.image.load(str(ASSETS_DIR / 'new.png')).convert_alpha()
        self.body_br=pygame.image.load(str(ASSETS_DIR / 'turn 2.png')).convert_alpha()
        self.body_bl=pygame.image.load(str(ASSETS_DIR / 'turn.png')).convert_alpha()
        
    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos=int(block.x * cell_size)
            y_pos=int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block= self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x :
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y :
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.y == -1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.y == 1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == 1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.y == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == -1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.y == 1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == 1:
                        block_rect = pygame.Rect(x_pos + 8,y_pos,cell_size,cell_size)
                        screen.blit(self.body_br,block_rect)
                     
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head=self.head_left
        elif head_relation == Vector2(-1,0): self.head=self.head_right
        elif head_relation == Vector2(0,1): self.head=self.head_up
        elif head_relation == Vector2(0,-1): self.head=self.head_down
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail=self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail=self.tail_right
        elif tail_relation == Vector2(0,1): self.tail=self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail=self.tail_down

    def move_snake(self):      
        if self.new_block == True : 
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction )
            self.body=body_copy[:] 
            self.new_block = False

        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction )
            self.body=body_copy[:]

    def add_block(self):
        self.new_block = True
    
    def reset(self):

        self.body= [Vector2(5,10),Vector2(4,10)]
        self.direction =Vector2(0,1) 

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        if self.fruit_score==1:
            apple = pygame.image.load(str(ASSETS_DIR / 'apple.png')).convert_alpha()
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(apple,fruit_rect)
        elif self.fruit_score==2:
            fruit_image = pygame.image.load(str(ASSETS_DIR / 'apple2.png')).convert_alpha()
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(fruit_image,fruit_rect)
        elif self.fruit_score==3:
            fruit_image = pygame.image.load(str(ASSETS_DIR / 'apple3.png')).convert_alpha()
            fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(fruit_image,fruit_rect)

    def randomize(self):
        self.fruit_score=random.randint(1,3)
        self.x=random.randint(0 , cell_number -1)
        self.y=random.randint(0 , cell_number -1)
        if self.x >= cell_number - 5 and self.y==cell_number//2:
            self.x=random.randint(0 , cell_number -1)
            self.y=random.randint(0 , cell_number -1)
        self.pos=Vector2(self.x , self.y)

class OBSTACLE:
    def __init__(self):
        self.x= cell_number-5
        self.y=cell_number//2 
        self.pos=Vector2(self.x , self.y) 

    def draw_obstacle(self):
        obstacle_image= pygame.image.load(str(ASSETS_DIR / 'obstacle2.png')).convert_alpha()
        obstacle_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size*5,cell_size)
        screen.blit(obstacle_image,obstacle_rect)

class MAIN:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
        self.obstacle=OBSTACLE()
        self.button=Button('Restart',200, 100 , (300, 350), 5)
        self.score=[0]
        self.count=0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_score_max()
        self.obstacle.draw_obstacle()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.score[self.count] += self.fruit.fruit_score
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number  or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                self.game_over()
        if self.snake.body[0].x >= cell_number-5 and self.snake.body[0].y == cell_number//2:
            self.game_over()
                
    def game_over(self):
        self.button.flag=True
        while self.button.flag:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((240,255,255))
            self.button.draw()
            pygame.display.update()
            clock.tick(60)
        if  not self.button.flag:
            self.count += 1
            self.score.append(0)
        self.snake.reset()      

    def draw_grass(self):
        grass_color=(167,209,61)
        for row in range(cell_number):
            if row % 2 == 1 :
                for col in range(cell_number):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(col *cell_size, row * cell_size ,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col *cell_size, row * cell_size ,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    
    def draw_score(self):
        score_text = "Score : " + str(self.score[self.count])
        score_surface = game_font . render(score_text ,True ,(0, 0, 0))
        score_x = int(cell_number * cell_size - 60 )
        score_y = int(cell_number * cell_size - 40 )
        score_rect= score_surface.get_rect( center = (score_x , score_y))
        bg_rect=pygame.Rect(score_rect.left-5, score_rect.top-5,score_rect.width+10,score_rect.height+10 )
        pygame.draw.rect(screen,(167, 209, 61),bg_rect)
        screen.blit(score_surface , score_rect)
        pygame.draw.rect(screen,(0, 0, 0),bg_rect,2)
    
    def draw_score_max(self):
        max=0
        for number in self.score:
            if number > max:
                max = number
        score_max_text = "Max : " + str(max)
        score_max_surface = game_font . render(score_max_text ,True ,(0, 0, 0))
        score_max_x = int( 50 )
        score_max_y = int(cell_number * cell_size - 40 )
        score_max_rect= score_max_surface.get_rect( center = (score_max_x , score_max_y))
        bg_max_rect=pygame.Rect(score_max_rect.left-5, score_max_rect.top-5,score_max_rect.width+10,score_max_rect.height+10 )
        pygame.draw.rect(screen,(167, 209, 61),bg_max_rect)
        screen.blit(score_max_surface , score_max_rect)
        pygame.draw.rect(screen,(0, 0, 0),bg_max_rect,2)

class Button:
    def __init__(self,text,width,height,pos,elevation):
        self.flag=True
        self.pressed=False
        self.elevation=elevation
        self.dynamic_elevation=elevation
        self.original_y_pos=pos[1]

        self.top_rect=pygame.Rect(pos,(width,height))
        self.top_color='#475F77'

        self.bottom_rect=pygame.Rect(pos,(width,elevation))
        self.bottom_color='#354B5E'

        self.text_surf= start_font.render(text,True,'#FFFFFF')
        self.text_rect=self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius=12)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color='#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation=0
                self.pressed = True
            else:
                self.dynamic_elevation= self.elevation
                if self.pressed:
                    self.pressed = False
                    self.flag=False
        else:
            self.dynamic_elevation= self.elevation
            self.top_color='#475F77'

pygame.init()

cell_size=40
cell_number=20
screen = pygame.display.set_mode((cell_size * cell_number,cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None , 25)
start_font = pygame.font.Font(None , 40)
main_game=MAIN()
button1=Button('Start',200, 100 , (300, 350), 5)

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while button1.flag:
    pygame.display.set_caption('Start')
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    screen.fill((240,255,255))
    button1.draw()
    #start_rect = pygame.Rect(0,0,800,800)
    #screen.blit(start_image,start_rect)
    pygame.display.update()
    clock.tick(60)

while True:
    pygame.display.set_caption('Snake game')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_RIGHT:

                if main_game.snake.direction.x != -1:
                    main_game.snake.direction=Vector2(1,0)
            if event.key==pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction=Vector2(-1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
