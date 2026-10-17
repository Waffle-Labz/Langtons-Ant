
import pygame

from config import *
from ant import Ant


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Langton's Ant")
    clock = pygame.time.Clock()

    grid_width = WIDTH // CELL_SIZE
    grid_height = HEIGHT // CELL_SIZE

    # Grid stores only cell states: 0 = white, -1 = black
    grid = [[0] * grid_height for _ in range(grid_width)]

    ant = Ant(START_X // CELL_SIZE, START_Y // CELL_SIZE)

    # Draw the initially empty grid once
    screen.fill(BG_COLOR)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Advance the simulation
        for _ in range(STEPS_PER_FRAME):
            old_x, old_y = ant.x, ant.y

            # Move updates the cell the ant leaves and changes its direction
            ant.move(grid)

            # Redraw the cell the ant has just left
            cell_state = grid[old_x][old_y]
            color = BLACK if cell_state == -1 else BG_COLOR

            pygame.draw.rect(
                screen,
                color,
                (
                    old_x * CELL_SIZE,
                    old_y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

        # Draw the ant separately from the underlying grid
        pygame.draw.rect(
            screen,
            ACTIVE,
            (
                ant.x * CELL_SIZE,
                ant.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
        )

        pygame.display.flip()
        clock.tick(max(1, round(1 / FRAME_DELAY)))

    pygame.quit()

if __name__ == "__main__":
    main()
