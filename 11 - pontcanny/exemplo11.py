import cv2
import numpy as np
import random
import requests
from io import BytesIO

STEP = 6
JITTER = 4
RAIO = 6
RAIO_PEQUENO = 3

url = 'https://cdn.wizard.com.br/wp-content/uploads/2017/01/05115936/aprenda-os-nomes-das-frutas-em-ingles.jpg'  # Substitua pela URL da imagem desejada

# Faz a requisição GET para obter a imagem
response = requests.get(url)
image_data = response.content

# Carrega a imagem usando o OpenCV
image = cv2.imdecode(np.array(bytearray(image_data), dtype=np.uint8), cv2.IMREAD_COLOR)

height, width, _ = image.shape
xrange = list(range(0, height, STEP))
yrange = list(range(0, width, STEP))

points = np.full((height, width, 3), (255, 255, 255), dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica o algoritmo de Canny na imagem
border = cv2.Canny(gray, 80, 240)

cv2.imshow("bordas_canny", border)
cv2.waitKey(0)

# Realiza amostragem dos pontos
random.shuffle(xrange)
random.shuffle(yrange)

for i in xrange:
    for j in yrange:
        x = i + random.randint(-JITTER, JITTER)
        y = j + random.randint(-JITTER, JITTER)

        x = min(max(x, 0), height - 1)
        y = min(max(y, 0), width - 1)

        color = tuple(map(int, image[x, y]))
        cv2.circle(points, (y, x), RAIO, color, -1, cv2.LINE_AA)

cv2.imshow("imagem_pontilhista", points)
cv2.waitKey(0)

pontos = []
for i in range(height):
    for j in range(width):
        if border[i, j] != 0:
            color = tuple(map(int, image[i, j]))
            pontos.append([j, i, color[0], color[1], color[2], 0])

random.shuffle(pontos)

for ponto in pontos:
    x, y, b, g, r, _ = ponto
    color = (b, g, r)
    cv2.circle(points, (x, y), RAIO_PEQUENO, color, -1, cv2.LINE_AA)

cv2.imshow("imagem_pontilhista_corrigida", points)
cv2.waitKey(0)

cv2.imwrite("cannypoints.png", points)
cv2.destroyAllWindows()
