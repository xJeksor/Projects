# Filip Urban
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = plt.imread('plain.bmp')
    img1 = plt.imread('plain.bmp')

    height = img.shape[0]
    width = img.shape[1]

    for i in range(height):
        for j in range(width):
            img[i, j] ^= np.uint8(420997321)

    plt.imsave('ecb_crypto.bmp', img)

    tmp = np.uint8(420997321)
    for i in range(height - 1):
        for j in range(width - 1):
            img1[i + 1, j + 1] = img1[i, j] ^ tmp
            tmp += img1[i, j]

    plt.imsave('cbc_crypto.bmp', img1)


if __name__ == '__main__':
    main()
