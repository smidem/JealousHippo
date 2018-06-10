import pandas as pd
from sys import argv
import distutils
from distutils.util import strtobool

script, filepath = argv

# def create_df(filepath):
#     return True

# open a csv file as a data frame compare expected values to actual values
def grader(csv_filepath):
    with open(csv_filepath, newline = '') as csv_file:
        df = pd.read_csv(csv_file, quoting = 3)
        df.columns = df.columns.str.lstrip()
        expressions = df.Expressions.tolist()
        expected = df['Expected Values'].str.lstrip().tolist()
        correct = 0
        total = df.shape[0]
        boolean_list = []
        for i, expression in enumerate(expressions):
            if eval(expression) == eval(expected[i]):
                correct += 1
        grade = "{}%".format(correct / total * 100)
        return grade
        #     print("{}, {}".format(eval(expression), eval(expected[i])))
        #     if ('(' or ')') not in value:
        #         words = value.split(' ')
        #         print(f"Words: {words}")
        #         for i, element in enumerate(words):
        #             if element == "True" or element == "False":
        #                 boolean_list += [words.pop(i)]
        #                 print(f"Booleans: {boolean_list}")

        #     if value:
        #         print(value)
        #     if (df.Expressions.eq(df['Expected Values'])):

# def evaluate(expression):
#     print(distutils.util.strtobool(expression))

# grader(filepath)
print("You received {} on this assignment".format(grader(filepath)))
