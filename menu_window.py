import pygame
from script.rw_json import*
pygame.init()
setting = read_json("setting.json","json")

FPS = 60
timer = pygame.time.Clock()

centet_x, center_y = setting["MENU"]["WIDTH"]//2,setting["MENU"]["HEIGTH"]//2
width_b, heigth_b = setting["MENU"]["WIDTH"]//2,setting["MENU"]["HEIGTH"]//10 

class Menu:
    def __init__(self):
        start_y =center_y - (heigth_b*4+4*40)//2
        self.BTN_BACK = pygame.rect.Rect((centet_x - width_b//2),start_y,width_b,heigth_b)
        self.BTN_SETTING = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b+40,width_b,heigth_b)
        self.BTN_NEW_GAME = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b*2+80,width_b,heigth_b)
        self.BTN_EXIT = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b*3+120,width_b,heigth_b)
        self.COLOR = (122,122,122)
        self.FONT = pygame.font.Font(None,heigth_b-20)
        self.FLAG = True

    def reset(self, win):
        pygame.draw.rect(win,self.COLOR,self.BTN_BACK)
        pygame.draw.rect(win,(0,0,0),self.BTN_BACK,width = 5)
        win.blit(self.FONT.render("BACK",True,(0,0,0)),(self.BTN_BACK.x+75, self.BTN_BACK.y + 20))

        pygame.draw.rect(win,self.COLOR,self.BTN_SETTING)
        pygame.draw.rect(win,(0,0,0),self.BTN_SETTING,width = 5)
        win.blit(self.FONT.render("SETTING",True,(0,0,0)),(self.BTN_SETTING.x+45, self.BTN_SETTING.y + 20))

        pygame.draw.rect(win,self.COLOR,self.BTN_NEW_GAME)
        pygame.draw.rect(win,(0,0,0),self.BTN_NEW_GAME,width = 5)
        win.blit(self.FONT.render("NEW GAME",True,(0,0,0)),(self.BTN_NEW_GAME.x+30, self.BTN_NEW_GAME.y + 20))

        pygame.draw.rect(win,self.COLOR,self.BTN_EXIT)
        pygame.draw.rect(win,(0,0,0),self.BTN_EXIT,width = 5)
        win.blit(self.FONT.render("EXIT",True,(0,0,0)),(self.BTN_EXIT.x+90, self.BTN_EXIT.y + 20))

class Setting_Menu:
    def __init__(self):
        start_y =center_y - (heigth_b*4+4*40)//2
        self.SIZE1 = pygame.rect.Rect((centet_x - width_b//2),start_y,heigth_b,heigth_b)
        self.SIZE2 = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b+40,heigth_b,heigth_b)
        self.SIZE3 = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b*2+80,heigth_b,heigth_b)
        self.BTN_OK = pygame.rect.Rect((centet_x - width_b//2),start_y+heigth_b*3+120,width_b,heigth_b)
        self.CHOOSE = 0
        self.COLOR = (170,170,170)
        self.FONT = pygame.font.Font(None,heigth_b-20)
    def rset(self,win):
        if self.CHOOSE == 1:
            pygame.draw.rect(win,(0,0,0),self.SIZE1)
        pygame.draw.rect(win,self.COLOR,self.SIZE1,width = 10)
        win.blit(self.FONT.render("450*300",True,(0,0,0)),(self.SIZE1.x+40 + heigth_b, self.SIZE1.y+20))
        if self.CHOOSE == 2:
            pygame.draw.rect(win,(0,0,0),self.SIZE2)
        pygame.draw.rect(win,self.COLOR,self.SIZE2,width = 10)
        win.blit(self.FONT.render("900*600",True,(0,0,0)),(self.SIZE2.x+40 + heigth_b, self.SIZE2.y+20))
        if self.CHOOSE == 3:
            pygame.draw.rect(win,(0,0,0),self.SIZE3)
        pygame.draw.rect(win,self.COLOR,self.SIZE3,width = 10)
        win.blit(self.FONT.render("1200*900",True,(0,0,0)),(self.SIZE3.x+40 + heigth_b, self.SIZE3.y+20))

        pygame.draw.rect(win,self.COLOR,self.BTN_OK)
        win.blit(self.FONT.render("OK",True,(0,0,0)),(self.BTN_OK.x+20 + heigth_b, self.BTN_OK.y+20))
def chahg_size(sett,name, w,h):
    sett[name]["WIDTH"]= sett["GAME"]["WIDTH"]//w
    sett[name]["HEIGTH"]= sett["GAME"]["HEIGTH"]//h
    
def run_menu(sett_game):
    menu_win = pygame.display.set_mode((setting["MENU"]["WIDTH"],setting["MENU"]["HEIGTH"]))
    menu = Menu()
    sett_menu = Setting_Menu()
    work =True
    exitt = False
    while work:
        menu_win.fill(tuple(setting["MENU"]["COLOR"]))
        if menu.FLAG:
            menu.reset(menu_win)
        else:
            sett_menu.rset(menu_win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.FLAG:
                    if  menu.BTN_EXIT.collidepoint(event.pos):
                        work = False
                        exitt = "EXIT"
                    elif  menu.BTN_BACK.collidepoint(event.pos):
                        work = False 
                        exitt = "BACK"
                    elif  menu.BTN_NEW_GAME.collidepoint(event.pos):
                        work = False
                        exitt = "NEW"
                    elif  menu.BTN_SETTING.collidepoint(event.pos):
                        menu.FLAG = False
                else:
                    print(sett_game["GAME"])
                    if sett_menu.SIZE1.collidepoint(event.pos):
                        sett_menu.CHOOSE = 1
                        sett_game["GAME"]["WIDTH"] = 450
                        sett_game["GAME"]["HEIGTH"] = 300

                    elif sett_menu.SIZE2.collidepoint(event.pos):
                        sett_menu.CHOOSE = 2
                        sett_game["GAME"]["WIDTH"] = 900
                        sett_game["GAME"]["HEIGTH"] = 600
                    elif sett_menu.SIZE3.collidepoint(event.pos):
                        sett_menu.CHOOSE = 3
                        sett_game["GAME"]["WIDTH"] = 1200
                        sett_game["GAME"]["HEIGTH"] = 900
                    elif sett_menu.BTN_OK.collidepoint(event.pos):
                        menu.FLAG = True
                        chahg_size(sett_game,"BALL",18,12)
                        chahg_size(sett_game,"RCT1",36,6)
                        chahg_size(sett_game,"RCT2",36,6)
                        sett_game["RCT2"]["RECT.x"] = sett_game["GAME"]["WIDTH"] - 25 - sett_game["RCT2"]["RECT.w"]
                        print(sett_game["GAME"])
                        write_json("setting.json",'json',sett_game)

        timer.tick(FPS)
        pygame.display.flip()
    return exitt
# run_menu()
