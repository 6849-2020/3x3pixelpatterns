import drawSvg as draw

def fold_row(row, x, mountain):
    result = row[:x]
    for i in range(len(row) - x):
        if mountain:       
            result[x - 1 - i] = result[x - 1 - i] + row[x + i][::-1]
        else:
            result[x - 1 - i] = row[x + i][::-1] + result[x - 1 - i]
    for i in range(2 * x - len(row)):
        if mountain:
            result[i] = result[i] + [0,] * len(row[0])
        else:
            result[i] = [0,] * len(row[0]) + result[i]
    return result

def fold_right(state, x, mountain):
    return [fold_row(row, x, mountain) for row in state]

def fold_left(state, x, mountain):
    return [fold_row(row[::-1], len(row) - x, mountain)[::-1] for row in state]

def fold_top(state, y, mountain):
    cols = fold_right([[state[r][c] for r in range(len(state))] for c in range(len(state[0]))], len(state) - y, mountain)
    return [[cols[r][c] for r in range(len(cols))] for c in range(len(cols[0]))]

def fold_bottom(state, y, mountain):
    cols = fold_left([[state[r][c] for r in range(len(state))] for c in range(len(state[0]))], len(state) - y, mountain)
    return [[cols[r][c] for r in range(len(cols))] for c in range(len(cols[0]))]


def initial_state(width, height, top_color):
    return [[[top_color, 3 - top_color] for j in range(width)] for i in range(height)]

COLORS = {1: '#bbb', 2: 'white'}
BORDER_COLOR = '#ddd'
EDGE_COLOR = 'black'

def draw_state(d, state, x0=0, y0=0, square_size=32):
    width, height, depth = len(state[0]), len(state), len(state[0][0])
    layers = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            layer = 0
            while state[i][j][layer] == 0:
                layer += 1
            color = COLORS[state[i][j][layer]]
            d.append(draw.Rectangle(x0 + j * square_size, y0 + i * square_size, square_size + 1, square_size + 1, fill=color))
            layers[i][j] = layer
    #Draw dividing lines
    #Vertical lines
    for i in range(height):
        for j in range(width - 1):
            if layers[i][j] == layers[i][j + 1]:
                d.append(draw.Lines(x0 + (j + 1) * square_size, y0 + i * square_size,
                                    x0 + (j + 1) * square_size, y0 + (i + 1) * square_size,
                                    close=False, stroke=BORDER_COLOR, stroke_width=1, fill='none'), z=0)
            else:
                d.append(draw.Lines(x0 + (j + 1) * square_size, y0 + i * square_size,
                                    x0 + (j + 1) * square_size, y0 + (i + 1) * square_size,
                                    close=False, stroke=EDGE_COLOR, stroke_width=2, fill='none'), z=10)
    #Horizontal lines
    for i in range(height - 1):
        for j in range(width):
            if layers[i][j] == layers[i + 1][j]:
                d.append(draw.Lines(x0 + j * square_size, y0 + (i + 1) * square_size,
                                    x0 + (j + 1) * square_size, y0 + (i + 1) * square_size,
                                    close=False, stroke=BORDER_COLOR, stroke_width=1, fill='none'), z=0)
            else:
                d.append(draw.Lines(x0 + j * square_size, y0 + (i + 1) * square_size,
                                    x0 + (j + 1) * square_size, y0 + (i + 1) * square_size,
                                    close=False, stroke=EDGE_COLOR, stroke_width=2, fill='none'), z=10)
    #Draw outside border            
    d.append(draw.Lines(x0, y0,
                        x0 + width * square_size, y0,
                        x0 + width * square_size, y0 + height * square_size,
                        x0, y0 + height * square_size,
                        close=True, stroke=EDGE_COLOR, stroke_width=2, fill='none'), z=10)

CREASE_COLOR = 'black'
def draw_folds(width, height, top_color, folds, square_size = 32):
    states = [initial_state(width, height, top_color),]
    fold_instructions = []

    arrowhead_valley = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, orient='auto')
    arrowhead_valley.append(draw.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, stroke_width=0.1, stroke = 'black', fill='black', close=True))
    arrowhead_mountain = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, stroke = 'grey', orient='auto')
    arrowhead_mountain.append(draw.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, stroke_width=0.1, stroke = 'grey', fill='white', close=True))
             
    for fold in folds:
        coord, foldType = int(fold[1:-1]), fold[-1] == 'M'
        h, w = len(states[-1]), len(states[-1][0])
        if foldType:
            dash = '10 2 2 2'
        else:
            dash = '4'
        if fold[0] == 'L':
            states.append(fold_left(states[-1], coord, foldType))
            line = (coord * square_size, 0, coord * square_size, h * square_size)
            if foldType:
                arrow = (coord * square_size, (h/2 + 1) * square_size, square_size * 2/3**0.5, 240, 300, False, 'grey', arrowhead_mountain, 5)
            else:
                arrow = (coord * square_size, (h/2 - 1) * square_size, square_size * 2/3**0.5, 120, 60, True, 'black', arrowhead_valley, 15)
        if fold[0] == 'R':
            states.append(fold_right(states[-1], coord, foldType))
            line = (coord * square_size, 0, coord * square_size, h * square_size)
            if foldType:
                arrow = (coord * square_size, (h/2 + 1) * square_size, square_size * 2/3**0.5, 300, 240, True, 'grey', arrowhead_mountain, 5)
            else:
                arrow = (coord * square_size, (h/2 - 1) * square_size, square_size * 2/3**0.5, 60, 120, False, 'black', arrowhead_valley, 15)
        if fold[0] == 'B':
            states.append(fold_bottom(states[-1], coord, foldType))
            coord = h - coord
            line = (0, coord * square_size, w * square_size, coord * square_size)
            if foldType:
                arrow = ((w/2 - 1) * square_size, coord * square_size, square_size * 2/3**0.5, 330, 30, False, 'grey', arrowhead_mountain, 5)
            else:
                arrow = ((w/2 + 1) * square_size, coord * square_size, square_size * 2/3**0.5, 210, 150, True, 'black', arrowhead_valley, 15)
        if fold[0] == 'T':
            states.append(fold_top(states[-1], coord, foldType))
            coord = h - coord
            line = (0, coord * square_size, w * square_size, coord * square_size)
            if foldType:
                arrow = ((w/2 - 1) * square_size, coord * square_size, square_size * 2/3**0.5, 30, 330, True, 'grey', arrowhead_mountain, 5)
            else:
                arrow = ((w/2 + 1) * square_size, coord * square_size, square_size * 2/3**0.5, 150, 210, False, 'black', arrowhead_valley, 15)
        fold_instructions.append((line, dash, arrow))
    width = square_size * (sum(len(state[0]) for state in states) + len(states) - 1)
    d = draw.Drawing(width + 1, square_size * len(states[0]) + 1)
    x0 = 0
    for (i, state) in enumerate(states):
        y0 = square_size/2 * (height - len(state))
        draw_state(d, state, x0, y0, square_size)
        if i < len(fold_instructions):
            cr, dash, ar = fold_instructions[i]
            d.append(draw.Line(x0 + cr[0], y0 + cr[1], x0 + cr[2], y0 + cr[3],
                           stroke=CREASE_COLOR, stroke_width = 1, fill='none', stroke_dasharray=dash), z=20)
            d.append(draw.Arc(x0 + ar[0], y0 + ar[1], ar[2], ar[3], ar[4], ar[5], stroke=ar[6], stroke_width=1, fill='none', marker_end=ar[7]), z = ar[8])
        x0 += square_size * (len(state[0]) + 1)
    return d

def folds_from_text_instructions(text):
    lines = text.split('\n')[::2]
    n = int(lines[0].split(' ')[1][:-1])
    start = lines[4].split(' ')
    size = start[3].split('x')
    width, height = int(size[0]), int(size[1])
    current_width, current_height = width, height
    top_color = 1 + (start[-3] == 'white')
    folds = []
    for line in lines[5:]:
        words = line.split(' ')
        if words[4] == 'bottom':
            coord = current_height - int(words[5].split('x')[1])
            fold = 'B' + str(coord)
            current_height = coord
        elif words[4] == 'top':
            coord = int(words[5].split('x')[1])
            fold = 'T' + str(coord)
            current_height = current_height - coord
        elif words[4] == 'leftmost':
            coord = int(words[5].split('x')[0])
            fold = 'L' + str(coord)
            current_width = current_width - coord
        elif words[4] == 'rightmost':
            coord = current_width - int(words[5].split('x')[0])
            fold = 'R' + str(coord)
            current_width = coord
        folds.append(fold + words[1][0])
    return (n, width, height, top_color, folds)

file = open('text_instructions.txt', 'r').read()
for pattern in file.split('\n\n\n\n'):
    n, width, height, top_color, folds = folds_from_text_instructions(pattern)
    d = draw_folds(width, height, top_color, folds)
    d.saveSvg('visual instructions/' + '0' * (n < 10) + str(n) + '.svg')
