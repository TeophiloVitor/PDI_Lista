import cv2
import numpy as np
import matplotlib.pyplot as plt

def swap_quadrants(image):
    # se a imagem tiver tamanho ímpar, recorta a região para o maior
    # tamanho par possível (-2 = 1111...1110)
    image = image[:image.shape[0] & -2, :image.shape[1] & -2]

    centerX = image.shape[1] // 2
    centerY = image.shape[0] // 2

    # rearranja os quadrantes da transformada de Fourier de forma que 
    # a origem fique no centro da imagem
    # A B   ->  D C
    # C D       B A
    A = image[:centerY, :centerX]
    B = image[:centerY, centerX:]
    C = image[centerY:, :centerX]
    D = image[centerY:, centerX:]

    # swap quadrants (Top-Left with Bottom-Right)
    tmp = A.copy()
    A[:] = D
    D[:] = tmp

    # swap quadrant (Top-Right with Bottom-Left)
    tmp = B.copy()
    B[:] = C
    C[:] = tmp

def calculate_magnitude_spectrum(image):
    # expande a imagem de entrada para o melhor tamanho no qual a DFT pode ser executada,
    # preenchendo com zeros a lateral inferior direita.
    dft_M = cv2.getOptimalDFTSize(image.shape[0])
    dft_N = cv2.getOptimalDFTSize(image.shape[1])
    padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)

    # calcula a DFT
    complex_image = cv2.dft(np.float32(padded), flags=cv2.DFT_COMPLEX_OUTPUT)
    swap_quadrants(complex_image)

    # calcula o espectro de magnitude
    magnitude = cv2.magnitude(complex_image[:, :, 0], complex_image[:, :, 1])
    magnitude += 1
    magnitude = np.log(magnitude)
    magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)

    return magnitude

# Carrega a imagem
image = cv2.imread("teste9.png", cv2.IMREAD_GRAYSCALE)

# Calcula o espectro de magnitude
magnitude_spectrum = calculate_magnitude_spectrum(image)

# Exibe a imagem original e o espectro de magnitude
plt.subplot(121), plt.imshow(image, cmap="gray")
plt.title("Imagem"), plt.axis("off")
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Espectro de magnitude"), plt.axis("off")
plt.show()