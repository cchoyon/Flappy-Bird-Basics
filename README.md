# Flappy Bird - Core Mechanics (Python + Pygame)

This is a basic implementation of the **core mechanics** of the classic Flappy Bird game using Python and Pygame. It’s designed to be easy to understand, especially for beginners learning about 2D game development.

## 🎮 Game Features

- **Gravity**: The player automatically falls down due to gravity.
- **Jumping**: Press the `SPACE` key to jump upward.
- **Pillars**: Randomly generated obstacle pillars come from the right.
- **Collision Detection**: The game ends if the player touches a pillar or the ground.
- **Game Restart**: Press `R` after a game over to restart everything.

## 🧠 Core Concepts Covered

- Pygame window and game loop
- Sprite creation with `pygame.Rect`
- Gravity and jump logic
- Keyboard input handling
- Collision detection with `.colliderect()`
- Procedural generation of obstacles (pillars)
- Resetting game state for restart

## 🚀 How to Run

1. Install Pygame:
   ```bash
   pip install pygame
