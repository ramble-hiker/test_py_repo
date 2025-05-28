from python_fns import *

def main ():
    throw_type = get_type()
    throw_amount = get_amount()

    if throw_type == "apple":
        throw_apple(throw_amount)
    elif throw_type == "orange":
        throw_orange(throw_amount)
    else:
        print("Incorrect input\n")


    # a = list()
    # a = [1,2,3]
    # print(a)

    # a.append(9)
    # print(a)

    # print(a[0])
    # a = 5
    # list_b = [1,2,3,4,5]
    # list_c = [5,4,3]
    # list_d = [list_b, list_c]
    # set_c = {2}
    # set_c.add(2)
    # print(set_c)

    
if __name__ == "__main__":
    main()