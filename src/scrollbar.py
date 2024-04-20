import pygame


GRAY = (197,194,197)
BLUE = (0,0,255)
WHITE = (255,255,255)

class ScrollBar(object):
    def __init__(self,window, image_height):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.y_axis = 0
        self.image_height = image_height
        self.change_y = 0
        
        bar_height = int((self.height - 40) / (image_height / (self.height * 1.0)))
        self.bar_rect = pygame.Rect(self.width - 20,20,20,bar_height)
        self.bar_up = pygame.Rect(self.width - 20,0,20,20)
        self.bar_down = pygame.Rect(self.width - 20,self.height - 20,20,20)
        
        self.bar_up_image = pygame.image.load("images/up.png").convert()
        self.bar_down_image = pygame.image.load("images/down.png").convert()
        
        self.on_bar = False
        self.mouse_diff = 0
        
    def update(self):
        self.y_axis += self.change_y
        
        if self.y_axis > 0:
            self.y_axis = 0
        elif (self.y_axis + self.image_height) < self.height:
            self.y_axis = self.height - self.image_height
            
        height_diff = self.image_height - self.height
        
        scroll_length = self.height - self.bar_rect.height - 40
        bar_half_lenght = self.bar_rect.height / 2 + 20
        
        if self.on_bar:
            pos = pygame.mouse.get_pos()
            self.bar_rect.y = pos[1] - self.mouse_diff
            if self.bar_rect.top < 20:
                self.bar_rect.top = 20
            elif self.bar_rect.bottom > (self.height - 20):
                self.bar_rect.bottom = self.height - 20
            
            self.y_axis = int(height_diff / (scroll_length * 1.0) * (self.bar_rect.centery - bar_half_lenght) * -1)
        else:
            self.bar_rect.centery =  scroll_length / (height_diff * 1.0) * (self.y_axis * -1) + bar_half_lenght
             
        
    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.bar_rect.collidepoint(pos):
                self.mouse_diff = pos[1] - self.bar_rect.y
                self.on_bar = True
            elif self.bar_up.collidepoint(pos):
                self.change_y = 5
            elif self.bar_down.collidepoint(pos):
                self.change_y = -5
                
        if event.type == pygame.MOUSEBUTTONUP:
            self.change_y = 0
            self.on_bar = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.change_y = 5
            elif event.key == pygame.K_DOWN:
                self.change_y = -5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.change_y = 0
            elif event.key == pygame.K_DOWN:
                self.change_y = 0
                
    def draw(self):
        print("drawing")
        pygame.draw.rect(self.window,GRAY,self.bar_rect)
        
        # self.window.blit(self.bar_up_image,(self.width - 20,0))
        # self.window.blit(self.bar_down_image,(self.width - 20,self.height - 20))