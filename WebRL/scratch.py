from random import *


class Player:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.damage_range = [10, 20]

  def attack(self, enemy):
    self.hp -= randint(enemy.damage_range[0], enemy.damage_range[1])
    enemy.hp -= randint(self.damage_range[0], self.damage_range[1])
    print(self.name, self.hp, self.check_if_dead())
    print(enemy.name, enemy.hp, enemy.check_if_dead())

  def check_if_dead(self):
    if self.hp <= 0:
        self.hp = 0
        return self.name + " is DEAD"
    else:
        return self.name + " is still alive!"

player1 = Player("Cody")
player2 = Player("Doug")

# player1.example_for_cody()

while player1.hp > 0 and player2.hp > 0:
  player1.attack(player2)



# old Game



def main2():

    room0 = Room(mapconfig.map0)
    curr_pos = room0.rooms[0]

    # routes.broadcast(curr_pos.give_connections())
    # routes.broadcast("Where do you wanna move?\n")
    # direction = input("Where do you wanna move?\n")
    direction = "east"
    if direction.lower() in ["north", "east", "south", "west"]:
        if curr_pos.traverse(direction.lower()):
            curr_pos = curr_pos.traverse(direction.lower())
            return("You have moved")

        else:
            return("There is no room that way")

    else:
        return("That's not a valid move")


def main1():
    map0 = Map(0, mapconfig.map0)
    player1 = Player("cody", map0.rooms[0])

    # curr_pos = map0.rooms[0]

    while True:
        print(curr_pos.give_connections())
        direction = input("Where do you wanna move?\n")
        if direction.lower() in ["north", "east", "south", "west"]:
            if curr_pos.traverse(direction.lower()):
                curr_pos = curr_pos.traverse(direction.lower())
                print("You have moved")

            else:
                print("There is no room that way")

        else:
            print("That's not a valid move")




class Room1:
    def __init__(self, position):
        self.xPosition = position[0]
        self.yPosition = position[1]
        self.connection_dict = {"north": None,
                                "east": None,
                                "south": None,
                                "west": None}
        self.tiles = []
        self.map_reference.rooms.append(self)

    def find_connections(self):
        # print(self.xPosition, self.yPosition)

        # West check
        if self.xPosition > 0:
            self.connection_dict["west"] = self.map_reference.layout[self.yPosition][self.xPosition - 1]
            # if self.West and debug:
            #     print("I have a connection to the West")

        # East check
        if self.xPosition != len(self.map_reference.layout[self.yPosition]) - 1:
            self.connection_dict["east"] = self.map_reference.layout[self.yPosition][self.xPosition + 1]
            # if self.East and debug:
            #     print("I have a connection to the East")

        # North check
        if self.yPosition > 0:
            self.connection_dict["north"] = self.map_reference.layout[self.yPosition - 1][self.xPosition]
            # if self.North and debug:
            #    print("I have a connection to the North")

        # South check
        if self.yPosition < len(self.map_reference.layout) - 1:
            self.connection_dict["south"] = self.map_reference.layout[self.yPosition + 1][self.xPosition]
            # if self.South and debug:
            #    print("I have a connection to the South")

    def give_connections(self):
        return [key for key, value in self.connection_dict.items() if value is not None]

    def traverse(self, direction):
        return self.connection_dict[direction]



class Map:
    def __init__(self, position, raw_layout):
        self.position = position
        self.rawLayout = raw_layout
        self.layout = []
        self.rooms = []
        self.build_map()

    def show_rooms(self):
        print(self.layout)
        for y in range(0, len(self.layout)):
            for x in range(0, len(self.layout[y])):
                print(self.layout[y][x])

    def build_map(self):
        for y in range(0, len(self.rawLayout)):
            self.layout.append([])
            for x in range(0, len(self.rawLayout[y])):
                if self.rawLayout[y][x] == "X":
                    self.layout[y].append(Tile(self, [x, y]))
                else:
                    self.layout[y].append(None)
        # self.show_rooms()
        self.build_connections()

    def build_connections(self):
        for room in self.rooms:
            room.find_connections()

