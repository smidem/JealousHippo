import pandas as pd

# create a map of the maze as data frame that includes interactive objects and
# the maze boundaries as strings.
maze_map = pd.DataFrame({ 'A' : pd.Series(["north west corner",
                                "north south hall", "south west corner",
                                "north west corner",
                                "compass and south west corner"]),
                          'B' : pd.Series(["shield and north east corner",
                                "torch and south west corner",
                                "minotaur and north wall",
                                "torch and south east corner",
                                "east west hall"]),
                          'C' : pd.Series(["north west corner",
                                "south east corner", "north east corner",
                                "south west corner", "east west hall"]),
                          'D' : pd.Series(["manticore and north wall",
                                "east west hall", "torch and south west corner",
                                "helmet and west facing end",
                                "east west hall"]),
                          'E' : pd.Series(["east west hall",
                                "sword and east facing end", "north east corner",
                                "south west corner", "east west hall"]),
                          'F' : pd.Series(["exit and south east corner",
                                "north east corner", "north south hall",
                                "hidden door south and south east corner",
                                "hidden door north and west facing end"])})

# initialize a current location variable
current_loc = 0
# commonly used strings
weapon = "    WEAPON ACQUIRED!"
attack_up = "    ATTACK INCREASED!"
# convert each column of the map to a string list that can be parsed.
a = maze_map['A'].str.split(' ').tolist()
b = maze_map['B'].str.split(' ').tolist()
c = maze_map['C'].str.split(' ').tolist()
d = maze_map['D'].str.split(' ').tolist()
e = maze_map['E'].str.split(' ').tolist()
f = maze_map['F'].str.split(' ').tolist()

# DO NOT USE, this function is still in development
def find_and(column):
    # create a list that will store the index of and in each row of the column
    # given
    and_idx = []
    and_count = 0
    # iterate over each row in the column given
    for i, row in enumerate(column):
        # test if and is in this row
        if any('and' in row for row in column):
            # iterate over each word in the row to find the position of 'and'
            for j, word in enumerate(row):
                # once 'and' is found store the index
                if word == 'and':
                    # append the index to the and_idx list and increment
                    # and_count
                    and_idx.append(j)
                    and_count += 1

        # if there is not an and in this row append an empty element to the
        # and_idx list in order to provide useful positional data
        if not ('and' in row):
            and_idx.append("")

    # iterate over each element in the and_idx list
    for element in and_idx:
        # if the element is not empty and only one 'and' was found, pop that
        # element off so that and_idx only returns an index instead of a list
        if ((not (element == '')) and (and_count == 1)):
            and_idx = and_idx.pop()
        # elif ((element == '') and (and_count == 0)):


    return and_idx

# separate interactive objects from maze boundaries and return the respecitve
# lists for each of those elements
def find_objects(column):
    objects = []
    and_idx = 0
    # iterate over each row in the column given
    for row in column:

        # any coordinates with objects will contain 'and'
        # check if any of these elements contain objects
        if any('and' in row for row in column):
            # iterate over each word in the row to find the position of 'and'
            for j, word in enumerate(row):
                # once 'and' is found store the preceeding words into the
                # objects list
                if word == 'and':
                    and_idx = j
                    objects += row[:and_idx]
        # if object is not found using the 'and' keyword, store an empty value
        # so that len(objects) still provides useful positional data
        else: objects += [""]

        # if only one object is found, return only the object and not a list of
        # length one
        if len(objects) == 1:
            objects = objects.pop()

    return objects

def find_boundaries(column):
    boundaries = []
    and_idx = 0
    # iterate over each row in the column given
    for row in column:

        # any coordinates with objects will contain 'and'
        if any('and' in row for row in column):
            # iterate over each word in the row to find the position of 'and'
            for j, word in enumerate(row):
                # once 'and' is located store the index in and_idx
                if word == 'and':
                    and_idx = j
        # check if an 'and' was found, and make sure that it occurs before the
        # end of the row
        if and_idx > 0 and (and_idx + 1 < len(row)):
            # add the elements of the row that occur after 'and' to the
            # boundaries list
            boundaries += [row[and_idx + 1:len(row)]]
            # reset and_idx to 0 for use in the next row
            and_idx = 0
        # if no 'and' was found add the whole row to the boundaries list
        elif and_idx == 0:
            boundaries += [row]
    # if only one field was passed to find_boundaries, transform boundaries to
    # a list instead of a list of lists
    if len(boundaries) == 1:
        # strip unecessary brackets from the element
        boundaries[0] = str(boundaries[0]).strip('[]')
        # split the list into individual words
        words = str(boundaries[0]).split(', ')
        # iterate over each word
        for i, word in enumerate(words):
            # strip unecessary quote characters and rebuild the list
            word = word.strip("''")
            # to avoid index out of bounds errors, append words to the list if
            # the first word has already been inserted into the first element
            # of boundaries
            if i > 0: boundaries.append(word)
            boundaries[i] = word
    return boundaries

def encounter_object(object):
    if "door" in object[0]:
        return "door"

def change_position(direction):
    global current_loc

def which_way():
    global current_loc
    restricted = ""
    you_are_here = """
    It is still very dark in this area. You wander around with
    your hands outstretched in an attempt to discover your
    surroundings.\n"""
    blocked_directions = """
    With some difficulty, you are able to discern
    that the ways to the {} and {} blocked.""".format(*restricted)
    dead_end = """
    You stumble around in the dark for some time and use your
    hands to explore the features in front of you. After some
    time, you determine that this is a dead end."""

# trash function, please ignore
def get_boundary_type(boundaries):
    boundary_types = ['corner', 'hall', 'end', 'wall']
    boundary = []
    if isinstance([], list):
        words = str(boundaries[0]).strip('["[", "]"]')
        words = words.split('"''", "''"')
        print(f"This is words: {words}")
        for word in words:
            print(word)

    if (boundary in boundary_types):
        return boundary

def interpret_boundaries(coordinates):
    boundaries = find_boundaries(coordinates)
    boundary_type = ""
    objects = find_objects(coordinates)
    length = len(boundaries)
    if length > 1:
        boundary_type = boundaries.pop(-1)

    restricted = []
    if (boundary_type == 'corner'):
        restricted = boundaries
    elif (boundary_type == 'hall'):
        if (boundaries[0] == 'east') and (boundaries[1] == 'west'):
            restricted = [up, down]
        elif (boundaries[0] == 'north') and (boundaries[1] == 'south'):
            restricted = [left, right]
    elif (boundary_type == 'end'):
        if ('west' in boundaries):
            restricted = [north, south, east]
        elif ('east' in boundaries):
            restricted = [north, south, west]

    if (('minotaur' in objects) or ('manticore' in objects)) and (length == 1):
        restricted = boundaries

    return restricted

def dead():
    print("    YOU DIED.")
    exit()

def failed_to_enter():
    print(
    """
    Just as you get up, a large bladed
    pendulum strikes you directly in the face.
    """)
    dead()

def start():
    global current_loc
    current_loc = a[4:5]

def entrance():
    global weapon
    global attack_up
    prologue_1 = """
    You awake in an extremely dark room with no
    memory of how you might have arrived here."""
    prologue_2 = """
    You can barely make out the faint glow of a
    doorway immediately in front of you.\n"""
    door_prompt = "    Do you go through the door?\n"
    proceed = """
    As you move through the door you hear a whooshing sound
    behind you. You turn around and see a large bladed pendulum
    passing right where you just were. Just then the door you
    passed through slams shut just inches from your face.
    You shake the handle vigorously, but it will not budge.
    At least you've narrowly avoided death for the time being.\n"""
    dodge_kick = """
    You tap into primal instincts of some kind, and you sense
    that you are in immediate danger. Without thinking, you
    lean just far enough out of the way to avoid a large bladed
    pendulum that was headed right for your face. On the
    pendulum's second pass you are able to detach it from the
    ceiling with a swift roundhouse kick. The large blade
    attached to pendulum comes crashing down right in front of
    your feet.\n"""
    weaponized_proceed = """
    Now armed with a weapon, you proceed to pass through the
    doorway in front of you. As you do so, the door slams shut
    behind you. You feel no fear though, because deep down you
    know you have been here before...\n"""
    print(prologue_1)
    print(prologue_2)
    print(door_prompt)
    answer = input("    > ").lower()
    if ('yes' in answer) or ('go through' in answer):
        print(proceed)
        start()
    elif ('dodge' in answer) and ('pendulum' in answer):
        print(dodge_kick)
        print(weapon)
        print(attack_up)
        print(weaponized_proceed)
        start()
    else: failed_to_enter()

def main():
    global current_loc
    entrance()

# main()
print(get_boundary_type(a[0:1]))
