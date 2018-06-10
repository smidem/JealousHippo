import pandas as pd
from sys import argv

script, filepath = argv

def grader(csv_filepath):
    """Open a csv file as a data frame and compare the Expected Values column
    to the output of boolean expressions in the Expressions column"""
    # open csv file using filepath provided as arg
    with open(csv_filepath, newline = '') as csv_file:
        # create a data frame with no quote characters to preserve leading
        # quotes on the entries that use them
        df = pd.read_csv(csv_file, quoting = 3)
        # strip leading spaces from column names
        df.columns = df.columns.str.lstrip()
        # save Expressions columns as a list
        expressions = df.Expressions.tolist()
        # remove leading spaces from entires in Expected Values column and
        # save the column as a list
        expected = df['Expected Values'].str.lstrip().tolist()
        # create a counter to keep track of how many times the expected value
        # is equal to the output of the expression
        correct = 0
        # store the total number of rows for this data frame
        total = df.shape[0]
        # iterate through each expression in the list
        for i, expression in enumerate(expressions):
            # test whether the output of the expression is equal to the
            # expected value
            if eval(expression) == eval(expected[i]):
                # if the expected value is correct increment the correct count
                correct += 1
        # determine the percentage of correct responses and format it as a
        # string
        grade = "{}%".format(correct / total * 100)
        return grade

print("You received {} on this assignment".format(grader(filepath)))
