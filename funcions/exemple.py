import pandas as pd

def create_exemple(): 
    """
    return a data frame exemple.
    """ 
    data = pd.DataFrame({
        'product': ['coffe', 'guanara', 'pastel'], 
        'price': [6, 5, 6],
        'quantity': [20, 10, 15]
    })
    return data
