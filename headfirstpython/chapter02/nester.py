import sys
"""This is the "nester.py" module and it provides one function called
    print_lol()which prints lists that may or may not include nested lists."""


def print_lol(the_list):
    """This function takes one positional argument called "the_list", which
        is any Python list (of - possibly - nested lists). Each data item in the
        provided list is (recursively) printed to the screen on it’s own line."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


def print_lol2(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol2(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)


def print_lol3(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol3(each_item, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)

def print_lol4(the_list, indent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol3(each_item, indent, level + 1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fn)
            print(each_item, file=fn)