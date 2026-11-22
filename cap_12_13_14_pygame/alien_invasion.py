import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import Gamestats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Cria uma instâmcia para armazenar estatísticas do jogo
        self.stats = Gamestats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Inicia Ivasão Alienígena em um estado inativo
        self.game_active = False

        # Cria o botão Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._uppdate_bullets()
                self._update_aliens()
                
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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Responde à colisões alienígenas """
        # Remove todos os projéteis e os alienígenas que tenham colidido
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destrói os projéteis existentes e cria uma frota nova
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """ Verifica se a frota está na borda e, em seguida, atualiza as posições """
        self._check_fleet_edges()
        self.aliens.update()

        # Detecta colisões entre alienígenas e espaçonaves
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Procura por alienígenas se chocando contra a parte inferior da tela
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """ Verifica se algum alienígena chegou à parte inferior da tela """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata isso como se a espaçonave tivesse sido abatida
                self.ship_hit()
                break

    def _ship_hit(self):
        """ Responde à espaçonave sendo abatida por um alienígena """
        if self.stats.ships_left > 0:
            # Drecrementa ships_left
            self.stats.ships_left -=1

            # Descarta quaisquer projéteis e alienígenas restantes
            self.bullets.empty()
            self.aliens.empty()

            # Cria uma frota nova e centraliza a espaçonave
            self._create_fleet()
            self.ship.center_ship()

            # pausa
            sleep(0.5)

        else:
            self.game_active = False
    
    def _create_fleet(self):
        """ Cria a frota de alienígenas """
        # Cria um alienígena econtinua adicionando alienígenas
        # Até que não haja mais espaço
        # O distanciamento entre os alienígenas é a largura
        # de um alienígena e uma altura de alienígena
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien_height

        current_x, current_Y = alien_width, alien_height
        while current_Y < (self.settings.screen_height - 3 * alien_width):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_Y)
                current_x += 2 * alien_width

            # Termina uma fileira; redefine o valor de x, e incrementa o valor de y
            current_x = alien_width
            current_Y += 2 * alien_height

    def _check_fleet_edges(self):
        """ Responde apropriadamente se algum alienígena alcançou uma borda """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Faz toda a frota descer e mudar de direção """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _create_alien(self, x_position, y_position):
        """ Cria um alienígena e o posiciona na frota """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
                            
    def _update_screen(self):
        """ Atualiza as imagens na tela e mude para a nova tela """
        self.screen.fill(self.settings.bg_collor)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Desenha o botão Play se o jogo estiver inativo
        if not self.game_active:
            self.play_button()

        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()
        self.clock.tick(60)
        
if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    ai = AlienInvasion()
    ai.run_game()