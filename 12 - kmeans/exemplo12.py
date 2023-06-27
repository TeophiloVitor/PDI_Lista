import cv2
import numpy as np
import requests
import io

nClusters = 8
nRodadas = 1

# URL da imagem da internet
image_url = "https://img.freepik.com/fotos-premium/colecao-de-frutas-de-fundo-alimentar-macas-bagas-banana-quadrado-laranjas-frutas_770123-2578.jpg?w=2000"

# Faz o download da imagem da internet
response = requests.get(image_url)
image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

samples = np.float32(image.reshape(-1, 3))

for i in range(10):
    criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10000, 0.0001)
    flags = cv2.KMEANS_RANDOM_CENTERS

    compactness, labels, centers = cv2.kmeans(samples, nClusters, None, criteria, nRodadas, flags)

    centers = np.uint8(centers)
    clustered_image = centers[labels.flatten()]
    clustered_image = clustered_image.reshape(image.shape)

    cv2.imshow("clustered image", clustered_image)

    nome1 = "kmeans_image_" + str(i) + ".png"
    cv2.imwrite(nome1, clustered_image)
    print("###")

    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
