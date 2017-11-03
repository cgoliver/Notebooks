from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def my3d_scatter(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z)

    plt.show()

if __name__ == "__main__":
    print("testing 3d scatter")
    my3d_scatter([1, 1, 2,3], [4, 5, 3, 1], [4, 4, 5, 1])
