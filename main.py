def add_item(lst, item):
    lst.append(item)

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)

def print_list(lst):
    for item in lst:
        print(item)
input("\nНатисніть Entr, щоб закрити програму...")