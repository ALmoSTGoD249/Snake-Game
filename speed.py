import pygame
import time
import random

pygame.init()

width, height = 800, 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Modern Snake Game')

# Colors
background_color = (30, 30, 30)  # Dark Gray
snake_color = (0, 255, 0)        # Bright Green
food_color = (255, 69, 0)        # Red-Orange
text_color = (255, 255, 255)     # White
button_color = (50, 150, 255)    # Blue
button_hover_color = (70, 200, 255) # Lighter Blue

# Snake properties
snake_block = 20
difficulty_speed = {'Easy': 20, 'Medium': 15, 'Hard': 10}

# Fonts
font_style = pygame.font.SysFont("arial", 30)
score_font = pygame.font.SysFont("arial", 40)
menu_font = pygame.font.SysFont("arial", 60)
copyright_font = pygame.font.SysFont("arial", 20)

clock = pygame.time.Clock()

# Score function
def score_display(score):
    value = score_font.render("Score: " + str(score), True, text_color)
    dis.blit(value, [10, 10])

# Snake function
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

# Display message function
def display_message(msg, color, size=30):
    font = pygame.font.SysFont("arial", size)
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [width / 2 - mesg.get_width() / 2, height / 3])

# Draw main menu
def draw_menu(selected_option):
    dis.fill(background_color)
    menu_title = menu_font.render("Snake Game - Python", True, text_color)
    dis.blit(menu_title, [width / 2 - menu_title.get_width() / 2, height / 4])

    options = ["Start", "Difficulty", "Quit"]
    for i, option in enumerate(options):
        color = button_hover_color if i == selected_option else button_color
        pygame.draw.rect(dis, color, [width / 2 - 100, height / 2 + i * 60, 200, 50])
        text = font_style.render(option, True, text_color)
        dis.blit(text, [width / 2 - text.get_width() / 2, height / 2 + i * 60 + 10])

    # Draw copyright notice
    copyright_text = copyright_font.render("© ALmoSTGoD249", True, text_color)
    dis.blit(copyright_text, [width - copyright_text.get_width() - 10, height - copyright_text.get_height() - 10])

    pygame.display.update()

# Draw difficulty menu
def draw_difficulty_menu(selected_difficulty):
    dis.fill(background_color)
    diff_title = menu_font.render("Select Difficulty", True, text_color)
    dis.blit(diff_title, [width / 2 - diff_title.get_width() / 2, height / 4])

    options = ["Easy", "Medium", "Hard"]
    for i, option in enumerate(options):
        color = button_hover_color if i == selected_difficulty else button_color
        pygame.draw.rect(dis, color, [width / 2 - 100, height / 2 + i * 60, 200, 50])
        text = font_style.render(option, True, text_color)
        dis.blit(text, [width / 2 - text.get_width() / 2, height / 2 + i * 60 + 10])

    # Draw copyright notice
    copyright_text = copyright_font.render("© ALmoSTGoD249", True, text_color)
    dis.blit(copyright_text, [width - copyright_text.get_width() - 10, height - copyright_text.get_height() - 10])

    pygame.display.update()

# Draw game over screen
def draw_game_over_screen():
    dis.fill(background_color)
    display_message("Game Over! Choose an option", text_color, 40)
    score_display(length_of_snake - 1)
    
    buttons = [("Retry", width / 2 - 100, height / 2), ("Quit", width / 2 - 100, height / 2 + 70)]
    
    for i, (text, x, y) in enumerate(buttons):
        color = button_hover_color if i == 0 else button_color
        pygame.draw.rect(dis, color, [x, y, 200, 50])
        btn_text = font_style.render(text, True, text_color)
        dis.blit(btn_text, [x + 60, y + 10])

    # Draw copyright notice
    copyright_text = copyright_font.render("© ALmoSTGoD249", True, text_color)
    dis.blit(copyright_text, [width - copyright_text.get_width() - 10, height - copyright_text.get_height() - 10])

    pygame.display.update()

# Main menu function
def menu():
    selected_option = 0
    menu_options = ["Start", "Difficulty", "Quit"]

    while True:
        draw_menu(selected_option)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Start":
                        return
                    elif menu_options[selected_option] == "Difficulty":
                        difficulty = difficulty_menu()
                        if difficulty:
                            return difficulty
                    elif menu_options[selected_option] == "Quit":
                        pygame.quit()
                        quit()

        pygame.display.update()

# Difficulty menu function
def difficulty_menu():
    selected_difficulty = 0
    difficulty_options = ["Easy", "Medium", "Hard"]

    while True:
        draw_difficulty_menu(selected_difficulty)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_difficulty = (selected_difficulty + 1) % len(difficulty_options)
                elif event.key == pygame.K_UP:
                    selected_difficulty = (selected_difficulty - 1) % len(difficulty_options)
                elif event.key == pygame.K_RETURN:
                    return difficulty_options[selected_difficulty]
                    
        pygame.display.update()

# Handle game over screen with buttons
def game_over_screen():
    game_close = True

    while game_close:
        draw_game_over_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Check if Retry button is clicked
                if width / 2 - 100 <= mouse_x <= width / 2 + 100 and height / 2 <= mouse_y <= height / 2 + 50:
                    return True  # Retry the game
                
                # Check if Quit button is clicked
                if width / 2 - 100 <= mouse_x <= width / 2 + 100 and height / 2 + 70 <= mouse_y <= height / 2 + 120:
                    pygame.quit()
                    quit()
        
        pygame.display.update()

# Main game loop
def game_loop(difficulty):
    global length_of_snake
    snake_speed = difficulty_speed[difficulty]
    
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            if not game_over_screen():
                game_loop(difficulty)  # Retry game
            game_over = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(background_color)
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
def start_game():
    difficulty = menu()  
    if difficulty:
        game_loop(difficulty)

start_game()
