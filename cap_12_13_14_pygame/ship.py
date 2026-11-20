import pygame

class Ship:
    """ Classe para cuidar  da espaçonave """
    
    def __init__(self, ai_game):
        """ Inicializa a espaçonave e defina sua posição inicial """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Coloca cada espaçonave nova na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        # Flags de movimento; comece com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
       """  Atualiza a posição da espaçonave com base na na flag de movimento """
       # Atualiza o valor de x da espaçonave, não o rect
       if self.moving_right and self.rect.right < self.screen_rect.rigth:
           self.rect.x += self.settings.ship_speed
       if self.moving_left and self.rect.left > 0:
           self.rect.x -= self.settings.ship_speed

       # Atualiza o objeto rect de self.x
       self.rect.x = self.x

    def blitme(self):
        """ Desenha a espaçonave em sua localização atual """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        pass
