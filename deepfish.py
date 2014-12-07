
class Deepfish(Player):
	def __init__(self, func, maxd=5):	#max depth of whatever
		self._func = func
		self._pos = sunfish.Position(sunfish.initial, 0, (True,True), (True,True), 0, 0)
		self._maxd = maxd

	def move(self, gn_current):
		assert(gn_current.board().turn == 0)

		if gn_current.move is not None:
			


def iterativeMTDF(pos, maxd, guess): 
	#initialize guess here?
	g = guess
	for d in range(0, maxd):
		g = MTDF(pos, g, d)
		#break when out of time
	return g

def MTDF(pos, d, guess, func):
	g = guess
	upperbound = float('inf')
	lowerbound = float('-inf')
	while lowerbound < upperbound:
		if g == lowerbound:
			beta = g + 1	#need to check bounds of state values
		else:
			beta = g

		g = alphabeta(pos, beta - 1, beta, d, func)

		if g < beta:
			upperbound = g
		else
			lowerbound = g

	return g

def alphabeta(pos, alpha, beta, d, func):
	#if it's already in the table
	if pos in table:
		N = table[pos]
		if N.lowerbound => beta: return N.lowerbound
		if N.upperbound <= alpha: return N.upperbound

		alpha = max(alpha, N.lowerbound)
		beta = min(beta, N.upperbound)

	if d == 0: g = func(pos)
	else if N == MAXNODE

		g = float("-inf")
		a = alpha #save original alpha value

		for move in pos.genMoves():
			if g < beta:
				g = max(g, alphabeta(move, a, beta, d-1))
				a = max(a, g)

	else # N == MINNODE

		g = float("inf")
		b = beta

		for move in pos.genMoves():
			if g > alpha:
				g = min(g, alphabeta(move, alpha, b, d-1))
				b = min(b, g)


	if g <= alpha:
		N.upperbound = g
	if g > alpha and g < beta:
		N.lowerbound = g 
		N.upperbound = g
	if g >= beta:
		N.lowerbound = g
	
	#put N in the table. 

	return g













