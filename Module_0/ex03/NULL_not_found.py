def NULL_not_found(object: any) -> int:
    match object:
        case None:
            type_name = "Nothing"
        case float() if object != object:
            type_name = "Cheese"
        case bool() if object is False:
            type_name = "Fake"
        case int() if object == 0:
            type_name = "Zero"
        case str() if object == "":
            type_name = "Empty"
        case _:
            print("Type not Found")
            return 1
    print(f"{type_name}: {object} {type(object)}")
    return (0)
