#This is our attempt at making Snake game
import pygame 
import random
import time
import os
from pygame.constants import K_b, K_d, K_g, K_i, K_n, K_o, K_a, K_k
pygame.mixer.init()
pygame.mixer.pre_init()
pygame.init()

#Window
screen_width,screen_height = 800,400
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Gandu Snake")
pygame.display.update()

#Colours
purple = (128,0,128)
cream = (255, 253, 208)
white = (255,255,255)
red = (255,0,0)
neon_red = (255, 7, 58)
orange = (255, 165, 0)
green = (0,255,0)
dark_green = (0,100,0)
neon_green = (57, 255, 20)
yellow = (255,255,0)
neon_yellow = (250,237,39)
blue = (0,0,225)
grey = (130,130,130)
black = (0,0,0)

#Backgorund Images
bgimg = pygame.image.load("Game Data\\level.jpg")
bgimg = pygame.transform.scale(bgimg, (800, 400)).convert_alpha()
menu = pygame.image.load("Game Data\\menu.png")
menu = pygame.transform.scale(menu, (800, 400)).convert_alpha()
charselect = pygame.image.load("Game Data\\character select.png")
charselect = pygame.transform.scale(charselect, (800, 400)).convert_alpha()
charinfo = pygame.image.load("Game Data\\characters.png")
charinfo = pygame.transform.scale(charinfo, (800, 400)).convert_alpha()
pause_scr = pygame.image.load("Game Data\\pause.png")
pause_scr = pygame.transform.scale(pause_scr, (800, 310))
end = pygame.image.load("Game Data\\end.png")
end = pygame.transform.scale(end, (800, 400)).convert_alpha()
htp = pygame.image.load("Game Data\\htp.png")
htp = pygame.transform.scale(htp, (800, 400)).convert_alpha()
about = pygame.image.load("Game Data\\about.png")
about = pygame.transform.scale(about, (800, 400)).convert_alpha()
controls = pygame.image.load("Game Data\\controls.png")
controls = pygame.transform.scale(controls, (800, 400)).convert_alpha()
quitt = pygame.image.load("Game Data\\quit.png")
quitt = pygame.transform.scale(quitt, (800, 400)).convert_alpha()
gobackmm = pygame.image.load("Game Data\\goback.png")
gobackmm = pygame.transform.scale(gobackmm, (800, 400)).convert_alpha()
#Ability Meters
ability_i = pygame.image.load("Game Data\\meter_i.png")
ability_i = pygame.transform.scale(ability_i, (185, 35)).convert_alpha()
ability_s = pygame.image.load("Game Data\\meter_s.png")
ability_s = pygame.transform.scale(ability_s, (185, 55)).convert_alpha()
#Snake Face
face = pygame.image.load("Game Data\\c_default.png")
# face = pygame.transform.scale(face, (30, 30)).convert_alpha()

#SFX and music Channels
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)
sound1 = pygame.mixer.Sound('Game Data\\food.mp3')
sound2 = pygame.mixer.Sound('Game Data\\gameover.mp3')
sound2.set_volume(0.3)
sound3 = pygame.mixer.Sound('Game Data\\power.mp3')
sound4 = pygame.mixer.Sound('Game Data\\invincibility.mp3')
sound5 = pygame.mixer.Sound('Game Data\\slow motion.mp3')
sound6 = pygame.mixer.Sound('Game Data\\theme.mp3')
sound6.set_volume(0.2)
sound7 = pygame.mixer.Sound('Game Data\\naagin.mp3')
sound7.set_volume(0.3)
sound8 = pygame.mixer.Sound('Game Data\\nokia.mp3')
sound8.set_volume(0.3)

#Fonts
font = pygame.font.SysFont("arialblack", 28)
font2 = pygame.font.SysFont("arialblack", 24)
clock = pygame.time.Clock()

#Global variables
home_y = True
power_timer = True
character_timer = True
play_m = True
music_n = False
sfx_n = False
theme = True
naagin = False
left = False
nokia = False
snakeface = "Game Data\\c_default.png"
playertheme = 'Game Data\\naagin.mp3'
charforinfo = 'Game Data\\m_snake.png'
snake_head = []

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snake_lst,snake_size_x,snake_size_y):
    for x,y in snake_lst:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size_x,snake_size_y])

def close():
    global music_n
    global play_m
    click = False
    global g_exit
    g_exit = False
    r = True
    while r == True and g_exit == False:
        gameWindow.fill(white)
        gameWindow.blit(quitt, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_y = pygame.image.load("Game Data\\button_y.png")
        button_y = pygame.transform.scale(button_y, (240, 60)).convert_alpha()
        button_y = gameWindow.blit(button_y, (280, 180))
        button_n = pygame.image.load("Game Data\\button_n.png")
        button_n = pygame.transform.scale(button_n, (240, 60)).convert_alpha()
        button_n = gameWindow.blit(button_n, (280, 260))
        if button_y.collidepoint((mx, my)):
            if click:
                g_exit = True
                click = False
        if button_n.collidepoint((mx, my)):
            if click:
                r = False
                click = False   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    r = False
                if event.key == pygame.K_RETURN:
                    g_exit = True
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def backtomm():
    global play_m
    global music_n
    click = False
    global g_exit
    g_exit = False
    r5 = True
    while r5 == True and g_exit == False:
        gameWindow.fill(white)
        gameWindow.blit(gobackmm, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_y = pygame.image.load("Game Data\\button_y.png")
        button_y = pygame.transform.scale(button_y, (240, 60)).convert_alpha()
        button_y = gameWindow.blit(button_y, (280, 180))
        button_n = pygame.image.load("Game Data\\button_n.png")
        button_n = pygame.transform.scale(button_n, (240, 60)).convert_alpha()
        button_n = gameWindow.blit(button_n, (280, 260))
        if button_y.collidepoint((mx, my)):
            if click:
                welcome()
                click = False
        if button_n.collidepoint((mx, my)):
            if click:
                r5 = False
                click = False   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    r5 = False
                if event.key == pygame.K_RETURN:
                    welcome()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def pause_scrn():
    global diff
    global start_time
    global music_n
    global play_m
    global power_timer
    global sfx_n 
    global chartheme
    global charactertheme
    click = False
    pause_m = True
    global g_exit
    g_exit = False
    r4 = True
    while r4 == True and g_exit == False:
        gameWindow.blit(pause_scr, (0, 60))
        mx, my = pygame.mouse.get_pos()
        if music_n == False:
            music_y = pygame.image.load("Game Data\\music_y.png")
            music_y = pygame.transform.scale(music_y, (240, 40)).convert_alpha()
            music_y = gameWindow.blit(music_y, (155, 170))
        elif music_n == True:
            music_y = pygame.image.load("Game Data\\music_n.png")
            music_y = pygame.transform.scale(music_y, (240, 40)).convert_alpha()
            music_y = gameWindow.blit(music_y, (155, 170))
        if sfx_n == False:
            sfx_y = pygame.image.load("Game Data\\sfx_y.png")
            sfx_y = pygame.transform.scale(sfx_y, (240, 40)).convert_alpha()
            sfx_y = gameWindow.blit(sfx_y, (405, 170))
        else:
            sfx_y = pygame.image.load("Game Data\\sfx_n.png")
            sfx_y = pygame.transform.scale(sfx_y, (240, 40)).convert_alpha()
            sfx_y = gameWindow.blit(sfx_y, (405, 170))
        
        p_cntrls = pygame.image.load("Game Data\\p_cntrls.png")
        p_cntrls = pygame.transform.scale(p_cntrls, (240, 30)).convert_alpha()
        p_cntrls = gameWindow.blit(p_cntrls, (280, 220))
        p_htp = pygame.image.load("Game Data\\p_htp.png")
        p_htp = pygame.transform.scale(p_htp, (240, 30)).convert_alpha()
        p_htp = gameWindow.blit(p_htp, (280, 260))
        p_restart = pygame.image.load("Game Data\\p_restart.png")
        p_restart = pygame.transform.scale(p_restart, (240, 30)).convert_alpha()
        p_restart = gameWindow.blit(p_restart, (530, 220))
        p_quit = pygame.image.load("Game Data\\p_quit.png")
        p_quit = pygame.transform.scale(p_quit, (240, 30)).convert_alpha()
        p_quit = gameWindow.blit(p_quit, (530, 260))
        p_resume = pygame.image.load("Game Data\\p_resume.png")
        p_resume = pygame.transform.scale(p_resume, (240, 30)).convert_alpha()
        p_resume = gameWindow.blit(p_resume, (30, 220))
        quit_tmm = pygame.image.load("Game Data\\quit_tmm.png")
        quit_tmm = pygame.transform.scale(quit_tmm, (240, 30)).convert_alpha()
        quit_tmm = gameWindow.blit(quit_tmm, (30, 260))

        if p_cntrls.collidepoint((mx, my)):
            if click:
                cntrls()  
                click = False
        if p_htp.collidepoint((mx, my)):
            if click:
                howtoplay()  
                click = False  
        if p_quit.collidepoint((mx, my)):
            if click:
                close()
                click = False
        if p_resume.collidepoint((mx, my)):
            if click:
                r4 = False
                click = False
        if p_restart.collidepoint((mx, my)):
            if click:
                gameloop()
                click = False
        if quit_tmm.collidepoint((mx, my)):
            if click:
                backtomm()
                click = False      
        if music_y.collidepoint((mx, my)) == True and play_m == True:
            if click:
                sound6.set_volume(0.0)
                sound7.set_volume(0.0)
                sound8.set_volume(0.0)
                music_n = True
                play_m = False
                click = False
        elif music_y.collidepoint((mx, my)) == True and play_m == False:
            if click:
                if theme == True:
                    sound6.set_volume(0.2)
                if naagin == True:
                    sound7.set_volume(0.3)
                if nokia == True:
                    sound8.set_volume(0.3)
                music_n = False
                play_m = True
                click = False
        if sfx_y.collidepoint((mx, my)) and pause_m == True:
            if click:
                sound1.set_volume(0.0)
                sound2.set_volume(0.0)
                sound3.set_volume(0.0)
                sfx_n = True  
                pause_m = False
                click = False
        elif sfx_y.collidepoint((mx, my)) and pause_m == False:
            if click:
                sound1.set_volume(1.0)
                sound2.set_volume(0.3)
                sound3.set_volume(1.0)
                sfx_n = False  
                pause_m = True
                click = False
                  
        for event in pygame.event.get():
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_p] or keypressed[pygame.K_BACKSPACE] or keypressed[pygame.K_RETURN]:
                power_timer = True
                faltutime = time.time()
                start_time = float(faltutime) - diff
                r4 = False
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cntrls()
                if event.key == pygame.K_TAB:
                    char_info()
                if event.key == pygame.K_h:
                    howtoplay()
                if event.key == pygame.K_i:
                    aboutus()
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if event.key == pygame.K_m:
                    if play_m == True:
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        if charactertheme == True:
                            if event.key == pygame.K_m:
                                if chartheme == True:
                                    pygame.mixer.music.pause()
                                    music_n = True
                                    chartheme = False
                                elif chartheme == False:
                                    pygame.mixer.music.unpause()
                                    music_n = False
                                    chartheme = True
                        elif charactertheme == False:
                            if theme == True:
                                sound6.set_volume(0.2)
                            if naagin == True:
                                sound7.set_volume(0.3)
                            if nokia == True:
                                sound8.set_volume(0.3)
                            play_m = True
                            music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def howtoplay():
    global music_y
    global play_m
    global home_y
    click = False
    global g_exit
    g_exit = False
    r2 = True 
    while r2 == True and g_exit == False:
        gameWindow.fill(white)
        gameWindow.blit(htp, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_h = pygame.image.load("Game Data\\button_h.png")
        button_h = pygame.transform.scale(button_h, (30, 30)).convert_alpha()
        button_h = gameWindow.blit(button_h, (760, 350))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (640, 350))
        button_c2 = pygame.image.load("Game Data\\button_c.png")
        button_c2 = pygame.transform.scale(button_c2, (25, 20)).convert_alpha()
        button_c2 = gameWindow.blit(button_c2, (185, 333))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (680, 350))
        button_char = pygame.image.load("Game Data\\button_char.png")
        button_char = pygame.transform.scale(button_char, (30, 30)).convert_alpha()
        button_char = gameWindow.blit(button_char, (600, 350))
        button_back = pygame.image.load("Game Data\\button_back.png")
        button_back = pygame.transform.scale(button_back, (30, 30)).convert_alpha()
        button_back = gameWindow.blit(button_back, (720, 350))
        if click:
            if home_y == True:
                if button_h.collidepoint((mx, my)):
                    welcome()
                    click = False
            elif home_y == False:
                if button_h.collidepoint((mx, my)):
                    backtomm()
                    click = False
            if button_c.collidepoint((mx, my)):
                cntrls()
                click = False
            if button_c2.collidepoint((mx, my)):
                cntrls()
                click = False
            if button_i.collidepoint((mx, my)):
                aboutus()
                click = False
            if button_char.collidepoint((mx, my)):
                char_info()
                click = False
            if button_back.collidepoint((mx, my)):
                r2 = False
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    r2 = False
                if event.key == pygame.K_ESCAPE:
                    backtomm() 
                if event.key == pygame.K_c:
                    cntrls()
                if event.key == pygame.K_TAB:
                    char_info()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True      
        pygame.display.update()
        clock.tick(60)

def aboutus():
    global play_m
    global music_n
    global home_y
    click = False
    global g_exit
    g_exit = False
    r3 = True 
    while r3 == True and g_exit == False:
        gameWindow.fill(white)
        gameWindow.blit(about, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_h = pygame.image.load("Game Data\\button_h.png")
        button_h = pygame.transform.scale(button_h, (30, 30)).convert_alpha()
        button_h = gameWindow.blit(button_h, (760, 350))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (640, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (680, 350))
        button_char = pygame.image.load("Game Data\\button_char.png")
        button_char = pygame.transform.scale(button_char, (30, 30)).convert_alpha()
        button_char = gameWindow.blit(button_char, (600, 350))
        button_back = pygame.image.load("Game Data\\button_back.png")
        button_back = pygame.transform.scale(button_back, (30, 30)).convert_alpha()
        button_back = gameWindow.blit(button_back, (720, 350))
        if click:
            if home_y == True:
                if button_h.collidepoint((mx, my)):
                    welcome()
                    click = False
            elif home_y == False:
                if button_h.collidepoint((mx, my)):
                    backtomm()
                    click = False
            if button_c.collidepoint((mx, my)):
                cntrls()
                click = False
            if button_qmark.collidepoint((mx, my)):
                howtoplay()
                click = False
            if button_char.collidepoint((mx, my)):
                char_info()
                click = False
            if button_back.collidepoint((mx, my)):
                r3 = False
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    r3 = False 
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if event.key == pygame.K_TAB:
                    char_info()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True     
        pygame.display.update()
        clock.tick(60)

def cntrls():
    global music_n
    global play_m
    global home_y
    click = False
    global g_exit
    g_exit = False
    run = True 
    while run == True and g_exit == False:
        gameWindow.fill(white)
        gameWindow.blit(controls, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_h = pygame.image.load("Game Data\\button_h.png")
        button_h = pygame.transform.scale(button_h, (30, 30)).convert_alpha()
        button_h = gameWindow.blit(button_h, (760, 350))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (680, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (640, 350))
        button_char = pygame.image.load("Game Data\\button_char.png")
        button_char = pygame.transform.scale(button_char, (30, 30)).convert_alpha()
        button_char = gameWindow.blit(button_char, (600, 350))
        button_back = pygame.image.load("Game Data\\button_back.png")
        button_back = pygame.transform.scale(button_back, (30, 30)).convert_alpha()
        button_back = gameWindow.blit(button_back, (720, 350))
        if click:
            if home_y == True:
                if button_h.collidepoint((mx, my)):
                    welcome()
                    click = False
            elif home_y == False:
                if button_h.collidepoint((mx, my)):
                    backtomm()
                    click = False
            if button_i.collidepoint((mx, my)):
                aboutus()
                click = False
            if button_char.collidepoint((mx, my)):
                char_info()
                click = False
            if button_qmark.collidepoint((mx, my)):
                howtoplay()
                click = False
            if button_char.collidepoint((mx, my)):
                char_info()
                click = False
            if button_back.collidepoint((mx, my)):
                run = False
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    run = False 
                if event.key == pygame.K_q:
                    close()       
                if event.key == pygame.K_h:
                    howtoplay()
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if event.key == pygame.K_TAB:
                    char_info()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        clock.tick(60)

def individualchar():
    global home_y
    global music_n
    global play_m
    global g_exit
    global charforinfo
    g_exit = False
    click = False
    r8 = True 
    while r8 == True and g_exit == False:
        charinfo = pygame.image.load(charforinfo)
        charinfo = pygame.transform.scale(charinfo, (800, 400)).convert_alpha()
        gameWindow.blit(charinfo, (0, 0))
        text_screen2("Press Spacebar in game to activate player theme", white, 50, 330)
        mx, my = pygame.mouse.get_pos()
        button_back = pygame.image.load("Game Data\\button_back.png")
        button_back = pygame.transform.scale(button_back, (30, 30)).convert_alpha()
        button_back = gameWindow.blit(button_back, (720, 350))
        button_h = pygame.image.load("Game Data\\button_h.png")
        button_h = pygame.transform.scale(button_h, (30, 30)).convert_alpha()
        button_h = gameWindow.blit(button_h, (760, 350))
        if click:
            if home_y == True:
                if button_h.collidepoint((mx, my)):
                    welcome()
                    click = False
            elif home_y == False:
                if button_h.collidepoint((mx, my)):
                    backtomm()
                    click = False
            if button_back.collidepoint((mx, my)):
                r8 = False
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()       
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if event.key == pygame.K_BACKSPACE:
                    r8 = False
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                        play_m = True
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def char_info():
    global home_y
    global play_m
    global music_n
    global charforinfo
    r6 = True
    click = False
    global g_exit
    g_exit = False
    if play_m == False and music_n == True:
        pygame.mixer.music.pause()

    while r6 == True and g_exit == False:
        gameWindow.blit(charinfo, (0, 0))
        mx, my = pygame.mouse.get_pos()
        b_default = pygame.image.load("Game Data\\b_snake.png")
        b_default = pygame.transform.scale(b_default, (250, 35)).convert_alpha()
        b_default = gameWindow.blit(b_default, (280, 130))
        b_lyla = pygame.image.load("Game Data\\b_lyla.png")
        b_lyla = pygame.transform.scale(b_lyla, (250, 50)).convert_alpha()
        b_lyla = gameWindow.blit(b_lyla, (10, 100))
        b_katarina = pygame.image.load("Game Data\\b_katarina.png")
        b_katarina = pygame.transform.scale(b_katarina, (250, 50)).convert_alpha()
        b_katarina = gameWindow.blit(b_katarina, (10, 160))
        b_dhandrul = pygame.image.load("Game Data\\b_big smoke.png")
        b_dhandrul = pygame.transform.scale(b_dhandrul, (250, 50)).convert_alpha()
        b_dhandrul = gameWindow.blit(b_dhandrul, (280, 250))
        b_vaindrum = pygame.image.load("Game Data\\b_vaindrum.png")
        b_vaindrum = pygame.transform.scale(b_vaindrum, (250, 50)).convert_alpha()
        b_vaindrum = gameWindow.blit(b_vaindrum, (530, 280))
        b_tinteev = pygame.image.load("Game Data\\b_tinteev.png")
        b_tinteev = pygame.transform.scale(b_tinteev, (250, 50)).convert_alpha()
        b_tinteev = gameWindow.blit(b_tinteev, (10, 220))
        b_mankey = pygame.image.load("Game Data\\b_mankey.png")
        b_mankey = pygame.transform.scale(b_mankey, (250, 50)).convert_alpha()
        b_mankey = gameWindow.blit(b_mankey, (280, 190))
        b_ganky = pygame.image.load("Game Data\\b_ganky.png")
        b_ganky = pygame.transform.scale(b_ganky, (250, 55)).convert_alpha()
        b_ganky = gameWindow.blit(b_ganky, (530, 160))
        b_dhrub = pygame.image.load("Game Data\\b_dhrub.png")
        b_dhrub = pygame.transform.scale(b_dhrub, (250, 50)).convert_alpha()
        b_dhrub = gameWindow.blit(b_dhrub, (10, 280))
        b_shiba = pygame.image.load("Game Data\\b_shiba.png")
        b_shiba = pygame.transform.scale(b_shiba, (250, 50)).convert_alpha()
        b_shiba = gameWindow.blit(b_shiba, (530, 100))
        b_shwarma = pygame.image.load("Game Data\\b_shwarma.png")
        b_shwarma = pygame.transform.scale(b_shwarma, (250, 50)).convert_alpha()
        b_shwarma = gameWindow.blit(b_shwarma, (530, 220))
        button_h = pygame.image.load("Game Data\\button_h.png")
        button_h = pygame.transform.scale(button_h, (30, 30)).convert_alpha()
        button_h = gameWindow.blit(button_h, (760, 350))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (680, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (640, 350))
        button_back = pygame.image.load("Game Data\\button_back.png")
        button_back = pygame.transform.scale(button_back, (30, 30)).convert_alpha()
        button_back = gameWindow.blit(button_back, (720, 350))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (600, 350))
        if click:
            if home_y == True:
                if button_h.collidepoint((mx, my)):
                    welcome()
                    click = False
            elif home_y == False:
                if button_h.collidepoint((mx, my)):
                    backtomm()
                    click = False
            if button_i.collidepoint((mx, my)):
                aboutus()
                click = False
            if button_back.collidepoint((mx, my)):
                r6 = False
                click = False
            if button_qmark.collidepoint((mx, my)):
                howtoplay()
                click = False
            if button_c.collidepoint((mx, my)):
                cntrls()
                click = False
            if b_default.collidepoint((mx, my)): 
                charforinfo = 'Game Data\\m_snake.png'
                click = False
                individualchar()
            if b_lyla.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_lyla.png'
                click = False
                individualchar()
            if b_katarina.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_katarina.png'
                click = False
                individualchar()
            if b_dhandrul.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_big smoke.png'
                click = False
                individualchar()
            if b_vaindrum.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_vaindrum.png'
                click = False
                individualchar()
            if b_tinteev.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_tinteev.png'
                click = False
                individualchar()
            if b_mankey.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_mankey.png'
                click = False
                individualchar()
            if b_ganky.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_ganky.png'
                click = False
                individualchar()
            if b_dhrub.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_dhrub.png'
                click = False
                individualchar()
            if b_shiba.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_shiba.png'
                click = False
                individualchar()
            if b_shwarma.collidepoint((mx, my)):
                charforinfo = 'Game Data\\m_shwarma.png'
                click = False
                individualchar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if event.key == pygame.K_BACKSPACE:
                    r6 = False
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        sound6.set_volume(0.0)
                        sound7.set_volume(0.0)
                        sound8.set_volume(0.0)
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        if theme == True:
                            sound6.set_volume(0.2)
                        if naagin == True:
                            sound7.set_volume(0.3)
                        if nokia == True:
                            sound8.set_volume(0.3)
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)
    
def char_sel():
    global character_timer
    global play_m
    global music_n
    global character
    character = None
    click = False
    r7 = True
    global g_exit
    global start_chartime
    start_chartime = 0
    g_exit = False
    characters = ['Snake', 'Lyla', 'Katarina', 'Big Smoke', 'Vaindrum', 'Tinteev', 'Mankey', 'Ganky', 'Dhrub', 'Shwarma']
    if play_m == False and music_n == True:
        pygame.mixer.music.pause()

    while r7 == True and g_exit == False:
        gameWindow.blit(charselect, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_default = pygame.image.load("Game Data\\default.png")
        button_default = pygame.transform.scale(button_default, (160, 70)).convert_alpha()
        button_default = gameWindow.blit(button_default, (30, 145))
        button_lyla = pygame.image.load("Game Data\\lyla.png")
        button_lyla = pygame.transform.scale(button_lyla, (160, 70)).convert_alpha()
        button_lyla = gameWindow.blit(button_lyla, (30, 230))
        button_katarina = pygame.image.load("Game Data\\katarina.png")
        button_katarina = pygame.transform.scale(button_katarina, (160, 70)).convert_alpha()
        button_katarina = gameWindow.blit(button_katarina, (30, 315))
        button_dhandrul = pygame.image.load("Game Data\\big smoke.png")
        button_dhandrul = pygame.transform.scale(button_dhandrul, (160, 70)).convert_alpha()
        button_dhandrul = gameWindow.blit(button_dhandrul, (220, 145))
        button_vaindrum = pygame.image.load("Game Data\\vaindrum.png")
        button_vaindrum = pygame.transform.scale(button_vaindrum, (160, 70)).convert_alpha()
        button_vaindrum = gameWindow.blit(button_vaindrum, (220, 230))
        button_tinteev = pygame.image.load("Game Data\\tinteev.png")
        button_tinteev = pygame.transform.scale(button_tinteev, (160, 70)).convert_alpha()
        button_tinteev = gameWindow.blit(button_tinteev, (220, 315))
        button_mankey = pygame.image.load("Game Data\\mankey.png")
        button_mankey = pygame.transform.scale(button_mankey, (160, 70)).convert_alpha()
        button_mankey = gameWindow.blit(button_mankey, (420, 145))
        button_ganky = pygame.image.load("Game Data\\ganky.png")
        button_ganky = pygame.transform.scale(button_ganky, (160, 70)).convert_alpha()
        button_ganky = gameWindow.blit(button_ganky, (420, 230))
        button_dhrub = pygame.image.load("Game Data\\dhrub.png")
        button_dhrub = pygame.transform.scale(button_dhrub, (175, 70)).convert_alpha()
        button_dhrub = gameWindow.blit(button_dhrub, (420, 315))
        button_shiba = pygame.image.load("Game Data\\shiba.png")
        button_shiba = pygame.transform.scale(button_shiba, (160, 70)).convert_alpha()
        button_shiba = gameWindow.blit(button_shiba, (610, 145))
        button_shwarma = pygame.image.load("Game Data\\shwarma.png")
        button_shwarma = pygame.transform.scale(button_shwarma, (160, 70)).convert_alpha()
        button_shwarma = gameWindow.blit(button_shwarma, (610, 230))
        button_random = pygame.image.load("Game Data\\random.png")
        button_random = pygame.transform.scale(button_random, (160, 70)).convert_alpha()
        button_random = gameWindow.blit(button_random, (610, 315))
        if click:
            if button_default.collidepoint((mx, my)):
                character = 'Snake'
                start_chartime = time.time()
                click = False
            if button_lyla.collidepoint((mx, my)):
                character = 'Lyla'
                start_chartime = time.time()
                click = False
            if button_katarina.collidepoint((mx, my)):
                character = 'Katarina'
                start_chartime = time.time()
                click = False
            if button_dhandrul.collidepoint((mx, my)):
                character = 'Big Smoke'
                start_chartime = time.time()
                click = False
            if button_vaindrum.collidepoint((mx, my)):
                character = 'Vaindrum'
                start_chartime = time.time()
                click = False
            if button_tinteev.collidepoint((mx, my)):
                character = 'Tinteev'
                start_chartime = time.time()
                click = False
            if button_mankey.collidepoint((mx, my)):
                character = 'Mankey'
                start_chartime = time.time()
                click = False
            if button_ganky.collidepoint((mx, my)):
                character = 'Ganky'
                start_chartime = time.time()
                click = False
            if button_dhrub.collidepoint((mx, my)):
                character = 'Dhrub'
                start_chartime = time.time()
                click = False
            if button_shiba.collidepoint((mx, my)):
                character = 'Shiba'
                start_chartime = time.time()
                click = False
            if button_shwarma.collidepoint((mx, my)):
                character = 'Shwarma'
                start_chartime = time.time()
                click = False
            if button_random.collidepoint((mx, my)):
                character = random.choice(characters)
                start_chartime = time.time()
                click = False
                
        cur_chartime = time.time()
        char_diff = float(cur_chartime) - float(start_chartime)
        char_diff = int(char_diff)
        if char_diff <= 3:
            text_screen2(f"Your character: {character}",white,220,80)
            text_screen2("Continue?" ,black,330,110)
            text_screen2(str(3-char_diff) ,white,393,140)
        if char_diff == 3:
            gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        play_m = True
                        music_n = False
                if event.key == pygame.K_BACKSPACE:
                    r7 = False
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def welcome():
    global home_y
    global play_m
    global music_n
    home_y = True
    click = False
    sound6.stop()
    sound7.stop()
    sound8.stop()
    global left
    global face
    global snakeface
    snakeface = "Game Data\\c_default.png"
    if left == True:
        face = pygame.transform.flip(face, True, False)
    pygame.mixer.music.load('Game Data\\menu.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
    global g_exit
    g_exit = False
    if play_m == False and music_n == True:
        pygame.mixer.music.pause()

    while not g_exit:
        gameWindow.fill(white)
        gameWindow.blit(menu, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.image.load("Game Data\\button1.png")
        button_1 = pygame.transform.scale(button_1, (180, 35)).convert_alpha()
        button_1 = gameWindow.blit(button_1, (310, 130))
        button_2 = pygame.image.load("Game Data\\button2.png")
        button_2 = pygame.transform.scale(button_2, (180, 35)).convert_alpha()
        button_2 = gameWindow.blit(button_2, (310, 175))
        button_3 = pygame.image.load("Game Data\\button3.png")
        button_3 = pygame.transform.scale(button_3, (180, 35)).convert_alpha()
        button_3 = gameWindow.blit(button_3, (310, 310))
        button_4 = pygame.image.load("Game Data\\button4.png")
        button_4 = pygame.transform.scale(button_4, (180, 35)).convert_alpha()
        button_4 = gameWindow.blit(button_4, (310, 220))
        button_5 = pygame.image.load("Game Data\\button5.png")
        button_5 = pygame.transform.scale(button_5, (180, 35)).convert_alpha()
        button_5 = gameWindow.blit(button_5, (310, 265))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (680, 350))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (760, 350))
        button_char = pygame.image.load("Game Data\\button_char.png")
        button_char = pygame.transform.scale(button_char, (30, 30)).convert_alpha()
        button_char = gameWindow.blit(button_char, (640, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (720, 350))
        if click:
            if button_1.collidepoint((mx, my)):
                char_sel()
                click = False
            if button_2.collidepoint((mx, my)):
                howtoplay()
                click = False
            if button_3.collidepoint((mx, my)):
                close()
                click = False
            if button_4.collidepoint((mx, my)):
                cntrls()
                click = False
            if button_5.collidepoint((mx, my)):
                char_info()
                click = False
            if button_c.collidepoint((mx, my)):
                cntrls()
                click = False
            if button_i.collidepoint((mx, my)):
                aboutus()
                click = False
            if button_qmark.collidepoint((mx, my)):
                howtoplay()
                click = False
            if button_char.collidepoint((mx, my)):
                char_info()
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    char_sel()
                if event.key == pygame.K_h:
                    howtoplay()
                if event.key == pygame.K_m:
                    if play_m == True:
                        pygame.mixer.music.pause()
                        play_m = False
                        music_n = True
                    elif play_m == False:
                        pygame.mixer.music.unpause()
                        play_m = True
                        music_n = False
                if event.key == pygame.K_c:
                    cntrls()
                if event.key == pygame.K_TAB:
                    char_info()
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True  
        pygame.display.update()
        clock.tick(60)

count_e = 0                        
def gameloop():
    global power_timer 
    global music_n 
    global g_exit 
    global play_m
    global start_time
    global diff
    global home_y
    global theme
    global left
    global naagin
    global nokia
    global snakeface
    global face
    global character
    global chartheme
    global charactertheme
    snakefaceability = False
    chartheme = True
    charactertheme = False
    left = False
    global playertheme
    if character == 'Snake':
        playertheme = "Game Data\\naagin.mp3"   
    elif character == 'Lyla':
        playertheme = "Game Data\\lyla.mp3"   
    elif character == 'Katarina':
        playertheme = "Game Data\\katarina.mp3"   
    elif character == 'Big Smoke':
        playertheme = "Game Data\\big smoke.mp3"   
    elif character == 'Vaindrum':
        playertheme = "Game Data\\vaindrum.mp3"   
    elif character == 'Tinteev':
        playertheme = "Game Data\\tinteev.mp3"   
    elif character == 'Mankey':
        playertheme = "Game Data\\mankey.mp3"   
    elif character == 'Ganky':
        playertheme = "Game Data\\ganky.mp3"   
    elif character == 'Dhrub':
        playertheme = "Game Data\\dhrub.mp3"   
    elif character == 'Shiba':
        playertheme = "Game Data\\shiba.mp3"   
    elif character == 'Shwarma':
        playertheme = "Game Data\\shwarma.mp3"  
    #theme = True
    #naagin = False
    home_y = False
    berry_choose = True
    prob_poison = ['poison_berry', 'No berry', 'No berry', 'No berry', 'No berry']
    poison_berry = 'No berry'
    power_act = None
    pygame.mixer.music.stop()  
    channel6.play(sound6, loops=-1)
    channel7.play(sound7, loops=-1)
    channel8.play(sound8, loops=-1)
    key3 = []
    l3_keys = []
    cheat_1 = [K_g,K_o,K_d]
    de_cheat_1 = []
    key32 = []
    l32_keys = []
    cheat_2 = [K_b,K_i,K_n,K_g,K_o]
    de_cheat_2 = []  
    key33 = []
    l33_keys = []
    cheat_3 = [K_n,K_a,K_a,K_g,K_i,K_n]
    de_cheat_3 = []
    key34 = []
    l34_keys = []
    cheat_4 = [K_n,K_o,K_k,K_i,K_a]
    de_cheat_4 = [] 
    if(not os.path.exists("Game Data\\highscore.txt")):
        with open("Game Data\\highscore.txt","w") as f:
            f.write("0")
    f = open("Game Data\\highscore.txt","r")
    highscore = f.read() 
    f.close()       
    g_exit = False
    game_over = False
    snake_x = 100
    snake_y = 100
    snake_size_x = 10
    snake_size_y = 10
    food_x = random.randint(10,790)
    food_y = random.randint(40,390)
    power_x = random.randint(10,790)
    power_y = random.randint(40,390)
    power_count = 0
    food_size_x = 10
    food_size_y = 10
    vel_x = 0
    vel_y = 0
    initial_vel = 5
    fps = 30
    score = 0
    clock = pygame.time.Clock()
    snake_lst = []
    snake_len = 1
    start_time = 0
    powers = ["Invincibility","Slow-mo"]
    if play_m == False and music_n == True:
        sound6.set_volume(0.0) 
        
    while not g_exit:
        global count_e
        count_e = time.time()
        if game_over:
            #Play again countdown
            t_limit = float(count_e) - float(count_s)
            t_limit = int(t_limit)
            if t_limit == 10:
                welcome()
            countdown_begin = time.time()
            with open("Game Data\\highscore.txt", "w" ) as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(end, (0, 0))
            text_screen(str(10 - t_limit), black, 380, 150)
            text_screen(str(score), orange, 480, 220)
            text_screen(str(highscore), orange, 480, 250)
            if score == 0:
                text_screen("Better Luck Next Time", orange, 200, 350)
            elif score >= int(highscore): 
                text_screen("Congrats! NEW HIGH SCORE!!!", orange, 120, 350) 
            elif score >= 10000:
                text_screen("Impressive", orange, 280, 350)
            elif score >= 100000:
                text_screen("You sure you didn't cheat?", orange, 120, 350)
            else:
                text_screen("GG", orange, 380, 350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    g_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()   
                    if event.key == pygame.K_ESCAPE:
                        backtomm()
        else:
            #naagin
            if l33_keys != cheat_3:
                sound7.set_volume(0.0)
                theme = True
                naagin = False
                #sound6.set_volume(0.2)
            elif l33_keys == cheat_3:
                sound6.set_volume(0.0)
                sound8.set_volume(0.0)
                pygame.mixer.music.stop()
                sound7.set_volume(0.3)
                play_m = True
                theme = False
                naagin = True
            #nokia
            if l34_keys != cheat_4:
                sound8.set_volume(0.0)
                theme = True
                nokia = False
                #sound6.set_volume(0.2)
            elif l34_keys == cheat_4:
                sound6.set_volume(0.0)
                sound7.set_volume(0.0)
                pygame.mixer.music.stop()
                sound8.set_volume(0.3)
                play_m = True
                theme = False
                nokia = True

            #snake face
            if snakefaceability == False:
                if character == 'Snake':
                    snakeface = "Game Data\\c_default.png"
                elif character == 'Lyla':
                    snakeface = "Game Data\\c_lyla.png"
                elif character == 'Katarina':
                    snakeface = "Game Data\\c_katarina.png"
                elif character == 'Big Smoke':
                    snakeface = "Game Data\\c_big smoke.png"
                elif character == 'Vaindrum':
                    snakeface = "Game Data\\c_vaindrum.png"
                elif character == 'Tinteev':
                    snakeface = "Game Data\\c_tinteev.png"
                elif character == 'Mankey':
                    snakeface = "Game Data\\c_mankey.png"
                elif character == 'Ganky':
                    snakeface = "Game Data\\c_ganky.png"
                elif character == 'Dhrub':
                    snakeface = "Game Data\\c_dhrub.png"
                elif character == 'Shiba':
                    snakeface = "Game Data\\c_shiba.png"
                elif character == 'Shwarma':
                    snakeface = "Game Data\\c_shwarma.png"
            elif snakefaceability == True:
                if character == 'Lyla':
                    snakeface = "Game Data\\c_lyla_act.png"
                elif character == 'Katarina':
                    snakeface = "Game Data\\c_katarina_act.png"
                elif character == 'Big Smoke':
                    snakeface = "Game Data\\c_big smoke_act.png"
                elif character == 'Vaindrum':
                    snakeface = "Game Data\\c_vaindrum_act.png"
                elif character == 'Tinteev':
                    snakeface = "Game Data\\c_tinteev_act.png"
                elif character == 'Mankey':
                    snakeface = "Game Data\\c_mankey_act.png"
                elif character == 'Ganky':
                    snakeface = "Game Data\\c_ganky_act.png"
                elif character == 'Dhrub':
                    snakeface = "Game Data\\c_dhrub_act.png"
                elif character == 'Shiba':
                    snakeface = "Game Data\\c_shiba_act.png"
                elif character == 'Shwarma':
                    snakeface = "Game Data\\c_shwarma_act.png"        

            face = pygame.image.load(snakeface)
            face = pygame.transform.scale(face, (23, 23)).convert_alpha()
            if left == True:
                face = pygame.transform.flip(face, True, False)

            keypress = pygame.key.get_pressed()    
            if keypress[pygame.K_RIGHT] or keypress[pygame.K_d]:
                vel_x = initial_vel
                vel_y = 0
                left = False
            if keypress[pygame.K_LEFT] or keypress[pygame.K_a]:
                vel_x = -initial_vel
                vel_y = 0
                left = True
            if keypress[pygame.K_UP] or keypress[pygame.K_w]:
                vel_y = -initial_vel
                vel_x = 0
            if keypress[pygame.K_DOWN] or keypress[pygame.K_s]:
                vel_y = initial_vel
                vel_x = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    g_exit = True
                if event.type == pygame.KEYDOWN:
                    # Cheat codes
                    #god
                    if l3_keys == cheat_1:
                        de_cheat_1.append(event.key)                    
                        if len(de_cheat_1) > 3:
                            del de_cheat_1[0]  
                            if de_cheat_1 == cheat_1:
                                l3_keys.append(event.key)
                                if len(l3_keys) > 3:
                                    del l3_keys[0]
                    if l3_keys != cheat_1 :
                        l3_keys.append(event.key)
                        if len(l3_keys) > 3:
                            del l3_keys[0]
                    key3.append(event.key)
                    if len(key3)>3:
                        del key3[0]

                    #bingo 
                    if l32_keys == cheat_2:
                        de_cheat_2.append(event.key)                    
                        if len(de_cheat_2) > 5:
                            del de_cheat_2[0]  
                            if de_cheat_2 == cheat_2:
                                l32_keys.append(event.key)
                                if len(l32_keys) > 5:
                                    del l32_keys[0]
                    if l32_keys != cheat_2 :
                        l32_keys.append(event.key)
                        if len(l32_keys) > 5:
                            del l32_keys[0]
                    key32.append(event.key)
                    if len(key32)>5:
                        del key32[0]

                    #naagin
                    if l33_keys == cheat_3:
                        de_cheat_3.append(event.key)                    
                        if len(de_cheat_3) > 6:
                            del de_cheat_3[0]  
                            if de_cheat_3 == cheat_3:
                                l33_keys.append(event.key)
                                if len(l33_keys) > 6:
                                    del l33_keys[0]
                    if l33_keys != cheat_3 :
                        l33_keys.append(event.key)
                        if len(l33_keys) > 6:
                            del l33_keys[0]
                    key33.append(event.key)
                    if len(key33)>6:
                        del key33[0]

                    #nokia
                    if l34_keys == cheat_4:
                        de_cheat_4.append(event.key)                    
                        if len(de_cheat_4) > 5:
                            del de_cheat_4[0]  
                            if de_cheat_4 == cheat_4:
                                l34_keys.append(event.key)
                                if len(l34_keys) > 5:
                                    del l34_keys[0]
                    if l34_keys != cheat_4 :
                        l34_keys.append(event.key)
                        if len(l34_keys) > 5:
                            del l34_keys[0]
                    key34.append(event.key)
                    if len(key34)>5:
                        del key34[0]

                    if event.key == pygame.K_ESCAPE:
                        backtomm()
                    if play_m == True:
                        if event.key == pygame.K_SPACE:
                            sound6.set_volume(0.0)
                            sound7.set_volume(0.0)
                            sound8.set_volume(0.0)
                            pygame.mixer.music.load(playertheme)
                            pygame.mixer.music.set_volume(0.3)
                            pygame.mixer.music.play(-1)
                            chartheme = True
                            charactertheme = True
                            play_m = False
                            music_n = False
                        if event.key == pygame.K_m:
                            sound6.set_volume(0.0)
                            sound7.set_volume(0.0)
                            sound8.set_volume(0.0)
                            play_m = False
                            music_n = True
                    elif play_m == False:
                        if charactertheme == True:
                            if event.key == pygame.K_m:
                                if chartheme == True:
                                    pygame.mixer.music.pause()
                                    music_n = True
                                    chartheme = False
                                elif chartheme == False:
                                    pygame.mixer.music.unpause()
                                    music_n = False
                                    chartheme = True
                            if event.key == pygame.K_SPACE:
                                sound6.set_volume(0.3)
                                pygame.mixer.music.stop()
                                charactertheme = False
                                play_m = True
                                music_n = False
                        elif charactertheme == False:
                            if event.key == pygame.K_m:
                                if theme == True:
                                    sound6.set_volume(0.2)
                                if naagin == True:
                                    sound7.set_volume(0.3)
                                if nokia == True:
                                    sound8.set_volume(0.3)
                                play_m = True
                                music_n = False 
                    if event.key == pygame.K_p:
                        power_timer = False
                        pause_scrn()
                    
                                      
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))

            #Snake eats food
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                channel1.play(sound1)
                score += 10
                snake_len += 2 
                food_x = random.randint(10,790)
                food_y = random.randint(40,390)
                if score > int(highscore) :
                    highscore = score

            #Snake collects orbs
            if abs(snake_x - power_x)<8 and abs(snake_y - power_y)<8:
                channel3.play(sound3)
                power_x = random.randint(10,790)
                power_y = random.randint(40,390)
                power_count += 1

            #Snake eats poison berry    
            if poison_berry == "poison_berry":
                if abs(snake_x - berry_x)<8 and abs(snake_y - berry_y)<8:
                    power_x = random.randint(10,790)
                    power_y = random.randint(40,390)
                    sound6.stop()
                    sound7.stop()
                    sound8.stop()
                    pygame.mixer.music.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    if left == True:
                        face = pygame.transform.flip(face, True, False)
                        left = False
                    game_over = True

            #Activating ability on random
            if power_count == 5:
                start_time = time.time()
                power_act = random.choice(powers)
                snakefaceability = True
                if left == True:
                    face = pygame.transform.flip(face, True, False)
                    #left = False
                if power_act == "Slow-mo":
                    channel5.play(sound5)
                if power_act == "Invincibility":
                    channel4.play(sound4)
                power_count = 0
            

            #Randomizing ploting of berries
            if berry_choose == True:
                poison_berry = random.choice(prob_poison)
                poison_time = time.time()
                if poison_berry == "poison_berry":
                    berry_x = random.randint(10,790)
                    berry_y = random.randint(40,390)
                berry_choose = False 

            cur_time = time.time()
            diff = float(cur_time) - float(start_time)
            diff = int(diff)
            berry_diff = float(cur_time) - float(poison_time)
            berry_diff = int(berry_diff)
            if berry_diff == 10:
                berry_choose = True

            #Displaying ability and its meter
            if diff < 0.5:
                text_screen2(f"{power_act}",blue,10,350)
            if diff <= 10:
                if power_act == "Slow-mo":
                    gameWindow.blit(ability_s, (550, 5))
                    initial_vel = 2.5
                    text_screen2(f": {10-diff}",blue,740,10)
                if power_act == "Invincibility":
                    gameWindow.blit(ability_i, (550, 5))
                    text_screen2(f": {10-diff}",blue,740,10)

            if diff == 10:
                power_act = None
                snakefaceability = False
            elif diff > 10 :
                initial_vel = 5


            #Displying Activation and deactivation of cheat codes
            if key3 == cheat_1:
                text_screen2("Cheat successfull",red,10,350)
            if key32 == cheat_2:
                text_screen2("Cheat successfull",red,10,350)
            if key33 == cheat_3:
                text_screen2("Music changed",red,10,350)
            if key34 == cheat_4:
                text_screen2("Music changed",red,10,350)

            #Movement of snake
            snake_y += vel_y
            snake_x += vel_x

            #Basic HUD
            text_screen2("Score: " + str(score), red, 5, 10)
            text_screen2("High Score: " + str(highscore), dark_green, 210, 10)

            #Size of snake increases
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            if len(snake_lst) > snake_len:
                del snake_lst[0]
            snake_h = snake_lst[-1]
            snake_head.append(snake_h)
            if len(snake_head) > 1:
                del snake_head[0]

            #Activating/Deactivating cheat codes
            if l32_keys != cheat_2:
                pass 
            elif l32_keys == cheat_2:
                score += 10
            if l3_keys == cheat_1 or power_act == "Invincibility":
                pass
            elif l3_keys != cheat_1 or power_act != "Invincibility":
                if head in snake_lst[:-1]:
                    sound6.stop()
                    sound7.stop()
                    sound8.stop()
                    pygame.mixer.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    if left == True:
                        face = pygame.transform.flip(face, True, False)
                        left = False
                    game_over = True
                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    sound6.stop()
                    sound7.stop()
                    sound8.stop()
                    pygame.mixer.music.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    if left == True:
                        face = pygame.transform.flip(face, True, False)
                        left = False
                    game_over = True

            if poison_berry != 'poison_berry':
                pygame.draw.rect(gameWindow,blue,[power_x,power_y,food_size_x,food_size_y])
            elif poison_berry == "poison_berry":
                pygame.draw.rect(gameWindow,purple,[berry_x,berry_y,food_size_x,food_size_y])
            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size_x,food_size_y])
            plot_snake(gameWindow,black,snake_lst, snake_size_x, snake_size_y)
            for x,y in snake_head:
                gameWindow.blit(face,[x-5,y-10])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

