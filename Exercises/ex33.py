numbers = []

def loop(max, increment):
    if max > 0:
        i = 0
        number = 0
        for i in range(0, max):
            print("At the top i is {}".format(i))
            numbers.append(number)
            number += increment
            print("Numbers now: ", numbers)
            print("At the bottom i is {}".format(i))

    print("The numbers: ")

    for num in numbers:
        print(num)

max = int(input("How many numbers would you like? "))
increment = int(input("How much would you like to increment by? "))
loop(max, increment)
