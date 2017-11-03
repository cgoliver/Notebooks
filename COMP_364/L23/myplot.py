import matplotlib.pyplot as plt

#set some attributes of the module

__doc__ = """
This module implements some useful plotting functions.
"""

__author__ = "Carlos"

def lineplot(y, title=None, xlabel=None, ylabel=None, save=False):
    """
    Makes simple line plot with given y values.
    return: None
    """
    plt.plot(y)
    
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title)
    if save:
        plt.savefig(save)
    plt.show()
    pass
print("hello from myplot!")
