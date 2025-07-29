"""
divide.py
---------
Provides a function to divide two numbers.

Functions
---------
divide(a, b)
    Returns the result of dividing a by b.
"""

def divide(a, b):
    """Return the result of dividing a by b.
    
    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.
    
    Returns
    -------
    float
        The result of a / b.
    
    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
