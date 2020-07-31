from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Set the starting room to the current room
player.current_room = world.starting_room
# player.travel('s')
# player.current_room.get_exits()

# Store visited rooms
visited = set()
visited.add(player.current_room)

go_back = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

stack = Stack()

visited_rooms = set()

map = world.rooms

# TODO: recursively 
def dft_recursive(current_room, map):
    # check to see if already in the visited rooms
    # when get to a room, add it to the visited rooms
    if current_room.id not in visited_rooms:
        visited_rooms.add(current_room.id)
    # find exits and shuffle for random pick to traverse
    # get_exits is a BFT
    exits = random.shuffle(Room.get_exits(current_room))

    # check each exit/direction
    # if it exists, check if in visited rooms
    # if room isn't add it to visited rooms
    if "n" in exits and current_room.get_room_in_direction("n") not in visited_rooms:
        visited_rooms.add(current_room.id)
    ## To keep direction moved, add room to the stack
        stack.push("n")
    ## also add it to the traversal path since not visited
        traversal_path.append("n")
    # travel that direction
    # if there is a room, move player to that room
    # by Room
    current_room = current_room.get_room_in_direction("n")

    if "s" in exits and current_room.get_room_in_direction("s") not in visited_rooms:
        visited_rooms.add(current_room.id)
        stack.push("s")
        current_room = current_room.get_room_in_direction("s")

    elif "e" in exits and current_room.get_room_in_direction("e") not in visited_rooms:
        visited_rooms.add(current_room.id)
        stack.push("e")
        current_room = current_room.get_room_in_direction("e")

    elif "w" in exits and current_room.get_room_in_direction("w") not in visited_rooms:
        visited_rooms.add(current_room.id)
        stack.push("w")
        current_room = current_room.get_room_in_direction("w")

    # if ❔is found, 
    else:
    # remove the last valid direction from the stack
        explore_this = stack.pop()
    # get the reverse direction from the opposite dictionary
        reverse = go_back.get(explore_this)
    # add the reverse direction to the traversal path
        traversal_path.append(reverse)
    # change current room to go_back path
        current_room = current_room.get_room_in_direction(reverse)

    return traversal_path 






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
