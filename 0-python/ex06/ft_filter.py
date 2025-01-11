def ft_filter(predicate, iterable):
	"""
	Filters an iterable, by returning
	truthy values using a predicate function
	if predicate is None, returns truthy values
	"""
	if not predicate:
		filtered = [e for e in iterable if bool(e) == True]
	else:	
		filtered = [e for e in iterable if predicate(e)]
	return filtered.__iter__()