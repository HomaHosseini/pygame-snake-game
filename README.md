# Snake Game — Python & Pygame

A 2D Snake game built with Python and Pygame, featuring custom sprite graphics, keyboard controls, fruit collection, obstacles, score tracking, and a restart button.

## Features

- **Snake movement:** Control the snake using the arrow keys.
- **Fruit collection:** Collect apples to grow the snake and earn points.
- **Different fruit values:** Three fruit types award different numbers of points.
- **Obstacle collision:** Avoid the obstacle and the boundaries of the game board.
- **Self-collision detection:** The game ends when the snake runs into itself.
- **Score tracking:** Display the current score and the highest score achieved during the session.
- **Custom graphics:** Use separate sprites for the snake's head, body, turns, tail, fruit, and obstacle.
- **Start and restart screens:** Use interactive buttons to start or restart a game.

## Technologies

- Python
- Pygame
- Object-oriented programming
- 2D graphics and event-driven programming

## Controls

| Key           | Action     |
| ------------- | ---------- |
| ↑ Up arrow    | Move up    |
| ↓ Down arrow  | Move down  |
| ← Left arrow  | Move left  |
| → Right arrow | Move right |

## Project Structure

```text
pygame-snake-game/
├── main.py
├── assets/
│   ├── snake head up.png
│   ├── snake head down.png
│   ├── snake head right.png
│   ├── snake head left.png
│   ├── apple.png
│   ├── apple2.png
│   ├── apple3.png
│   └── ...
└── README.md
```

## Implementation Overview

The game uses several classes to organize its logic:

- `SNAKE`: Maintains the snake's body, movement direction, growth, and sprite selection.
- `FRUIT`: Generates fruit at random grid positions and assigns a point value.
- `OBSTACLE`: Defines and draws the obstacle.
- `MAIN`: Coordinates game updates, collision checks, scoring, and rendering.
- `Button`: Implements the start and restart buttons.

The game board is grid-based. The snake moves at timed intervals, while Pygame handles rendering and user input.
