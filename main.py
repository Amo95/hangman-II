import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# load images
images = list()
for i in range(7):
  image =  pygame.image.load(f"hangman{i}.png")
  images.append(image)

# game variables
hangman_status = 0


FPS = 60
clock = pygame.time.Clock()
run = True

while run:
  clock.tick(FPS)

  # update andrefresh display
  # background
  win.fill((255,255,255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

      # mouse events
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      print(pos)

pygame.quit()