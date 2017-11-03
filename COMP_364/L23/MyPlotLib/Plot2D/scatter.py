import matplotlib.pyplot as plt

def myscatter(x, y):
    plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    print("testing scatter")
    myscatter([1, 1, 3, 2, 4, 5, 6, 4], [5, 5, 4, 2, 4, 1, 0, 2])
