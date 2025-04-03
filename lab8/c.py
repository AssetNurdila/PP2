import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    drawing = False
    shape = 'freehand'  # Default drawing mode
    start_pos = None  # For rectangle and circle
    color = (0, 0, 255)  # Default blue
    
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
                
                # Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    color = (0, 0, 0)  # Eraser mode
                
                # Shape selection
                if event.key == pygame.K_f:
                    shape = 'freehand'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_v:
                    shape = 'rectangle'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                
            if event.type == pygame.MOUSEBUTTONUP:
                if shape == 'rectangle':
                    pygame.draw.rect(screen, color, pygame.Rect(start_pos, (event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])))
                elif shape == 'circle':
                    center = start_pos
                    radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, color, center, radius)
                drawing = False
                
            if event.type == pygame.MOUSEMOTION and drawing and shape == 'freehand':
                pygame.draw.circle(screen, color, event.pos, radius)
                
        pygame.display.flip()
        clock.tick(60)

main()
