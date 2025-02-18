import pygame
import sys
import math
from constants import *

# Helper function to draw buttons
def draw_button(screen, button_rect, text, font, color, text_color):
    pygame.draw.rect(screen, color, button_rect)
    button_text = font.render(text, True, text_color)
    screen.blit(button_text, (
        button_rect.x + button_rect.width // 2 - button_text.get_width() // 2,
        button_rect.y + button_rect.height // 2 - button_text.get_height() // 2,
    ))

def draw_high_score(screen, score_font, pulse):
    yellow_pulse = int(255 * pulse)
    high_score_text = score_font.render("NEW HIGH SCORE!", True, (255, yellow_pulse, 0))
    
    scale = 1.0 + (pulse * 0.2)
    scaled_width = int(high_score_text.get_width() * scale)
    scaled_height = int(high_score_text.get_height() * scale)
    
    scaled_text = pygame.transform.scale(high_score_text, (scaled_width, scaled_height))
    text_x = SCREEN_WIDTH // 2 - scaled_width // 2
    text_y = SCREEN_HEIGHT // 2 - 120
    screen.blit(scaled_text, (text_x, text_y))

def game_over_loop(screen, score_display):
    # Initialize fonts
    font = pygame.font.SysFont("simsun", 74)
    button_font = pygame.font.SysFont("simsun", 50)
    score_font = pygame.font.SysFont("simsun", 36)
    
    restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.pos
                if restart_button.collidepoint(mouse_pos):
                    return
                elif quit_button.collidepoint(mouse_pos):
                    score_display.update_high_score()
                    pygame.quit()
                    sys.exit()

        # Animation logic
        current_time = pygame.time.get_ticks()
        pulse = (math.sin(current_time * 0.005) + 1) * 0.5

        screen.fill(SCREEN_COLOR)

        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 250))

        score_text = score_font.render(f"Final Score: {score_display.score}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 70))

        if score_display.check_high_score():
            draw_high_score(screen, score_font, pulse)

        # Draw buttons using helper function
        draw_button(screen, restart_button, "Restart", button_font, (0, 255, 0), (0, 0, 0))
        draw_button(screen, quit_button, "Quit", button_font, (255, 0, 0), (0, 0, 0))

        pygame.display.flip()
