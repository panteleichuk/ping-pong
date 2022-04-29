import pygame
import math
from random import randint
from script.menu_window import*
setting = read_json("setting.json", "json")
width, height = setting["GAME"]["WIDTH"],setting["GAME"]["HEIGTH"]
pygame.init()
class Setting:
    def __init__(self, width = width, heigth = height, 
                        image = None,color=tuple(setting["GAME"]["COLOR"]),
                        x = 0, y = 0):
        self.WIDTH = width
        self.HEIGTH = heigth
        self.IMAGE = image
        self.COLOR = color
        if self.IMAGE:
            self.IMAGE = path_f(image)
            self.IMAGE = pygame.image.load(self.IMAGE)
            self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH,self.HEIGTH))
        self.X = x
        self.Y = y
        self.creat_wall_btn()
    def creat_wall_btn(self):
        self.wall = [pygame.rect.Rect(10,0,self.WIDTH-20,10),pygame.rect.Rect(10,self.HEIGTH-10,self.WIDTH-20,10)]
        self.wall_LR =  [pygame.rect.Rect(0,0,10,self.HEIGTH),pygame.rect.Rect(self.WIDTH-10,0,10,self.HEIGTH)]
        self.btn_menu = pygame.rect.Rect(self.WIDTH//2 - 50, 5, self.WIDTH//9,self.HEIGTH//15)
        self.font = pygame.font.Font(None,self.WIDTH//30)

    def back(self,setting_game):
        self.WIDTH = setting_game["WIDTH"]
        self.HEIGTH = setting_game["HEIGTH"]
        self.creat_wall_btn()
    def reset(self, window):
        if self.IMAGE:
            window.blit(self.IMAGE, (self.X,self.Y))
        else:
            window.fill(self.COLOR)
        pygame.draw.rect(window,(222,122,122),self.btn_menu)
        window.blit(self.font.render("MENU",True,(0,0,0)),(self.btn_menu.x+20,self.btn_menu.y+10))
class Racet(Setting):
    def __init__(self,name, width = 700, heigth = 500, image = None,color=None, x = 0, y = 0, speed = 0):
        super().__init__(width , heigth , image ,color, x , y)
        self.RECT = pygame.rect.Rect(x,y,self.WIDTH,self.HEIGTH)
        self.SPEED = speed
        self.COUNT = 0
        self.font = pygame.font.Font(None,self.WIDTH*2)
        self.NAME = name
    def new_game(self):
        self.RECT.y = 20
        self.COUNT = 0
    def back(self,dict_):
        self.COUNT = dict_["COUNT"]
        self.SPEED = dict_["SPEED"]
        self.COLOR = tuple(dict_["RECT.c"])
        self.RECT.x = dict_[ "RECT.x"]
        self.X = dict_[ "RECT.x"]
        self.RECT.y = dict_["RECT.y"]
        self.WIDTH = dict_["RECT.w"]
        self.HEIGTH = dict_["RECT.h"]
        self.font = pygame.font.Font(None,self.WIDTH*2)
    def creat_dict(self):
        rct_dict = {
                "RECT.x":self.RECT.x,
                "RECT.y":self.RECT.y,
                "RECT.w":self.WIDTH,
                "RECT.h":self.HEIGTH,
                "RECT.c":self.COLOR,
                "SPEED":self.SPEED,
                "COUNT":self.COUNT
        }
        setting[self.NAME] = rct_dict
    def reset(self, window):
        window.blit(  self.font.render( str(self.COUNT),True,self.COLOR ),(self.X,self.Y)  )
        if self.IMAGE:
            window.blit(self.IMAGE, (self.RECT.x,self.RECT.y))
        else:
            pygame.draw.rect(window,self.COLOR,self.RECT,border_radius = 15)
            pygame.draw.rect(window,(0,0,0),self.RECT,width=5,border_radius = 15)

    def move(self, side):
        key = pygame.key.get_pressed()
        if side == "left":
            if key[pygame.K_w] and self.RECT.y >= self.SPEED:
                    self.RECT.y -= self.SPEED
                    
            elif key[pygame.K_s] and self.RECT.y <= (sett.HEIGTH - self.HEIGTH - self.SPEED) :
                    self.RECT.y += self.SPEED  
                             
        else:
            if key[pygame.K_UP] and self.RECT.y >= self.SPEED:
                    self.RECT.y -= self.SPEED
                   
            elif key[pygame.K_DOWN] and self.RECT.y <= (sett.HEIGTH - self.HEIGTH - self.SPEED) :
                    self.RECT.y+= self.SPEED
                   
        
class Ball(Racet):
    def __init__(self, name, width = 700, heigth = 500, image = None,color=None, x = 0, y = 0):
        super().__init__(name,width , heigth , image ,color, x , y, 0)
        self.SP_X = 10 * math.cos(randint(1,5) *2 * math.pi)
        self.SP_Y =  10 * math.sin(randint(1,5) *2 * math.pi)
    def new_game(self):
        self.RECT.x = width//2
        self.RECT.y = height//2 
    def reset(self, window):
        if self.IMAGE:
            window.blit(self.IMAGE, (self.RECT.x,self.RECT.y))
        else:
            pygame.draw.circle(window,self.COLOR,(self.RECT.x+self.WIDTH//2,self.RECT.y+self.HEIGTH//2),self.WIDTH//2)
    def random_sp(self):
        x,y = self.SP_X,self.SP_Y
        self.SP_X = randint(4,10) 
        self.SP_Y =  randint(4,10) 
        if x>0:  self.SP_X *= -1
        if y>0: self.SP_Y *= -1
    def move(self):
        self.RECT.x += self.SP_X
        self.RECT.y += self.SP_Y
        if self.RECT.colliderect(sett.wall[0]) or self.RECT.colliderect(sett.wall[1]):
            self.random_sp()
        if self.RECT.colliderect(sett.wall_LR[0]):
            self.random_sp()
            self.RECT.x,self.RECT.y = sett.WIDTH//2,sett.HEIGTH//2
            rct2.COUNT += 1
        elif self.RECT.colliderect(sett.wall_LR[1]):
            self.random_sp()
            self.RECT.x,self.RECT.y = sett.WIDTH//2,sett.HEIGTH//2
            rct1.COUNT += 1
      


sett = Setting(color = (109,135,100))
ball =Ball("BALL",50,50,None,(164,196,0),sett.WIDTH//2+100,sett.HEIGTH//2)

rct1 = Racet("RCT1",25,100,None,(100,118,135),20,20,8)
rct2 = Racet("RCT2",25,100,None,(118,96,138),sett.WIDTH - 45,20,8)


dict_ract1 = dict()
dict_ract2 = dict()
dict_ball = dict()
def run_game():
    count = 0
    global setting
    kind_win = "game"
    if kind_win == "game":
        window = pygame.display.set_mode((sett.WIDTH, sett.HEIGTH))
    pygame.display.set_caption("Ping-pong")

    count = 0
    game = True
    clock = pygame.time.Clock()
    FPS = 60

    while game:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sett.btn_menu.collidepoint(event.pos):
                    dict_ract1 = rct1.creat_dict()
                    dict_ract2 = rct2.creat_dict()
                    dict_ball = ball.creat_dict()
                    print(setting)
                    write_json("setting.json",'json',setting)
                    kind_win = "menu"
                   

        
        if kind_win == "game":
            sett.reset(window)
            
            if count >0 :
                window.blit(font.render("START "+ str(count//10) +" seconds",True,(255,0,0)),(width//2-50,height//2-100))
                count -= 1
            ball.reset(window)
            rct1.reset(window)
            rct2.reset(window)
            if count <= 0:
                if rct1.COUNT < 3 and rct2.COUNT <3:
                    rct1.move("left")
                    rct2.move("rigth")
                    ball.move()
                else:
                    if rct1.COUNT >3: 
                        count = 0    
                        window.blit(rct1.font.render("WINN ROCET1(LEFT)",True,rct1.COLOR),(sett.WIDTH//2,sett.HEIGTH//2))
                    else:
                        window.blit(rct2.font.render("WINN ROCET2(Rigth)",True,rct2.COLOR),(sett.WIDTH//2,sett.HEIGTH//2))
                    count -= 1
                if count == -300:
                    kind_win = "menu"
          
        else:
            exitt = run_menu(setting)
            if exitt == "EXIT":
                game = False
            elif exitt == "NEW":
                count = 500
                rct1.new_game()
                rct2.new_game()
                ball.new_game()
                window = pygame.display.set_mode((sett.WIDTH, sett.HEIGTH))
                kind_win = "game"

            elif exitt == "BACK":
                        kind_win = "game"
                        setting = read_json("setting.json","json")
                        print(setting["GAME"])
                        sett.back(setting["GAME"])
                        ball.back(setting["BALL"])
                        rct1.back(setting["RCT1"])
                        rct2.back(setting["RCT2"])  
                        window = pygame.display.set_mode((sett.WIDTH, sett.HEIGTH))
                      

        pygame.display.update()
        clock.tick(FPS)

run_game()
