def insert_sorted_dict_array(array: list, item: dict, key: str):
    half = 0
    value = item[key]
    temp_array = array
    found = False
    while not found:
        half = round(len(temp_array) / 2)
        half_value = temp_array[half][key]
        if value < half_value:
            temp_array = temp_array[:half]
        elif value > half_value:
            temp_array = temp_array[half:]
        else:
            found = True

    return array[:half] + [item] + array[half:]

