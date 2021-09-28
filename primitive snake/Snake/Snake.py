import pygame 
import random
import time
import os
from pygame.constants import K_b, K_d, K_g, K_i, K_n, K_o
pygame.mixer.init()
pygame.mixer.pre_init()
pygame.init()

screen_width,screen_height = 800,400
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("RETRO SNAKE")
pygame.display.update()

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

bgimg = pygame.image.load("Game Data\\level.jpg")
bgimg = pygame.transform.scale(bgimg, (800, 400)).convert_alpha()
menu = pygame.image.load("Game Data\\menu.png")
menu = pygame.transform.scale(menu, (800, 400)).convert_alpha()
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
ability_i = pygame.image.load("Game Data\\meter_i.png")
ability_i = pygame.transform.scale(ability_i, (185, 35)).convert_alpha()
ability_s = pygame.image.load("Game Data\\meter_s.png")
ability_s = pygame.transform.scale(ability_s, (185, 55)).convert_alpha()

pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
sound1 = pygame.mixer.Sound('Game Data\\food.mp3')
sound2 = pygame.mixer.Sound('Game Data\\gameover.mp3')
sound2.set_volume(0.3)
sound3 = pygame.mixer.Sound('Game Data\\power.mp3')

font = pygame.font.SysFont(None, 55)
font2 = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

home_y = True
power_timer = True
play_m = True
music_n = False
sfx_n = False

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snake_lst,snake_size_x,snake_size_y):
    for x,y in snake_lst:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size_x,snake_size_y])

def close():
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def backtomm():
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
                pygame.mixer.music.pause()
                music_n = True
                play_m = False
                click = False
        elif music_y.collidepoint((mx, my)) == True and play_m == False:
            if click:
                pygame.mixer.music.unpause()
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
                if event.key == pygame.K_h:
                    howtoplay()
                if event.key == pygame.K_i:
                    aboutus()
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_ESCAPE:
                    backtomm()
                if play_m == True:        
                    if event.key == pygame.K_m:
                        pygame.mixer.music.pause()
                        play_m = False
                        music_n = True
                elif play_m == False:
                    if event.key == pygame.K_m:
                        pygame.mixer.music.unpause()
                        play_m = True 
                        music_n = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

def howtoplay():
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
        button_h = gameWindow.blit(button_h, (680, 350))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (720, 350))
        button_c2 = pygame.image.load("Game Data\\button_c.png")
        button_c2 = pygame.transform.scale(button_c2, (25, 20)).convert_alpha()
        button_c2 = gameWindow.blit(button_c2, (185, 310))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (760, 350))
        if home_y == True:
            if button_h.collidepoint((mx, my)):
                if click:
                    welcome()
                    click = False
        elif home_y == False:
            if button_h.collidepoint((mx, my)):
                if click:
                    backtomm()
                    click = False
        if button_c.collidepoint((mx, my)):
            if click:
                cntrls()
                click = False
        if button_c2.collidepoint((mx, my)):
            if click:
                cntrls()
                click = False
        if button_i.collidepoint((mx, my)):
            if click:
                aboutus()
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
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True      
        pygame.display.update()
        clock.tick(60)

def aboutus():
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
        button_h = gameWindow.blit(button_h, (680, 350))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (720, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (760, 350))
        if home_y == True:
            if button_h.collidepoint((mx, my)):
                if click:
                    welcome()
                    click = False
        elif home_y == False:
            if button_h.collidepoint((mx, my)):
                if click:
                    backtomm()
                    click = False
        if button_c.collidepoint((mx, my)):
            if click:
                cntrls()
                click = False
        if button_qmark.collidepoint((mx, my)):
            if click:
                howtoplay()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True     
        pygame.display.update()
        clock.tick(60)

def cntrls():
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
        button_h = gameWindow.blit(button_h, (680, 350))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (760, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (720, 350))
        if home_y == True:
            if button_h.collidepoint((mx, my)):
                if click:
                    welcome()
                    click = False
        elif home_y == False:
            if button_h.collidepoint((mx, my)):
                if click:
                    backtomm()
                    click = False
        if button_i.collidepoint((mx, my)):
            if click:
                aboutus()
                click = False
        if button_qmark.collidepoint((mx, my)):
            if click:
                howtoplay()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        pygame.display.update()
        clock.tick(60)
 
def welcome():
    click = False
    pygame.mixer.music.load('Game Data\\menu.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
    global g_exit
    g_exit = False
    while not g_exit:
        gameWindow.fill(white)
        gameWindow.blit(menu, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.image.load("Game Data\\button1.png")
        button_1 = pygame.transform.scale(button_1, (180, 40)).convert_alpha()
        button_1 = gameWindow.blit(button_1, (320, 150))
        button_2 = pygame.image.load("Game Data\\button2.png")
        button_2 = pygame.transform.scale(button_2, (180, 40)).convert_alpha()
        button_2 = gameWindow.blit(button_2, (320, 200))
        button_3 = pygame.image.load("Game Data\\button3.png")
        button_3 = pygame.transform.scale(button_3, (180, 40)).convert_alpha()
        button_3 = gameWindow.blit(button_3, (320, 250))
        button_c = pygame.image.load("Game Data\\button_c.png")
        button_c = pygame.transform.scale(button_c, (30, 30)).convert_alpha()
        button_c = gameWindow.blit(button_c, (680, 350))
        button_i = pygame.image.load("Game Data\\button_i.png")
        button_i = pygame.transform.scale(button_i, (30, 30)).convert_alpha()
        button_i = gameWindow.blit(button_i, (760, 350))
        button_qmark = pygame.image.load("Game Data\\button_qmark.png")
        button_qmark = pygame.transform.scale(button_qmark, (30, 30)).convert_alpha()
        button_qmark = gameWindow.blit(button_qmark, (720, 350))
        if button_1.collidepoint((mx, my)):
            if click:
                gameloop()
                click = False
        if button_2.collidepoint((mx, my)):
             if click:
                howtoplay()
                click = False
        if button_3.collidepoint((mx, my)):
            if click:
                close()
                click = False
        if button_c.collidepoint((mx, my)):
            if click:
                cntrls()
                click = False
        if button_i.collidepoint((mx, my)):
            if click:
                aboutus()
                click = False
        if button_qmark.collidepoint((mx, my)):
            if click:
                howtoplay()
                click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                if event.key == pygame.K_h:
                    howtoplay()
                if event.key == pygame.K_c:
                    cntrls()
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
    home_y = False
    berry_choose = True
    prob_poison = ['poison_berry', 'No berry', 'No berry', 'No berry', 'No berry']
    poison_berry = 'No berry'
    power_act = None
    pygame.mixer.music.load("Game Data\\theme.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)  
    key3 = []
    l3_keys = []
    cheat_1 = [K_g,K_o,K_d]
    de_cheat_1 = []
    key32 = []
    l32_keys = []
    cheat_2 = [K_b,K_i,K_n,K_g,K_o]
    de_cheat_2 = []  
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
        pygame.mixer.music.pause()
        
    while not g_exit:
        global count_e
        count_e = time.time()
        if game_over:
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
            keypress = pygame.key.get_pressed()    
            if keypress[pygame.K_RIGHT] or keypress[pygame.K_d]:
                vel_x = initial_vel
                vel_y = 0
            if keypress[pygame.K_LEFT] or keypress[pygame.K_a]:
                vel_x = -initial_vel
                vel_y = 0
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
                    if event.key == pygame.K_ESCAPE:
                        backtomm()
                    if event.key == pygame.K_m:
                        if play_m == True:
                            pygame.mixer.music.pause()
                            play_m = False
                            music_n = True
                        elif play_m == False:
                            pygame.mixer.music.unpause()
                            play_m = True
                            music_n = False                        
                    if event.key == pygame.K_p:
                        power_timer = False
                        pause_scrn()
                    
                    # Cheat
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
                     
                    if l32_keys == cheat_2:
                        de_cheat_2.append(event.key)                    
                        if len(de_cheat_2) > 5:
                            del de_cheat_2[0]  
                            if de_cheat_2 == cheat_2:
                                l32_keys.append(event.key)
                                if len(l32_keys) > 3:
                                    del l32_keys[0]
                    if l32_keys != cheat_2 :
                        l32_keys.append(event.key)
                        if len(l32_keys) > 5:
                            del l32_keys[0]
                    key32.append(event.key)
                    if len(key32)>5:
                        del key32[0]                        
                                      
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                channel1.play(sound1)
                score += 10
                snake_len += 1 
                food_x = random.randint(10,790)
                food_y = random.randint(40,390)
                if score > int(highscore) :
                    highscore = score
            if abs(snake_x - power_x)<8 and abs(snake_y - power_y)<8:
                channel3.play(sound3)
                power_x = random.randint(10,790)
                power_y = random.randint(40,390)
                power_count += 1
                
            if poison_berry == "poison_berry":
                if abs(snake_x - berry_x)<8 and abs(snake_y - berry_y)<8:
                    power_x = random.randint(10,790)
                    power_y = random.randint(40,390)
                    pygame.mixer.music.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    game_over = True

            if power_count == 5:
                start_time = time.time()
                power_act = random.choice(powers)  
                power_count = 0
            
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
            elif diff > 10 :
                initial_vel = 5

            if key3 == cheat_1:
                text_screen2("Cheat successfull",red,10,350)
            if key32 == cheat_2:
                text_screen2("Cheat successfull",red,10,350)
            snake_y += vel_y
            snake_x += vel_x

            text_screen2("Score: " + str(score), red, 5, 10)
            text_screen2("High Score: " + str(highscore), dark_green, 210, 10)

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            if len(snake_lst) > snake_len:
                del snake_lst[0]
            if l32_keys != cheat_2:
                pass 
            elif l32_keys == cheat_2:
                score += 10
            if l3_keys == cheat_1 or power_act == "Invincibility":
                pass
            elif l3_keys != cheat_1 or power_act != "Invincibility":
                if head in snake_lst[:-1]:
                    pygame.mixer.music.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    game_over = True
                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    pygame.mixer.music.stop()
                    channel2.play(sound2)
                    count_s = time.time()
                    game_over = True

            if poison_berry != 'poison_berry':
                pygame.draw.rect(gameWindow,blue,[power_x,power_y,food_size_x,food_size_y])
            elif poison_berry == "poison_berry":
                pygame.draw.rect(gameWindow,purple,[berry_x,berry_y,food_size_x,food_size_y])
            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size_x,food_size_y])
            plot_snake(gameWindow,black,snake_lst, snake_size_x, snake_size_y)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

