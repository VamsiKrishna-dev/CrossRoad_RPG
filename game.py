import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.white_color = (255, 255, 255)
        self.level = 1.0

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.background = GameObject(
            0, 0, self.width, self.height, "assets/background.png"
        )

        self.treasure = GameObject(285, 30, 35, 35, "assets/treasure.png")

        self.reset_map()

        

    def reset_map(self):
        self.player = Player(285, 550, 30, 30, "assets/player.png", 2)

        speed = 3 + (self.level * 2)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 90, 30, 30, "assets/enemy.png", 3),
                Enemy(550, 250, 30, 30, "assets/enemy.png", 3),
                Enemy(0, 400, 30, 30, "assets/enemy.png", 3),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(550, 250, 30, 30, "assets/enemy.png", 3),
                Enemy(0, 400, 30, 30, "assets/enemy.png", 3),
            ]
        else:
            self.enemies = [
                Enemy(550, 250, 30, 30, "assets/enemy.png", 3),
            ]

    def draw_objects(self):
        self.game_window.fill(self.white_color)
        self.game_window.blit(
            self.background.image, (self.background.x, self.background.y)
        )
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:

            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.movement(player_direction, self.height)
        for enemy in self.enemies:
            enemy.movement(self.width)

    def detect_collision(self, object1, object2):

        if object1.y > (object2.y + object2.height):
            return False
        elif (object1.y + object1.height) < object2.y:
            return False

        if object1.x > (object2.x + object2.width):
            return False
        elif (object1.x + object1.width) < object2.x:
            return False

        return True

    def is_collided(self):

        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False

    def game_loop(self):
        player_direction = 0
        while True:
            # Handle Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                    else:
                        pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
            # Execute Logic

            self.move_objects(player_direction)

            # Update Display
            self.draw_objects()

            # # Detect Collisions
            if self.is_collided():
                self.reset_map()

            self.clock.tick(60)
