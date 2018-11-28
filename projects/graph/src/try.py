def time_planner(a, b, dur):
	if len(a) >= len(b):
		longest = a
		shortest = b
	elif len(a) < len(b):
		longest = b
		shortest = a
	for i in longest:
		if i[1] - i[0] >= dur:
			for j in shortest:
				if j[1] - i[0] >= dur:
					if i[0] in range(j[0], j[1]):
						return (i[0], i[0] + dur)
	return None
