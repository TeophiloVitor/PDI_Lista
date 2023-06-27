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
        print("Não foi possível ler a imagem")
        return

    p_1 = int(input("Informe o P1: "))
    p_2 = int(input("Informe o P2: "))

    width = image.shape[1]
    height = image.shape[0]
    print(f"{width}x{height}")

    if p_1 >= height:
        p_1 = height
    if p_2 >= width:
        p_2 = width

    for i in range(p_1, p_2):
        for j in range(p_1, p_2):
            image[i, j] = 255 - image[i, j]

    cv2.imshow("Janela", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
