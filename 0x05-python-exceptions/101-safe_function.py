#!/usr/bin/pythons
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
