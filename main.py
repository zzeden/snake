import pygame
import time

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1

snake_block = [(1, 1), (1, 2), (1, 3), (2, 3)]
size = [(SIZE_BLOCK + MARGIN) * COUNT_BLOCKS + 20, (SIZE_BLOCK + MARGIN) * COUNT_BLOCKS + HEADER_MARGIN + 10]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("snake")


def draw_block(colori, rowi, columni):
    pygame.draw.rect(screen, colori,
                     [10 + SIZE_BLOCK * columni + columni, HEADER_MARGIN + SIZE_BLOCK * rowi + rowi, SIZE_BLOCK,
                      SIZE_BLOCK])


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()
        if event.type == pygame.key.key_code("down"):
            print("down")
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
            draw_block(color, row, calonka)

    time.sleep(1)
    for s in snake_block:
        draw_block(SNAKE_COLOR, s[0] ,s[1])

    pygame.display.flip()
