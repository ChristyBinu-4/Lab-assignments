maximum, minimum = 1000, -1000

def alpha_beta(depth, nodeIndex, maximize,
			value_list, alpha, beta):

	if depth == 3:
		return value_list[nodeIndex]

	if maximize:
		best = minimum

		for i in range(0, 2):
			
			value = alpha_beta(depth + 1, nodeIndex * 2 + i,
						False, value_list, alpha, beta)
			best = max(best, value)
			alpha = max(alpha, best)

			if beta <= alpha:
				break
		
		return best
	
	else:
		best = maximum

		for i in range(0, 2):
		
			value = alpha_beta(depth + 1, nodeIndex * 2 + i,
							True, value_list, alpha, beta)
			best = min(best, value)
			beta = min(beta, best)

			if beta <= alpha:
				break
		
		return best

values_list = [3, 5, 6, 9, 1, 2, 0, -1]
print("The terminal nodes : ")
for i in values_list:
  print(i, end=" ")
print("\nThe optimal value is :", alpha_beta(0, 0, True, values_list, minimum, maximum))


