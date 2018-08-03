# import routes
import mapconfig
import datetime
import threading
import time
# import eventlet
from random import randint
debug = True

playerDict = {}

class Player:
    def __init__(self, sessiondId):
        self.sessionId = sessiondId
        self.name = sessiondId

        self.max_hp = 10
        self.hp = 10
        self.hp_regen = 1

        self.max_stamina = 10
        self.stamina = 10
        self.stamina_regen = 1

        self.damage_range = [10, 20]
        self.current_room = room
        self.current_tile = self.current_room.tiles[0][0]
        self.x_position = self.current_tile.x_anchor
        self.y_position = self.current_tile.y_anchor

        self.armor = None
        self.weapon = None
        self.shield = None

        playerDict[self.sessionId] = self

    def move(self, direction):
        if direction == "forward":
            next_tile = self.current_tile.Up
        elif direction == "backward":
            next_tile = self.current_tile.Down
        elif direction == "left":
            next_tile = self.current_tile.Left
        elif direction == "right":
            next_tile = self.current_tile.Right

        if self.stamina > 0:
            if next_tile and next_tile.walkable:
                self.stamina -= 1
                if next_tile.occupant:
                    print("attack!")
                    attack(self, next_tile.occupant)
                else:
                    self.current_tile.occupant = None
                    self.current_tile = next_tile
                    self.current_tile.occupant = self
                    self.x_position = self.current_tile.x_anchor
                    self.y_position = self.current_tile.y_anchor

    def staminatick(self):
        self.stamina += self.stamina_regen
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        # print(self.stamina)



class Tile:
    def __init__(self, x_position, y_position, room):
        self.size = 36
        self.x_position = x_position
        self.y_position = y_position
        self.x_anchor = (x_position * self.size) + (self.size / 2)
        self.y_anchor = (y_position * self.size) + (self.size / 2)
        self.items = []
        self.character = None
        self.room = room
        self.occupant = None

        # connections:
        self.Up = None
        self.Down = None
        self.Left = None
        self.Right = None

        # type:
        self.walkable = False

# moveDict = {
    # 1: "up",
    # 2: "down",
    # 3: "left",
    # 4: "right"
# }


class Room:
    def __init__(self, raw_layout):
        self.raw_layout = raw_layout
        self.tiles = []
        self.build_room()
        self.width = len(self.raw_layout[0])
        self.height = len(self.raw_layout)

    def build_room(self):
        for y in range(0, len(self.raw_layout)):
            self.tiles.append([])
            for x in range(0, len(self.raw_layout[y])):
                tile = Tile(x, y, self)
                self.tiles[y].append(tile)
                if self.raw_layout[y][x] == "X":
                    tile.walkable = True


    def show_rooms(self):
        # print(self.raw_layout)
        for y in range(0, len(self.raw_layout)):
            for x in range(0, len(self.raw_layout[y])):
                print(self.raw_layout[y][x])

    def show_connections(self):
        for row in self.tiles:
            for tile in row:
                print(tile.x_position, tile.y_position, tile.Up, tile.Down, tile.Left, tile.Right, tile.walkable)

    def build_connections(self):
        for row in self.tiles:
            for tile in row:
                # West check
                if tile.x_position > 0:
                    tile.Left = self.tiles[tile.y_position][tile.x_position - 1]
                    # if self.West and debug:
                    #     print("I have a connection to the West")

                # East check
                if tile.x_position != len(self.tiles[tile.y_position]) - 1:
                    tile.Right = self.tiles[tile.y_position][tile.x_position + 1]
                    # if self.East and debug:
                    #     print("I have a connection to the East")

                # North check
                if tile.y_position > 0:
                    tile.Up = self.tiles[tile.y_position - 1][tile.x_position]
                    # if self.North and debug:
                    #    print("I have a connection to the North")

                # South check
                if tile.y_position < len(self.tiles) - 1:
                    tile.Down = self.tiles[tile.y_position + 1][tile.x_position]
                    # if self.South and debug:
                    #    print("I have a connection to the South")

    def traverse(self, current_tile, direction):
        raise NotImplementedError


def attack(aggressor, defender):
    print("attack called")
    print(aggressor.name)
    print(defender.name)


def stamina_update():
    next_call = time.time()
    while 1:
        # print("stamupdate")
        # print(datetime.datetime.now())
        next_call = next_call + 1
        time.sleep(next_call - time.time())
        for key, value in playerDict.items():
            value.staminatick()




def main():
    room = Room(mapconfig.map0)
    room.show_rooms()
    room.build_connections()
    room.show_connections()


if __name__ == "__main__":
    main()

room = Room(mapconfig.map0)
room.show_rooms()
room.build_connections()
room.show_connections()

# Example for drawing grid
def drawGrid(width, height, size):
  segmentsList = []
  # vertical lines
  for x_axis in range(0, width):
    segmentsList.append({"a": {"x": x_axis * size, "y": 0}, "b": {"x": x_axis * size, "y": height * size}})

  # horizontal lines
  for y_axis in range(0, height):
    segmentsList.append({"a": {"x": 0, "y": y_axis * size}, "b": {"x": width * size, "y": y_axis * size}})
  return segmentsList

# print(drawGrid(2, 2, 1))
