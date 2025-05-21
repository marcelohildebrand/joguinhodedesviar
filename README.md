# Desvie das Formas - A Pygame Dodge Game

## Description
"Desvie das Formas" is an exciting arcade-style game built with Pygame. The player controls a blue circle and must skillfully dodge an onslaught of falling red shapes, including squares and triangles. The primary objective is to achieve the highest possible score while strategically managing a limited number of lives. The game concludes when the player runs out of lives, at which point they can view their score and attempt to earn a spot on the leaderboard.

## Features
*   **Scoring System**: Earn points for each shape successfully dodged. The longer you survive, the higher your score!
*   **Lives System**: Players start with a set number of lives, losing one for each collision with a falling shape.
*   **Game Over Screen**: When all lives are lost, a "Game Over" screen is displayed, showing the player's final score. From here, players can choose to restart the game or view the leaderboard.
*   **Persistent Leaderboard**: The game features a persistent leaderboard that saves the top 10 scores along with the dates they were achieved. This information is stored in a `historico.json` file.
*   **Game History**: Every game session, including the score and date, is recorded in the `historico.json` file, allowing players to track their progress over time.

## Setup Instructions
1.  **Ensure Python is Installed**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).
2.  **Install Pygame**: The core gameplay relies on the Pygame library. Install it using pip:
    ```bash
    pip install pygame
    ```
3.  **Other Dependencies**: Additional Python packages required for the game are listed in `requirements.txt`. While Pygame is the primary dependency for gameplay, you can install all dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `requirements.txt` might not exist yet or might need to be created if other specific libraries are used beyond Pygame).

## How to Run
1.  **Navigate to the Project Directory**: Open your terminal or command prompt and change to the directory where you've saved the game files.
    ```bash
    cd path/to/your/game_directory
    ```
2.  **Run the Game**: Execute the main game file using Python:
    ```bash
    python app.py
    ```

Enjoy the game!
