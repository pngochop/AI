Assignment 1 - Hop N Pham

[depth], [numCreated], [numExpanded], [maxFringe]
In this cases the max branching factor b is 4, d is depth, and l is limit.
-------------------------------------------------------------------
BFS Output: 
    Time Complexity: O(b^d)
1.
python Puzzle.py "123456789AB DEFC" BFS
1, 3, 1, 1

2.
python Puzzle.py "123456789ABC DEF" BFS
3, 16, 7, 10

-------------------------------------------------------------------
DFS Output:
    Time Complexity: O(b^d)
1.
python Puzzle.py "123456789AB DEFC" DFS
Fail to find the solution in two minutes -->  stuck on an infinite depth search.

2.
python Puzzle.py "123456789ABC DEF" DFS
Fail to find the solution in two minutes -->  stuck on an infinite depth search.

-------------------------------------------------------------------
DLS Output:
    Time Complexity:O(b^l)
1.
python Puzzle.py "123456789ABC DFE" DLS 2
-1, 0, 0, 0
2.
python Puzzle.py "123456789ABC DEF" DLS 3
3, 16, 16, 4

-------------------------------------------------------------------
GBFS h1 Output:
    Time Complexity:O(b^d)
1.
python Puzzle.py “123456789AB DEFC” GBFS h1
1, 3, 1, 3

2.
python Puzzle.py "123456789A BCDEF" GBFS h1
24, 6120, 3005, 3116

-------------------------------------------------------------------
GBFS h2 Output:
    Time Complexity:O(b^d)
1.
python Puzzle.py “123456789AB DEFC” GBFS h2
1, 3, 1, 3

2.
python Puzzle.py "123456789A BCDEF" GBFS h2
42, 880, 448, 433
-------------------------------------------------------------------
AStar h1 Output:
    Time Complexity:O(b^d)
1.
python Puzzle.py “123456789AB DEFC” AStar h1
1, 3, 1, 3

2.
python Puzzle.py “123456789ABD EFC” AStar h1
11, 289, 140, 150

AStar h2 Output:
    Time Complexity:O(b^d)
1.
python Puzzle.py "123456789ABC DEF" AStar h2
3, 6, 3, 4

2.
python Puzzle.py “123456789ABD EFC” AStar h2
11, 132, 62, 71


