import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
COUNT_BLOCKS = 20
MARGIN = 1

size = [400, 600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("snake")

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()

    screen.fill(FRAME_COLOR)
    for row in range(COUNT_BLOCKS):
        for calonka in range(COUNT_BLOCKS):
            if calonka % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + SIZE_BLOCK * calonka + calonka, 20 + SIZE_BLOCK * row + row, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
