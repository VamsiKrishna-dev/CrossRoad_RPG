import pytest
import pygame
from game import Game
from gameObject import GameObject
from enemy import Enemy
from player import Player


def test_init():
    game = Game()
    assert game.width == 600
    assert game.height == 600
    assert game.level == 1.0
    assert isinstance(game.game_window, pygame.Surface)
    assert isinstance(game.background, GameObject) 
    assert isinstance(game.treasure, GameObject)
    assert isinstance(game.player, Player)
    assert isinstance(game.enemies[0], Enemy)

def test_reset_map():
    game = Game()
    game.level = 2.0
    game.reset_map()
    assert game.player.speed == 2
    assert isinstance(game.enemies[0], Enemy)
    assert len(game.enemies) == 2
    game.level = 4.0
    game.reset_map()
    assert isinstance(game.enemies[0], Enemy)
    assert len(game.enemies) == 3

def test_move_objects():
    game = Game()
    game.player.x = 10
    game.player.y = 10
    game.move_objects(-1)
    assert game.player.y == 8
    assert game.player.x == 10
    game.move_objects(1)
    assert game.player.y == 10

def test_detect_collision():
    game = Game()
    game.player.x = 10
    game.player.y = 10
    game.player.width = 30
    game.player.height = 30
    game.treasure.x = 15
    game.treasure.y = 15
    game.treasure.width = 20
    game.treasure.height = 20
    assert game.detect_collision(game.player, game.treasure) == True
    game.treasure.x = 50
    game.treasure.y = 50
    assert game.detect_collision(game.player, game.treasure) == False

def test_is_collided():
    game = Game()
    game.player.x = 10
    game.player.y = 10
    game.player.width = 30
    game.player.height = 30
    game.treasure.x = 15
    game.treasure.y = 15
    game.treasure.width = 20
    game.treasure.height = 20
    assert game.is_collided() == True
    assert game.level == 1.5
    game.treasure.x = 50
    game.treasure.y = 50
    assert game.is_collided() == False
