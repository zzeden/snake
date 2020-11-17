import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
COUNT_BLOCKS = 20

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
    for calonka in range(COUNT_BLOCKS):
        pygame.draw.rect(screen, WHITE, [10 + SIZE_BLOCK * calonka, 20, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
