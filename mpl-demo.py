import argparse
import sys
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=u'Test Matplotlib Plot')


def main():
    args = parser.parse_args()

    fig, ax = plt.subplots()

    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (1.58, -2.57)),
        (Path.CURVE4, (0.35, -1.1)),
        (Path.CURVE4, (-1.75, 2.0)),
        (Path.CURVE4, (0.375, 2.0)),
        (Path.LINETO, (0.85, 1.15)),
        (Path.CURVE4, (2.2, 3.2)),
        (Path.CURVE4, (3, 0.05)),
        (Path.CURVE4, (2.0, -0.5)),
        (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
    ax.add_patch(patch)

    x, y = zip(*path.vertices)
    line, = ax.plot(x, y, 'go-')

    ax.grid()
    ax.axis('equal')
    plt.savefig('heart.png', dpi=200)
    plt.savefig('heart.pdf', dpi=200)
    plt.show()

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
