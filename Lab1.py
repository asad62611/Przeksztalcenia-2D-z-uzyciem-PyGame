import pygame
import sys

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Polygon Transformation")

clock = pygame.time.Clock()

def draw_polygon(polygon, position):
    screen.blit(polygon, position)

def main():
    num_sides = 13
    radius = 150

    original_polygon = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    original_polygon.fill((0, 0, 0, 0))
    pygame.draw.polygon(original_polygon, BLUE, [(radius + radius * pygame.math.Vector2(1, 0).rotate(360 / num_sides * i).x,
                                                   radius + radius * pygame.math.Vector2(1, 0).rotate(360 / num_sides * i).y)
                                                  for i in range(num_sides)])

    angle = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                screen.fill(YELLOW)
                if event.key == pygame.K_1:
                    draw_polygon(original_polygon, (0, SCREEN_HEIGHT - original_polygon.get_height()))
                elif event.key == pygame.K_2:
                    rotated_scaled_polygon = pygame.transform.rotozoom(original_polygon, 45, 1.5)
                    draw_polygon(rotated_scaled_polygon, (0, SCREEN_HEIGHT - rotated_scaled_polygon.get_height()))
                elif event.key == pygame.K_3:
                    squeezed_polygon = pygame.transform.scale(original_polygon, (int(radius * 2 * 0.5), radius * 2))
                    squeezed_polygon = pygame.transform.flip(squeezed_polygon, False, True)
                    draw_polygon(squeezed_polygon, (0, SCREEN_HEIGHT - squeezed_polygon.get_height()))
                elif event.key == pygame.K_4:
                    stretched_polygon = pygame.transform.scale(original_polygon, (int(radius * 2 * 1.5), radius * 2))
                    draw_polygon(stretched_polygon, (0, SCREEN_HEIGHT - stretched_polygon.get_height()))
                elif event.key == pygame.K_5:
                    squeezed_top_down_polygon = pygame.transform.scale(original_polygon, (radius * 2, int(radius * 2 * 1.5)))
                    draw_polygon(squeezed_top_down_polygon, (0, 0))
                elif event.key == pygame.K_6:
                    rotated_polygon = pygame.transform.rotate(original_polygon, 90)
                    draw_polygon(rotated_polygon, (0, SCREEN_HEIGHT - rotated_polygon.get_height()))
                elif event.key == pygame.K_7:
                    mirrored_squeezed_polygon = pygame.transform.scale(original_polygon, (int(radius * 2 * 0.5), radius * 2))
                    mirrored_squeezed_polygon = pygame.transform.flip(mirrored_squeezed_polygon, True, False)
                    draw_polygon(mirrored_squeezed_polygon, (0, SCREEN_HEIGHT - mirrored_squeezed_polygon.get_height()))
                elif event.key == pygame.K_8:
                    angle += 30 
                    transformed_polygon = pygame.transform.rotozoom(original_polygon, angle, 1)
                    transformed_polygon = pygame.transform.scale(transformed_polygon, (int(radius * 2 * 1.2), int(radius * 2 * 0.8)))
                    draw_polygon(transformed_polygon, ((SCREEN_WIDTH - transformed_polygon.get_width()) // 2, (SCREEN_HEIGHT - transformed_polygon.get_height()) // 2))
                elif event.key == pygame.K_9:
                    mirrored_stretched_polygon = pygame.transform.scale(original_polygon, (int(radius * 2 * 1.5), radius * 2))
                    mirrored_stretched_polygon = pygame.transform.flip(mirrored_stretched_polygon, False, True)
                    draw_polygon(mirrored_stretched_polygon, (SCREEN_WIDTH - mirrored_stretched_polygon.get_width(), SCREEN_HEIGHT - mirrored_stretched_polygon.get_height()))
                elif event.key == pygame.K_0:
                    screen.fill((255,255,255))
                    pygame.draw.circle(screen, (0,0,0),(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2), 200 )
                    pygame.draw.rect(screen , YELLOW, ( SCREEN_WIDTH/2-100 , SCREEN_HEIGHT/2-100 , 200 , 200) )

        pygame.display.flip()
        clock.tick(1000)

if __name__ == "__main__":
    main()
