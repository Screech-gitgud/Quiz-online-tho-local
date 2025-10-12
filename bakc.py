import pygame as pyg
from sys import exit


pyg.init()
screen = pyg.display.set_mode((1080, 720))
pyg.display.set_caption("Quiz")
clock = pyg.time.Clock()


font_title = pyg.font.Font('bm-euljiro.ttf', 100)
font_question = pyg.font.Font('bm-euljiro.ttf', 40)
font_answer = pyg.font.Font('bm-euljiro.ttf', 35)
menu_font = pyg.font.Font('bm-euljiro.ttf', 45)

WHITE = (255, 255, 255)
TURQUOISE = (0, 194, 203)
GOLD = (255, 215, 0)
BG_COLOR ='#0268d2'


background = pyg.image.load('start_wall.jpeg')


questions = [
    "Who was termed the title The Father of India?",
    "What is 2 + 2?"
]
answers = [
    ["a) Mahatma Gandhi", "b) Nehru", "c) Rajnath Kovind", "d) Bose"],
    ["1", "2", "3", "4"]
]
correct_answers = [0, 3]


score = 0
current_q = 0
ans_given = False
question_start_time = 0
delay_start_time = 0
sound_On=True
TIME_LIMIT = 15
DELAY_AFTER_ANSWER = 800


def draw_text(text, font, color, center):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=center)
    screen.blit(surf, rect)
    return rect

def is_hovered(text, font, center, mouse_pos):
    rect = font.render(text, True, WHITE).get_rect(center=center)
    return rect.collidepoint(mouse_pos)

def draw_answers(q_index):
    rects = []
    positions = [(270, 450), (810, 450), (270, 540), (810, 540)]

    for i in range(4):
        rect = draw_text(answers[q_index][i], font_answer, WHITE, positions[i])
        rects.append((rect, i))
    return rects

def show_question(index):
    draw_text(f"Q) {questions[index]}", font_question, WHITE, (540, 120))

def show_time_left(seconds):
    draw_text(f"Time: {seconds}", font_answer, WHITE, (150, 180))

def show_score(score):
    draw_text(f"Score: {score}", font_answer, WHITE, (930, 180))

def show_game_over(score):
    screen.fill((0, 0, 50))
    draw_text("Quiz Over", font_title, GOLD, (540, 200))
    draw_text(f"Your Score: {score}", font_question, WHITE, (540, 330))
    draw_text("Press ESC to return to menu", font_answer, WHITE, (540, 500))
    pyg.display.update()


def main_menu():
    while True:
        screen.fill(BG_COLOR)
        screen.blit(background, (0, 0))
        mouse_pos = pyg.mouse.get_pos()
        events = pyg.event.get()

        draw_text("Online Quiz", font_title, GOLD, (540, 100))

        start_rect = draw_text("Start", menu_font, TURQUOISE if is_hovered("Start", menu_font, (540, 280), mouse_pos) else WHITE, (540, 280))
        options_rect = draw_text("Options", menu_font, TURQUOISE if is_hovered("Options", menu_font, (540, 360), mouse_pos) else WHITE, (540, 360))
        quit_rect = draw_text("Quit", menu_font, TURQUOISE if is_hovered("Quit", menu_font, (540, 440), mouse_pos) else WHITE, (540, 440))

        pyg.display.update()

        for event in events:
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(mouse_pos):
                    return 'start'
                elif options_rect.collidepoint(mouse_pos):
                    return 'options'
                elif quit_rect.collidepoint(mouse_pos):
                    pyg.quit()
                    exit()

def option_screen():
    global sound_On
    global draw_rect
    flip=0
    while True:
        screen.fill(BG_COLOR)
        mouse_pos = pyg.mouse.get_pos()
        events = pyg.event.get()

        draw_text("Options", font_title, GOLD, (540, 100))
        if sound_On==True:
            draw_rect=draw_text("Sound: ON", font_answer, WHITE, (540, 250))
        else:
            draw_rect=draw_text("Sound: OFF", font_answer, WHITE, (540, 250))                         
        draw_text("Difficulty: Normal", font_answer, WHITE, (540, 320))
        back_rect = draw_text("Back", menu_font, TURQUOISE if is_hovered("Back", menu_font, (540, 500), mouse_pos) else WHITE, (540, 500))

        pyg.display.update()

        for event in events:
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
            if  draw_rect.collidepoint(mouse_pos) and event.type==pyg.MOUSEBUTTONDOWN:
                if sound_On==True:
                    sound_On=False
                else:
                    sound_On=True
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    return




while True:
    game_state = main_menu()

    if game_state == 'options':
        option_screen()
        continue

    elif game_state == 'start':
        current_q = 0
        score = 0
        ans_given = False
        game_over = False
        question_start_time = pyg.time.get_ticks()

        while not game_over:
            screen.fill(BG_COLOR)
            current_time = pyg.time.get_ticks()
            elapsed = (current_time - question_start_time) / 1000
            time_left = max(0, int(TIME_LIMIT - elapsed + 0.999))

            show_question(current_q)
            answer_rects = draw_answers(current_q)
            show_time_left(time_left)
            show_score(score)

            mouse_pos = pyg.mouse.get_pos()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    exit()
                elif not ans_given and event.type == pyg.MOUSEBUTTONDOWN:
                    for rect, idx in answer_rects:
                        if rect.collidepoint(mouse_pos):
                            ans_given = True
                            delay_start_time = current_time
                            if idx == correct_answers[current_q]:
                                score += 10
                            else:
                                score -= 5

            if not ans_given and elapsed >= TIME_LIMIT:
                ans_given = True
                delay_start_time = current_time
                score -= 5

            if ans_given and current_time - delay_start_time >= DELAY_AFTER_ANSWER:
                current_q += 1
                if current_q >= len(questions):
                    game_over = True
                else:
                    ans_given = False
                    question_start_time = pyg.time.get_ticks()

            pyg.display.update()
            clock.tick(60)
        while True:
            show_game_over(score)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    exit()
                elif event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE:
                    break
            else:
                continue
            break
print('hello')        

