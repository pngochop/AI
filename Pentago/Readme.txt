MiniMax and AlphaBeta Search Algorithms:

Branching Factor (b) = n_positions * n_blocks * n_directions = 36 * 4 * 2 = 288

AlphaBeta:
	Expanded Nodes: 
	- Nodes Expanded: 33168, Depth Limit: 2 (After player did 5 moves, Player won!)
	- Nodes Expanded: 1501093, Depth Limit: 3 (After player did 6 moves, Player won!)
	- Tried Depth Limit = 4,5 AI had smarter choices
	
	Best Case:
	- Time Complexity:  O(b^(d/2))
	- Space Complexity: O(b^(d/2))

	Worst Case:
	- Time Complexity:  O(b^d)
	- Space Complexity: O(b^d)

MiniMax:
	Expanded Nodes: After player did 3 moves.
	- Nodes Expanded: 119288, Depth Limit: 2
	- Nodes Expanded: 25000560, Depth Limit: 3

	Best Case:
	- Time Complexity:  O(b^d)
	- Space Complexity: O(b^d)

	Worst Case:
	- Time Complexity:  O(b^d)
	- Space Complexity: O(b^d)

Number of Expanded nodes recorded with algorithm determining second move, after player turn '1/5 1r'