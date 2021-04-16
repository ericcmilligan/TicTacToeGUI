import pygame
import os
from turtle import onscreenclick

Width, Height = 800, 500
pygame.init()
Window = pygame.display.set_mode((Width, Height))
Grid_Image = pygame.image.load("ASSETS\grid.png").convert()
pygame.display.set_caption("Tic Tac Toe")
Grid = pygame.transform.scale(Grid_Image, (Width, Height))
run = True
fps = 30



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        Window.fill((0, 0, 0))
        Window.blit(Grid, [0, 0])
        pygame.display.update()



main()

if __name__ == "__main__":
    main()
