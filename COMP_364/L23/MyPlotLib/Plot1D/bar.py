import numpy as np
import matplotlib.pyplot as plt

def mybar(y):
    """
    Bar graph with y as the heights.
    """
    plt.bar(np.arange(0, len(y), 1), y)
    plt.show()
if __name__ == "__main__":
    print("testing")
    mybar([1, 2, 3, 4])
