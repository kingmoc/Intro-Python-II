from room import Room
from cmd import Cmd

# File Imports
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Items("flashlight", "used in dark places!")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Items("rope", "used to tie other items together"), Items("horn", "used to call for danger")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Items("hat", "We all need style"), Items("sunglasses", "The sun hurts!")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Items("banana", "Hmmm - Who left this here?"), Items("toothbrush", "All I need now is some toothpaste")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Items("lamp", "This could be Alladin pt2"), Items("iphone", "Multipurpose Device for all Comps")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Test Area

# room['outside'].items = [Item("rope", "used to tie other items together"),Item("horn", "used to call for danger")]
# print(room['outside'].items)
# print("------before--------") 
# room['outside'].add_item(Items("random", "I need to test this item has been added"))
# Items("random", "I need to test this item has been added"), Items("test", "Test description")
# room['outside'].add_item()
# for item in room['outside'].items:
#     print(item.name)
# # print("------after--------") 




#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("JoeyG.", room['outside'])

"""
room['outside'].add_item(Items("random", "I need to test this item has been added"))
print(room['outside'].items, "Item Added")
room['outside'].remove_item(Items("random", "I need to test this item has been added"))
print(room['outside'].items, "Item Removed")
"""


# print(type(room['outside'].items), "In Main")
# print(room['outside'].items, "Current")

# room['outside'].remove_item(Items("random", "I need to test this item has been added"))
# print(room['outside'].items)

class MyPrompt(Cmd):
    prompt = 'Old House> '
    intro = "Welcome! Type ? to list commands"

    def do_hello(self, inp):
        print(f"Hi {player.name} {player.current_room.name}")

    def do_ri(self, inp):
        print(f"List of Items in this Room: \n ")
        for i, item in enumerate(player.current_room.items, start = 1):
            print(f"{i}: {item.name} - {item.description}")
        print("\n")

    def do_pi(self, inp):
        print(f"List of Items Currently Holding: \n ")

        for i, item in enumerate(player.items, start = 1):
            print(f"{i}: {item.name} - {item.description}")

    def do_get(self, inp):
        print(f"Grabbing {inp} ...\n")
        item = [item for item in player.current_room.items if item.name == inp]

        if not item:
            print(f"Sorry the {inp} is NOT in this room!")
        else:
            player.add_item(item[0])
            player.current_room.remove_item(item[0])
            for item in player.items:
                if item.name == inp:
                    item.on_take()
                
    def do_drop(self, inp):
        print(f"Dropping the {inp} ...! \n")
        item = [item for item in player.items if item.name == inp]

        if not item:
            print(f"Sorry - you do not posses this item (look elsewhere)")
        else:
            player.remove_item(item[0])
            player.current_room.add_item(item[0])
            for item in player.current_room.items:
                if item.name == inp:
                    item.on_drop()
    
    def do_n(self, inp):
        if not player.current_room.n_to:
            print("Cannot Go North")
        else:
            print(player.current_room.n_to)
            player.current_room = player.current_room.n_to
    
    def do_s(self, inp):
        if not player.current_room.s_to:
            print("Cannot Go South")
        else:
            print(player.current_room.s_to)
            player.current_room = player.current_room.s_to

    def do_e(self, inp):
        if not player.current_room.e_to:
            print("Cannot Go East")
        else:
            print(player.current_room.e_to)
            player.current_room = player.current_room.e_to

    def do_w(self, inp):
        if not player.current_room.w_to:
            print("Cannot Go West")
        else:
            print(player.current_room.w_to)
            player.current_room = player.current_room.w_to

    def do_q(self, inp):
        print("Thanks for playing")
        return True

if __name__ == '__main__':
    MyPrompt().cmdloop()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
