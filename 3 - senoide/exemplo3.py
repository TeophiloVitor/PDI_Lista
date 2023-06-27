import cv2
import numpy as np
import math

SIDE = 256  # Dimensão da imagem (256x256 pixels)
PERIODOS = 8  # Número de períodos da senoide

def main():
    # Nome do arquivo de imagem e arquivo YML
    ss_img = f"senoide-{SIDE}.png"
    ss_yml = f"senoide-{SIDE}.yml"

    # Criação de uma matriz de zeros com as dimensões desejadas
    image = np.zeros((SIDE, SIDE), dtype=np.float32)

    # Abre o arquivo YML para escrita
    fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_WRITE)

    # Preenche a matriz com os valores da senoide
    for i in range(SIDE):
        for j in range(SIDE):
            image[i, j] = 127 * math.sin(2 * math.pi * PERIODOS * j / SIDE) + 128

    # Grava a matriz no arquivo YML
    fs.write("mat", image)
    fs.release()

    # Normaliza os valores da matriz no intervalo [0, 255]
    image_normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    # Converte a matriz para o tipo de dado uint8 (8 bits sem sinal)
    image_normalized = image_normalized.astype(np.uint8)

    # Salva a imagem no formato PNG
    cv2.imwrite(ss_img, image_normalized)

    # Abre o arquivo YML para leitura
    fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_READ)

    # Carrega a matriz do arquivo YML
    image_loaded = fs.getNode("mat").mat()
    fs.release()

    # Normaliza os valores da matriz carregada no intervalo [0, 255]
    image_loaded_normalized = cv2.normalize(image_loaded, None, 0, 255, cv2.NORM_MINMAX)

    # Converte a matriz para o tipo de dado uint8 (8 bits sem sinal)
    image_loaded_normalized = image_loaded_normalized.astype(np.uint8)

    # Exibe a imagem carregada na janela
    cv2.imshow("image", image_loaded_normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
