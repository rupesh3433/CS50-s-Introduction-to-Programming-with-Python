def main():
    grocery_dict = get_grocery_items()
    if grocery_dict:
        #sorted function only returns list of keys, not value
        sorted_list_of_keys = sorted(grocery_dict)
        for key in sorted_list_of_keys:
            print(grocery_dict[key], key.upper())

def get_grocery_items():
    grocery_list = []
    while True:
        try:
            item = input().strip()
            if item:
                grocery_list.append(item)
        except EOFError:
            break
    grocery_dict = {}
    for item in grocery_list:
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    return grocery_dict


main()
