import pygame

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, self.color, [10, 10, self.width, self.height])

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("yellow_car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.

        self.rect = self.image.get_rect()

    pygame.display.set_caption('Move Sprite With Keyboard')

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
