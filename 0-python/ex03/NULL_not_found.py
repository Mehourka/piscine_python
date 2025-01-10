Map = {
    type(None): "Nothing",
    float: "Cheese",
    int: "Zero",
    str: "Empty",
    bool: "Fake"
}


def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object != object:
        pass
    elif object or obj_type not in Map:
        print("Type not found")
        return 1

    print(Map[obj_type], ":", object, type(object))
    return 0
