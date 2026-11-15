import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():

    def __init__(self):
        """ inicializa o jogo e cria recursos de jogo """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()
            self.ship.update()
            self._uppdate_bullets()
            self._update_screen()
            self.clock.tick(60)
          
    def _check_events(self):
        """ Responde as teclas pressionadas e a eventos do mouse """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                elif event.type == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

    def _check_keydown_events(self, event):
        """ Responde a teclas clicadas """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
    
    def _check_keyup_events(self, event):
        """ Responde a teclas soltas """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        """ Cria um novo projétil e o adiciona ao grupo de projéteis """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                                  
                          
    def _update_bullets(self):
        """ Atualiza a posição dos projéteis e descarta projéteis antigos"""
        # Atualiza as posições dos projéteis
        self.bullets.update()
        
        # Descarta os projéteis que desaparecem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """ Atualiza as imagens na tela e mude para a nova tela """
        self.screen.fill(self.settings.bg_collor)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()
        self.clock.tick(60)
        
if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()