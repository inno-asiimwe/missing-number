def find_missing(list1, list2):

    if isinstance(list1, list) and isinstance(list2, list):

        if len(list1) == len(list2):
            return 0
        if len(list1) < len(list2):
            for item in list2:
                if not item in list1:
                    return item

        for item in list1:
            if not item in list2:
                return item
    raise(TypeError, "one or more inputs not a list")
