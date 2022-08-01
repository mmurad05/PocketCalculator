# Mohammad Murad
# vdr4jr
# This program creates multiple functions to recreate a simple four function calculator
# The calculator also remembers the log of recent operations performed

# Initializes the variables needed for the calculator functions
cur_num = 0
rec_op = ""
rec_arg = 0
cur_exp = "0"


def get_value():
    '''
    :return: (int) the value of current number
    '''
    return cur_num


def clear(n=0):
    '''
    Clears recent operations and argument, sets the current
    number and expression to the argument of n

    :param n: (int) defaults to 0, user input
    :return cur_num: (int) value of current number
    '''

    global rec_op
    rec_op = ""
    global rec_arg
    rec_arg = 0
    global cur_num
    cur_num = n
    global cur_exp
    cur_exp = str(n)
    return cur_num


def step(op, arg):
    '''
    Updates the recent arguments and recent operation variables
    Performs the correct operator based on the operator
    Calls helper function to update the current expression

    :param op: (str) the operation to be performed
    :param arg: (int) the number to perform the operation by
    :return cur_num: (int) value of current number
    '''

    global cur_num
    global rec_op
    rec_op = op
    global rec_arg
    rec_arg = arg
    if op == "+":
        cur_num += arg
    elif op == "-":
        cur_num -= arg
    elif op == "*":
        cur_num *= arg
    else:
        cur_num //= arg
    up_exp(op, arg)
    return cur_num


def up_exp(op, arg):
    '''
    Updates current expression based on argument and operation

    :param op: (str) the operation that has been performed
    :param arg: (int) the number the operation has been performed by
    :return: none
    '''

    global cur_exp
    cur_exp = "(" + cur_exp + ")" + op + str(arg)


def repeat():
    '''
    Repeats recent operation if there was one then returns cur_num, else just returns cur_num

    :return cur_num: (int) value of current num
    '''
    global rec_op
    global cur_num
    global rec_arg
    if rec_op == "":
        return cur_num
    else:
        step(rec_op, rec_arg)
        return cur_num


def get_expr():
    '''
    returns current expression

    :return cur_exp: (str) value of cur_exp
    '''
    global cur_exp
    return cur_exp
