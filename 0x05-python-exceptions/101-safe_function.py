#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    function that print an integer

    Args:

    value: can be any data

    Return:
    true if integer else false 

    """
    try: 
        print("{:d}".format(value))
    except ( ValueError, StderrError):
        return False 
