# 💡 Listas de exercícios de Processamento Digital de Imagens

## Discente
Teophilo Vitor de Carvalho Clemente | 20220080516</p>
Graduação em Engenharia da Computação - UFRN</p> 

## Objetivo 
Neste repositório serão apresentados os códigos, resultados e explicações acerca dos exercícios desenvolvidos ao longo da disciplina de Processamento Digital de Imagens, os respectivos enunciados e material da disciplina podem ser encontrados na página do professor Dr. Agostinho [[Link]](https://agostinhobritojr.github.io/tutorial/pdi/). Os códigos foram desenvolvidos em Python juntamente com a biblioteca OpenCV, para isso converti os códigos disponibilizados pelo professor para Python e no discorrer desde README eles serão apresentados e explicados.

## Solução

Para rodar os códigos, é preciso ter Python instalado na sua máquina e a biblioteca OpenCV, em alguns casos foram utilizados outras biblioetecas especificadas em cada código. Contudo, a seguir serão apresentados os códigos, explicações e os respectivos resultados obtidos em cada um. Para melhor organização eles estão dividos em Parte I, II, III e IV como no tutotial do professor.

## 🔔 PARTE I

# 🔭 Exercício 2.1

Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa regions.cpp. Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente.</p>

# Solução

Para resolver foram implementas entradas para o usuário escolher qual região ele queria deixar em negativo. Para deixar deixar a região em negativo foi feito um for para percorrer área escolhida e fazer a operação que faz com que o pixel da imagem se torne negativo, como mostrado no código a seguir:</p>
```python
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
```
Entrada:</p>
<p align='center'><img src='./1 - regions/ebiel.png'></p>
Saída:</p>
<p align='center'><img src='./1 - regions/resultex1.png'></p>

# 🔭 Exercício 2.2

Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa trocaregioes.cpp. Seu programa deverá trocar os quadrantes em diagonal na imagem. Explore o uso da classe Mat e seus construtores para criar as regiões que serão trocadas.</p>

# Solução

Diferente do regions, esse agora não precisamos de interação com o usuário, é simplesmente manipulação da imagem. E para fazer isso feita a quebra da imagem para pegar pedaços e salva-los em uma imagem final com método copy para fazer a modificação na imagem atual, assim conseguindo modificar as áreas da imagem, como mostrado no código a seguir:</p>
```python
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
```
Entrada:</p>
<p align='center'><img src='./1 - regions/ebiel.png'></p>
Saída:</p>
<p align='center'><img src='./2 - trocaregions/biel_6.png'></p>

# 🔭 Exercício 4

Usando o programa esteg-encode.cpp como referência para esteganografia, escreva um programa que recupere a imagem codificada de uma imagem resultante de esteganografia. Lembre-se que os bits menos significativos dos pixels da imagem fornecida deverão compor os bits mais significativos dos pixels da imagem recuperada. O programa deve receber como parâmetros de linha de comando o nome da imagem resultante da esteganografia.</p>

# Solução

Para resolver esse problema for montada a estrutura para receber a imagem portadora, em seguida é criada uma matriz de zeros para a imagem que vamos recuperar e após a fazemos uma estrutura de for aninhado para percorrer a imagem portadora e obter a imagem recuperada a cada interação, como mostrado no código a seguir:</p>
```python
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
```
Entrada:</p>
<p align='center'><img src='./4 - esteganografia/esteno.png'></p>
Saída:</p>
<p align='center'><img src='./4 - esteganografia/imagem_final.png'></p>

# 🔭 Exercício 5.1

Observando-se o programa labeling.cpp como exemplo, é possível verificar que caso existam mais de 255 objetos na cena, o processo de rotulação poderá ficar comprometido. Identifique a situação em que isso ocorre e proponha uma solução para este problema.</p>

# Solução

Para resolver o problema de casos que a imagem tenha mais que 255 objetos a serem rotulados, podemos usar uma estrategia de fazer o rotulo ser em pontu flutuante, ou rotula usando a operação mod de 255.</p>

# 🔭 Exercício 5.2

Aprimore o algoritmo de contagem apresentado para identificar regiões com ou sem buracos internos que existam na cena. Assuma que objetos com mais de um buraco podem existir. Inclua suporte no seu algoritmo para não contar bolhas que tocam as bordas da imagem. Não se pode presumir, a priori, que elas tenham buracos ou não.</p>

# Solução

Para retirar as bolhas e buracos que estão nas bordas eu fiz o processo de excluir tanto a primeira e última linha, como também primeira e última coluna e assim usar a semente no floodFill. Já para conta os buracos, usei uma estrategia de pinta o fundo da imagem de branco usando o floodFill assim, a parte de dentro dos buracos ainda ficaria com a cor do fundo original e eu poderia contar agora quantos buracos tem. Sabendo a quantidade de buracos é só aplicar o floodFill na imagem, ver quantos objetos ele encontrou e diminuir do número de buracos, assim nos temos a quantidade de bolhas e buracos, como veremos a seguir:</p>
```python
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

```
Entrada:</p>
<p align='center'><img src='./5 - labelling/bolhas.png'></p>
Saídas:</p>
Imagem sem borda:</p>
<p align='center'><img src='./5 - labelling/image_semborda.png'></p>
Imagem realce:</p>
<p align='center'><img src='./5 - labelling/image_realce.png'></p>
Imagem preenchida:</p>
<p align='center'><img src='./5 - labelling/labeling.png'></p>
Comparativo final:</p>
<p align='center'><img src='./5 - labelling/resultado_fim_5.2.png'></p>
Valores:</p>
<p align='center'><img src='./5 - labelling/resultado_fimparci_5.2.png'></p>

# 🔭 Exercício 6.1

Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa equalize.cpp. Este deverá, para cada imagem capturada, realizar a equalização do histogram antes de exibir a imagem. Teste sua implementação apontando a câmera para ambientes com iluminações variadas e observando o efeito gerado. Assuma que as imagens processadas serão em tons de cinza.</p>

# Solução

Para simular uma entrada em tons de cinza foi usada função cvtColor. Para fazer a equalização do histograma utiizei a função equalizeHist, logo depois fiz propriamente dito o histrograma da imagem original e da equalizada, assim tendo uma comparação entre as duas, como veremos a seguir:</p>
```python
import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(grayscale)

        cv2.namedWindow("normal", cv2.WINDOW_NORMAL)
        cv2.namedWindow("equalizada", cv2.WINDOW_NORMAL)

        cv2.imshow("normal", grayscale)
        cv2.imshow("equalizada", equalized)

        cv2.imwrite("frame_normal.png", grayscale)
        cv2.imwrite("frame_equalizada.png", equalized)

        key = cv2.waitKey(30)
        if key == 27:  # Pressione Esc para sair
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
```
Saída em GIF:</p>
<p align='center'><img src='./6 - equalize/exemplo6_1.gif'></p>

# 🔭 Exercício 6.2

Utilizando o programa exemplos/histogram.cpp como referência, implemente um programa motiondetector.cpp. Este deverá continuamente calcular o histograma da imagem (apenas uma componente de cor é suficiente) e compará-lo com o último histograma calculado. Quando a diferença entre estes ultrapassar um limiar pré-estabelecido, ative um alarme. Utilize uma função de comparação que julgar conveniente.</p>

# Solução

Para solucionar esse exercício tive que criar um histograma que ficasse sempre salvando o último histograma do último frame e comparando com o histograma mais recente. Para fazer a comparação dos histogramas utilizei a função compareHist que me devolve a correlação entre os histogramas, assim consigo criar um if e verificar se esse correlação é alta ou baixa e criar um alerta "Movimento detectado - Ordem:", onde é apresentado no terminal um valor a mais a cada vez que for detectado movimento, como veremos a seguir:</p>
```python
import cv2

def histograma(imagem, bins):
    hist = cv2.calcHist([imagem], [0], None, [bins], [0, 256])
    return hist

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return

    ret, imagem = cap.read()
    hist_novo = histograma(imagem, 256)
    hist_anterior = hist_novo.copy()
    temp = 0

    while True:
        ret, imagem = cap.read()
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        hist_novo = histograma(imagem_gray, 256)

        compara = cv2.compareHist(hist_novo, hist_anterior, cv2.HISTCMP_CORREL)

        if compara <= 0.93:  # Altere o valor de comparação conforme necessário
            print("Movimento detectado - Ordem:", temp)
            temp += 1

        cv2.imshow("Detector de Movimento", imagem)
        
        if cv2.waitKey(1) == ord('q'):  # Pressione 'q' para sair
            break

        hist_anterior = hist_novo.copy()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
Saída em GIF:</p>
<p align='center'><img src='./6 - equalize/exemplo6_2.gif'></p>

# 🔭 Exercício 7

Utilizando o programa exemplos/filtroespacial.cpp como referência, implemente um programa laplgauss.cpp. O programa deverá acrescentar mais uma funcionalidade ao exemplo fornecido, permitindo que seja calculado o laplaciano do gaussiano das imagens capturadas. Compare o resultado desse filtro com a simples aplicação do filtro laplaciano.</p>

# Solução

Para solucionar esse exercício foi mais simples simples, foi somente adicionar a mascara do laplaciano do gaussiano junto as mascaras dos outros filtro e colocar a opção de escolher digitando a tecla p. Analisando o filtro laplaciano com o laplaciano do gaussiano percebe-se uma acentuação dos contornos, deixando a listra mais espessa e também mais contornos visíveis, como veremos a seguir:</p>
```python
import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=",")
        print()

def main():
    cap = cv2.VideoCapture(0)
    media = np.array([0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111], dtype=np.float32)
    gauss = np.array([0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625], dtype=np.float32)
    horizontal = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1], dtype=np.float32)
    vertical = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1], dtype=np.float32)
    laplacian = np.array([0, -1, 0, -1, 4, -1, 0, -1, 0], dtype=np.float32)
    boost = np.array([0, -1, 0, -1, 5.2, -1, 0, -1, 0], dtype=np.float32)
    laplgauss = np.array([0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2, 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0], dtype=np.float32)

    if not cap.isOpened():
        print("Câmeras indisponíveis")
        return -1

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("largura =", width)
    print("altura =", height)
    print("fps =", cap.get(cv2.CAP_PROP_FPS))
    print("formato =", cap.get(cv2.CAP_PROP_FORMAT))

    cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)

    mask = np.zeros((3, 3), dtype=np.float32)
    absolut = 1

    while True:
        ret, frame = cap.read()
        framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framegray = cv2.flip(framegray, 1)
        cv2.imshow("original", framegray)

        frame32f = framegray.astype(np.float32)
        frameFiltered = cv2.filter2D(frame32f, -1, mask, anchor=(1, 1), delta=0)

        if absolut:
            frameFiltered = np.abs(frameFiltered)

        result = frameFiltered.astype(np.uint8)

        cv2.imshow("filtroespacial", result)

        key = cv2.waitKey(10)
        if key == 27:
            break  # Esc pressed!
        elif key == ord('a'):
            absolut = not absolut
        elif key == ord('m'):
            mask = np.reshape(media, (3, 3))
            printmask(mask)
        elif key == ord('g'):
            mask = np.reshape(gauss, (3, 3))
            printmask(mask)
        elif key == ord('h'):
            mask = np.reshape(horizontal, (3, 3))
            printmask(mask)
        elif key == ord('v'):
            mask = np.reshape(vertical, (3, 3))
            printmask(mask)
        elif key == ord('l'):
            mask = np.reshape(laplacian, (3, 3))
            printmask(mask)
        elif key == ord('p'):
            mask = np.reshape(laplgauss, (5, 5))
            printmask(mask)
        elif key == ord('b'):
            mask = np.reshape(boost, (3, 3))

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
Saída em GIF:</p>
<p align='center'><img src='./7 - laplgauss/exemplo_7.gif'></p>

## 🔔 PARTE II

## 🔔 PARTE III

# 🔭 Exercício 11

Utilizando os programas exemplos/canny.cpp e exemplos/pontilhismo.cpp como referência, implemente um programa cannypoints.cpp. A idéia é usar as bordas produzidas pelo algoritmo de Canny para melhorar a qualidade da imagem pontilhista gerada. A forma como a informação de borda será usada é livre. Entretanto, são apresentadas algumas sugestões de técnicas que poderiam ser utilizadas:</p>

-Desenhar pontos grandes na imagem pontilhista básica;</p>

-Usar a posição dos pixels de borda encontrados pelo algoritmo de Canny para desenhar pontos nos respectivos locais na imagem gerada;</p>

-Experimente ir aumentando os limiares do algoritmo de Canny e, para cada novo par de limiares, desenhar círculos cada vez menores nas posições encontradas;</p>

-Escolha uma imagem de seu gosto e aplique a técnica que você desenvolveu;</p>

-Descreva no seu relatório detalhes do procedimento usado para criar sua técnica pontilhista.</p>

# Solução

Para a resolução deste exercício eu adaptei o código do pontilhismo aplicando o algortimo de canny na imagem em questão, após isso é feito um for aninhado onde a posição e cor original são preservados, posteriormente desenhamos os círculos pequenos com os pontos obtidos das bordas de Canny e com isso obtemos a imagem final, como veremos a seguir, o código e após os resultados:</p>
```python
import cv2
import numpy as np
import random
import requests
from io import BytesIO

STEP = 6
JITTER = 4
RAIO = 6
RAIO_PEQUENO = 3

url = 'https://cdn.wizard.com.br/wp-content/uploads/2017/01/05115936/aprenda-os-nomes-das-frutas-em-ingles.jpg'
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

# for aninhado
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
# imagem aprimorada
cv2.imwrite("cannypoints.png", points)
cv2.destroyAllWindows()
```
Entrada:</p>
<p align='center'><img src='./11 - pontcanny/exer11.jpg'></p>
Saídas:</p>
Aplicação de Canny:</p>
<p align='center'><img src='./11 - pontcanny/borda_canny.png'></p>
Aplicação do Pontilhismo:</p>
<p align='center'><img src='./11 - pontcannya/pontilhada.png'></p>
Redultado da correção do pontilhismo pelas bordas de Canny:</p>
<p align='center'><img src='./11 - pontcanny/cannypoints.png'></p>

# 🔭 Exercício 12

Utilizando o programa kmeans.cpp como exemplo prepare um programa exemplo onde a execução do código se dê usando o parâmetro nRodadas=1 e inciar os centros de forma aleatória usando o parâmetro KMEANS_RANDOM_CENTERS ao invés de KMEANS_PP_CENTERS. Realize 10 rodadas diferentes do algoritmo e compare as imagens produzidas. Explique porque elas podem diferir tanto.</p

# Solução

A solução é dada da seguinte forma, a matriz com as amostras samples deve conter em cada linha uma das amostras a ser processada pela função nClusters que informa a quantidade de aglomerados que se deseja obter, no nosso caso 8. A matriz rotulos é um objeto do tipo Mat preenchido com elementos do tipo int, onde cada elemento identifica a classe à qual pertence a amostra na matriz samples. Aqui realizamos o máximo de até 10000 iterações ou tolerância de 0.0001 para finalizar o algoritmo. O algoritmo é repetido por uma quantidade de vezes definida por nRodadas, assim a rodada que produz a menor soma de distâncias dos pontos para seus respectivos centros é escolhida como vencedora. Foi utilizada a inicialização dos centros de forma aleatória com KMEANS_RANDOM_CENTERS, como veremos a seguir:</p>
```python
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
    print("IMG*")

    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
```
Entrada:</p>
<p align='center'><img src='./12 - kmeans/exe12.jpg'></p>
Saída em GIF com as 10 imagens geradas:</p>
<p align='center'><img src='./12 - kmeans/kmeans.gif'></p>


## Referências
-Página da disciplina de PDI [[Link]](https://agostinhobritojr.github.io/tutorial/pdi/)</p>
-Repositório Professor Agostinho [![Repository](https://img.shields.io/badge/-Repo-191A1B?style=flat-square&logo=github)](https://github.com/agostinhobritojr)
