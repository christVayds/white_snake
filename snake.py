import pygame
import random

class Snake(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.head = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.body = [pygame.Rect(self.x-self.width, self.y, self.width, self.height)]
        self.dirx = 1
        self.diry = 0
        self.direction = 'right'
        self.dead = False
        self.score = 0
        self.scores = [5, 7, 10, 12, 15, 17, 18, 22]

    def update(self, screen):
        for body in self.body:
            if self.head.x == body.x and self.head.y == body.y:
                self.dead = True

        self.body.append(self.head)
        for body in range(len(self.body)-1):
            self.body[body].x, self.body[body].y = self.body[body+1].x, self.body[body+1].y
        self.head.x += self.dirx * self.width
        self.head.y += self.diry * self.height
        self.body.remove(self.head)

        pygame.draw.rect(screen, (255,255,255), self.head)
        
        for body in self.body:
            pygame.draw.rect(screen, (255,255,255), body)
    
    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.direction != 'left':
                self.dirx = 1
                self.diry = 0
                self.direction = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.direction != 'right':
                self.dirx = -1
                self.diry = 0
                self.direction = 'left'
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.direction != 'down':
                self.dirx = 0
                self.diry = -1
                self.direction = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.direction != 'up':
                self.dirx = 0
                self.diry = 1
                self.direction = 'down'

    def handleCollision(self, food):
        if self.head.center == food.food.center:
            self.add()
            food.repos()
            self.score += 1
        if self.head.x < 0 or self.head.x >= 750:
            self.dead = True
        elif self.head.y < 0 or self.head.y > 550:
            self.dead = True

    def add(self):
        self.body.append(pygame.Rect(self.body[-1].x, self.body[-1].y, self.width, self.height))

    def addLevel(self):
        if self.score in self.scores:
            self.scores.remove(self.score)
            return 1
        return 0

class Food(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.x, self.y = int(random.choice(list(range(int(750/self.width))))) * self.width, int(random.choice(list(range(int(570/self.height))))) * self.height
        self.food = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.food)

    def repos(self):
        self.food.x, self.food.y = int(random.choice(range(int(750/self.width)))) * self.width, int(random.choice(range(int(570/self.height)))) * self.height