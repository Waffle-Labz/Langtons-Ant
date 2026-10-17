# Langton's Ant

<img width="873" height="873" alt="image" src="https://github.com/user-attachments/assets/0685937d-e787-47e7-84d1-546625917fae" />

A 2D simulation of [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant), a cellular automaton in which an ant moves across a grid, changing cell colours according to simple rules. Despite its simplicity, the system produces complex patterns, including a repeating structure known as the *highway*.

Built with Python and Pygame.

## How It Works

The simulation consists of a grid of black and white cells and an ant that moves one cell at a time.

At each step, the ant follows two rules:

- **White cell:** Turn 90° clockwise, change the cell to black, and move forward.
- **Black cell:** Turn 90° anticlockwise, change the cell to white, and move forward.

The grid wraps around at its edges, allowing the ant to re-enter from the opposite side.

Although the rules are simple, repeated iterations produce increasingly complex patterns.

## Features

- Grid-based cellular automaton
- Directional movement with clockwise and anticlockwise turns
- Automatic cell colour changes
- Toroidal grid boundaries
- Configurable simulation dimensions, cell size, starting position, and steps per frame
- Pygame visualisation with a distinct colour for the ant

## Requirements

- Python 3
- Pygame

## Configuration

Simulation settings can be adjusted in `config.py`, including:

- Window width and height
- Cell size
- Initial ant position
- Number of simulation steps per frame
- Background, cell, and ant colours
- Frame timing

Increasing the number of steps per frame allows the simulation to advance more quickly.

## Project Structure

```text
langtons-ant/
├── main.py
├── ant.py
├── config.py
└── README.md
```

## Technologies

- Python
- Pygame

## Concepts Demonstrated

- Cellular automata
- Grid-based simulation
- Modular programming
- Emergent behaviour
- Real-time visualisation
