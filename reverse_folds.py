from functools import reduce
from itertools import product
import sys

#State arrays are 2D rectangular arrays full of integers from -2 to 2, inclusive
#The numbers represent colored grid squares as follows:
#-2 - white, bottom
#-1 - black, bottom
#0  - unknown
#1  - black, top
#2  - white, top

patterns = {1: ((1, 2, 2), (2, 2, 2), (2, 2, 2)),
            2: ((2, 1, 2), (2, 2, 2), (2, 2, 2)),
            3: ((2, 2, 2), (2, 1, 2), (2, 2, 2)),
            4: ((1, 1, 2), (2, 2, 2), (2, 2, 2)),
            5: ((1, 2, 1), (2, 2, 2), (2, 2, 2)),
            6: ((1, 2, 2), (2, 1, 2), (2, 2, 2)),
            7: ((1, 2, 2), (2, 2, 1), (2, 2, 2)),
            8: ((1, 2, 2), (2, 2, 2), (2, 2, 1)),
            9: ((2, 1, 2), (1, 2, 2), (2, 2, 2)),
            10: ((2, 1, 2), (2, 1, 2), (2, 2, 2)),
            11: ((2, 1, 2), (2, 2, 2), (2, 1, 2)),
            12: ((1, 1, 1), (2, 2, 2), (2, 2, 2)),
            13: ((1, 1, 2), (1, 2, 2), (2, 2, 2)),
            14: ((1, 1, 2), (2, 1, 2), (2, 2, 2)),
            15: ((1, 1, 2), (2, 2, 1), (2, 2, 2)),
            16: ((1, 1, 2), (2, 2, 2), (1, 2, 2)),
            17: ((1, 1, 2), (2, 2, 2), (2, 1, 2)),
            18: ((1, 1, 2), (2, 2, 2), (2, 2, 1)),
            19: ((1, 2, 1), (2, 1, 2), (2, 2, 2)),
            20: ((1, 2, 1), (2, 2, 2), (2, 2, 1)),
            21: ((1, 2, 1), (2, 2, 2), (2, 1, 2)),
            22: ((1, 2, 2), (2, 1, 2), (2, 1, 2)),
            23: ((1, 2, 2), (2, 1, 2), (2, 2, 1)),
            24: ((2, 1, 2), (1, 1, 2), (2, 2, 2)),
            25: ((2, 1, 2), (1, 2, 1), (2, 2, 2)),
            26: ((2, 1, 2), (1, 2, 2), (2, 2, 1)),
            27: ((2, 1, 2), (2, 1, 2), (2, 1, 2)),
            28: ((1, 1, 1), (1, 2, 2), (2, 2, 2)),
            29: ((1, 1, 1), (2, 1, 2), (2, 2, 2)),
            30: ((1, 1, 1), (2, 2, 2), (1, 2, 2)),
            31: ((1, 1, 1), (2, 2, 2), (2, 1, 2)),
            32: ((1, 1, 2), (1, 1, 2), (2, 2, 2)),
            33: ((1, 1, 2), (1, 2, 1), (2, 2, 2)),
            34: ((1, 1, 2), (1, 2, 2), (2, 2, 1)),
            35: ((1, 1, 2), (2, 1, 1), (2, 2, 2)),
            36: ((1, 1, 2), (2, 1, 2), (1, 2, 2)),
            37: ((1, 1, 2), (2, 1, 2), (2, 1, 2)),
            38: ((1, 1, 2), (2, 1, 2), (2, 2, 1)),
            39: ((1, 1, 2), (2, 2, 1), (1, 2, 2)),
            40: ((1, 1, 2), (2, 2, 1), (2, 1, 2)),
            41: ((1, 1, 2), (2, 2, 1), (2, 2, 1)),
            42: ((1, 1, 2), (2, 2, 2), (1, 1, 2)),
            43: ((1, 1, 2), (2, 2, 2), (1, 2, 1)),
            44: ((1, 1, 2), (2, 2, 2), (2, 1, 1)),
            45: ((1, 2, 1), (2, 1, 2), (1, 2, 2)),
            46: ((1, 2, 1), (2, 1, 2), (2, 1, 2)),
            47: ((1, 2, 1), (2, 2, 2), (1, 2, 1)),
            48: ((1, 2, 2), (2, 1, 1), (2, 1, 2)),
            49: ((2, 1, 2), (1, 1, 1), (2, 2, 2)),
            50: ((2, 1, 2), (1, 2, 1), (2, 1, 2))}

def check(state, known_min = 0):
    ''' check(state array, known_min = 0) -> bool
Checks if state is a square, and if black and white are on different sides.
It checks if state only contains 0s, and either -1s and 2s (white on top and black on bottom),
or -2s and 1s (white on bottom and black on top).
It requires that the size of the state is at least known_min (to save computational power)'''
    if len(state) != len(state[0]):
        return False
    if len(state) < known_min:
        return False
    elements = reduce(lambda s, r: s.union(r), state, set())
    if elements in ({-2, 1}, {-2, 0, 1}):
        return 1
    if elements in ({-1, 2}, {-1, 0, 2}):
        return 2
    return False

def pixel_pattern(state):
    pattern = []
    for row in state:
        for i in row:
            if i in (1, -1):
                pattern.append(i)
            if len(x): #continue coding here
                pass

def flipped(square, mountain):
    return (square > 0 and not mountain) or (square < 0 and mountain)

def unfold_row(row, x, mountain):
    ''' unfold_row(row of state array, x coordinate, mountain) '''
    newRow = list(row[:x])
    for i in row[x:]:
        if flipped(i, mountain):
            newRow.append(0)
        else:
            newRow.append(i)
    if x == 0:
        flippedPart = row[::-1]
    else:
        flippedPart = row[:x - 1:-1]
    for i in flippedPart:
        if flipped(i, mountain):
            newRow.append(-i)
        else:
            newRow.append(0)
    return tuple(newRow)

def unfold_right(state, x, mountain):
    return tuple([unfold_row(row, x, mountain) for row in state])

def unfold_left(state, x, mountain):
    return tuple([unfold_row(row[::-1], len(row) - x, mountain)[::-1] for row in state])

#Could make unfold_bottom and unfold_top more efficient by directly manipulating rows instead of rotating first
def unfold_bottom_old(state, y, mountain):
    cols = unfold_right([[state[r][c] for r in range(len(state))] for c in range(len(state[0]))], y, mountain)
    return [[cols[r][c] for r in range(len(cols))] for c in range(len(cols[0]))]

def unfold_top_old(state, y, mountain):
    cols = unfold_left([[state[r][c] for r in range(len(state))] for c in range(len(state[0]))], y, mountain)
    return [[cols[r][c] for r in range(len(cols))] for c in range(len(cols[0]))]

def unfold_bottom(state, y, mountain):
    newState = list(state[:y])
    for row in state[y:]:
        newState.append(tuple([(0 if flipped(i, mountain) else i) for i in row]))
    if y == 0:
        flippedPart = state[::-1]
    else:
        flippedPart = state[:y - 1:-1]
    for row in flippedPart:
        newState.append(tuple([(-i if flipped(i, mountain) else 0) for i in row]))
    return tuple(newState)

def unfold_top(state, y, mountain):
    return unfold_bottom(state[::-1], len(state) - y, mountain)[::-1]

def rotate(state):
    return tuple([tuple([state[r][c] for r in range(len(state) - 1, -1, -1)]) for c in range(len(state[0]))])

def reflect_vertical(state):
    return tuple([row[::-1] for row in state])

def variations(state):
    r1 = rotate(state)
    r2 = rotate(r1)
    r3 = rotate(r2)
    return (state, r1, r2, r3,
            reflect_vertical(state), reflect_vertical(r1), reflect_vertical(r2), reflect_vertical(r3))

def find_unfolding(pattern, max_size, max_steps = None, known_min = 0):
    queue = set((pattern,))
    folds = {(pattern, 0): ()}
    steps = 0
    while queue and (max_steps is None or steps < max_steps):
        #print('Processing ' + str(len(queue)) + ' ' + str(steps) + '-step folds')
        steps += 1
        newQueue = set()
        for state in queue:
            toCheck = []
            #Horizontal folds (vertical creases)
            for (x, foldType) in product(range(1, len(state[0])), (True, False)):
                if 2 * len(state[0]) - x <= max_size:
                    newState = unfold_right(state, x, foldType)
                    toCheck.append(newState)
                    folds[(newState, steps)] = folds[(state, steps - 1)] + ('R' + str(x) + 'VM'[foldType],)
                if len(state[0]) + x <= max_size:
                    newState = unfold_left(state, x, foldType)
                    toCheck.append(newState)
                    folds[(newState, steps)] = folds[(state, steps - 1)] + ('L' + str(x) + 'VM'[foldType],)
            #Vertical folds (horizontal creases)
            for (y, foldType) in product(range(1, len(state)), (True, False)):
                if len(state) + y <= max_size:
                    newState = unfold_top(state, y, foldType)
                    toCheck.append(newState)
                    folds[(newState, steps)] = folds[(state, steps - 1)] + ('T' + str(y) + 'VM'[foldType],)
                if 2 * len(state) - y <= max_size:
                    newState = unfold_bottom(state, y, foldType)
                    toCheck.append(newState)
                    folds[(newState, steps)] = folds[(state, steps - 1)] + ('B' + str(y) + 'VM'[foldType],)
            for newState in toCheck:
                if check(newState, known_min):
                     return newState, folds[(newState, steps)], check(newState)
                for v in variations(newState):
                    if v in newQueue:
                        break
                else:
                    newQueue.add(newState)
        queue = newQueue
    return False

def folding_instructions(folds, starting_side):
    instructions = []
    width, height = 3, 3
    for c, fold in enumerate(folds):
        direction = fold[0]
        coordinate = int(fold[1:-1])
        foldType = {'V': 'Valley', 'M': 'Mountain'}[fold[-1]]
        dirName, foldWidth, foldHeight, width, height = {'R': ('rightmost', width - coordinate, height, 2 * width - coordinate, height),
                                          'L': ('leftmost', coordinate, height, width + coordinate, height),
                                          'T': ('top', width, coordinate, width, height + coordinate),
                                          'B': ('bottom', width, height - coordinate, width, 2 * height - coordinate)}[direction]
        instructions.append(str(len(folds) - c) + '. ' + foldType + ' fold the ' + dirName + ' ' + str(foldWidth) + 'x' + str(foldHeight) + ' ' + ('rectangle' if (foldWidth > 1 and foldHeight > 1) else 'strip'))
    return 'Start with a ' + str(width) + 'x' + str(height) + ' sheet of paper with the ' + (None, 'black', 'white')[starting_side] + ' side up' + '\n' + '\n'.join(instructions[::-1]), width

def smallest_start(pattern, max_size):
    for s in range(4, max_size + 1):
        #print()
        #print('Checking ' + str(s) + 'x' + str(s) + ' squares')
        k = find_unfolding(pattern, s)
        if k:
            return folding_instructions(k[1], k[2])
    return None
    #print('None found with size <= ' + str(max_size))

def fewest_folds(pattern, max_size):
    best = None
    for s in range(4, max_size + 1):
        k = find_unfolding(pattern, s)
        if not best or len(best[0]) > len(k[0]):
            best = k
    if best:
        return folding_instructions(best[1], best[2])
    else:
        return None

def print_pattern(pattern):
    print('\n'.join(''.join('!X_'[i] for i in row) for row in pattern))

for i in range(1, 51):
    x = smallest_start(patterns[i], 8)
    if x is None:
        print('Pattern ' + str(i) + ': none found with size <= 8')
        print_pattern(patterns[i])
    else:
        print('Pattern ' + str(i) + ': ' + str(x[1]) + 'x' + str(x[1]) + ', ' + str(x[0].count('\n')) + ' steps')
        print_pattern(patterns[i])
        print(x[0])
    print()
    sys.stdout.flush()
