class Room():
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_rooms = {}

    # setters

    def set_description(self, room_description):
        self.description = room_description

    def set_name(self,room_name):
        self.name = room_name

    # getters

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name



    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("This is the " + self.get_name() + ". " + self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self




    def describe(self):
        print(self.name + " : " + self.description)
