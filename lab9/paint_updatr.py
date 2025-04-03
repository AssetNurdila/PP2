import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15  # Радиус кисти для свободного рисования
    drawing = False  # Флаг    показывающий, идёт ли рисование
    shape = 'freehand'  # — свободное рисование
    start_pos = None  # Начальная точка  rjhlbyf для фигур
    color = (0, 0, 255)  # Цвет по умолчанию — синий
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Выбор цвета
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Красный
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Зелёный
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Синий
                elif event.key == pygame.K_e:
                    color = (0, 0, 0)  # Чёрный (ластик)
                
                # Выбор формы
                if event.key == pygame.K_f:
                    shape = 'freehand'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_v:
                    shape = 'rectangle'
                elif event.key == pygame.K_s:
                    shape = 'square'
                elif event.key == pygame.K_t:
                    shape = 'triangle_right'
                elif event.key == pygame.K_e:
                    shape = 'triangle_equilateral'
                elif event.key == pygame.K_h:
                    shape = 'rhombus'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                
            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if shape == 'rectangle':
                    pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
                elif shape == 'square':
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) # formulas
                    pygame.draw.rect(screen, color, pygame.Rect(start_pos, (side, side)))
                elif shape == 'circle':
                    radius = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(screen, color, start_pos, radius)
                elif shape == 'triangle_right':

                    pygame.draw.polygon(screen, color, [start_pos, (start_pos[0], end_pos[1]), end_pos])
                elif shape == 'triangle_equilateral':
                    height = abs(end_pos[1] - start_pos[1])
                    base = height * (2 / math.sqrt(3))
                    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1]),
                                                         (start_pos[0] - base // 2, end_pos[1]),
                                                         (start_pos[0] + base // 2, end_pos[1])])
                elif shape == 'rhombus':
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1] - height // 2),
                                                         (start_pos[0] - width // 2, start_pos[1]),
                                                         (start_pos[0], start_pos[1] + height // 2),
                                                         (start_pos[0] + width // 2, start_pos[1])])
                drawing = False
                
            if event.type == pygame.MOUSEMOTION and drawing and shape == 'freehand':
                pygame.draw.circle(screen, color, event.pos, radius)
                
        pygame.display.flip()
        clock.tick(60)

main()
