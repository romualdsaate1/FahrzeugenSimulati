import pygame
import sys
import random

import os
from lxml import etree

tree = etree.parse("parameter.xml")
root = tree.getroot()



GREY = (128,128,128)
SILVER = (192,192,192)
LIGHTGREY = (211,211,211)
GAINSBORO = (220,220,220)
CIEL = (0, 200, 255)
ORANGE = 255, 100, 0
yellow = (200,200,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        #self.image = pygame.Surface([15, 15])
        self.image = pygame.image.load("yellow_car.png").convert_alpha()
       # self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [#[0, 0, 20, 90, GREEN],
                 #[0, 330, 20, 300, GREEN],
                 #[780, 0, 20, 90, GREEN],
                #[780, 330, 20, 300, GREEN],
                 [0, 70, 800, 20, GREEN],
                 [0, 330, 800, 20, GREEN],
                 [0, 93, 800, 3, WHITE],
                 [0, 99, 800, 3, WHITE],
                 [0, 323, 800, 3, WHITE],
                 [0, 317, 800, 3, WHITE],
                 [620, 217, 200, 100, RED]

              #   [20, 50, 200, 500, BLUE]
                 ]

         # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)




class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 70, 800, 20, BLUE],
                 [0, 330, 800, 20, BLUE],
                 [0, 93, 800, 3, WHITE],
                 [0, 99, 800, 3, WHITE],
                 [0, 323, 800, 3, WHITE],
                 [0, 317, 800, 3, WHITE],
                 [0, 217, 160, 100, RED]

                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 70, 800, 20, PURPLE],
                 [0, 330, 800, 20, PURPLE],
                 [0, 93, 800, 3, WHITE],
                 [0, 99, 800, 3, WHITE],
                 [0, 323, 800, 3, WHITE],
                 [0, 317, 800, 3, WHITE]
                 ]
#        pygame.draw.line(20, 210, 25, 2, WHITE)

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

       # for x in range(100, 800, 100):
        #    for y in range(50, 451, 300):
         #       wall = Wall(x, y, 20, 200, RED)
          #      self.wall_list.add(wall)


          # for y in range(0, 830, 50):

              #  wall = Wall(y, 210, 25, 2, WHITE)
              #  self.wall_list.add(wall)
 # Draw Line painting on the road
  #  pygame.draw.line(screen, WHITE, [0, 400], [SCREENWIDTH, 400], 8)
   # pygame.draw.line(screen, WHITE, [0, 412], [SCREENWIDTH, 412], 8)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    SCREENWIDTH = 800
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    # Create an 800x600 sized screen
    # screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Projekt2')


    # Create the player paddle object
    player = Player(100, 250)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # --- Drawing ---
        screen.fill(GAINSBORO)

        # Draw The Road
        
        pygame.draw.rect(screen, GREY, [0, 75, SCREENWIDTH, 265])

        # Draw Line painting on the road

        #pygame.draw.line(screen, WHITE, [0, 400], [SCREENWIDTH, 400], 8)
        #pygame.draw.line(screen, WHITE, [0, 412], [SCREENWIDTH, 412], 8)
        for y in range(10, 820, 70):
            pygame.draw.line(screen, WHITE, [y, 247], [y, 247], 35)
            pygame.draw.line(screen, WHITE, [y, 172], [y, 172], 35)

            #self.line_list.add(line)
        # wall = Wall(y, 210, 25, 2, WHITE)
        # self.wall_list.add(wall)

        # Creation Bouton lancer
        #bou1 = Button(screen, text='Pause', width=10, command=newstart)
        #bou1.pack(side=LEFT, padx=20, pady=50)


        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)



    pygame.quit()


if __name__ == "__main__":
    main()