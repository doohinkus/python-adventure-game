from room import Room
from items import Item
# create rooms
kitchen = Room()
kitchen.set_name("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")


dining_hall = Room()
dining_hall.set_name("Dining Hall")
dining_hall.set_description("A large room with gold decorations on each wall.")


ballroom = Room()
ballroom.set_name("Ballroom")
ballroom.set_description("A vast room with hardwood floors")

# link rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# show details
dining_hall.get_details()
kitchen.get_details()

current_room = kitchen

sword = Item()

sword.set_name("Battle Sword")
sword.set_description("Powerful greatsword for slashing enemies")
sword.get_details()

# playing = True
#
# while playing:
#     print("\n")
#     current_room.get_details()
#     command = raw_input("> ")
#     current_room = current_room.move(command)
#     if command == "quit":
#         playing = False
