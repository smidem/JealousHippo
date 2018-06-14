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
    no_objects = []

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

        # if an object was found using the 'and' keyword, store the boundary
        # information following 'and' into the no_objects list
        if and_idx > 0 and (and_idx + 1 < len(row)):
            no_objects += [row[and_idx + 1:len(row)]]
        # if no object was found, append this row to the no_objects list as is
        elif and_idx == 0:
            no_objects += [row]

    # check if more than one row was processed into no_objects
    # if so, reformat the list so that it returns a single list instead of
    # a list within a list
    if len(no_objects) == 1:
        # strip additional brackets from list element
        no_objects[0] = str(no_objects[0]).strip("[]")
        # break list element back into words
        words = str(no_objects[0]).split(', ')
        # iterate over words and remove additional quote characters
        for i, word in enumerate(words):
            word = word.strip("''")
            # if we are not on the first word, append additional words to the
            # end of the list
            if i > 0: no_objects.append(word)
            # if we are on the first word, insert it into no_objects as the
            # first element in the list
            no_objects[i] = word

    return objects, no_objects

def encounter_object(object):
    if "door" in object[0]:
        return "door"

def change_position(current, direction):
    return current

def find_boundary(boundaries):
    boundary_types = ['corner', 'hall', 'end']
    boundary = set(boundaries).intersection(boundary_types).pop()
    return boundary

print(find_boundary(separate_objects(a[:1])[1]))
# current_position = separate_objects(f[4:5])
