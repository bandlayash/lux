# imports
import pygame
import asyncio



async def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0

    # Initial settings for player
    player_pos = pygame.Vector2(25, screen.get_height() - 50)  # Bottom-left corner position
    player_angle = 0  # Angle in degrees
    rotation_speed = 200  # Rotation speed in degrees per second

    #flashlight sprite
    player_sprite = pygame.image.load("flashlight.png").convert_alpha()  # Add transparency support
    player_sprite = pygame.transform.scale(player_sprite, (player_sprite.get_width() // 2, player_sprite.get_height() // 2))  # Match your current rectangle size


    # FPS counter function
    fps_counter = pygame.time.Clock.get_fps
    while True:
        # quit window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((255, 255, 255))

        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Rotation with A and D keys
        if keys[pygame.K_a]:
            player_angle += rotation_speed * dt
        if keys[pygame.K_d]:
            player_angle -= rotation_speed * dt

        # Drawing the rotated rectangle
        #rect_surface = pygame.Surface((50, 200), pygame.SRCALPHA)  # Create a new surface for the rectangle
        #pygame.draw.rect(rect_surface, "black", (0, 0, 50, 200))
        rotated_surface = pygame.transform.rotate(player_sprite, player_angle)
        rotated_rect = rotated_surface.get_rect(center=player_pos)  # Update position to center of rotation
        screen.blit(rotated_surface, rotated_rect.topleft)

        # FPS counter
        fps = fps_counter(clock)
        font = pygame.font.Font(None, 30)
        fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))
        screen.blit(fps_text, (10, 10))

        # Update display and timing
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        await asyncio.sleep(0)
        
asyncio.run(main())


    
