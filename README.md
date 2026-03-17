# Tie Fighter Targeting Game (Python)

## Overview

This project is a **Python arcade-style shooting game** built using the **Turtle graphics module**.

The player controls a targeting reticle and must shoot down a randomly moving **Tie Fighter** inspired by the *Star Wars* universe. The objective is to successfully hit the Tie Fighter **three times** while it moves unpredictably across a space-themed background.

The game demonstrates key programming concepts including:

* Object-oriented programming
* Event-driven input
* Collision detection
* Randomized movement
* Game loops and state management
* Turtle graphics animation

---

# Game Preview

The game window contains:

* A **space-themed background**
* Randomly placed **stars and planets**
* A **moving Tie Fighter**
* A **red targeting reticle**
* Laser blasts fired by the player

The player must aim carefully to destroy the Tie Fighter before it escapes.

---

# Gameplay

### Objective

Hit the Tie Fighter **three times** to win the game.

### Controls

| Key      | Action             |
| -------- | ------------------ |
| ↑        | Move reticle up    |
| ↓        | Move reticle down  |
| ←        | Move reticle left  |
| →        | Move reticle right |
| Spacebar | Fire laser         |
| Escape   | Quit game          |

---

# Game Mechanics

### Tie Fighter Movement

The Tie Fighter moves randomly across the screen using trigonometric movement.

* Random direction
* Continuous motion
* Bounces off screen boundaries

Movement uses cosine and sine calculations for directional travel.

---

### Laser System

When the **spacebar** is pressed:

* A red laser blast fires from the reticle
* The laser spreads outward in four directions
* The laser originates from the reticle center

The laser remains active until it either:

* Hits the Tie Fighter
* Is released by the player

---

### Collision Detection

Hit detection uses the **distance formula**:

```
distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
```

If the distance between the reticle and the Tie Fighter is less than a defined threshold, the hit is registered.

Each successful hit increases the player's score.

---

### Scoring

The score appears in the **top-left corner** of the screen.

Example:

```
Score: 2 / 3
```

After **three successful hits**, the game ends.

---

# Game Over Screen

When the player reaches three hits:

* The screen displays **Game Over**
* The player is prompted to press **Escape** to exit

---

# Project Structure

```
Tie Fighter Game
│
├── Tie_Fighter_Game.py
├── Tie Fighter Game.sln
├── Tie Fighter Game.pyproj
└── configuration files
```

The main game logic is located in:

```
Tie_Fighter_Game.py
```

---

# Code Structure

The program is organized into several classes:

### TieFighter

Handles:

* Drawing the Tie Fighter
* Random movement
* Boundary detection

---

### Reticle

Handles:

* Crosshair drawing
* Player-controlled movement
* Position tracking

---

### Laser

Handles:

* Laser firing
* Drawing laser beams
* Collision detection

---

### Game

Controls the overall game:

* Game loop
* Score tracking
* Collision handling
* Event listeners
* Game over screen

---

# Technologies Used

Python
Turtle Graphics
Random library
Math library

---

# How to Run

1. Install Python
2. Download the project
3. Run the main script

```
python Tie_Fighter_Game.py
```

The Turtle graphics window will open and the game will start automatically.

---

# Concepts Demonstrated

Object-Oriented Programming
Event-driven programming
Game loop design
Collision detection mathematics
Graphical rendering using Turtle
Keyboard input handling

---

# Possible Improvements

Future improvements could include:

* Sound effects for laser firing
* Animated Tie Fighter graphics
* Difficulty levels
* Increasing enemy speed
* Score tracking between rounds
* Multiple enemies
* Health system or timer

---

# Author

AJ Flower

University Programming Project
