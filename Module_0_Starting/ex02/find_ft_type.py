def all_thing_is_obj(object: any) -> int:
    data_type = type(object)
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: f"{object} is in the kitchen",
    }
    type_name = type_map.get(data_type)
    if (type_name is None):
        print("Type not found")
    else:
        print(type_name, data_type, sep=" : ")
    return (42)
