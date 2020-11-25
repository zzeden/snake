import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
HEADER_COLOR = (0,204,153)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1

size = [(SIZE_BLOCK + MARGIN) * COUNT_BLOCKS + 20, (SIZE_BLOCK + MARGIN) * COUNT_BLOCKS + HEADER_MARGIN + 10]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("snake")

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for calonka in range(COUNT_BLOCKS):
            if row % 2 == 0:
                if calonka % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
            else:
                if calonka % 2 == 0:
                    color = WHITE
                else:
                    color = BLUE
            pygame.draw.rect(screen, color, [10 + SIZE_BLOCK * calonka + calonka, HEADER_MARGIN + SIZE_BLOCK * row + row, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
