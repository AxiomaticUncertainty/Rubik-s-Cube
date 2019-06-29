from cb import *

def executeScramble(obj, scramble):
    for move in scramble.split(' '):
        axis = 0 if move == 'U' else 1 if move == 'F' else 2 if move == 'R' else 3 if move == 'B' else 4 if move == 'L' else 5

        if move[0] == 'U':
            axis = 0
        elif move[0] == 'F':
            axis = 1
        elif move[0] == 'R':
            axis = 2
        elif move[0] == 'B':
            axis = 3
        elif move[0] == 'L':
            axis = 4
        else:
            axis = 5

        print(move, axis)
        if len(move) == 1:
            obj.turn(axis, 1, 1)
        elif move[1] == '2':
            obj.turn(axis, 1, 1)
            obj.turn(axis, 1, 1)
        else:
            obj.turn(axis, 1, 1)
            obj.turn(axis, 1, 1)
            obj.turn(axis, 1, 1)

        print(obj)

if __name__ == "__main__":
    c = cube(3)
    print(c)
    executeScramble(c, input('Enter a scramble...'))
