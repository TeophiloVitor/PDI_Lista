import cv2
import requests
import numpy as np
from io import BytesIO

def main():
    image_url = "https://agostinhobritojr.github.io/tutorial/pdi/figs/biel.png"

    response = requests.get(image_url)
    if response.status_code != 200:
        print("Erro ao fazer o download da imagem")
        return

    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Não foi possível abrir a imagem")
        return

    cv2.namedWindow("janela", cv2.WINDOW_AUTOSIZE)

    width = image.shape[1]  # largura
    height = image.shape[0]  # altura

    image_aux = image[0:height // 2, 0:width // 2].copy()
    cv2.imwrite("biel_1.png", image_aux)

    image[0:height // 2, 0:width // 2] = image[height // 2:height, width // 2:width].copy()
    cv2.imwrite("biel_2.png", image)

    image[height // 2:height, width // 2:width] = image_aux.copy()
    cv2.imwrite("biel_3.png", image)

    image_aux = image[0:height // 2, width // 2:width].copy()
    cv2.imwrite("biel_4.png", image_aux)

    image[0:height // 2, width // 2:width] = image[height // 2:height, 0:width // 2].copy()
    cv2.imwrite("biel_5.png", image)

    image[height // 2:height, 0:width // 2] = image_aux.copy()
    cv2.imwrite("biel_6.png", image)

    cv2.imshow("janela", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
