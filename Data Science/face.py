from scipy import misc
import matplotlib.pyplot as plt

def test():
    face = misc.face()
    plt.imshow(face)
    plt.show()