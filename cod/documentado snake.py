# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:37:58 2024

@author: nayde
"""

import pygame
import time
import random

class SnakeGame:
    """
    Clase que representa el juego de Snake.

    Attributes:
        WIDTH (int): Ancho de la pantalla del juego.
        HEIGHT (int): Alto de la pantalla del juego.
        screen (pygame.Surface): Superficie de la pantalla del juego.
        clock (pygame.time.Clock): Reloj del juego para controlar la velocidad.
        snake_block (int): Tamaño del bloque de la serpiente.
        snake_speed (int): Velocidad de la serpiente.
        font_style (pygame.font.Font): Estilo de la fuente utilizada para mostrar texto.
        apple1_img (pygame.Surface): Imagen de la manzana 1.
        apple2_img (pygame.Surface): Imagen de la manzana 2.
        CELESTE (tuple): Color celeste utilizado en el juego.
        RED (tuple): Color rojo utilizado en el juego.
        GREEN (tuple): Color verde utilizado en el juego.
        BLUE (tuple): Color azul utilizado en el juego.
    """

    def __init__(self):
        """
        Inicializa el juego de Snake y configura la pantalla.

        """
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake_block = 15
        self.snake_speed = 10
        self.font_style = pygame.font.SysFont(None, 50)
        self.apple1_img = pygame.image.load("C:/Users/nayde/Desktop/Proyecto-personal/data/apple1.jpg")
        self.apple2_img = pygame.image.load("C:/Users/nayde/Desktop/Proyecto-personal/data/apple2.png")
        self.apple1_img = pygame.transform.scale(self.apple1_img, (self.snake_block*2, self.snake_block*2))
        self.apple2_img = pygame.transform.scale(self.apple2_img, (self.snake_block*2, self.snake_block*2))
        self.CELESTE = (135, 206, 250)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

    @property
    def snake_list(self):
        """
        Obtiene la lista del snake.

        Returns:
            list: Lista del snake.
        """
        return self._snake_list

    @snake_list.setter
    def snake_list(self, snake_list):
        """
        Establece la lista del snake.

        Parameters:
            snake_list (list): Lista del snake.
        """
        self._snake_list = snake_list

    @property
    def snake2_list(self):
        """
        Obtiene la lista del segundo snake.

        Returns:
            list: Lista del segundo snake.
        """
        return self._snake2_list

    @snake2_list.setter
    def snake2_list(self, snake2_list):
        """
        Establece la lista del segundo snake.

        Parameters:
            snake2_list (list): Lista del segundo snake.
        """
        self._snake2_list = snake2_list

    @property
    def length_of_snake(self):
        """
        Obtiene la longitud del snake.

        Returns:
            int: Longitud del snake.
        """
        return self._length_of_snake

    @length_of_snake.setter
    def length_of_snake(self, length_of_snake):
        """
        Establece la longitud del snake.

        Parameters:
            length_of_snake (int): Longitud del snake.
        """
        self._length_of_snake = length_of_snake

    @property
    def length_of_snake2(self):
        """
        Obtiene la longitud del segundo snake.

        Returns:
            int: Longitud del segundo snake.
        """
        return self._length_of_snake2

    @length_of_snake2.setter
    def length_of_snake2(self, length_of_snake2):
        """
        Establece la longitud del segundo snake.

        Parameters:
            length_of_snake2 (int): Longitud del segundo snake.
        """
        self._length_of_snake2 = length_of_snake2

    def our_snake(self, snake_block, snake_list, color):
        """
        Dibuja el snake en la pantalla.

        Parameters:
            snake_block (int): Tamaño del bloque del snake.
            snake_list (list): Lista del snake.
            color (tuple): Color del snake.
        """
        for x in snake_list:
            pygame.draw.rect(self.screen, color, [x[0], x[1], snake_block, snake_block])

    def message(self, msg, color):
        """
        Muestra un mensaje en la pantalla.

        Parameters:
            msg (str): Mensaje a mostrar.
            color (tuple): Color del mensaje.
        """
        mesg = self.font_style.render(msg, True, color)
        self.screen.blit(mesg, [self.WIDTH / 6, self.HEIGHT / 3])

    def generate_food_position(self):
        """
        Genera una posición aleatoria para la manzana.

        Returns:
            tuple: Posición aleatoria para la manzana.
        """
        foodx = random.randrange(0, self.WIDTH - self.snake_block * 2, self.snake_block)
        foody = random.randrange(0, self.HEIGHT - self.snake_block * 2, self.snake_block)
        return foodx, foody

    def game_loop(self):
        """
        Bucle principal del juego.

        Main game loop.
        """
        self.game_over = False
        self.game_close = False

        self.x1 = self.WIDTH // 2
        self.y1 = self.HEIGHT // 2
        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.length_of_snake = 1

        self.foodx1, self.foody1 = self.generate_food_position()
        self.foodx2, self.foody2 = self.generate_food_position()

        self.x2 = self.WIDTH // 4
        self.y2 = self.HEIGHT // 4
        self.x2_change = 0
        self.y2_change = 0

        self.snake2_list = []
        self.length_of_snake2 = 1

        while not self.game_over:
            while self.game_close:
                self.screen.fill(self.CELESTE)
                self.message("Game Over! Press Q-Quit or C-Play Again", self.RED)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN: # Controla la serpiente 1
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -self.snake_block
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = self.snake_block
                        self.x1_change = 0

                    elif event.key == pygame.K_a: # Controla la serpiente 2
                        self.x2_change = -self.snake_block
                        self.y2_change = 0
                    elif event.key == pygame.K_d:
                        self.x2_change = self.snake_block
                        self.y2_change = 0
                    elif event.key == pygame.K_w:
                        self.y2_change = -self.snake_block
                        self.x2_change = 0
                    elif event.key == pygame.K_s:
                        self.y2_change = self.snake_block
                        self.x2_change = 0
                        
            # Verifica si la serpiente ha chocado con el borde
            if self.x1 >= self.WIDTH or self.x1 < 0 or self.y1 >= self.HEIGHT or self.y1 < 0 or self.x2 >= self.WIDTH or self.x2 < 0 or self.y2 >= self.HEIGHT or self.y2 < 0:
                self.game_close = True
            # Actualiza la posición de las serpientes
            self.x1 += self.x1_change
            self.y1 += self.y1_change
            self.x2 += self.x2_change
            self.y2 += self.y2_change
            
            # Dibuja la pantalla
            self.screen.fill(self.CELESTE)
            self.screen.blit(self.apple1_img, [self.foodx1, self.foody1])
            self.screen.blit(self.apple2_img, [self.foodx2, self.foody2])

            snake_head = []
            snake_head.append(self.x1)
            snake_head.append(self.y1)
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.length_of_snake:
                del self.snake_list[0]
            
            # Verifica si la serpiente 1 se ha chocado consigo misma
            for x in self.snake_list[:-1]:
                if x == snake_head:
                    self.game_close = True
                    
             # Dibuja la serpiente 1
            self.our_snake(self.snake_block, self.snake_list, self.GREEN)
            
            # Actualiza la lista de segmentos de la serpiente 2
            snake2_head = []
            snake2_head.append(self.x2)
            snake2_head.append(self.y2)
            self.snake2_list.append(snake2_head)
            if len(self.snake2_list) > self.length_of_snake2:
                del self.snake2_list[0]
            
            # Verifica si la serpiente 2 se ha chocado consigo misma
            for x in self.snake2_list[:-1]:
                if x == snake2_head:
                    self.game_close = True
            
            # Dibuja la serpiente 2
            self.our_snake(self.snake_block, self.snake2_list, self.BLUE)

            pygame.display.update()
            # Verifica si la serpiente 1/ serpiente 2 han comido una manzana, la que les corresponde
            if self.x1 in range(self.foodx1, self.foodx1 + self.snake_block * 2) and self.y1 in range(self.foody1, self.foody1 + self.snake_block * 2):
                self.foodx1, self.foody1 = self.generate_food_position()
                self.length_of_snake += 1

            if self.x2 in range(self.foodx2, self.foodx2 + self.snake_block * 2) and self.y2 in range(self.foody2, self.foody2 + self.snake_block * 2):
                self.foodx2, self.foody2 = self.generate_food_position()
                self.length_of_snake2 += 1

            self.clock.tick(self.snake_speed)
        # Cierra pygame
        pygame.quit()
        quit()

    def __str__(self):
        """
        Representación de la clase como string.

        Returns:
            str: Representación de la clase como string.
        """
        return "Snake Game"

if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()