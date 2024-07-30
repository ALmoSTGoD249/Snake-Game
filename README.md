# Snake-Game

## Overview
A modern version of the classic Snake game implemented in Python using the Pygame library. The game features a clean, dark-themed UI and allows players to select difficulty levels. The game also includes a menu for starting the game, selecting difficulty, and quitting, as well as a game over screen with options to retry or quit.

## Features
- **Difficulty Levels:** Easy, Medium, and Hard
- **Clean UI:** Dark gray background with bright green snake and red-orange food
- **Game Over Screen:** Allows players to retry or quit
- **Modern Aesthetics:** Includes subtle copyright notice

## Requirements
- Python 3.x
- Pygame library

## Installation
1. **Install Python**: Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

## Running the Game
1. Clone or download the repository.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the game script:
   ```bash
   python speed.py
   ```

## Code Overview

### `snake_game.py`
- **Initialization**: Sets up Pygame and game window.
- **Colors and Fonts**: Defines color schemes and font styles.
- **Functions**:
  - `score_display(score)`: Displays the current score.
  - `draw_snake(snake_block, snake_list)`: Renders the snake.
  - `display_message(msg, color, size)`: Displays messages on the screen.
  - `draw_menu(selected_option)`: Renders the main menu.
  - `draw_difficulty_menu(selected_difficulty)`: Renders the difficulty selection menu.
  - `draw_game_over_screen()`: Displays the game over screen.
  - `menu()`: Handles the main menu logic.
  - `difficulty_menu()`: Handles the difficulty selection logic.
  - `game_over_screen()`: Handles the game over screen logic.
  - `game_loop(difficulty)`: Main game loop that handles game logic and rendering.
  - `start_game()`: Starts the game by calling the menu and game loop.

## Customization
You can modify the following elements to customize the game:
- **Colors**: Change `background_color`, `snake_color`, `food_color`, and other color variables.
- **Fonts**: Adjust font styles by modifying `font_style`, `score_font`, `menu_font`, and `copyright_font`.
- **Difficulty Levels**: Adjust speeds and difficulty levels in the `difficulty_speed` dictionary.

## License
© ALmoSTGoD249

This project is licensed under the MIT License. 

## Contact
For any questions or feedback, please contact me at [soumadeepmaity2@gmail.com](mailto:soumadeepmaity2@gmail.com).

---

Feel free to customize the README further based on your project's specific needs or additional features.
