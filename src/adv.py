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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("JoeyG.", room['outside'])

def get_directions(the_rm):
    dir = []
    if player.current_room.n_to:
        dir.append('n')
    if player.current_room.w_to:
        dir.append('w')
    if player.current_room.e_to:
        dir.append('e')
    if player.current_room.s_to:
        dir.append('s')
    d = ", ".join(dir)
    dir = f"You can go: {d}"
    return dir

class MyPrompt(Cmd):
    prompt = 'Old House> '
    intro = "Welcome! Type ? to list commands"

    print(get_directions(player.current_room))

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
        print('\n')

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
        print(get_directions(player.current_room), '\n')
    
    def do_s(self, inp):
        if not player.current_room.s_to:
            print("Cannot Go South")
        else:
            print(player.current_room.s_to)
            player.current_room = player.current_room.s_to
        print(get_directions(player.current_room), '\n')

    def do_e(self, inp):
        if not player.current_room.e_to:
            print("Cannot Go East")
        else:
            print(player.current_room.e_to)
            player.current_room = player.current_room.e_to
        print(get_directions(player.current_room), '\n')

    def do_w(self, inp):
        if not player.current_room.w_to:
            print("Cannot Go West")
        else:
            print(player.current_room.w_to)
            player.current_room = player.current_room.w_to
        print(get_directions(player.current_room), '\n')

    def do_q(self, inp):
        print("Thanks for playing")
        return True

if __name__ == '__main__':
    MyPrompt().cmdloop()

