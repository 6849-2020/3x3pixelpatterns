from functools import reduce
from itertools import product

#State arrays are 2D rectangular arrays full of integers from -2 to 2, inclusive
#The numbers represent colored grid squares as follows:
#-2 - white, bottom
#-1 - black, bottom
#0  - unknown
#1  - black, top
#2  - white, top

#Sparse states are in the form (w, h, points), with points being a list of 9 3-tuples
#In the sparse representation (x, y, d) represents the (x, y) coordinates of the square, and d represents color, and if it's on the top or bottom by the scheme above

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

def fold_row(row, x, mountain):
    if 2 * x < len(row):
        return False
    newRow = list(row[:x])
    for i in range(x, len(row)):
        if flipped(row[i], mountain):
            return False
        if newRow[2 * x - 1 - i] != 0:
            return False
        newRow[2 * x - 1 - i] = -row[i]
    return newRow

def unfold_point_right(width, height, point, x, mountain):
    if point[0] < x or not flipped(point[2], mountain):
        return point
    return (2 * width - 1 - point[0], point[1], -point[2])

def unfold_point_left(width, height, point, x, mountain):
    if point[0] >= x or not flipped(point[2], mountain):
        return (point[0] + x, point[1], point[2])
    return (x - 1 - point[0], point[1], -point[2])

def unfold_point_bottom(width, height, point, y, mountain):
    if point[1] < y or not flipped(point[2], mountain):
        return point
    return (point[0], 2 * height - 1 - point[1], -point[2])

def unfold_point_top(width, height, point, y, mountain):
    if point[1] >= y or not flipped(point[2], mountain):
        return (point[0], point[1] + y, point[2])
    return (point[0], y - 1 - point[1], -point[2])

def unfold_sparse(state, direction, coord, mountain):
    width, height, points = state
    unfold_func = {'R': unfold_point_right, 'L': unfold_point_left,
                   'B': unfold_point_bottom, 'T': unfold_point_top}[direction]
    newPoints = tuple([unfold_func(width, height, point, coord, mountain) for point in points])
    if direction == 'R':
        width = 2 * width - coord
    elif direction == 'L':
        width += coord
    elif direction == 'B':
        height = 2 * height - coord
    elif direction == 'T':
        height += coord
    return sort_sparse((width, height, newPoints))

def pattern_to_sparse(pattern):
    return (3, 3, tuple([(j, i, pattern[i][j]) for (i, j) in product(range(3), range(3))]))

def check_sparse(state):
    width, height, points = state
    if width != height:
        return False
    elements = set(point[2] for point in points)
    if elements in ({-2, 1}, {-2, 0, 1}):
        return 1
    if elements in ({-1, 2}, {-1, 0, 2}):
        return 2
    return False

def sparse_matches_dense(sparse, dense):
    width, height, points = sparse
    if width != len(dense[0]) or height != len(dense):
        return False
    for point in points:
        if dense[point[1]][point[0]] != point[2]:
            return False
    return True

def rotate(state):
    return tuple([tuple([state[r][c] for r in range(len(state) - 1, -1, -1)]) for c in range(len(state[0]))])

def reflect_vertical(state):
    ''' reflect_vertical(state) -> state, reflected about a vertical axis '''
    return tuple([row[::-1] for row in state])

def rotate_sparse(state):
    width, height, points = state
    return (height, width, tuple((point[1], width - 1 - point[0], point[2]) for point in points))

def reflect_vertical_sparse(state):
    width, height, points = state
    return (width, height, tuple((width - 1 - point[0], point[1], point[2]) for point in points))

def variations(state):
    ''' variations(state) -> list of 8 reflections/rotates of state '''
    r1 = rotate(state)
    r2 = rotate(r1)
    r3 = rotate(r2)
    return (state, r1, r2, r3,
            reflect_vertical(state), reflect_vertical(r1), reflect_vertical(r2), reflect_vertical(r3))

def variations_sparse(state):
    r1 = rotate_sparse(state)
    r2 = rotate_sparse(r1)
    r3 = rotate_sparse(r2)
    return (state, r1, r2, r3,
            reflect_vertical_sparse(state), reflect_vertical_sparse(r1),
            reflect_vertical_sparse(r2), reflect_vertical_sparse(r3))

def sort_sparse(state):
    width, height, points = state
    return (width, height, tuple(sorted(points, key = lambda p: p[0] + 100 * p[1])))

def already_present(state, queue):
    ''' already_present(state, queue) -> bool
Checks if state, or any variation of it, is already present in the queue. '''
    for v in variations(state):
        if v in queue:
            return True
    return False

def find_unfolding(pattern, max_size, max_steps = None, known_min = 0, sparse = False):
    if sparse:
        queue = set((pattern_to_sparse(pattern),))
        folds = {(pattern_to_sparse(pattern), 0): ()}
    else:
        queue = set((pattern,))
        folds = {(pattern, 0): ()}
    steps = 0
    while queue and (max_steps is None or steps < max_steps):
        print('Processing ' + str(len(queue)) + ' ' + str(steps) + '-step folds')
        steps += 1
        newQueue = set()
        n = 0
        for state in queue:
            n += 1
            if n % 10000 == 0:
                print(str(n) + '/' + str(len(queue)) + ': ' + str(100 * n/len(queue)) + '%')
            toCheck = []

            if sparse:
                width, height = state[:2]
            else:
                width, height = len(state[0]), len(state)
                
            #Horizontal folds (vertical creases)
            if steps == max_steps:
                #Right
                x = 2 * width - height
                if 0 < x < width:
                    for foldType in (True, False):
                        if sparse:
                            newState = unfold_sparse(state, 'R', x, foldType)
                        else:
                            newState = unfold_right(state, x, foldType)
                        if sparse and check_sparse(newState):
                            return newState, folds[(state, steps - 1)] + ('R' + str(x) + 'VM'[foldType],), check_sparse(newState)
                        if not sparse and check(newState, known_min):
                            return newState, folds[(state, steps - 1)] + ('R' + str(x) + 'VM'[foldType],), check(newState)
                        
                #Left
                x = height - width
                if 0 < x < width:
                    for foldType in (True, False):
                        if sparse:
                            newState = unfold_sparse(state, 'L', x, foldType)
                        else:
                            newState = unfold_left(state, x, foldType)
                        if sparse and check_sparse(newState):
                            return newState, folds[(state, steps - 1)] + ('L' + str(x) + 'VM'[foldType],), check_sparse(newState)
                        if not sparse and check(newState, known_min):
                            return newState, folds[(state, steps - 1)] + ('L' + str(x) + 'VM'[foldType],), check(newState)
                        
                #Top
                y = width - height
                if 0 < y < height:
                    for foldType in (True, False):
                        if sparse:
                            newState = unfold_sparse(state, 'T', y, foldType)
                        else:
                            newState = unfold_right(state, y, foldType)
                        if sparse and check_sparse(newState):
                            return newState, folds[(state, steps - 1)] + ('T' + str(y) + 'VM'[foldType],), check_sparse(newState)
                        if not sparse and check(newState, known_min):
                            return newState, folds[(state, steps - 1)] + ('T' + str(y) + 'VM'[foldType],), check(newState)
                        
                #Top
                y = 2 * height - width
                if 0 < y < height:
                    for foldType in (True, False):
                        if sparse:
                            newState = unfold_sparse(state, 'B', y, foldType)
                        else:
                            newState = unfold_right(state, y, foldType)
                        if sparse and check_sparse(newState):
                            return newState, folds[(state, steps - 1)] + ('B' + str(y) + 'VM'[foldType],), check_sparse(newState)
                        if not sparse and check(newState, known_min):
                            return newState, folds[(state, steps - 1)] + ('B' + str(y) + 'VM'[foldType],), check(newState)
            else:
                for (x, foldType) in product(range(1, width), (True, False)):
                    if 2 * width - x <= max_size:
                        if sparse:
                            newState = unfold_sparse(state, 'R', x, foldType)
                        else:
                            newState = unfold_right(state, x, foldType)
                        toCheck.append((newState, 'R' + str(x) + 'VM'[foldType]))
                    if width + x <= max_size:
                        if sparse:
                            newState = unfold_sparse(state, 'L', x, foldType)
                        else:
                            newState = unfold_left(state, x, foldType)
                        toCheck.append((newState, 'L' + str(x) + 'VM'[foldType]))
                        
                #Vertical folds (horizontal creases)
                for (y, foldType) in product(range(1, height), (True, False)):
                    if height + y <= max_size:
                        if sparse:
                            newState = unfold_sparse(state, 'T', y, foldType)
                        else:
                            newState = unfold_top(state, y, foldType)
                        toCheck.append((newState, 'T' + str(y) + 'VM'[foldType]))
                    if 2 * height - y <= max_size:
                        if sparse:
                            newState = unfold_sparse(state, 'B', y, foldType)
                        else:
                            newState = unfold_bottom(state, y, foldType)
                        toCheck.append((newState, 'B' + str(y) + 'VM'[foldType]))
                        
                for newState, newFold in toCheck:
                    if sparse and check_sparse(newState):
                        return newState, folds[(state, steps - 1)] + (newFold,), check_sparse(newState)
                    elif not sparse and check(newState, known_min):
                        return newState, folds[(state, steps - 1)] + (newFold,), check(newState)

                    if sparse:
                        for v in variations_sparse(newState):
                            if sort_sparse(v) in newQueue:
                                break
                        else:
                            newQueue.add(newState)
                            folds[(newState, steps)] = folds[(state, steps - 1)] + (newFold,)
                    else:
                        for v in variations(newState):
                            if v in newQueue:
                                break
                        else:
                            newQueue.add(newState)
                            folds[(newState, steps)] = folds[(state, steps - 1)] + (newFold,)
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

def smallest_start(pattern, max_size, min_size = 4):
    for s in range(min_size, max_size + 1):
        print()
        print('Checking ' + str(s) + 'x' + str(s) + ' squares')
        k = find_unfolding(pattern, s)
        if k:
            #return folding_instructions(k[1], k[2])
            print(folding_instructions(k[1], k[2])[0])
            return
    #return None
    print('None found with size <= ' + str(max_size))

def print_pattern(pattern):
    print('\n'.join(''.join('!X_'[i] for i in row) for row in pattern))

a = find_unfolding(patterns[50], 9, None, 9, True)
x = open('50.txt', 'w')
x.write(str(a))
x.close()
##for i in range(1, 51):
##    x = smallest_start(patterns[i], 8)
##    if x is None:
##        print('Pattern ' + str(i) + ': none found with size <= 8')
##        print_pattern(patterns[i])
##    else:
##        print('Pattern ' + str(i) + ': ' + str(x[1]) + 'x' + str(x[1]) + ', ' + str(x[0].count('\n')) + ' steps')
##        print_pattern(patterns[i])
##        print(x[0])
##    print()
