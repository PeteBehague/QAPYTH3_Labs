#! /usr/bin/python

"""
    This module supplies functions sprintf, fprintf,
    and printf.
    
    >>> printf("%s","hello")
    hello
    >>> printf("%x",42)
    2a
    >>> printf("|%06.2f %-12s|", 3.1426, "hello")
    |003.14 hello       |

    Generate Hex value for 15310212104174
    >>> var = sprintf("%X",15310212104174)
    >>> print(var)
    DECAFC0FFEE
"""
import sys

def sprintf(fmt, *args):
    rstr = fmt % args
    return rstr

def fprintf(file, fmt, *args):
    file.write(sprintf(fmt, *args))
    return
    
def printf(fmt, *args):
    fprintf(sys.stdout, fmt, *args)
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    