# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction):
        if getattr(player.current_room, f"{direction}_to") is not None:
            player.current_room = if getattr(player.current_room, f"{direction}_to")
        else:
            print("You can not move in that direction")
