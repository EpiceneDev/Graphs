from room import Room
from player import Player
from world import World
from stack import Stack

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

map = world.rooms

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
# traversal_path = []

# # Put the player into the first room
# # player.current_room = world.starting_room
# player = Player(world.starting_room)

# # Put starting room into current room
# current_room = world.starting_room

# # Main set to store visited rooms 
# visited = set()

# # Reference dict for going in reverse
# go_back = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# stack = Stack()

# # Add the current room to the main set
# visited.add(player.current_room.id)

# # Secondary set to store exits
# visited_exits = set()



player = Player(world.starting_room)

current_room = world.starting_room

traversal_path = []

visited = set()

go_back = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} 

direction_dict = {'n': 'n', 's': 's', 'e': 'e', 'w': 'w'}
direction_list = ['n', 's', 'e', 'w']

stack = Stack()

player.current_room = world.starting_room

visited.add(player.current_room.id)

visited_exits = set()

# To populate the main data with the rooms
while len(visited) != len(room_graph):

    # # If not in the secondary list
    # # add it to the visited exits
    # if current_room.id not in visited:
    #     visited.add(current_room.id)

    # # Add the current room to the secondary set
    # visited_exits.add(current_room)

    # # find exits and shuffle for random pick to traverse
    # # get_exits is a BFT
    # exits = random.shuffle(current_room.get_exits())

    # # Check each exit/direction to see if in the secondary list 
    # # Add the room to the main list if needed
    # if "n" in exits and current_room.get_room_in_direction("n") not in visited_exits:
    #     visited_exits.add(current_room.id)

    # # Add to the stack to keep track of the moves
    #     stack.push("n")

    # ## Also add it to the traversal path since not visited
    #     traversal_path.append("n")

    # # if there is a room, move player to that room
    #     player.travel("n")

    visited_exits.add(current_room)
  
    exits = current_room.get_exits()   
  
    if current_room.id not in visited:
        visited.add(current_room.id) 

    if "n" in exits and current_room.get_room_in_direction("n") not in visited_exits:
        stack.push("n")
        traversal_path.append("n")
        current_room = current_room.get_room_in_direction("n")  
     
    elif "s" in exits and current_room.get_room_in_direction("s") not in visited_exits:
        stack.push("s")
        traversal_path.append("s")
        current_room = current_room.get_room_in_direction("s")  

    elif "e" in exits and current_room.get_room_in_direction("e") not in visited_exits:
        stack.push("e")
        traversal_path.append("e")
        current_room = current_room.get_room_in_direction("e")  

    elif "w" in exits and current_room.get_room_in_direction("w") not in visited_exits:
        stack.push("w")
        traversal_path.append("w")
        current_room = current_room.get_room_in_direction("w") 


    else: 
    # remove the last valid direction from the stack
        direction = stack.pop()
    # get the reverse direction from the go-back dictionary
        reverse = go_back.get(direction)
    # add the reverse direction to the traversal path
        traversal_path.append(reverse)
    # change current room to go_back path
        current_room = current_room.get_room_in_direction(reverse)





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
