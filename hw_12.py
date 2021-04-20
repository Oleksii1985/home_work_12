import json


def make_dict():
    """Return dictionary from json-file"""
    with open("HW.json", 'r') as json_file:
        start_dict = json.load(json_file)
    return start_dict


def dict_sort_by_type(start_dict):
    """Return dictionary with sorted types of values"""
    employee = start_dict['employee']
    main_dict = {}
    for human in employee:
        first_name = human.get('firstName')
        last_name = human.get('lastName')
        total_name = f"{first_name} {last_name}"
        int_ = []
        string_ = []
        float_ = []
        none_ = []
        bool_ = []
        for k, v in human.items():
            if type(v) == int:
                int_.append(v)
            elif type(v) == str:
                string_.append(v)
            elif type(v) == float:
                float_.append(v)
            elif type(v) is None:
                none_.append(v)
            elif type(v) == bool:
                bool_.append(v)
        my_dict_types = {'int': int_, 'string': string_, 'float': float_, 'None': none_, 'bool': bool_}
        my_dict_names = {total_name: my_dict_types}
        main_dict.update(my_dict_names)
        start_dict.update({'employee': main_dict})
    return start_dict


def save_sorted_dict(start_dict):
    with open('HW_result.json', 'w') as file:
        json.dump(start_dict, file, indent=3)


def main():
    save_sorted_dict(dict_sort_by_type(make_dict()))


main()
