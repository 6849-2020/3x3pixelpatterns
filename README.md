This is a small repository to compute how to fold an arbitrary black and white pixel pattern, starting from a square sheet of paper with black and white sides, using only simple folds parallel to the edges of the paper. There are modes to minimize the size of the starting paper, and to minimize the number of folds necessary.

The functions in `reverse_folds.py` will generate text instructions on how to fold each pattern (and text_instructions.txt has these instructions for every possible 3×3 pattern), and draw_instructions.py has code to convert these text instructions into SVG drawings (that you can see in the "visual instructions" folder).

The key of the algorithm is to "work backwards", as the name `reverse_folds.py` suggests: we start with a target pattern and guess the last fold, keeping track of where each pixel in the final pattern would have to start. We breadth-first-search until we reach a state where all the black pixels are on one side, and the white pixels on the other. At this point, we can reverse the series of folds to get back to the desired pattern.

We also prune any state where the sheet of paper gets too large (governed by the `max_size` parameter) to narrow the search space. Note that the implementation of this algorithm in this repository is probably highly inefficient, and may take a long time to run for any shapes larger than 3×3.

Happy folding!

---

This code was developed by MrQwerties during the MIT class [6.849: Geometric Folding Algorithms, Fall 2020](https://courses.csail.mit.edu/6.849/fall20/).
