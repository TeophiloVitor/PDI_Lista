import cv2
import requests
import numpy as np
from io import BytesIO

def main():
    image_url = "https://agostinhobritojr.github.io/tutorial/pdi/figs/bolhas.png"

    response = requests.get(image_url)
    if response.status_code != 200:
        print("Erro ao fazer o download da imagem")
        return

    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Imagem não carregou corretamente")
        return

    cv2.imshow("imagem original", image)

    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")

    # Excluir bordas
    for i in range(height):
        if image[0, i] == 255:
            cv2.floodFill(image, None, (i, 0), 0)
        if image[width - 1, i] == 255:
            cv2.floodFill(image, None, (i, width - 1), 0)

    for i in range(width):
        if image[i, 0] == 255:
            cv2.floodFill(image, None, (0, i), 0)
        if image[i, height - 1] == 255:
            cv2.floodFill(image, None, (height - 1, i), 0)

    cv2.imwrite("image_semborda.png", image)

    # Buscar objetos presentes
    nobjects = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 255:
                nobjects += 1
                cv2.floodFill(image, None, (j, i), nobjects)

    equalized = cv2.equalizeHist(image)
    cv2.imshow("imagem contada", image)
    cv2.imshow("realce", equalized)

    cv2.imwrite("image_realce.png", equalized)

    # Pintar fundo de branco para contagem de buracos
    cv2.floodFill(image, None, (0, 0), 255)

    # Procurando buracos
    counter = 0
    for i in range(height):
        for j in range(width):
            if image[i, j] == 0 and image[i, j - 1] > counter:
                counter += 1
                cv2.floodFill(image, None, (j - 1, i), counter)

    print(f"bolhas: {nobjects} e bolhas com buracos: {counter}")
    cv2.imshow("image final", image)
    cv2.imwrite("labeling.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
