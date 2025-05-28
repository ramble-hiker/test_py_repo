# import external functions
from python_fns import *

def main ():
    """use external functions, ask what fruit to throw, how many
    return what you chose in statement"""

    throw_type = get_type()
    throw_amount = get_amount()

    if throw_type == "apple":
        throw_apple(throw_amount)
    elif throw_type == "orange":
        throw_orange(throw_amount)
    else:
        print("Incorrect input\n")

    # List practice
    # create list
    # a = list()

    # add to list
    # a = [1,2,3]

    # print list
    # print(a)

    # append and print list
    # a.append(9)
    # print(a)
    
    # print index 0
    # print(a[0])

    # reassign, a as int = 5
    # a = 5

    # make list of lists
    # list_b = [1,2,3,4,5]
    # list_c = [5,4,3]
    # list_d = [list_b, list_c]

    # make set, review adding same value to set, print
    # set_c = {2}
    # set_c.add(2)
    # print(set_c)

    
if __name__ == "__main__":
    main()