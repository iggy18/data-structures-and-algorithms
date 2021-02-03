def left_join(dict_one, dict_two):
    joined_dict = dict()
    for key in dict_one:
        joined_dict[key] = [dict_one[key]]
        if dict_two.get(key):
            joined_dict[key].append(dict_two[key])
        else:
            joined_dict[key].append(None)
    return joined_dict
