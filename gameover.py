import pygame
import sys
from constants import *


def draw_buttons(screen):
    font = pygame.font.Font("simsun", 50)

    # Define button properties
    restart_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50)
    quit_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 20, 200, 50)

    # Draw buttons
    pygame.draw.rect(screen, (0, 255, 0), restart_button)  # Green Restart button
    pygame.draw.rect(screen, (255, 0, 0), quit_button)    # Red Quit button

    # Draw text
    restart_text = font.render("Restart", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))
    screen.blit(restart_text, (restart_button.x + 50, restart_button.y + 5))
    screen.blit(quit_text, (quit_button.x + 65, quit_button.y + 5))

    pygame.display.flip()

    return restart_button, quit_button


def game_over_loop(screen):
    font = pygame.font.Font(None, 74)  # Font for "Game Over" text
    button_font = pygame.font.Font(None, 50)  # Font for button text

    # Define the button properties
    restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)

    # Draw the "Game Over" screen
    screen.fill((0, 0, 0))  # Fill the screen with black
    text = font.render("Game Over", True, (255, 0, 0))  # Render "Game Over" in red
    screen.blit(
        text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100)
    )  # Center the text

    # Draw buttons
    pygame.draw.rect(screen, (0, 255, 0), restart_button)  # Green Restart button
    restart_text = button_font.render("Restart", True, (0, 0, 0))  # Black text
    screen.blit(
        restart_text,
        (
            restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2,
            restart_button.y + restart_button.height // 2 - restart_text.get_height() // 2,
        ),
    )

    pygame.draw.rect(screen, (255, 0, 0), quit_button)  # Red Quit button
    quit_text = button_font.render("Quit", True, (0, 0, 0))  # Black text
    screen.blit(
        quit_text,
        (
            quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
            quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2,
        ),
    )

    pygame.display.flip()  # Update the display

    # Game Over loop to handle events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the program if the window is closed
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse clicks
                mouse_pos = event.pos  # Get the mouse position when clicked

                if restart_button.collidepoint(mouse_pos):  # Check if "Restart" was clicked
                    return  # Exit this loop to restart the game
                elif quit_button.collidepoint(mouse_pos):  # Check if "Quit" was clicked
                    pygame.quit()
                    sys.exit()  # Exit the game completely