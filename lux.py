#imports
import pygame

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fps_counter = pygame.time.Clock.get_fps

while running:
    #quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.draw.circle(screen, "blue", player_pos, 40)
    keys = pygame.key.get_pressed()

    #fps counter
    fps = fps_counter(clock)
    font = pygame.font.Font("C:\Windows\Fonts\SHOWG.ttf", 30)
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    

    # WASD functionality
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    pygame.display.flip()
    dt = clock.tick(120) / 1000
pygame.quit()