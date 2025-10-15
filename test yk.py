import pygame as pyg
import mysql.connector
from sys import exit
pyg.init()
init_time=pyg.time.get_ticks()
pyg.display.set_caption("Quiz")
#Constants:
screen_Dimensions=(1080,720)
Screen=pyg.display.set_mode(screen_Dimensions)
bg_color='#0268d2'
Font_Title=pyg.font.Font("bm-euljiro.ttf",70)
Font_Title_Small=pyg.font.Font("bm-euljiro.ttf",45)
Font_Answer=pyg.font.Font("bm-euljiro.ttf",30)
Quiz_name=Font_Title.render("Online Quiz",False,'Gold')
background = pyg.image.load('start_wall.jpeg')
clock=pyg.time.Clock()
#Variables:
Game_run=True
start=True
Sound_on=True
play_sound=True
show_general_instructions=True
#Functions:
def Draw_Screen():
    new_screen=pyg.display.set_mode(screen_Dimensions)
    new_screen.fill(bg_color)
    return new_screen
def Draw_button(text,but_x,but_y):
    text_rect=text.get_rect(center=(but_x,but_y))
    Screen.blit(text,text_rect)
    return {'rect':text_rect,'text':text}
def Is_clicked(button_rect,mouse_pos):
    if button_rect["rect"].collidepoint(mouse_pos) and event.type==pyg.MOUSEBUTTONDOWN:
        return True
    else:
        return False
def Is_hovered(button_rect,mouse_pos):
    if button_rect['rect'].collidepoint(mouse_pos):
        return True
    else:
        return False
def definetley_hovering(button_rect,mouse_pos,x,y):
    if button_rect['rect'].collidepoint(mouse_pos):
        text=button_rect['text']
        text_rendered=Font_Answer.render(text,False,"Turquoise")
        text_rect=text_rendered.get_rect(center=(x,y))
        Screen.blit(text_rendered,text_rect)
    pyg.display.update()
def start_screen():
    global start_rect
    global options_rect
    global quit_rect
    global show_general_instructions
    Screen.blit(background,(0,0))
    Draw_button(Quiz_name,540,100)
    start_rect=Draw_button(Font_Title_Small.render("START",False,'White'),540,300)
    options_rect=Draw_button(Font_Title_Small.render("OPTIONS",False,'White'),540,400)
    quit_rect=Draw_button(Font_Title_Small.render("QUIT",False,'White'),540,500)
    if  Is_hovered(start_rect,mouse_pos):
        Draw_button(Font_Title_Small.render("START",False,'Turquoise'),540,300)
    elif Is_hovered(options_rect,mouse_pos):
        Draw_button(Font_Title_Small.render("OPTIONS",False,'Turquoise'),540,400)
    elif Is_hovered(quit_rect,mouse_pos):
        Draw_button(Font_Title_Small.render("QUIT",False,'Turquoise'),540,500)
    if Is_clicked(quit_rect,mouse_pos):
        exit()
def options_screen():
    global start
    global play_sound
    global Sound_on
    Option_loop_bool=True
    while Option_loop_bool==True:
        sound_label = "Sound: ON" if Sound_on else "Sound: OFF"
        events=pyg.event.get()  
        mouse_pos=pyg.mouse.get_pos()
        Screen.fill(bg_color)
        mouse_pos = pyg.mouse.get_pos()
        Draw_button(Font_Title.render("OPTIONS",False,'Gold'),540,100)
        Sound_rect=Draw_button(Font_Title_Small.render(sound_label,False, 'White'),540, 350)       
        Draw_button(Font_Title_Small.render("Difficulty: Normal", False, 'White'),540, 460)
        back_rect= Draw_button(Font_Title_Small.render("Back", False,'White'),540,560)
        if Is_hovered(back_rect,mouse_pos):
            back_rect= Draw_button(Font_Title_Small.render("Back", False,'Turquoise'),540,560)
        if Is_hovered(Sound_rect,mouse_pos):
            Sound_rect=Draw_button(Font_Title_Small.render(sound_label, False, 'Turquoise'), 540, 350)    
        for event in events:
         if event.type==pyg.QUIT:
             exit()  
         if back_rect["rect"].collidepoint(mouse_pos) and event.type==pyg.MOUSEBUTTONDOWN:
            start=True
            Option_loop_bool=False
            break 
         if Sound_rect['rect'].collidepoint(mouse_pos) and event.type==pyg.MOUSEBUTTONDOWN:
             Sound_rect=Draw_button(Font_Title_Small.render(sound_label,False, 'White'),540, 350)
             Sound_on=not Sound_on
             play_sound=Sound_on
        pyg.display.update()
def General_instructions():
    global show_general_instructions
    while True:
     Screen.fill(bg_color)
     G_I_text=Font_Title_Small.render("General Instructions",False,"Gold")
     Draw_button(G_I_text,540,100)
while Game_run:
    mouse_pos=pyg.mouse.get_pos()
    events= pyg.event.get()
    for event in events:
        if event.type==pyg.QUIT:exit()
    if start==True:
     start_screen()
    if Is_clicked(start_rect,mouse_pos):
        start=False
        Screen.fill(bg_color)
    if Is_clicked(options_rect,mouse_pos):
        start=False
        options_screen()
    pyg.display.update()