import pandas as pd

# create a map of the maze as data frame that includes interactive objects and
# the maze boundaries as strings.
maze_map = pd.DataFrame({ 'A' : pd.Series(["up left corner",
                                "north south hall", "down left corner",
                                "up left corner",
                                "entrance and down left corner"]),
                          'B' : pd.Series(["shield and up right corner",
                                "torch and down left corner",
                                "minotaur and up",
                                "torch and down right corner",
                                "east west hall"]),
                          'C' : pd.Series(["up left corner",
                                "down right corner", "up right corner",
                                "down left corner", "east west hall"]),
                          'D' : pd.Series(["manticore and up",
                                "east west hall", "torch and down left corner",
                                "helmet and west facing end",
                                "east west hall"]),
                          'E' : pd.Series(["east west hall",
                                "sword and east facing end", "up right corner",
                                "down left corner", "east west hall"]),
                          'F' : pd.Series(["exit and down right corner",
                                "up right corner", "north south hall",
                                "hidden door down and down right corner",
                                "hidden door up and west facing end"])})

# convert each column of the map to a string list that can be parsed.
a = maze_map['A'].str.split(' ').tolist()
b = maze_map['B'].str.split(' ').tolist()
c = maze_map['C'].str.split(' ').tolist()
d = maze_map['D'].str.split(' ').tolist()
e = maze_map['E'].str.split(' ').tolist()
f = maze_map['F'].str.split(' ').tolist()

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

    for row in column:
        if any("and" in row for row in column):
            for j, word in enumerate(row):
                if word == "and":
                    and_idx = j

        if and_idx > 0 and (and_idx + 1 < len(row)):
            boundaries += [row[and_idx + 1:len(row)]]
            and_idx = 0
        elif and_idx == 0:
            boundaries += [row]

    if len(boundaries) == 1:
        boundaries[0] = str(boundaries[0]).strip('[]')
        words = str(boundaries[0]).split(', ')
        for i, word in enumerate(words):
            word = word.strip("''")
            if i > 0: boundaries.append(word)
            boundaries[i] = word
    return boundaries

def encounter_object(object):
    if "door" in object[0]:
        return "door"

def change_position(current, direction):
    return current

def get_boundary_type(boundaries):
    boundary_types = ['corner', 'hall', 'end']
    boundary = set(boundaries).intersection(boundary_types).pop()
    return boundary

print(find_boundaries(f))
# print(find_boundary(separate_objects(a[:1])[1]))
# current_position = separate_objects(f[4:5])
