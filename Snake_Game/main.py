import pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # Clear screen
        self.parent_screen.blit(self.block, (self.x, self.y))  # Draw snake
        pygame.display.flip()  # Update display

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pygame Snake Game")
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_UP:
                        self.snake.move_up()
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                    elif event.key == K_LEFT:
                        self.snake.move_left()
                    elif event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            self.snake.draw()
            self.clock.tick(60)  # Cap frame rate to 60 FPS

if __name__ == "__main__":
    game = Game()
    game.run()
