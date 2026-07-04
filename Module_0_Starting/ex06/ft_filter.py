def ft_filter(function, iterable):
    """
    Return a list of items from iterable for which function(item) is True.

    This is a custom re-implementation of Python's built-in filter().

    Args:
        function: A function that takes one argument and returns a boolean,
                  or None (in which case bool() is used).
        iterable: Any iterable object (list, tuple, string, etc.).

    Returns:
        list: A new list containing the items where function(item) is True.

    Note:
        Unlike the built-in filter(), this returns a list (not an iterator).
    """
    if function is None:
        function = bool
    return [item for item in iterable if function(item)]
