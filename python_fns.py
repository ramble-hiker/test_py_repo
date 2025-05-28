def get_type():
    """returns string throw type"""
    throw_type = input("What do you want to throw (\"apple or orange\"?)\n")
    return throw_type
def get_amount():
    """returns number thrown"""
    throw_amount = input("How many do you want to throw")
    return throw_amount
def throw_apple(throw_amount):
    print("You throw ", throw_amount, " apples!")
def throw_orange(throw_amount):
    print("You throw ", throw_amount, " oranges!")