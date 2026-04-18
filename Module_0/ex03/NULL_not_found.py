def NULL_not_found(object: any) -> int:
    data_type = type(object)
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: f"{object} is in the kitchen",
        None: "Nothing",
        
    }
    type_name = type_map.get(data_type)
    print(type_name, data_type, sep=" : ")
    return (42)
