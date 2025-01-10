known_types = {
	list: "List",
	tuple: "Tuple",
	set: "Set",
	dict: "Dict",
	str: "Brian is in the kitchen",
}

def all_thing_is_obj(object: any) -> int:
	obj_type = type(object)
	if obj_type in known_types:
		print(
			known_types[obj_type],
			":",
			obj_type
		)
	else:
		print("Type not found")

	return 42