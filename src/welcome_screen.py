import pygame


class WelcomeScreen():
    def __init__(self, root):
        self.root = root
        font = pygame.font.SysFont('digitaltsplum', 70)
        img = font.render('Cellular Automaton', True,(81, 113, 165))
        self.center_element(img, 40)

    def center_element(self, text_img: pygame.Surface, y:int):
        rect = text_img.get_rect()
        rect_width = rect.right - rect.left
        left_x = (self.root.size[0] - rect_width)/2
        self.root.display.blit(text_img, (left_x, 20))


    def render(self):
        self.check_event()
        pygame.display.update()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x,y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.root.init_grid()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    self.init_grid()
            if event.type == pygame.QUIT:
                pygame.quit()