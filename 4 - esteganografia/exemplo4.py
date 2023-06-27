import cv2
import numpy as np
import sys

nbits = 3

def recover_image():
    # Verificar se o nome do arquivo de imagem foi fornecido como argumento de linha de comando
    if len(sys.argv) < 2:
        sys.exit(1)

    # Carregar a imagem resultante da esteganografia
    imagem_resultante = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

    if imagem_resultante is None:
        print("Não foi possível carregar a imagem resultante da esteganografia.")
        sys.exit(1)

    # Criar uma matriz de zeros para a imagem recuperada
    imagem_recuperada = np.zeros_like(imagem_resultante)

    for i in range(imagem_resultante.shape[0]):
        for j in range(imagem_resultante.shape[1]):
            val_resultante = imagem_resultante[i, j]
            val_recuperada = np.zeros(3, dtype=np.uint8)

            for k in range(3):
                val_recuperada[k] = val_resultante[k] << (8 - nbits) & 0xFF

            imagem_recuperada[i, j] = val_recuperada

    filename = 'imagem_final.png'

    cv2.imwrite(filename, imagem_recuperada)
    # Exibir a imagem recuperada
    cv2.imshow("Imagem Final", imagem_recuperada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recover_image()
